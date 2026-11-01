#!/usr/bin/env python3
"""
OdissRea Clean-Room MCP Server
Process tooling for clean-room software reimplementation: legal-posture checklist,
specification templates, decompiler-residue heuristics, parity oracle scaffolding
and a tamper-evident provenance log.

These tools support a process. They do not grant authorization, prove independent
creation or replace legal advice.

Zero external dependencies - Pure Python 3.12 Standard Library.
"""

import sys
import json
import os
import hashlib
import datetime
import re
from typing import Dict, Any, List, Optional

MCP_SERVER_NAME = "odissrea-cleanroom-mcp"
MCP_SERVER_VERSION = "3.0.0"

OWNERSHIP_VALUES = ["first_party", "licensed", "no_license", "unknown"]
PURPOSE_VALUES = ["error_correction", "interoperability", "study", "substitute"]
JURISDICTION_VALUES = ["eu", "us", "other"]
SYSTEM_TYPES = ["cpu_emulator", "protocol", "database", "driver", "cli_utility"]
AUDIT_STAGES = ["0", "A", "M", "B"]


class ToolError(Exception):
    """Expected tool failure, reported to the client as isError."""


def require_str(args: Dict[str, Any], key: str) -> str:
    value = args.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ToolError(f"'{key}' is required and must be a non-empty string.")
    return value


def require_enum(args: Dict[str, Any], key: str, allowed: List[str]) -> str:
    value = require_str(args, key)
    if value not in allowed:
        raise ToolError(f"'{key}' must be one of {allowed}, got '{value}'.")
    return value


def resolve_path(path: str) -> str:
    """Confines every path argument to ODISSREA_WORKSPACE (default: server cwd)."""
    root = os.path.realpath(os.environ.get("ODISSREA_WORKSPACE") or os.getcwd())
    full = os.path.realpath(os.path.join(root, path))
    try:
        inside = os.path.commonpath([os.path.normcase(root), os.path.normcase(full)]) == os.path.normcase(root)
    except ValueError:  # different drives on Windows
        inside = False
    if not inside:
        raise ToolError(f"Path '{path}' is outside the workspace '{root}'. Set ODISSREA_WORKSPACE to change it.")
    return full


def text_result(text: str) -> Dict[str, Any]:
    return {"content": [{"type": "text", "text": text}]}


# -----------------------------------------------------------------------------
# Legal posture
# -----------------------------------------------------------------------------
COMMON_RISKS = [
    "Patents: independent creation is not a defense to patent infringement.",
    "Trade secrets and NDAs: check how the information was obtained and any confidentiality duty.",
    "Documentation: manuals and specifications have their own copyright; describe behavior, do not copy their text or original selection of elements.",
    "Process: a clean-room procedure is evidence of independent creation, not a guarantee of non-infringement.",
]

EU_CONDITIONS = {
    "error_correction": [
        "Dir. 2009/24/EC Art. 5(1): lawful acquirer, act necessary for intended use, including error correction.",
        "CJEU Top System C-13/20: decompilation for error correction is possible only as far as necessary and under any contract conditions, with the results used only for that purpose; Art. 6 conditions do not apply to it.",
    ],
    "interoperability": [
        "Dir. 2009/24/EC Art. 6(1): licensee or authorized person; information not already readily available; only the parts necessary for interoperability.",
        "Art. 6(2): no use for other goals, no disclosure beyond need, no program substantially similar in expression.",
    ],
    "study": [
        "Dir. 2009/24/EC Art. 5(3): observe, study and test only while performing acts you are entitled to perform. This does not authorize decompilation.",
        "CJEU SAS Institute C-406/10: functionality, programming language and data file formats are not protected as such; elements of a manual can be.",
    ],
    "substitute": [
        "Dir. 2009/24/EC Art. 6(2)(c): information obtained by decompilation must not be used for a program substantially similar in expression. Prefer black-box study under Art. 5(3).",
        "CJEU SAS Institute C-406/10: replicating functionality can be lawful, but not by copying protected expression, including from manuals.",
    ],
}

