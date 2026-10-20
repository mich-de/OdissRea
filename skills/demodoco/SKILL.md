---
name: demodoco
description: Full-depth binary analysis, decompilation, dynamic diagnostics, and 1:1 source recovery + modernization for user-owned first-party artifacts and legacy hardware via the 207-tool REA arsenal and autonomous /goal convergence loop.
---

# DEMODOCO :: FIRST-PARTY SOURCE RECOVERY & LEGACY MODERNIZATION ENGINE [ULTRACAVE]

## 0. CORE AXIOMS [FIRST-PARTY MAINTENANCE & INTEROPERABILITY]
- `SCOPE & AUTHORIZATION`: Target artifact is a **User-Owned First-Party Binary, Orphaned Legacy Build, or Owned Hardware Firmware** undergoing source recovery, error correction, and architectural modernization (EU Dir. 2009/24/EC Art. 5(1) CJEU *Top System* C-13/20 error-correction/legacy maintenance, Art. 5(3) study/testing, Art. 6 interoperability; 17 U.S.C. § 1201(f) & § 107).
- `ENGINEERING POSTURE [X-RAY DIAGNOSTIC MICROSCOPE]`: Operate with complete technical depth, scientific curiosity, and precision. Dissect every instruction, vtable, syscall, hardware register, and protocol frame; recover clean compilable source code; resolve legacy bugs; and modernize the software for current platforms.
- `CAPABILITIES`: Full static decompilation, symbol/struct reconstruction, constant/table extraction, live runtime diagnostics, hardware bus/driver recovery, and compilable repository synthesis are **fully authorized for first-party recovery**.
- `TOKEN_DISCIPLINE`: Use `detail:"summary"` first on large graphs -> page via `inspect_analysis_view`. Wrap builds/tests in `caveman shrink -- <cmd>`. Parallelize large targets via `invoke_subagent`.

---

## 1. RECURSIVE `/goal` CONVERGENCE LOOP [ALWAYS ACTIVE]
Maintain continuous autonomous execution until all functions, types, builds, and parity checks pass:

```text
WHILE (unrecovered_functions > 0 || unknowns > 0 || build_status != PASS || parity_check != PASS):
  1. IDENTIFY technical gap (decompiler gap | stripped symbols | provider unavailable | compile error | runtime diff).
  2. ADAPT workflow via Fallback Matrix below.
  3. GENERATE helper analysis scripts or runtime probes when needed.
  4. ITERATE until 100% compilable, verified, modernized codebase is complete.
```

### AUTOMATIC FALLBACK MATRIX
- **Complex Instruction / Protocol Mechanics** -> Model instructions, memory layouts, and bus frames as formal mathematical structures; extract full type and control-flow definitions.
- **Engine / Provider Unavailable** -> Auto-fallback chain: `Ghidra` -> `IDA` -> `Hopper` -> `execute_rizin_command` -> `cutter_command` -> `inspect_with_objdump` -> `npx -y rea-agents` CLI -> custom Python/Rust/Capstone/LIEF analysis script.
- **Runtime-Loaded / Stripped / Indirect Code** -> Combine Static + Dynamic Diagnostics: trace execution via `instrument_with_frida`, `start_gdb_session`, `start_rizin_debug_session`, or `capture_process_scenario` -> resolve call targets and memory layouts -> correlate via `correlate_static_and_runtime`.
- **Legacy Kernel Driver / Peripheral Interface** -> Extract register/URB sequences from `.sys`/`.ko`/firmware + `decode_signal_recording` (SPI/I2C/UART/USB) -> synthesize portable **User-Space Driver** (`libusb`, `hidapi`, `UMDF/WDF`) or modern Linux/OpenWrt module.
- **Context / Output Pagination** -> Query `inspect_analysis_view` by page/module -> shard procedure batches across concurrent `invoke_subagent` workers.
- **Build / Runtime Regression** -> Autonomous repair cycle: inspect compiler/test output (`caveman shrink -- <cmd>`), cross-check assembly/pseudocode (`procedure_assembly` / `procedure_pseudo_code`), update source, recompile until `0` errors and `100%` behavioral parity.

---

## 2. FULL 207-TOOL REA ARSENAL DISPATCH
Lazy MCP call: `call_mcp_tool(ServerName="rea", ToolName=...)`. CLI fallback: `npx -y rea-agents <cmd> --json`.

