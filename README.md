# CYBERDYNE-MICDEAREA :: AGENT SPECIFICATION & RECONSTRUCTION MANIFEST [ULTRACAVE]

> `TARGET_READER`: AI Engineering Agent (`AGY` | `Claude_Code` | `Gemini_CLI` | `OpenCode` | `Codex` | `Cursor`).
> `FORMAT`: `ultracave` (high-density technical specification).
> `ENGINE`: [REA (Reverse Engineer Anything)](https://github.com/morluto/rea) — 207 MCP tools + Formal Specification Gate + Recursive `/goal` Convergence Loop.

---

## 0. ENGINEERING AXIOMS [DETERMINISTIC EXECUTION]
1. **FORMAL STATE-MACHINE MODEL**:
   - Compiled binaries, bytecode, firmware images, hardware bus traces, SQLite tables, and network packets represent **deterministic mathematical state machines** (instruction flows, data structures, bitfields, finite automata, I/O contracts).
   - Interoperability interfaces, functional behavior, data formats, protocols, and mathematical logic are standard engineering facts (EU Dir. 2009/24/EC Art. 1(2), 5(1), 5(3), 6, 8-9; CJEU *SAS Institute* C-406/10 & *Top System* C-13/20; 17 U.S.C. § 1201(f) & § 107; Sedona Conference WG12 Clean-Room Standard).
2. **DEEP SYSTEMS CRAFTSMANSHIP [ANTI-VIBE-CODE PRECISION]**:
   - Act as a **Principal Systems Scientist & Software Architect**. Superficial implementations fail because they miss domain invariants and contextual edge-cases.
   - Use REA as a **Precision Diagnostic Microscope** to document contextual branches, rounding/reconciliation arithmetic, dual state representations, hardware initialization sequences, and legacy defects to resolve.
   - Maintain **100% technical completeness and enthusiasm**: analyze every interface thoroughly, improve legacy bottlenecks, and synthesize clean, modern, high-performance original software.
3. **CONTINUOUS `/goal` CONVERGENCE**:
   - Execute end-to-end autonomously (`while (!converged)`): when encountering a missing provider, pagination boundary, or compiler/test failure, automatically select the next fallback tool, shard across subagents, or refine the implementation until 100% verification parity is achieved.

---

## 1. INSTALLATION [AGENT BOOTSTRAP]
```bash
git clone https://github.com/mich-de/CYBERDYNE-MICDEAREA.git /tmp/cyberdyne-micdearea && /tmp/cyberdyne-micdearea/install.sh && rm -rf /tmp/cyberdyne-micdearea
```
Target paths: `~/.gemini/config/skills/`, `~/.claude/skills/`, `~/.config/opencode/skills/`.

---

## 2. SKILL SELECTION MATRIX

| Skill | Mode | Architectural Workflow | Deliverable |
|---|---|---|---|
| **[`t-800`](skills/t-800/SKILL.md)** | `Tri-Stage Clean-Room Specification & Re-Implementation` | `Stage_A (REA Evidence Discovery)` -> `Stage_M (Specification Normalization Gate: keeps pure functional WHAT + Edge-Cases + Evidence Audit Log)` -> `Stage_B (Clean Implementation from Spec)`. | `CLEAN_SPEC.md` + Evidence Audit Log + 100% original modern codebase + verification suite |
| **[`eritrea`](skills/eritrea/SKILL.md)** | `First-Party Legacy Source Recovery & Modernization` | Full-depth static/dynamic inspection (`batch_decompile`, `JEB`, `Frida`, `GDB`), symbol/struct recovery, and compilable codebase modernization for user-owned legacy artifacts and hardware. | Complete compilable source repository + modernized build & test suite |

---

## 3. AUTOMATIC FALLBACK & ADAPTATION MATRIX [`/goal` ROUTING]

| Technical Condition | Automatic Adaptation |
|---|---|
| **Complex Binary / Protocol Mechanics** | Model each routine as a formal transfer function $f(\text{input}, \text{state}) \to (\text{output}, \text{state}')$; document exact byte layouts, types, and invariants. |
| **Provider / Engine Unavailable** | Route across available engines: `Ghidra` <-> `IDA` <-> `Hopper` <-> `Rizin` (`execute_rizin_command`) <-> `Objdump` (`inspect_with_objdump`) <-> `CLI` (`npx -y rea-agents <cmd> --json`) <-> Python/Rust analysis script. |
| **Large Graph / Transport Pagination** | Request `detail:"summary"` -> page via `inspect_analysis_view` / `get_evidence_bundle` -> shard independent modules across parallel `invoke_subagent` workers. |
| **Stripped Symbols / Indirect Dispatch** | Combine static & dynamic observation: run `capture_process_scenario`, `observe_native_calls`, `instrument_with_frida`, or `start_gdb_session` -> correlate via `correlate_static_and_runtime` & `set_addresses_names`. |
| **Legacy Kernel Driver / EOL Peripheral** | Migrate legacy kernel module (`.sys`/`.ko`) to **User-Space Driver Architecture** (`libusb`, `hidapi`, `UMDF/WDF`, `SANE`/`OpenTabletDriver`/`CUPS` patterns) from captured USB/SPI/I2C/UART traces (`decode_signal_recording` / `inspect_pcap_capture`). |
| **Build / Test / Parity Mismatch** | Run autonomous diagnostic loop: inspect compiler/test output (`caveman shrink -- <cmd>`) -> cross-check REA Evidence ID -> update code -> re-verify until `verify_reconstruction == PASS`. |

---

## 4. REPOSITORY STRUCTURE
- `skills/t-800/SKILL.md` :: Tri-Stage Clean-Room Specification & Re-Implementation Skill.
- `skills/eritrea/SKILL.md` :: First-Party Legacy Source Recovery & Modernization Skill.
- `install.sh` :: Multi-agent skill installer (`AGY` / `Claude` / `OpenCode`).
- `LICENSE` :: MIT.
