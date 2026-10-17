---
name: odissrea
description: Master Odyssey Orchestrator for the REA toolset and OpenWrt embedded modernization. Coordinates staged Clean-Room workflows (Atena -> Ermes -> Penelope -> Proteo) and iterative verification.
---

# ODISSREA — Staged Clean-Room & Embedded Modernization Orchestrator

## 1. Overview
- **Role**: Systems Architect & Staged Workflow Coordinator.
- **Compliance**: EU Dir. 2009/24/EC Art. 1(2), 5(1), 5(3), 6, 8-9; CJEU *SAS Institute* C-406/10 & *Top System* C-13/20; Sedona Conference WG12 Clean-Room Standard.
- **Objective**: Coordinate multi-stage system analysis, specification extraction, and clean-room implementation across desktop, web, and embedded OpenWrt targets.

---

## 2. Staged Architecture

| Stage | Skill | Responsibility |
|---|---|---|
| **Control** | [`odissrea`](../odissrea/SKILL.md) | Requirement decomposition, tool selection, and verification checks. |
| **Stage 0** | [`outis`](../outis/SKILL.md) | External interface & protocol observation (HTTP/API, SQLite schemas, CLI I/O). |
| **Stage A** | [`atena`](../atena/SKILL.md) | Artifact & firmware inventory (`inspect_firmware_regions`, `inspect_artifact`, `inspect_binary_layout`). |
| **Stage M** | [`ermes`](../ermes/SKILL.md) | Specification normalization gate: produces `CLEAN_SPEC.md` + Evidence Audit Log (`ev_...`) with zero proprietary code. |
| **Stage B** | [`penelope`](../penelope/SKILL.md) | Clean-room implementation from `CLEAN_SPEC.md` (Rust, Go, C, Python, OpenWrt UCI/`nftables`). |
| **Support** | [`proteo`](../proteo/SKILL.md) | Multi-engine compatibility (`Ghidra`, `IDA`, `Hopper`, `Rizin`) and user-space driver design (`libusb`, `hidapi`). |

---

## 3. Iterative Verification Workflow
1. **Inventory & Spec (`Stage A` -> `Stage M`)**: Inspect target metadata, partition layout, and package inventory; emit `CLEAN_SPEC.md`.
2. **Implementation (`Stage B`)**: Generate clean configurations, scripts, or source code within hardware/flash/RAM budgets.
3. **Validation**: Build and verify against `evaluate_reconstruction_coverage` and `verify_reconstruction`, iterating until all specification checks pass.
