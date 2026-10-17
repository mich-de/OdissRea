---
name: ogigia
description: Orphaned legacy software, database schema, crash dump, and user-space peripheral driver rescue via REA static/dynamic diagnostics.
---

# OGIGIA (OGYGIA) :: ORPHANED LEGACY SYSTEM & DATA RESCUE

## 0. SCOPE & STATUTORY COMPLIANCE
- **Purpose**: Rescue data, storage schemas, business logic invariants, and peripheral interfaces from orphaned/End-of-Life (EoL) applications, proprietary archives, crash dumps, and legacy kernel drivers.
- **Legal Basis**: EU Directive 2009/24/EC Art. 5(1), Art. 5(3), and Art. 6 (data portability, error correction, and hardware/software interoperability).

---

## 1. LEGACY RESCUE WORKFLOW (`/goal`)

```text
WHILE (unmapped_tables > 0 || unresolved_unknowns > 0 || driver_transfers_unverified > 0):
  1. EXTRACT archives, installers, embedded resources, and SQLite databases.
  2. DIAGNOSE crashes, runtime bottlenecks, and indirect call targets.
  3. DOCUMENT storage schemas, file formats, and USB/HID/serial peripheral protocols.
  4. SYNTHESIZE portable data migrators and user-space drivers (libusb/hidapi).
```

---

## 2. REA TOOL DISPATCH

### A. DATABASE, ARCHIVE & CRASH DIAGNOSTICS
- **SQLite & Storage**: `inspect_sqlite_database`(`schema_scope:"database"`, `table_names:[...]`, `include_row_counts:true`).
- **Containers & Resources**: `inspect_artifact` -> `extract_artifact`, `inspect_pe_resources`, `inspect_plist`, `inspect_keyed_archive`, `inspect_asset_catalog`, `decode_interface_builder`.
- **Crash & Fault Analysis**: `inspect_recorded_crash`, `start_gdb_session` -> `gdb_console`, `start_rizin_debug_session` -> `rizin_debug_command`.

### B. DYNAMIC RUNTIME CORRELATION & UNKNOWN RESOLUTION
- `record_unknown` -> `list_unknowns` -> `update_unknown` -> `verify_unknown_resolution`.
- `capture_process_scenario`, `observe_native_calls`, `instrument_with_frida`, `correlate_static_and_runtime`, `compare_process_captures`.

### C. USER-SPACE PERIPHERAL DRIVER SYNTHESIS
- Inspect legacy `.sys`/`.ko` imports (`IoCallDriver`, `UsbBuildInterruptOrBulkTransferRequest`, `ioctl`) + `decode_signal_recording` -> replace obsolete kernel drivers with portable user-space modules (`libusb`, `hidapi`, `WebUSB`).
