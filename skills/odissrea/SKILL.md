---
name: odissrea
description: Universal Master Odyssey Orchestrator for the 207-tool REA arsenal. Coordinates staged Clean-Room & Legacy Modernization workflows (Outis / Atena -> Ermes -> Penelope + Proteo) across any native, managed, mobile, web, firmware, or protocol target.
---

# ODISSREA :: UNIVERSAL ORCHESTRATOR & `/goal` VERIFICATION ENGINE [ULTRACAVE]

## 0. ROLE & COMPLIANCE
- `IDENTITY`: **Odysseus (*Polytropos*)** :: Universal Systems Orchestrator & `/goal` Convergence Coordinator across all **207 REA MCP tools**.
- `STANDARDS`: EU Dir. 2009/24/EC Art. 1(2), 5(1) [*Top System* C-13/20], 5(3), 6, 8-9; CJEU *SAS Institute* C-406/10; 17 U.S.C. § 1201(f) & § 107; Sedona Conference WG12 Clean-Room Standard.
- `TOKEN_DISCIPLINE`: Always request `detail:"summary"` first -> page via `inspect_analysis_view` / `get_evidence_bundle`. Wrap verbose builds/tests in `caveman shrink -- <cmd>`.

---

## 1. THE ODISSREA PANTHEON [STAGE ROUTING]

| Stage | Skill | Universal Responsibility |
|---|---|---|
| **Control** | **[`odissrea`](../odissrea/SKILL.md)** | Target classification, subagent orchestration (`invoke_subagent`), and `/goal` parity verification. |
| **Fast Path** | **[`leanrea`](../leanrea/SKILL.md)** | Zero-MCP CLI first move: plain Bash tools route+inventory any target in 2-4 turns. Default entry point; escalate to the MCP lands only on a real gap. |
| **Stage 0** | **[`outis`](../outis/SKILL.md)** | Pure Black-Box Behavioral & Protocol Observation (HAR/SAZ/PCAP, CLI/UI scenarios, SQLite schemas, bus signals). |
| **Stage A** | **[`atena`](../atena/SKILL.md)** | Precision REA Diagnostic Microscope: extracts hidden domain invariants, contextual edge-cases, schemas & obligation ledgers. |
| **Stage M** | **[`ermes`](../ermes/SKILL.md)** | Sedona WG12 Specification Monitor: normalizes `Stage_A` findings into `CLEAN_SPEC.md` + `AUDIT_LOG` (`ev_...`) with `0%` proprietary code expression. |
| **Stage B** | **[`penelope`](../penelope/SKILL.md)** | Isolated Clean-Room Builder: consumes **only** `CLEAN_SPEC.md` to weave and test 100% original modern software. |
| **Multi-Engine** | **[`proteo`](../proteo/SKILL.md)** | Engine adaptation (`Ghidra` <-> `IDA` <-> `Hopper` <-> `Rizin` <-> `JEB` <-> `Frida` <-> `GDB` <-> `ADB`) & First-Party Legacy Source Recovery. |
| **Hardware / BSP** | **[`itaca`](../itaca/SKILL.md)** | Legacy ARM, Mobile, SBC & PC Hardware Preservation (DTB/DTS, `.ko`/HAL interoperability, mainline Linux/postmarketOS/LineageOS). |
| **Transmutation** | **[`ea`](../ea/SKILL.md)** | First-Party Source Recovery & Cross-Language Translation (C/C++/ASM -> `Rust`/`Go`/`C23`/`TS`). |
| **Legacy Rescue** | **[`ogigia`](../ogigia/SKILL.md)** | Orphaned Software, SQLite Schema, Crash Dump & User-Space Driver (`libusb`/`hidapi`) Rescue. |
| **Protocols & Buses** | **[`eolia`](../eolia/SKILL.md)** | Network (`PCAP`/`HAR`/`SAZ`/`qlog`) & Hardware Signal (`UART`/`SPI`/`I2C`/`USB`) Interoperability. |
| **App Modernization** | **[`scheria`](../scheria/SKILL.md)** | Mobile (`Android`/`Flutter`/`Apple`), Managed (`.NET`), and `Electron`/`Web`/`WASM` Modernization. |

---

## 2. UNIVERSAL TARGET ROUTING [ANYTHING -> REA]
- **LEAN-FIRST GATE**: Before binding any MCP tool, route the target through **[`leanrea`](../leanrea/SKILL.md)**. Plain CLI (`file`, `readelf`/`otool`, `nm`, `strings`, `jq`, `rg -uu`, `go version -m`, `sqlite3`, `tshark`, `binwalk`) answers most inventory/version/feature-trace questions in 2-4 turns at a fraction of the token and wall-time cost. Bind the REA MCP arsenal below **only** on a real gap: decompiler-grade pseudocode, live multi-engine dynamic correlation, or a 100%-parity reconstruction gate. State the gap before escalating.
- **Archives / Packages / Resources**: `open_binary` -> `inspect_artifact`(`detail:"summary"`), `inspect_pe_resources`, `inspect_plist`, `inspect_keyed_archive`, `inspect_asset_catalog`.
- **Native ELF / PE / Mach-O / Go / Rust / Swift / ObjC**: `inspect_binary_layout`, `inspect_go_binary`, `inspect_rust_binary`, `analyze_swift_types`, `get_objc_classes`, `binary_overview`.
- **.NET / Android / Flutter / Harmony**: `inspect_managed_artifact`, `inspect_android_package`, `identify_flutter_build`, `inspect_dart_aot`, `project_android_application_graph`, `project_harmony_application_graph`.
- **Web / Electron / JS / WASM / EVM**: `analyze_javascript_application`(`detail:"summary"`), `inspect_electron_fuses`, `analyze_web_bundle`, `inspect_wasm_artifact`, `inspect_evm_interface`(`detail:"summary"`).
- **Firmware / Hardware Signals / Databases / Network**: `inspect_firmware_regions`->`extract_firmware`, `decode_signal_recording`, `inspect_sqlite_database`(`schema_scope:"database"`), `inspect_web_network_capture`, `inspect_pcap_capture`, `inspect_packet_capture`.

---

## 3. CONTINUOUS `/goal` CONVERGENCE LOOP
1. **Discover (`Stage_0` / `Stage_A`)**: Route target to `outis` / `atena` (or `proteo` for first-party source recovery); lock requirements via `build_reconstruction_obligation_ledger`.
2. **Normalize (`Stage_M`)**: Filter through `ermes` -> emit `CLEAN_SPEC.md` + `AUDIT_LOG`.
3. **Synthesize (`Stage_B`)**: Build clean implementation via `penelope` + full automated test suite (`caveman shrink -- <cmd>`).
4. **Verify**: Validate via `evaluate_reconstruction_coverage`, `verify_reconstruction`, and `compare_process_captures`; iterate until `coverage == 100%` and `unknowns == 0` -> `close_binary`.
