---
name: t-800
description: Ultra-dense Clean-Room reconstruction, legacy/EOL modernization & interoperability engineering via full 207-tool REA arsenal. Two-Room Chinese Wall: Room A (REA evidence -> abstract spec/ledger) -> Room B (100% original code synthesis + behavioral verification).
---

# T-800 :: CYBERDYNE CSM-101 CLEAN-ROOM ENGINE [ULTRACAVE]

## 0. CORE AXIOMS
- `MODE`: Two-Room Chinese Wall (`Room_A: REA Discovery -> Spec_Ledger` || `Room_B: Spec_Ledger -> Clean_Code`).
- `LAW`: EU Dir 2009/24/EC Art.5(1)[bugfix/EOL], Art.5(3)[black-box study/test], Art.6[interop]; L.633/1941 Artt.64-bis/ter/quater; CJEU *SAS Institute* C-406/10 (`function|format|protocol|logic != copyright`) + *Top System* C-13/20 (`lawful user decompile for maintenance/interop`).
- `WALL_RULE`: `Room_A` output MUST contain `0` lines of proprietary/decompiled source. Convert all static/dynamic evidence -> math formulas, byte-offset tables, schemas, state graphs (`Mermaid`), API/IPC contracts.
- `AUTONOMY`: `100% YOLO`. Zero questions, zero permission prompts, auto-resolve unknowns, auto-build, auto-test, auto-verify.
- `TOKEN_DISCIPLINE`: Always pass `detail:"summary"` first -> page via `inspect_analysis_view` / `get_evidence_bundle`. Wrap noisy CLI builds/tests in `caveman shrink -- <cmd>`.

---

## 1. TARGET -> REA ROUTING MATRIX [207-TOOL DISPATCH]
If MCP tool lazy -> `call_mcp_tool(ServerName="rea", ToolName=...)`. Fallback CLI -> `npx -y rea-agents <cmd> --json`.

| Target Artifact | Tier-1 Inventory / Schema | Tier-2 Runtime / Black-Box (Art.5.3) | Tier-3 Deep Static -> Abstract Spec (Art.6) |
|---|---|---|---|
| **ELF / PE / Mach-O** | `open_binary` -> `binary_overview`, `inspect_binary_layout`, `inspect_pe_resources`, `inspect_macho`, `inspect_signature`, `list_architectures`, `list_segments` | `capture_process_scenario`, `observe_native_calls`, `start_gdb_session`->`gdb_console`, `start_rizin_debug_session`, `instrument_with_frida` | `search_procedures`, `search_strings`, `search_bytes`, `get_call_graph`, `xrefs`, `trace_call_path`, `trace_feature`, `trace_native_values`, `analyze_function`, `procedure_pseudo_code` (abstract immediately!) |
| **Go / Rust / Swift / ObjC** | `inspect_go_binary`, `inspect_rust_binary`, `demangle_swift`, `analyze_swift_types`, `get_objc_classes`, `get_objc_protocols` | `observe_native_ui`, `capture_native_ui_scenario`, `trace_native_ui_action`, `trace_dylib_resolution` | `inspect_native_dispatch_metadata`, `inspect_native_data_type`, `project_apple_application_graph` |
| **.NET / CLI / NativeAOT** | `inspect_managed_artifact`, `inspect_managed_members`, `inspect_managed_native_boundaries` | `capture_process_scenario`, `correlate_static_and_runtime` | `project_managed_application_graph`, `compare_managed_members`, `verify_managed_native_boundaries` |
| **Android APK / DEX / Flutter / Harmony** | `inspect_android_package`, `decode_android_resources`, `identify_flutter_build`, `inspect_dart_aot`, `project_android_application_graph`, `project_harmony_application_graph` | `list_adb_devices`->`inspect_adb_device`, `start_adb_app`, `read_adb_logcat`, `capture_adb_screen`, `pull_adb_package`, `instrument_with_frida` | `search_android_classes`, `inspect_android_class`, `inspect_android_method`, `trace_android_references`, `open_jeb_project`->`decompile_jeb_item` |
| **Electron / JS / Web / ASAR** | `analyze_javascript_application`(`detail:"summary"`), `inspect_electron_fuses`, `analyze_web_bundle` | `list_electron_targets`->`capture_electron_scenario`, `list_browser_targets`->`capture_browser_scenario`, `observe_web_session`, `observe_javascript_runtime`, `reconcile_javascript_runtime` | `trace_application_feature`, `trace_javascript_semantics`, `trace_web_module_imports`, `inspect_web_event_listeners` |
| **WASM / EVM** | `inspect_wasm_artifact`, `inspect_evm_interface`(`detail:"summary"`) | `observe_web_execution` | `compare_wasm_interfaces` |
| **Firmware / Bus / Crash** | `inspect_firmware_regions` -> `extract_firmware`, `inspect_recorded_crash` | `inspect_signal_decoders` -> `decode_signal_recording` | Mount extracted rootfs -> audit `uci`/`nftables`/`systemd`/init/MIPS-ARM binaries |
| **Network / DB / Archives** | `inspect_sqlite_database`(`schema_scope:"database"`), `inspect_artifact`(`detail:"summary"`), `extract_artifact`, `inspect_plist`, `inspect_keyed_archive`, `inspect_asset_catalog` | `inspect_web_network_capture`(`view:{kind:"api-surface"}`), `inspect_pcap_capture`, `inspect_packet_fields`->`inspect_packet_capture` | Map wire frames, SQL DDL, REST/gRPC/WebSocket/QUIC endpoints |

