import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVER = os.path.join(REPO, "mcp", "odissrea_cleanroom_server.py")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


server = load("cleanroom_server", SERVER)
installer = load("install_mcp_config", os.path.join(REPO, "mcp", "install_mcp_config.py"))


def call(tool, **arguments):
    response = server.handle_request({"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": tool, "arguments": arguments}})
    result = response["result"]
    return result["content"][0]["text"], result.get("isError", False)


class WorkspaceTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = os.path.realpath(tmp.name)
        previous = os.environ.get("ODISSREA_WORKSPACE")
        os.environ["ODISSREA_WORKSPACE"] = self.root
        self.addCleanup(lambda: os.environ.pop("ODISSREA_WORKSPACE") if previous is None else os.environ.update(ODISSREA_WORKSPACE=previous))

    def write(self, name, content):
        path = os.path.join(self.root, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path


class LegalPostureTest(WorkspaceTest):
    def test_never_grants_clearance_and_flags_blockers(self):
        text, is_error = call("assess_legal_posture", target="x", ownership="unknown", purpose="substitute", jurisdiction="us", circumvents_protection=True)
        self.assertFalse(is_error)
        self.assertIn("not clearance", text)
        self.assertIn("Rights not established", text)
        self.assertIn("1201", text)
        self.assertIn("Patents", text)

    def test_rejects_invalid_enum(self):
        _, is_error = call("assess_legal_posture", target="x", ownership="mine", purpose="study", jurisdiction="eu")
        self.assertTrue(is_error)


class HygieneTest(WorkspaceTest):
    def scan(self, name, content):
        self.write(name, content)
        return call("validate_boundary_hygiene", target_path=name)

    def test_any_finding_fails(self):
        text, _ = self.scan("a.c", "void sub_401000(void){}")
        self.assertIn("Status**: FAIL", text)

    def test_detects_ghidra_names(self):
        for sample in ("FUN_00401000", "LAB_00401010", "param_1", "iVar1", "local_18", "undefined4"):
            text, _ = self.scan("a.c", sample)
            self.assertIn("Status**: FAIL", text, sample)

    def test_clean_file_passes_with_limit_stated(self):
        text, _ = self.scan("a.c", "int add(int left, int right) { return left + right; }")
        self.assertIn("PASS (heuristic)", text)
        self.assertIn("does not prove", text)

    def test_empty_directory_is_an_error(self):
        os.makedirs(os.path.join(self.root, "empty"))
        _, is_error = call("validate_boundary_hygiene", target_path="empty")
        self.assertTrue(is_error)

    def test_github_directory_is_scanned(self):
        self.write(".github/a.c", "sub_401000")
        text, _ = call("validate_boundary_hygiene", target_path=".")
        self.assertIn("Status**: FAIL", text)

    def test_copyright_holder_allowlist(self):
        self.write("a.c", "// Copyright (c) 2026 Acme")
        text, _ = call("validate_boundary_hygiene", target_path="a.c")
        self.assertIn("FAIL", text)
        text, _ = call("validate_boundary_hygiene", target_path="a.c", allowed_copyright_holders=["acme"])
        self.assertIn("PASS", text)


class PathScopeTest(WorkspaceTest):
    def test_rejects_paths_outside_workspace(self):
        outside = os.path.join(os.path.dirname(self.root), "escape.md")
        for path in (outside, "../escape.md"):
            _, is_error = call("scaffold_clean_spec", target_name="x", system_type="protocol", output_path=path)
            self.assertTrue(is_error, path)
        self.assertFalse(os.path.exists(outside))


class SpecTest(WorkspaceTest):
    def test_template_matches_type(self):
        call("scaffold_clean_spec", target_name="x", system_type="protocol", output_path="p.md")
        with open(os.path.join(self.root, "p.md"), encoding="utf-8") as f:
            spec = f.read()
        self.assertIn("Message", spec)
        self.assertNotIn("Register", spec)
        self.assertNotIn("0%", spec)

    def test_never_overwrites(self):
        self.write("CLEAN_SPEC.md", "KEEP")
        _, is_error = call("scaffold_clean_spec", target_name="x", system_type="driver")
        self.assertTrue(is_error)
        with open(os.path.join(self.root, "CLEAN_SPEC.md"), encoding="utf-8") as f:
            self.assertEqual(f.read(), "KEEP")

    def test_unknown_type_is_an_error(self):
        _, is_error = call("scaffold_clean_spec", target_name="x", system_type="toaster")
        self.assertTrue(is_error)


class OracleTest(WorkspaceTest):
    def oracle(self, *candidate):
        call("setup_parity_oracle", output_dir="o")
        harness = os.path.join(self.root, "o", "run_oracle.py")
        return subprocess.run([sys.executable, harness, "--", *candidate], capture_output=True, text=True)

    def set_vectors(self, vectors):
        call("setup_parity_oracle", output_dir="o")
        self.write("o/vectors.json", json.dumps(vectors))

    def candidate(self):
        return [sys.executable, self.write("cand.py", "import sys; print(sys.stdin.read().upper(), end='')")]

    def test_no_candidate_is_a_setup_error(self):
        self.set_vectors([{"expected_stdout": ""}])
        self.assertEqual(self.oracle().returncode, 2)

    def test_empty_vectors_are_a_setup_error(self):
        self.assertEqual(self.oracle(*self.candidate()).returncode, 2)

    def test_pass_and_mismatch(self):
        self.set_vectors([{"name": "up", "stdin": "ab", "expected_stdout": "AB"}])
        self.assertEqual(self.oracle(*self.candidate()).returncode, 0)
        self.set_vectors([{"name": "up", "stdin": "ab", "expected_stdout": "ab"}])
        self.assertEqual(self.oracle(*self.candidate()).returncode, 1)

    def test_rerun_keeps_vectors(self):
        self.set_vectors([{"expected_stdout": "KEEP"}])
        call("setup_parity_oracle", output_dir="o")
        with open(os.path.join(self.root, "o", "vectors.json"), encoding="utf-8") as f:
            self.assertIn("KEEP", f.read())


class AuditTest(WorkspaceTest):
    def record(self, stage, actor, saw, **extra):
        return call("record_audit_provenance", stage=stage, actor=actor, materials_seen=["m"], saw_target_internals=saw, **extra)

    def setUp(self):
        super().setUp()
        self.write("CLEAN_SPEC.md", "spec")

    def test_missing_spec_is_rejected_and_not_logged(self):
        _, is_error = self.record("M", "gate", False, spec_file="missing.md")
        self.assertTrue(is_error)
        self.assertFalse(os.path.exists(os.path.join(self.root, "AUDIT_LOG.jsonl")))

    def test_separation_enforced(self):
        self.assertFalse(self.record("A", "analyst", False)[1])
        _, is_error = self.record("B", "ANALYST", False, spec_file="CLEAN_SPEC.md")
        self.assertTrue(is_error)
        _, is_error = self.record("B", "builder", True, spec_file="CLEAN_SPEC.md")
        self.assertTrue(is_error)
        self.assertFalse(self.record("B", "builder", False, spec_file="CLEAN_SPEC.md")[1])

    def test_chain_detects_edit_and_blocks_append(self):
        self.record("A", "analyst", True)
        self.record("M", "gate", True, spec_file="CLEAN_SPEC.md")
        self.assertFalse(call("verify_audit_chain")[1])
        path = os.path.join(self.root, "AUDIT_LOG.jsonl")
        with open(path, encoding="utf-8") as f:
            content = f.read()
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.replace("analyst", "someone", 1))
        self.assertTrue(call("verify_audit_chain")[1])
        self.assertTrue(self.record("A", "other", True)[1])


