---
name: ea
description: First-party binary-to-source recovery and cross-language modernization (C/C++/ASM to Rust/Go/C23/TS) for user-owned software artifacts via REA static and dynamic analysis.
---

# EA (AEAEA) :: FIRST-PARTY SOURCE RECOVERY & CROSS-LANGUAGE TRANSMUTATION

## 0. SCOPE & STATUTORY COMPLIANCE
- **Purpose**: Recover lost source code, repair defects, and translate user-owned or legitimately licensed legacy binaries into modern, memory-safe languages (`Rust`, `Go`, `C23`, `TypeScript`, `Swift`, `Kotlin`).
- **Legal Basis**: EU Directive 2009/24/EC Art. 5(1) (CJEU *Top System* C-13/20 error correction & maintenance by lawful acquirer) and Art. 6 (interoperability).

---

## 1. SOURCE RECOVERY & TRANSMUTATION LOOP (`/goal`)

```text
WHILE (unrecovered_procedures > 0 || unresolved_types > 0 || build_status != PASS || parity_check != PASS):
  1. INVENTORY segments, symbols, imports, strings, and call graphs via REA.
  2. RECONSTRUCT data structures, vtables, enums, and calling conventions.
  3. DECOMPILE & TRANSLATE procedures into idiomatic target-language modules.
  4. VERIFY compilation, unit tests, and binary/functional parity via REA.
```

---

## 2. REA TOOL DISPATCH

### A. STATIC DECOMPILATION & CALL-GRAPH RECOVERY
- **Session & Layout**: `open_binary`(`provider_id:"ghidra"|"ida"|"hopper"`), `binary_overview`, `inspect_binary_layout`, `list_segments`, `list_procedures`, `list_strings`, `list_names`.
- **Procedure Recovery**: `batch_decompile`, `procedure_pseudo_code`, `analyze_function`, `procedure_assembly`, `read_function_instructions`, `inspect_with_objdump`, `execute_rizin_command`, `cutter_command`.
- **Control & Data Flow**: `get_call_graph`, `procedure_callers`, `procedure_callees`, `xrefs`, `find_xrefs_to_name`, `resolve_native_call_targets`, `trace_call_path`, `trace_feature`, `trace_native_values`.

### B. TYPE, STRUCT & SYMBOL RECONSTRUCTION
- `inspect_native_data_type`, `inspect_native_dispatch_metadata`, `inspect_native_load_image`, `inspect_native_api`, `read_bytes`, `search_bytes`.
- Semantic annotation: `set_address_name`, `set_addresses_names`, `annotate_native_function`, `set_comment`, `set_inline_comment`.
- Language-specific recovery: `inspect_go_binary`, `inspect_rust_binary`, `demangle_swift`, `analyze_swift_types`, `get_objc_classes`, `get_objc_protocols`, `inspect_pe_resources`.

### C. PARITY & OBLIGATION VERIFICATION
- `build_reconstruction_obligation_ledger` -> `evaluate_reconstruction_coverage` -> `verify_reconstruction` -> `compare_functions` -> `compare_artifacts` -> `close_binary`.