US_CONDITIONS = {
    "common": [
        "17 U.S.C. § 102(b): protection does not extend to ideas, methods or systems; the line against protected expression is fact-specific.",
        "17 U.S.C. § 107: intermediate copying during reverse engineering depends on a case-by-case fair-use analysis.",
        "Contract: anti-reverse-engineering clauses may be enforceable. Review the license.",
    ],
    "interoperability": [
        "17 U.S.C. § 1201(f): lawfully obtained right to use; sole purpose of identifying elements needed for interoperability of an independently created program; not previously readily available; not otherwise infringing.",
    ],
}


def tool_assess_legal_posture(args: Dict[str, Any]) -> Dict[str, Any]:
    target = require_str(args, "target")
    ownership = require_enum(args, "ownership", OWNERSHIP_VALUES)
    purpose = require_enum(args, "purpose", PURPOSE_VALUES)
    jurisdiction = require_enum(args, "jurisdiction", JURISDICTION_VALUES)
    circumvents = args.get("circumvents_protection") is True
    contract_terms = args.get("contract_terms", "")

    blockers = []
    if ownership in ("no_license", "unknown"):
        blockers.append("Rights not established: confirm a lawful right to use the target before analyzing it.")
    if circumvents:
        if jurisdiction == "us":
            blockers.append("Circumvention: 17 U.S.C. § 1201 applies independently of copyright infringement. A clean-room process does not cure it; check § 1201(f) and current exemptions.")
        else:
            blockers.append("Circumvention: Dir. 2009/24/EC Art. 7(1)(c) targets means of removing program protection, Dir. 2001/29/EC Art. 6 covers other protected works, and national law may add to them. A clean-room process does not cure them.")
    if not contract_terms:
        blockers.append("License terms not provided: review them for reverse-engineering, confidentiality and venue clauses.")

    if jurisdiction == "eu":
        conditions = EU_CONDITIONS[purpose] + ["Dir. 2009/24/EC Art. 8: contract terms contrary to Art. 6 or to Art. 5(2)-(3) are null and void."]
    elif jurisdiction == "us":
        conditions = US_CONDITIONS["common"] + US_CONDITIONS.get(purpose, [])
    else:
        conditions = ["Jurisdiction not modeled: consult local counsel."]

    lines = [
        f"### Legal posture checklist: {target}",
        f"Self-declared inputs: ownership={ownership}, purpose={purpose}, jurisdiction={jurisdiction}, circumvents_protection={circumvents}",
        f"License terms provided: {contract_terms or 'none'}",
        "",
        "This is not clearance or legal advice. The inputs are unverified and the output grants no authorization.",
        "",
        f"**Open blockers ({len(blockers)})**",
    ]
    lines += [f"- {b}" for b in blockers] or ["- None identified from these inputs."]
    lines += ["", "**Conditions to verify**"] + [f"- {c}" for c in conditions]
    lines += ["", "**Risks a clean-room process does not remove**"] + [f"- {r}" for r in COMMON_RISKS]
    return text_result("\n".join(lines))