class ProtocolTest(WorkspaceTest):
    def test_stdio_session(self):
        requests = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "method": "notifications/cancelled", "params": {}},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "validate_boundary_hygiene", "arguments": {"target_path": "../outside"}}},
            {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "get_safe_harbor_attestation", "arguments": {}}},
        ]
        proc = subprocess.run(
            [sys.executable, SERVER],
            input="\n".join(json.dumps(r) for r in requests) + "\n",
            capture_output=True, text=True, encoding="utf-8", cwd=self.root,
        )
        responses = [json.loads(line) for line in proc.stdout.splitlines()]
        self.assertEqual([r["id"] for r in responses], [1, 2, 3, 4])
        self.assertEqual({t["name"] for t in responses[1]["result"]["tools"]}, set(server.TOOL_HANDLERS))
        self.assertTrue(responses[2]["result"]["isError"])
        self.assertIn("error", responses[3])


class InstallerTest(WorkspaceTest):
    def test_merge_keeps_other_servers_backs_up_and_drops_bom(self):
        path = os.path.join(self.root, "cfg", "mcp_config.json")
        os.makedirs(os.path.dirname(path))
        with open(path, "w", encoding="utf-8-sig") as f:
            json.dump({"mcpServers": {"other": {"command": "x"}}, "keep": 1}, f)
        installer.merge_config(path, "/s.py", "python")
        with open(path, "rb") as f:
            raw = f.read()
        self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
        config = json.loads(raw)
        self.assertEqual(config["keep"], 1)
        self.assertIn("other", config["mcpServers"])
        self.assertIn(installer.SERVER_NAME, config["mcpServers"])
        self.assertEqual(len([n for n in os.listdir(os.path.dirname(path)) if n.endswith(".bak")]), 1)

    def test_invalid_json_is_left_untouched(self):
        path = self.write("mcp_config.json", "{broken")
        with self.assertRaises(ValueError):
            installer.merge_config(path, "/s.py", "python")
        with open(path, encoding="utf-8") as f:
            self.assertEqual(f.read(), "{broken")


if __name__ == "__main__":
    unittest.main()