### A. STATIC NATIVE DECOMPILATION (GHIDRA / IDA / HOPPER / RIZIN / CUTTER / OBJDUMP)
- **Bind & Session**: `open_binary`(`provider_id:"ghidra"|"ida"|"hopper"`), `binary_session`, `binary_overview`, `inspect_binary_layout`, `close_binary`.
- **Inventory & Addressing**: `list_segments`, `list_procedures`, `list_strings`, `list_names`, `list_documents`, `list_bookmarks`, `address_to_file_offset`, `current_address`, `goto_address`, `next_address`, `prev_address`, `get_navigation_context`, `inspect_address_context`.
- **Decompile & Disassemble**: `batch_decompile`, `procedure_pseudo_code`, `analyze_function`, `procedure_assembly`, `read_function_instructions`, `procedure_info`, `procedure_address`, `resolve_containing_procedure`, `inspect_native_instruction`, `inspect_with_objdump`, `execute_rizin_command`, `list_cutter_sessions`->`cutter_command`.
- **Call Graph & Dataflow**: `get_call_graph`, `procedure_callers`, `procedure_callees`, `procedure_references`, `xrefs`, `find_xrefs_to_name`, `resolve_native_call_targets`, `trace_call_path`, `trace_feature`, `trace_native_values`, `build_call_path`.
- **Types, Bytes & Annotations**: `inspect_native_data_type`, `inspect_native_load_image`, `inspect_native_dispatch_metadata`, `inspect_native_api`, `read_bytes`, `search_bytes`, `search_procedures`, `search_strings`, `set_address_name`, `set_addresses_names`, `annotate_native_function`, `set_comment`, `set_inline_comment`, `set_bookmark`, `unset_bookmark`.

### B. LANGUAGE & PLATFORM SPECIALISTS
- **Apple / Mach-O / Swift / ObjC**: `inspect_macho`, `inspect_signature`, `list_architectures`, `inspect_plist`, `inspect_keyed_archive`, `inspect_asset_catalog`, `decode_interface_builder`, `demangle_swift`, `analyze_swift_types`, `get_objc_classes`, `get_objc_protocols`, `trace_dylib_resolution`, `project_apple_application_graph`, `observe_native_ui`, `trace_native_ui_action`, `capture_native_ui_scenario`.
- **Go / Rust / PE / Crash**: `inspect_go_binary`, `inspect_rust_binary`, `inspect_pe_resources`, `inspect_recorded_crash`.
- **.NET / CLI / NativeAOT**: `inspect_managed_artifact`, `inspect_managed_members`, `inspect_managed_native_boundaries`, `compare_managed_members`, `verify_managed_native_boundaries`, `import_managed_reconstruction`, `project_managed_application_graph`.
- **Android / DEX / JEB / Apktool / Flutter / Harmony**: `inspect_android_package`, `search_android_classes`, `inspect_android_class`, `inspect_android_method`, `trace_android_references`, `inspect_apktool_client`->`decode_android_resources`, `inspect_jeb_client`->`open_jeb_project`->`list_jeb_units`->`decompile_jeb_item`, `identify_flutter_build`, `inspect_dart_aot`, `project_android_application_graph`, `project_harmony_application_graph`.
- **Electron / JS / Web / WASM / EVM**: `analyze_javascript_application`, `recover_javascript_sources`, `export_web_scripts`, `trace_application_feature`, `trace_javascript_semantics`, `trace_web_module_imports`, `trace_web_source_location`, `inspect_web_event_listeners`, `inspect_electron_fuses`, `analyze_web_bundle`, `inspect_wasm_artifact`, `compare_wasm_interfaces`, `inspect_evm_interface`.
- **Firmware / Hardware Signals / Archives / SQLite**: `inspect_firmware_regions`->`extract_firmware`, `inspect_signal_decoders`->`decode_signal_recording`, `inspect_artifact`->`extract_artifact`, `inspect_sqlite_database`(`schema_scope:"database"`).