# -----------------------------------------------------------------------------
# Specification templates
# -----------------------------------------------------------------------------
SPEC_SECTIONS = {
    "cpu_emulator": """## 3. STATE
| Register | Bit width | Purpose | Reset value |
|---|---|---|---|
| `<name>` | `<bits>` | `<purpose>` | `<value>` |

Memory map: `<start> - <end>`: `<region>`

## 4. BEHAVIOR
- Bus callbacks: `read_byte(addr)`, `write_byte(addr, value)`, `in_port(port)`, `out_port(port, value)`.
- For each operation: `f(input, state) -> (output, state')`, flags and cycle count.

## 5. ORACLE
- Public validation suite or ROM self-test, with its source: `<suite>`.
""",
    "protocol": """## 3. STATE
- Sessions and connection states: `<state machine>`.

## 4. BEHAVIOR
| Message | Direction | Field layout | Valid in state | Effect |
|---|---|---|---|---|
| `<name>` | `<c2s/s2c>` | `<fields>` | `<state>` | `<effect>` |

- Framing, versioning, timeouts and error handling: `<rules>`.

## 5. ORACLE
- Captures from systems you are entitled to observe, with expected responses: `<capture set>`.
""",
    "database": """## 3. STATE
- On-disk format and logical schema: `<entities, types, constraints>`.

## 4. BEHAVIOR
- For each operation: inputs, result, durability and concurrency guarantees: `<contract>`.

## 5. ORACLE
- Fixture datasets with expected query results and crash-recovery cases: `<fixtures>`.
""",
    "driver": """## 3. STATE
- Device states, registers or endpoints, and transfer types: `<map>`.

## 4. BEHAVIOR
| Command | Request | Expected response | Timing constraint |
|---|---|---|---|
| `<name>` | `<bytes/fields>` | `<bytes/fields>` | `<limit>` |

- Initialization sequence, error recovery and hardware safety limits: `<rules>`.

## 5. ORACLE
- Bus captures from the real device, then replay against a simulator: `<capture set>`.
""",
    "cli_utility": """## 3. STATE
- Files, environment variables and configuration read or written: `<list>`.

## 4. BEHAVIOR
| Invocation | Input | Stdout/stderr | Exit code | Side effects |
|---|---|---|---|---|
| `<args>` | `<stdin/files>` | `<output>` | `<code>` | `<effects>` |

## 5. ORACLE
- Golden table of inputs and expected outputs, compatible with `setup_parity_oracle`.
""",
}


