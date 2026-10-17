---
name: eolia
description: Network protocol, packet capture (PCAP/HAR/SAZ/qlog), IPC, and hardware bus signal (UART/SPI/I2C/USB) interoperability analysis via REA.
---

# EOLIA (AEOLIA) :: PROTOCOL, PACKET & SIGNAL INTEROPERABILITY

## 0. SCOPE & STATUTORY COMPLIANCE
- **Purpose**: Analyze network traffic captures, RPC/IPC message framing, and hardware logic signals to produce formal protocol specifications, firewall policies, and interoperable clients/servers.
- **Legal Basis**: EU Directive 2009/24/EC Art. 5(3) & Art. 6; CJEU *SAS Institute* C-406/10 (data formats and communication protocols are functional interfaces eligible for clean-room reimplementation).

---

## 1. PROTOCOL & SIGNAL CONVERGENCE LOOP (`/goal`)

```text
WHILE (undocumented_endpoints > 0 || unparsed_frames > 0 || schema_validation != PASS):
  1. CAPTURE or load PCAP/PCAPNG, HAR/SAZ/qlog, or logic analyzer recordings.
  2. EXTRACT framing, headers, state transitions, error codes, and serialization formats.
  3. FORMALIZE OpenAPI / Protobuf / JSON Schema / binary frame state machines.
  4. VERIFY clean-room protocol parity across request/response test vectors.
```

---

## 2. REA TOOL DISPATCH

### A. NETWORK & WEB TRAFFIC INSPECTION
- **PCAP / Wire Captures**: `inspect_pcap_client`, `inspect_pcap_capture`, `inspect_packet_capture`, `inspect_packet_fields`.
- **HTTP / WebSockets / QUIC**: `inspect_web_network_capture` (`HAR`, `SAZ`, `qlog`), `compare_web_captures`.
- **Live Scenario Observation**: `observe_web_session`, `capture_browser_scenario`, `capture_electron_scenario`, `capture_process_scenario`.

### B. HARDWARE BUS & LOGIC SIGNAL DECODING
- `inspect_signal_decoders` -> `decode_signal_recording`: Decode `UART`, `SPI`, `I2C`, `USB`, `CAN`, `JTAG`, `SWD`, and `1-Wire` protocol frames into timestamped transaction tables.
