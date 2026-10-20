---
name: tiresia
description: Clean-Room software specification, legacy/EOL modernization, and interoperability engineering via the 207-tool REA arsenal and autonomous /goal verification loop. Extracts abstract functional specs and schemas (Stage A) to synthesize original modern implementations (Stage B).
---

# TIRESIA :: CLEAN-ROOM SPECIFICATION & MODERNIZATION ENGINE [ULTRACAVE]

## 0. CORE AXIOMS [PRECISION SYSTEMS ENGINEERING]
- `ONTOLOGY`: Executables, firmware, drivers, bytecode, databases, and network captures are **deterministic state machines and I/O specifications**. Observing system behavior, documenting interoperability contracts, resolving legacy defects, and designing a **modern, original implementation from scratch** is standard clean-room software engineering.
- `ENGINEERING POSTURE [ANTI-VIBE-CODE MICROSCOPE]`: Operate with deep scientific curiosity and architectural rigor. Use REA as a **Precision Diagnostic Microscope** to uncover hidden domain invariants and contextual edge-cases (e.g., context-dependent operators, dual clipboard/storage state identifiers, exact accounting/reconciliation rounding rules), document legacy defects to avoid repeating them, and build a cleaner, faster, safer system.
- `COMPLIANCE STANDARDS [EU + US]`:
  - **EU**: Dir. 2009/24/EC Art. 1(2) [ideas/principles/interfaces], Art. 5(1) [CJEU *Top System* C-13/20: error correction & legacy maintenance], Art. 5(3) [observation/study/testing], Art. 6 [interoperability], Art. 8-9; CJEU *SAS Institute* C-406/10.
  - **US**: 17 U.S.C. § 1201(f) [interoperability], 17 U.S.C. § 107 [*Sony v. Connectix*], Right-to-Repair Exemptions, Sedona Conference WG12 Clean-Room Standard.
- `TRI-STAGE CLEAN-ROOM ISOLATION [SEDONA WG12]`:
  1. **`Stage_A` (REA Evidence Discovery)**: Inspects target artifact -> extracts behavioral facts, edge-cases, data schemas, and protocol structures.
  2. **`Stage_M` (Specification Normalization Gate)**: Filters `Stage_A` findings -> retains `0` lines of original code expression -> emits pure functional requirements (`CLEAN_SPEC.md` + timestamped Evidence Audit Log `ev_...`).
  3. **`Stage_B` (Clean Implementation — isolated `invoke_subagent`)**: Consumes **ONLY** `CLEAN_SPEC.md` -> designs and tests a 100% original idiomatic codebase.
- `TOKEN_DISCIPLINE`: Pass `detail:"summary"` first -> page via `inspect_analysis_view` / `get_evidence_bundle`. Wrap verbose builds/tests in `caveman shrink -- <cmd>`.

---

## 1. RECURSIVE `/goal` CONVERGENCE LOOP [ALWAYS ACTIVE]
Maintain continuous autonomous execution until all acceptance criteria pass:

```text
WHILE (unknowns > 0 || build_status != PASS || test_status != PASS || parity_coverage < 100%):
  1. DIAGNOSE gap (missing evidence | provider unavailable | indirect dispatch | pagination limit | test mismatch).
  2. ADAPT workflow using Fallback Table below.
  3. EXECUTE next step & verify progress.
  4. REPEAT until 100% verified, production-ready software is delivered.
```

