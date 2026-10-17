---
name: scheria
description: Mobile (Android APK/DEX/Flutter, Apple IPA/Swift), Managed (.NET), and Web/Electron/WASM application graph analysis and modernization via REA.
---

# SCHERIA :: MOBILE, MANAGED & WEB/ELECTRON APPLICATION MODERNIZATION

## 0. SCOPE & STATUTORY COMPLIANCE
- **Purpose**: Analyze and modernize packaged mobile applications (Android/iOS/HarmonyOS), managed assemblies (.NET/CLI), and desktop/web bundles (Electron/JS/WASM) for cross-platform portability and interoperability.
- **Legal Basis**: EU Directive 2009/24/EC Art. 5(1), Art. 5(3), and Art. 6.

---

## 1. APPLICATION GRAPH & MODERNIZATION LOOP (`/goal`)

```text
WHILE (unmapped_components > 0 || bridge_mismatches > 0 || coverage_gate != PASS):
  1. PROJECT application architecture graph (Android / Apple / Harmony / Managed / Web).
  2. INSPECT bytecode, P/Invoke/JNI/N-API bridges, UI hierarchies, and state stores.
  3. DOCUMENT feature flows, API contracts, and export shapes.
  4. VERIFY modernized application parity via REA comparison gates.
```

---

## 2. REA TOOL DISPATCH

### A. ANDROID, FLUTTER & HARMONYOS
- `project_android_application_graph`, `project_harmony_application_graph`, `inspect_android_package`, `search_android_classes`, `inspect_android_class`, `inspect_android_method`, `trace_android_references`.
- Decompilation & Resources: `inspect_jeb_client` -> `open_jeb_project` -> `list_jeb_units` -> `decompile_jeb_item`; `inspect_apktool_client` -> `decode_android_resources`.
- Flutter / Dart AOT: `identify_flutter_build`, `inspect_dart_aot`.
- Device Diagnostics: `list_adb_devices`, `inspect_adb_device`, `list_adb_packages`, `inspect_adb_package`, `read_adb_logcat`, `inspect_adb_display`, `inspect_adb_window`.

### B. APPLE (MACOS / IOS) & .NET MANAGED RUNTIMES
- **Apple**: `project_apple_application_graph`, `inspect_macho`, `inspect_signature`, `demangle_swift`, `analyze_swift_types`, `get_objc_classes`, `get_objc_protocols`, `trace_dylib_resolution`, `observe_native_ui`, `trace_native_ui_action`, `capture_native_ui_scenario`.
- **.NET / CLI / NativeAOT**: `project_managed_application_graph`, `inspect_managed_artifact`, `inspect_managed_members`, `inspect_managed_native_boundaries`, `compare_managed_members`, `verify_managed_native_boundaries`, `import_managed_reconstruction`.

### C. ELECTRON, JAVASCRIPT, WASM & EVM
- **JS / Electron**: `analyze_javascript_application`, `recover_javascript_sources`, `export_web_scripts`, `trace_application_feature`, `trace_javascript_semantics`, `trace_web_module_imports`, `trace_web_source_location`, `inspect_web_event_listeners`, `inspect_electron_fuses`, `list_electron_targets`, `inspect_electron_page`, `reconcile_javascript_runtime`, `compare_source_to_bundle`, `compare_javascript_export_shapes`.
- **WASM & EVM**: `inspect_wasm_artifact`, `compare_wasm_interfaces`, `inspect_evm_interface`.