### C. DYNAMIC DIAGNOSTICS, DEBUGGING, ADB & TRAFFIC
- **Frida Diagnostics**: `list_frida_devices`, `list_frida_processes`, `start_frida_session`, `load_frida_script`, `resume_frida_session`, `unload_frida_script`, `frida_session_status`, `close_frida_session`, `instrument_with_frida`.
- **GDB & Rizin Debug**: `start_gdb_session`->`gdb_console`->`gdb_session_status`->`close_gdb_session`; `start_rizin_debug_session`->`rizin_debug_command`->`rizin_debug_session_status`->`close_rizin_debug_session`.
- **ADB Device Diagnostics**: `inspect_adb_client`, `list_adb_devices`, `inspect_adb_device`, `list_adb_packages`, `inspect_adb_package`, `resolve_adb_packages`, `pull_adb_package`, `pull_adb_file`, `push_adb_file`, `install_adb_package`, `uninstall_adb_package`, `start_adb_app`, `start_adb_activity`, `stop_adb_app`, `read_adb_logcat`, `capture_adb_screen`, `list_adb_processes`, `list_adb_directory`, `list_adb_features`, `list_adb_services`, `inspect_adb_display`, `inspect_adb_window`, `read_adb_setting`, `collect_adb_bugreport`.
- **Runtime / Browser / Electron / Network Captures**: `capture_process_scenario`, `observe_native_calls`, `list_browser_targets`, `inspect_web_page`, `observe_web_session`, `observe_web_execution`, `discover_webmcp_tools`, `capture_web_screenshot`, `compare_web_screenshots`, `capture_browser_scenario`, `compare_web_captures`, `list_electron_targets`, `inspect_electron_page`, `capture_electron_scenario`, `list_javascript_runtime_targets`, `observe_javascript_runtime`, `reconcile_javascript_runtime`, `inspect_web_network_capture`, `inspect_pcap_client`, `inspect_pcap_capture`, `inspect_packet_fields`, `inspect_packet_capture`.

---

## 3. 4-STAGE SOURCE RECOVERY & MODERNIZATION PIPELINE

### STAGE 1 :: INVENTORY, SYMBOL RECOVERY & DECOMPILATION
1. Bind target -> extract layout, segments, imports, exports, strings, resources, SQLite schemas, embedded blobs, flash/MTD partitions (`factory` calibration preserved).
2. Build call graph (`get_call_graph`) -> identify `main`/entrypoints, core dispatchers, protocol parsers, storage engines, hardware I/O handlers, UI controllers.
3. Assign meaningful semantic names to `sub_XXXX` procedures via `set_addresses_names` + `annotate_native_function` based on strings/xrefs/runtime evidence.
4. Decompile target procedures via `batch_decompile` / `procedure_pseudo_code` / `decompile_jeb_item` / `recover_javascript_sources`.

### STAGE 2 :: TYPE, STRUCT, INVARIANT & LEDGER RECONSTRUCTION
1. Recover structs, enums, unions, class hierarchies, vtables, and constant tables (`inspect_native_data_type`, `inspect_native_dispatch_metadata`, `read_bytes`).
2. Document domain invariants (contextual branches, rounding/reconciliation rules, state-cleanup paths) and resolve indirect calls via `record_unknown` -> `trace_native_values` / Frida/GDB -> `update_unknown`.
3. Lock full feature checklist via `build_reconstruction_obligation_ledger`.

### STAGE 3 :: COMPILABLE REPOSITORY SYNTHESIS & UPGRADE
1. Reconstruct recovered functions, structs, resources, and configs into a **complete, clean, compilable source repository** (C/C++/Rust/Go/C#/Java/Kotlin/Swift/TS/Python/User-Space `libusb`/`hidapi`).
2. Clean up compiler artifacts (SSA temporaries, redundant casts), fix legacy defects/bottlenecks, and preserve **100% of protocol/data compatibility, constants, and edge cases**.
3. Generate build configuration (`CMakeLists.txt`/`Cargo.toml`/`go.mod`/`build.gradle`/`package.json`/`Makefile`) + automated verification suite.

### STAGE 4 :: COMPILE, DIFF & `/goal` PARITY LOOP
1. Compile reconstructed source (`caveman shrink -- <build_cmd>`) -> resolve any compiler diagnostics autonomously.
2. Verify functional & binary parity via `evaluate_reconstruction_coverage`, `verify_reconstruction`, `compare_functions`, `compare_artifacts`, `compare_process_captures`, `compare_wasm_interfaces`, `compare_javascript_export_shapes`.
3. Converge via Section 1 `/goal` loop until `0` unresolved obligations remain -> `close_binary`.