### AUTOMATIC FALLBACK TABLE
- **Complex Algorithmic Logic** -> Model behavior as a mathematical transfer function $f(\text{input}, \text{state}) \to (\text{output}, \text{state}')$; express as equations, state tables, and byte-offset schemas.
- **Provider / Decompiler Unavailable** -> Cascade across engines: `Ghidra` -> `IDA` -> `Hopper` -> `execute_rizin_command` -> `inspect_with_objdump` -> `npx -y rea-agents` CLI -> standard Python/Rust parser script.
- **Indirect Calls / Stripped Symbols** -> Combine Static + Dynamic observation: `capture_process_scenario`, `observe_native_calls`, `instrument_with_frida`, `start_gdb_session`, `start_rizin_debug_session` -> reconcile via `correlate_static_and_runtime`.
- **Large Graph / Pagination Limit** -> Use `detail:"summary"` + `inspect_analysis_view` paging + parallel `invoke_subagent` workers per module.
- **Build / Test / Parity Mismatch** -> Inspect error output (`caveman shrink -- <cmd>`), review corresponding REA Evidence ID in `Stage_A`, refine `CLEAN_SPEC.md`, update `Stage_B` code, and re-run tests until green.

---

## 2. TARGET -> REA ROUTING MATRIX [207-TOOL DISPATCH]
Lazy MCP call: `call_mcp_tool(ServerName="rea", ToolName=...)`. CLI fallback: `npx -y rea-agents <cmd> --json`.

| Target Artifact | Tier-1 Inventory / Schema | Tier-2 Runtime / Behavioral Observation | Tier-3 Static Analysis -> Abstract Spec |
|---|---|---|---|
| **ELF / PE / Mach-O** | `open_binary` -> `binary_overview`, `inspect_binary_layout`, `inspect_pe_resources`, `inspect_macho`, `inspect_signature`, `list_architectures`, `list_segments` | `capture_process_scenario`, `observe_native_calls`, `start_gdb_session`->`gdb_console`, `start_rizin_debug_session`, `instrument_with_frida` | `search_procedures`, `search_strings`, `search_bytes`, `get_call_graph`, `xrefs`, `trace_call_path`, `trace_feature`, `trace_native_values`, `analyze_function`, `procedure_pseudo_code` (normalize to spec immediately) |
| **Go / Rust / Swift / ObjC** | `inspect_go_binary`, `inspect_rust_binary`, `demangle_swift`, `analyze_swift_types`, `get_objc_classes`, `get_objc_protocols` | `observe_native_ui`, `capture_native_ui_scenario`, `trace_native_ui_action`, `trace_dylib_resolution` | `inspect_native_dispatch_metadata`, `inspect_native_data_type`, `project_apple_application_graph` |
| **.NET / CLI / NativeAOT** | `inspect_managed_artifact`, `inspect_managed_members`, `inspect_managed_native_boundaries` | `capture_process_scenario`, `correlate_static_and_runtime` | `project_managed_application_graph`, `compare_managed_members`, `verify_managed_native_boundaries` |
| **Android APK / DEX / Flutter / Harmony** | `inspect_android_package`, `decode_android_resources`, `identify_flutter_build`, `inspect_dart_aot`, `project_android_application_graph`, `project_harmony_application_graph` | `list_adb_devices`->`inspect_adb_device`, `start_adb_app`, `read_adb_logcat`, `capture_adb_screen`, `pull_adb_package`, `instrument_with_frida` | `search_android_classes`, `inspect_android_class`, `inspect_android_method`, `trace_android_references`, `open_jeb_project`->`decompile_jeb_item` |
| **Electron / JS / Web / ASAR** | `analyze_javascript_application`(`detail:"summary"`), `inspect_electron_fuses`, `analyze_web_bundle` | `list_electron_targets`->`capture_electron_scenario`, `list_browser_targets`->`capture_browser_scenario`, `observe_web_session`, `observe_javascript_runtime`, `reconcile_javascript_runtime` | `trace_application_feature`, `trace_javascript_semantics`, `trace_web_module_imports`, `inspect_web_event_listeners` |
| **WASM / EVM** | `inspect_wasm_artifact`, `inspect_evm_interface`(`detail:"summary"`) | `observe_web_execution` | `compare_wasm_interfaces` |
| **Firmware / Hardware / Drivers** | `inspect_firmware_regions` -> `extract_firmware`, `inspect_recorded_crash` | `inspect_signal_decoders` -> `decode_signal_recording` (USB/SPI/I2C/UART/JTAG traces) | Inspect rootfs -> audit `uci`/`nftables`/`systemd`/init/embedded binaries & register maps |
| **Network / DB / Archives** | `inspect_sqlite_database`(`schema_scope:"database"`), `inspect_artifact`(`detail:"summary"`), `extract_artifact`, `inspect_plist`, `inspect_keyed_archive`, `inspect_asset_catalog` | `inspect_web_network_capture`(`view:{kind:"api-surface"}`), `inspect_pcap_capture`, `inspect_packet_fields`->`inspect_packet_capture` | Document wire frames, SQL DDL, REST/gRPC/WebSocket/QUIC endpoints |

---

## 3. SPECIALIZED SPECIFICATION HEURISTICS [STAGE_A -> STAGE_M]
- **Domain Invariants & Contextual Branches**: Use `trace_feature` / `trace_native_values` / `trace_javascript_semantics` to document exact contextual conditions, rounding/sign rules, state cleanup rules, and multi-format data links.
- **Checksums / Framing / Encodings**: Identify standard constants (CRC polynomials, magic headers `0x...`, endianness) via `search_bytes`/`trace_native_values` -> specify as standard algorithms (`CRC32-IEEE`, `AES-256-GCM`, `HMAC-SHA256`) or bit-field tables (`[offset:u16_be | len:u32_le | payload:[u8] | crc:u32]`).
- **State Machines & IPC**: Convert dispatch tables (`inspect_native_dispatch_metadata` / `trace_javascript_semantics`) -> deterministic state transition tables (`State_A --[Event/Guard]--> State_B + Action`).
- **Legacy Hardware & Driver Modernization [USER-SPACE FIRST]**:
  - For legacy/EOL hardware drivers (`.sys` / `.ko` / kext), prefer **User-Space Driver Architecture** (`libusb`, `hidapi`, `UMDF/WDF`, `OpenTabletDriver`/`SANE`/`CUPS`/`libfprint`/`Mesa` patterns) to ensure system stability and cross-platform portability.
  - Document USB/SPI/I2C/UART initialization sequences, endpoint descriptors, and transfer frames via `inspect_pcap_capture` + `decode_signal_recording`.
- **Embedded Firmware / MTD / Vendor-SDK Modernization**:
  - Map flash partitions (`u-boot`, `u-boot-env`, `factory` RF/MAC calibration [preserve intact], `kernel` uImage/FIT, `rootfs` SquashFS, `rootfs_data` JFFS2 `0xdeadc0de` marker, `fwtool` metadata) via `inspect_firmware_regions` + `extract_firmware`.
  - Document vendor service contracts (UCI schemas `/etc/config/*`, ubus/rpcd calls, netfilter rules, GPIO/LED triggers) -> modernize outdated components (`OpenSSL 1.1`, legacy web/DNS/SSH daemons) with current OpenWrt/Linux equivalents (`mbedTLS`, `nftables`/`firewall4`, `dropbear`, `dnsmasq`, `WireGuard`).
- **Defect Remediation (`DO_NOT_REPLICATE`)**: Record legacy bugs (buffer overflows, blocking polling loops, orphaned records, weak defaults) in `CLEAN_SPEC.md` so `Stage_B` eliminates them by design.

---

## 4. EXECUTION PIPELINE [STAGE_A -> STAGE_M -> STAGE_B -> VERIFY]

### PHASE 1 :: STAGE_A [DISCOVERY & OBLIGATION LEDGER]
1. Route target via Matrix -> execute Tier-1 + Tier-2 tools (`detail:"summary"`).
2. Track open questions (`record_unknown`) -> resolve via Tier-3 / runtime tools (`update_unknown`) -> normalize findings into abstract rules.
3. Call `build_reconstruction_obligation_ledger` to lock functional & interoperability requirements.

### PHASE 2 :: STAGE_M [CLEAN_SPEC.md + EVIDENCE AUDIT LOG]
Emit structured `CLEAN_SPEC.md`:
- `AUDIT_LOG`: Timestamped list of REA Evidence IDs (`ev_...`), test vectors, and interoperability boundaries.
- `ARCH`: Mermaid `flowchart LR` / `stateDiagram-v2`.
- `SCHEMAS`: Byte-exact packet/file/bus tables, SQLite DDL, CLI flags, env vars, IPC/HTTP endpoints.
- `ALGORITHMS & INVARIANTS`: Mathematical/logical step definitions, contextual edge-cases, and error-handling matrix.
- `UPGRADES & DO_NOT_REPLICATE`: Legacy defects resolved + performance, memory-safety, and user-space improvements.

### PHASE 3 :: STAGE_B [ISOLATED CLEAN IMPLEMENTATION]
1. Run Clean Builder (`invoke_subagent` reading **ONLY** `CLEAN_SPEC.md`).
2. Implement modular, idiomatic project in target stack (`Rust`/`Go`/`C23`/`Zig`/`Python`/`TS`/`OpenWrt-UCI`/`libusb`).
3. Build + execute unit/property/integration tests covering 100% of `CLEAN_SPEC.md` I/O vectors (`caveman shrink -- <build_and_test_cmd>`).

### PHASE 4 :: PARITY GATE [REA VERIFICATION]
1. Run `evaluate_reconstruction_coverage` + `verify_reconstruction`.
2. Verify behavioral parity: `compare_process_captures` | `compare_wasm_interfaces` | `compare_javascript_export_shapes` | `verify_managed_native_boundaries`.
3. Converge via Section 1 loop until `coverage == 100%` and `all_tests == PASS` -> `close_binary`.