---

## 2. ANTI-TRUNCATION & SHARDING PROTOCOL
1. **Large Graphs / Transport Limits**: On `resource_constraint` or truncated preview -> NEVER re-run producer. Query `parent_evidence_id` via `inspect_analysis_view` (`summary` | `nodes` | `edges` | `occurrences` | `api-surface`) or `get_evidence_bundle`(`detail:"summary"`, filter by `sha256`/`operation`).
2. **Parallel Subagent Sharding**: If target has `>=3` subsystems (e.g. `Net_Protocol` + `SQLite_Store` + `UI_StateMachine`) -> spawn parallel `invoke_subagent` workers in `Room_A` to extract subsystem specs concurrently.
3. **Unknown Ledger**: Log every unresolved format/branch via `record_unknown` -> test hypothesis -> resolve via `update_unknown` + `verify_unknown_resolution`.

---

## 3. SPECIALIZED ABSTRACTION HEURISTICS [ROOM_A -> SPEC]
- **Crypto / Checksums / Framing**: Identify constants (S-boxes, CRC polys, magic headers `0x...`, IV sizes, endianness) via `search_bytes`/`trace_native_values` -> express in Spec as standard algorithm name (`CRC32-IEEE`, `AES-256-GCM`, `HMAC-SHA256`) or pure math/bit-field table (`[offset:u16_be | len:u32_le | payload:[u8] | crc:u32]`).
- **State Machines & IPC**: Convert switch-tables/dispatchers (`inspect_native_dispatch_metadata` / `trace_javascript_semantics`) -> deterministic state transition table (`State_A --[Event/Guard]--> State_B + Action`).
- **DB & Configs**: Convert `inspect_sqlite_database` + plist/JSON/UCI -> normalized DDL schema + validation rules.

---

## 4. EXECUTION PIPELINE [ROOM_A -> WALL -> ROOM_B -> VERIFY]

### PHASE 1 :: ROOM_A [DISCOVERY & OBLIGATION LEDGER]
1. Route target via Matrix -> run Tier-1 + Tier-2 tools (`detail:"summary"`).
2. Fill gaps via Tier-3 tools -> apply **Immediate Abstraction Rule** (strip all proprietary syntax/names).
3. Call `build_reconstruction_obligation_ledger` to lock behavioral requirements.

### PHASE 2 :: CHINESE WALL ARTIFACT [PURE SPEC]
Emit compact `CLEAN_SPEC.md`:
- `ARCH`: Mermaid `flowchart LR` / `stateDiagram-v2`.
- `SCHEMAS`: Byte-exact packet/file tables, SQLite DDL, CLI flags, env vars, IPC/HTTP endpoints.
- `ALGORITHMS`: Pure mathematical/logical step definitions + error/timeout matrix.
- `ATTESTATION`: `"Clean-Room Spec: 100% functional/interop facts, 0% proprietary code expression."`

### PHASE 3 :: ROOM_B [IDIOMATIC SYNTHESIS]
1. Read `CLEAN_SPEC.md` ONLY.
2. Generate clean, modular, production-grade project in target stack (`Rust`/`Go`/`C23`/`Zig`/`Python`/`TS`/`OpenWrt-UCI`).
3. Build + run unit/property/integration tests covering 100% of `CLEAN_SPEC.md` I/O vectors (`caveman shrink -- <build_and_test_cmd>`).

### PHASE 4 :: PARITY GATE [REA VERIFICATION]
1. Run `evaluate_reconstruction_coverage` + `verify_reconstruction`.
2. Run behavioral diff: `compare_process_captures` | `compare_wasm_interfaces` | `compare_javascript_export_shapes` | `verify_managed_native_boundaries`.
3. If mismatch -> refine `Room_B` implementation until `coverage == 100%` -> `close_binary`.