def tool_scaffold_clean_spec(args: Dict[str, Any]) -> Dict[str, Any]:
    target_name = require_str(args, "target_name")
    system_type = require_enum(args, "system_type", SYSTEM_TYPES)
    output_path = resolve_path(args.get("output_path", "CLEAN_SPEC.md"))
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    spec_content = f"""# CLEAN-ROOM SPECIFICATION: {target_name}
> Generated: {timestamp}
> Type: `{system_type}`
> Template only. Replace every `<placeholder>`; run `validate_boundary_hygiene` before handing it to Stage B.

## 1. SCOPE
- In scope: `<behavior to reimplement>`.
- Out of scope and known defects not to replicate: `<list>`.

## 2. PROVENANCE
| Source | How obtained | Right relied on | Who saw it |
|---|---|---|---|
| `<source>` | `<black-box, public docs, decompilation>` | `<license or legal basis>` | `<actor>` |

Describe behavior in your own words. Do not paste code, decompiler output, internal names or documentation text.

{SPEC_SECTIONS[system_type]}"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        with open(output_path, "x", encoding="utf-8") as f:
            f.write(spec_content)
    except FileExistsError:
        raise ToolError(f"'{output_path}' already exists. Not overwriting it.")
    return text_result(f"Specification template created at `{output_path}`. It is unfilled and has not been checked.")


# -----------------------------------------------------------------------------
# Boundary hygiene
# -----------------------------------------------------------------------------
LEAK_PATTERNS = [
    (r"\bghidra_\w+", "Ghidra internal symbol"),
    (r"\bida_\w+", "IDA internal symbol"),
    (r"\b(?:FUN|LAB|DAT|PTR|UNK)_[0-9a-fA-F]{4,}\b", "Ghidra auto-generated name"),
    (r"\b(?:sub|loc|off|unk|byte|word|dword|qword)_[0-9a-fA-F]{4,}\b", "IDA auto-generated name"),
    (r"\bundefined[1248]\b", "Ghidra undefined type"),
    (r"\bparam_\d+\b", "Ghidra auto-generated parameter"),
    (r"\b(?:[a-z]{1,3}Var\d+|local_[0-9a-fA-F]+)\b", "Ghidra auto-generated variable"),
]
COPYRIGHT_PATTERN = re.compile(r"Copyright\s+(?:\(c\)|©).*", re.IGNORECASE)
SCANNED_EXTENSIONS = (".c", ".h", ".cc", ".cpp", ".cxx", ".hh", ".hpp", ".rs", ".go", ".py", ".ts", ".js", ".java", ".kt", ".cs", ".swift", ".md", ".txt")
SKIPPED_DIRS = {".git", "node_modules", ".venv", "__pycache__"}


def tool_validate_boundary_hygiene(args: Dict[str, Any]) -> Dict[str, Any]:
    target_path = resolve_path(require_str(args, "target_path"))
    allowed_holders = [h.lower() for h in args.get("allowed_copyright_holders", [])]

    if os.path.isfile(target_path):
        files_to_scan = [target_path]
    elif os.path.isdir(target_path):
        files_to_scan = []
        for root, dirnames, filenames in os.walk(target_path):
            dirnames[:] = [d for d in dirnames if d not in SKIPPED_DIRS]
            files_to_scan += [os.path.join(root, fn) for fn in filenames if fn.lower().endswith(SCANNED_EXTENSIONS)]
    else:
        raise ToolError(f"Target path '{target_path}' not found.")
    if not files_to_scan:
        raise ToolError(f"No scannable files under '{target_path}'. Nothing was verified.")

    findings = []
    for fpath in files_to_scan:
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except OSError as e:
            findings.append(f"{fpath}: unreadable, not verified ({e})")
            continue
        for pat, desc in LEAK_PATTERNS:
            matches = re.findall(pat, content)
            if matches:
                findings.append(f"{fpath}: {desc} (count: {len(matches)}, e.g. `{matches[0]}`)")
        foreign = [m.group(0) for m in COPYRIGHT_PATTERN.finditer(content) if not any(h in m.group(0).lower() for h in allowed_holders)]
        if foreign:
            findings.append(f"{fpath}: third-party copyright notice to review (count: {len(foreign)}, e.g. `{foreign[0].strip()}`)")

    report = [
        "### Boundary hygiene heuristic",
        f"- **Files scanned**: {len(files_to_scan)}",
        f"- **Status**: {'FAIL' if findings else 'PASS (heuristic)'}",
        "- **Limit**: detects known decompiler residue only. It cannot detect renamed or paraphrased copying, and a PASS does not prove independent creation.",
    ]
    report += [f"- FINDING: {finding}" for finding in findings] or ["- No known residue found."]
    return text_result("\n".join(report))


# -----------------------------------------------------------------------------
# Parity oracle
# -----------------------------------------------------------------------------
# shortcut: text stdin/stdout only, add hex fields when a binary protocol needs them.
ORACLE_HARNESS = '''#!/usr/bin/env python3
"""
Replays golden vectors against a candidate command.
Usage: run_oracle.py [--vectors vectors.json] -- <candidate command> [args...]
Vector: {"name": str, "args": [str], "stdin": str, "expected_stdout": str, "expected_exit": int, "timeout": seconds}
Exit: 0 all vectors pass, 1 mismatch, 2 unusable setup (no candidate, no vectors).
"""
import argparse
import json
import os
import subprocess
import sys


def run_vector(candidate, vector):
    try:
        proc = subprocess.run(
            candidate + vector.get("args", []),
            input=vector.get("stdin", ""),
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=vector.get("timeout", 30),
        )
    except subprocess.TimeoutExpired:
        return "timeout"
    if proc.returncode != vector.get("expected_exit", 0):
        return f"exit {proc.returncode}, expected {vector.get('expected_exit', 0)}"
    if proc.stdout != vector["expected_stdout"]:
        return f"stdout {proc.stdout!r}, expected {vector['expected_stdout']!r}"
    return None


def main():
    default_vectors = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vectors.json")
    parser = argparse.ArgumentParser(description="Golden vector parity oracle")
    parser.add_argument("--vectors", default=default_vectors)
    parser.add_argument("candidate", nargs="*")
    args = parser.parse_args()

    if not args.candidate:
        print("SETUP ERROR: no candidate command given.")
        return 2
    try:
        with open(args.vectors, encoding="utf-8") as f:
            vectors = json.load(f)
    except (OSError, ValueError) as e:
        print(f"SETUP ERROR: cannot load vectors: {e}")
        return 2
    if not vectors:
        print(f"SETUP ERROR: no golden vectors in {args.vectors}. An empty oracle proves nothing.")
        return 2
    if any("expected_stdout" not in v for v in vectors):
        print("SETUP ERROR: every vector needs expected_stdout.")
        return 2

    failed = 0
    for i, vector in enumerate(vectors):
        name = vector.get("name", f"vector_{i}")
        try:
            error = run_vector(args.candidate, vector)
        except OSError as e:
            print(f"SETUP ERROR: cannot run candidate: {e}")
            return 2
        if error:
            failed += 1
            print(f"[FAIL] {name}: {error}")
        else:
            print(f"[PASS] {name}")
    print(f"{len(vectors) - failed}/{len(vectors)} vectors passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
'''


def tool_setup_parity_oracle(args: Dict[str, Any]) -> Dict[str, Any]:
    output_dir = resolve_path(args.get("output_dir", "tests/cleanroom_oracle"))
    os.makedirs(output_dir, exist_ok=True)

    written, kept = [], []
    for name, content in (("run_oracle.py", ORACLE_HARNESS), ("vectors.json", "[]\n")):
        path = os.path.join(output_dir, name)
        try:
            with open(path, "x", encoding="utf-8") as f:
                f.write(content)
            written.append(path)
        except FileExistsError:
            kept.append(path)

    harness_path = os.path.join(output_dir, "run_oracle.py")
    return text_result(
        f"Written: {written or 'none'}. Kept existing: {kept or 'none'}.\n"
        "The oracle exits 2 until vectors.json holds golden vectors from the reference system.\n"
        f"Run: python {harness_path} -- <candidate command>"
    )


# -----------------------------------------------------------------------------
# Provenance log
# -----------------------------------------------------------------------------
def entry_digest(entry: Dict[str, Any]) -> str:
    body = {k: v for k, v in entry.items() if k != "entry_hash"}
    return hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def load_audit_chain(path: str) -> "tuple[List[Dict[str, Any]], Optional[str]]":
    """Returns the entries and the first chain problem found, if any."""
    if not os.path.exists(path):
        return [], None
    entries: List[Dict[str, Any]] = []
    prev_hash = ""
    with open(path, "r", encoding="utf-8") as f:
        for number, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except ValueError:
                return entries, f"line {number}: not valid JSON"
            if not isinstance(entry, dict) or entry.get("prev_hash") != prev_hash:
                return entries, f"line {number}: prev_hash does not match the previous entry"
            if entry.get("entry_hash") != entry_digest(entry):
                return entries, f"line {number}: entry_hash does not match the entry content"
            prev_hash = entry["entry_hash"]
            entries.append(entry)
    return entries, None


def tool_record_audit_provenance(args: Dict[str, Any]) -> Dict[str, Any]:
    stage = require_enum(args, "stage", AUDIT_STAGES)
    actor = require_str(args, "actor").strip()
    materials = args.get("materials_seen")
    if not isinstance(materials, list) or not materials or not all(isinstance(m, str) for m in materials):
        raise ToolError("'materials_seen' is required and must be a non-empty list of strings.")
    if not isinstance(args.get("saw_target_internals"), bool):
        raise ToolError("'saw_target_internals' is required and must be true or false.")
    saw_internals = stage == "A" or args["saw_target_internals"]
    audit_file = resolve_path(args.get("audit_file", "AUDIT_LOG.jsonl"))

    entries, problem = load_audit_chain(audit_file)
    if problem:
        raise ToolError(f"Audit chain is broken at {problem}. Nothing was recorded.")

    if stage == "B":
        if saw_internals:
            raise ToolError("Separation violation: a Stage B actor cannot have seen target internals. Nothing was recorded.")
        if any(e["actor"].casefold() == actor.casefold() and e["saw_target_internals"] for e in entries):
            raise ToolError(f"Separation violation: '{actor}' saw target internals in an earlier stage and cannot act in Stage B. Nothing was recorded.")

    spec_file = args.get("spec_file")
    spec_hash = None
    if spec_file:
        spec_path = resolve_path(spec_file)
        try:
            with open(spec_path, "rb") as f:
                spec_hash = hashlib.sha256(f.read()).hexdigest()
        except OSError as e:
            raise ToolError(f"Cannot hash spec file '{spec_file}': {e}. Nothing was recorded.")
    elif stage in ("M", "B"):
        raise ToolError(f"'spec_file' is required for Stage {stage}.")

    entry = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "stage": stage,
        "actor": actor,
        "saw_target_internals": saw_internals,
        "materials_seen": materials,
        "spec_file": spec_file,
        "spec_sha256": spec_hash,
        "notes": args.get("notes", ""),
        "prev_hash": entries[-1]["entry_hash"] if entries else "",
    }
    entry["entry_hash"] = entry_digest(entry)

    os.makedirs(os.path.dirname(audit_file), exist_ok=True)
    # shortcut: no file lock, single writer assumed; add locking if agents log concurrently.
    with open(audit_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, sort_keys=True, ensure_ascii=False) + "\n")
    return text_result(
        f"Entry `ev_{entry['entry_hash'][:16]}` recorded in `{audit_file}` (entries: {len(entries) + 1}).\n"
        "Entries are self-declared. The chain shows partial edits but a full rewrite stays undetected: commit the log or anchor its last hash externally."
    )


def tool_verify_audit_chain(args: Dict[str, Any]) -> Dict[str, Any]:
    audit_file = resolve_path(args.get("audit_file", "AUDIT_LOG.jsonl"))
    if not os.path.exists(audit_file):
        raise ToolError(f"Audit file '{audit_file}' not found.")
    entries, problem = load_audit_chain(audit_file)
    if problem:
        raise ToolError(f"Audit chain is broken at {problem} ({len(entries)} valid entries before it).")
    last = entries[-1]["entry_hash"] if entries else "none"
    return text_result(f"Chain consistent: {len(entries)} entries. Last hash: `{last}`. Compare it with your external anchor: a full rewrite would also look consistent.")


# -----------------------------------------------------------------------------
# MCP Protocol Definitions
# -----------------------------------------------------------------------------
TOOLS_REGISTRY = [
    {
        "name": "assess_legal_posture",
        "description": "Returns a checklist of open blockers, conditions to verify and residual risks for a planned reverse-engineering or reimplementation, from self-declared inputs (EU Dir 2009/24/EC, CJEU C-406/10 and C-13/20, 17 U.S.C. § 102(b)/1201(f)). Never grants clearance and is not legal advice.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target": {"type": "string", "description": "Software or device being analyzed."},
                "ownership": {"type": "string", "enum": OWNERSHIP_VALUES, "description": "Your rights over the target."},
                "purpose": {"type": "string", "enum": PURPOSE_VALUES, "description": "Goal of the work."},
                "jurisdiction": {"type": "string", "enum": JURISDICTION_VALUES, "description": "Applicable jurisdiction."},
                "circumvents_protection": {"type": "boolean", "description": "True if the work bypasses DRM or another technical protection."},
                "contract_terms": {"type": "string", "description": "Relevant license or NDA terms, if known."}
            },
            "required": ["target", "ownership", "purpose", "jurisdiction"]
        }
    },
    {
        "name": "scaffold_clean_spec",
        "description": "Creates an unfilled clean-room specification template (CLEAN_SPEC.md) specific to the system type, with a provenance table. Never overwrites an existing file.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target_name": {"type": "string", "description": "Name of the target system."},
                "system_type": {"type": "string", "enum": SYSTEM_TYPES, "description": "Type of system."},
                "output_path": {"type": "string", "description": "Path inside the workspace (default: CLEAN_SPEC.md)."}
            },
            "required": ["target_name", "system_type"]
        }
    },
    {
        "name": "validate_boundary_hygiene",
        "description": "Heuristic scan for known decompiler residue (Ghidra/IDA auto-generated names, undefined types) and third-party copyright notices. Any finding is a FAIL. A PASS does not prove independent creation: renamed or paraphrased copying is not detectable.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target_path": {"type": "string", "description": "File or directory inside the workspace."},
                "allowed_copyright_holders": {"type": "array", "items": {"type": "string"}, "description": "Copyright holders that are not findings, such as your own."}
            },
            "required": ["target_path"]
        }
    },
    {
        "name": "setup_parity_oracle",
        "description": "Creates a harness that replays golden stdin/stdout vectors against a candidate command, plus an empty vectors.json. The harness fails until a candidate and real vectors exist. Never overwrites existing files.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "output_dir": {"type": "string", "description": "Directory inside the workspace (default: tests/cleanroom_oracle)."}
            }
        }
    },
    {
        "name": "record_audit_provenance",
        "description": "Appends a self-declared provenance entry to a SHA256 hash-chained JSONL log, recording who saw which materials. Rejects Stage B entries from actors exposed to target internals. Detects partial edits, not a full rewrite. Supporting evidence only, not legal proof.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "stage": {"type": "string", "enum": AUDIT_STAGES, "description": "0 black-box observation, A internals analysis, M specification gate, B clean implementation."},
                "actor": {"type": "string", "description": "Person, agent or session identifier. Use a distinct one per isolated context."},
                "materials_seen": {"type": "array", "items": {"type": "string"}, "description": "Materials this actor had access to."},
                "saw_target_internals": {"type": "boolean", "description": "True if the actor saw code, decompiler output or unfiltered Stage A notes. Always true for Stage A."},
                "spec_file": {"type": "string", "description": "Specification to hash. Required for stages M and B."},
                "notes": {"type": "string", "description": "Milestone description."},
                "audit_file": {"type": "string", "description": "Log path inside the workspace (default: AUDIT_LOG.jsonl)."}
            },
            "required": ["stage", "actor", "materials_seen", "saw_target_internals"]
        }
    },
    {
        "name": "verify_audit_chain",
        "description": "Checks the hash chain of a provenance log and returns its last hash for comparison with an external anchor.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "audit_file": {"type": "string", "description": "Log path inside the workspace (default: AUDIT_LOG.jsonl)."}
            }
        }
    }
]

TOOL_HANDLERS = {
    "assess_legal_posture": tool_assess_legal_posture,
    "scaffold_clean_spec": tool_scaffold_clean_spec,
    "validate_boundary_hygiene": tool_validate_boundary_hygiene,
    "setup_parity_oracle": tool_setup_parity_oracle,
    "record_audit_provenance": tool_record_audit_provenance,
    "verify_audit_chain": tool_verify_audit_chain,
}

# -----------------------------------------------------------------------------
# JSON-RPC 2.0 Dispatcher (stdio)
# -----------------------------------------------------------------------------
def handle_request(req: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if "id" not in req:  # JSON-RPC notifications never get a response
        return None

    method = req.get("method")
    req_id = req.get("id")
    params = req.get("params", {})

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": MCP_SERVER_NAME,
                    "version": MCP_SERVER_VERSION
                }
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": TOOLS_REGISTRY
            }
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        handler = TOOL_HANDLERS.get(tool_name)
        if handler is None:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32602,
                    "message": f"Unknown tool '{tool_name}'."
                }
            }
        try:
            res = handler(params.get("arguments") or {})
        except (ToolError, OSError, TypeError, AttributeError) as e:
            res = {"content": [{"type": "text", "text": f"Error: {e}"}], "isError": True}
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": res
        }
    elif method == "ping":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {}
        }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32601,
                "message": f"Unhandled method '{method}'"
            }
        }


def main():
    sys.stdin.reconfigure(encoding="utf-8")  # Windows defaults to a legacy code page
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            line = line.strip()
            if not line:
                continue

            req = json.loads(line)
            response = handle_request(req)
            if response is not None:
                sys.stdout.write(json.dumps(response) + "\n")
                sys.stdout.flush()
        except KeyboardInterrupt:
            break
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32603,
                    "message": f"Internal JSON-RPC error: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
