# 🏛️ OdissRea — Universal Digital Repair & Clean-Room Modernization Manual for REA

> `FORMAT`: `ultracave` (high-density, zero-fluff technical specification).  
> `ENGINE`: [REA (Reverse Engineer Anything)](https://github.com/morluto/rea) — 207 MCP tools across Native, Managed, Mobile, Web/Electron, WASM/EVM, Firmware, Databases, and Network Protocols.  
> `ETHOS`: **Anythink** — Universal Pragmatic Interoperability & Right-to-Repair across any vendor lock-in, OS, architecture, or protocol barrier. Think outside box, outside OS.

---

## 0. OPERATIONAL CONTEXT: ABANDONMENT, PRACTICAL HACKING & THE ANYTHINK PRINCIPLE

### A. THE ABANDONMENT CRISIS
- **Definition**: Devices, firmware, and software where original vendor terminated official support.
- **Consequences**: Zero security updates, arbitrary cloud shutdowns, artificial hardware bricking, escalating electronic waste (e-waste).
- **Remedy**: Independent technical repair, reverse engineering, and clean-room firmware reconstruction. Essential for industrial infrastructure continuity, digital sovereignty, and ecological sustainability.

### B. PRACTICAL HACKING (WHITE-HAT HARDWARE/SOFTWARE REVERSING)
- **Methodology**: Action-oriented, non-destructive exploration of physical hardware and compiled binaries without official documentation.
- **Objectives**: Diagnose defects, restore lost access, extract hardware descriptors, synthesize open-source drivers, and modernize software stacks.
- **Core Arsenal**:
  - Hardware buses & debug headers: UART, JTAG, SWD, SPI, I2C.
  - Memory extraction: In-circuit SOIC-8 test clips, hot-air desoldering, SPI/NAND programmers (CH341A, FT232H, Bus Pirate), `flashrom`.
  - Static triage: `strings`, `binwalk`, entropy mapping (`binwalk -E`).
  - Disassembly & Decompilation: Ghidra, IDA Pro, Rizin, Cutter, REA 207-tool MCP server.
  - Dynamic instrumentation & testing: QEMU architecture emulation, Renode board simulation, Frida runtime hooking, Hardware-in-the-Loop (HIL) testbeds.

### C. THE "ANYTHINK" PRINCIPLE (UNIVERSAL INTEROPERABILITY ETHOS)
- **Meaning**: "Whatever you think / need to make it work".
- **Rule**: Not bound to single vendor, OS, or architecture. Open, universal problem-solving ethos: if hardware exists and physics permits, software can be adapted, repaired, and liberated.

---

## 1. LEGAL BACKGROUND & RIGHT TO REPAIR

> Not legal advice. These rules have conditions and vary by country. Work only on devices and software you own or may use. Medical, aviation, utility metering, vehicle and other regulated systems have further rules that copyright exceptions do not touch.

- **Core Axiom**: *"If you can't fix it, you don't own it."*
- **EU Software Directive (2009/24/EC)**:
  - **Art. 5(1)**: absent specific contract terms, a lawful acquirer may perform the acts necessary to use the program as intended, including error correction. CJEU *Top System* C-13/20: this can include decompilation where necessary, under any contract conditions, with the results used only to correct errors.
  - **Art. 5(3)**: a person with a right to use a copy may observe, study or test it while performing acts they are entitled to perform. CJEU *SAS Institute* C-406/10: functionality, programming language and data file formats are not protected as such, but elements of a user manual can be.
  - **Art. 6**: decompilation only where indispensable for the interoperability of an independently created program, by a licensee, for information not already readily available and for the necessary parts only. The results may not be used for a program substantially similar in expression.
  - **Art. 7(1)(c) and Art. 8**: distributing means of removing program protection is sanctioned. Contract terms contrary to Art. 6 or Art. 5(2)-(3) are void, while patents, trade marks, trade secrets and contract law still apply.
- **US Law**:
  - **17 U.S.C. § 1201(f)**: a narrow interoperability exception, for a person with a lawfully obtained right to use the program. **§ 107**: fair use, decided case by case.
  - **FTC, *Nixing the Fix* (2021)**: found scant evidence to support manufacturers' justifications for repair restrictions.
  - **State repair laws**: Minnesota, California, New York and Colorado have enacted them, with scope varying by product.
- **Clean-room process**: supporting evidence of independent creation, not a guarantee. It does not cover patents, contracts, trade marks or technical protection measures.

---

## 2. THE ODISSREA PANTHEON [UNIVERSAL MULTI-AGENT ARCHITECTURE]

```mermaid
flowchart TD
    Ulisse["🏛️ odissrea (Odysseus)\nMaster Target Router & /goal Verification"]
    Lean["⚡ telemaco (Telemachus)\nZero-MCP CLI Fast Path (default first move)"]
    Ulisse --> Lean
    
    subgraph Stage0["Stage 0 :: Black-Box External Observation"]
        Outis["👁️ outis (Outis)\nNetwork, UI, Bus Signals & SQLite Schemas"]
    end

    subgraph StageA["Stage A :: REA Diagnostic Microscope"]
        Atena["🦉 atena (Athena)\nDomain Invariants, Contextual Branches & Obligation Ledgers"]
    end

    subgraph StageM["Stage M :: Spec Normalizer"]
        Ermes["🪽 ermes (Hermes)\nCLEAN_SPEC.md + Audit Logs"]
    end

    subgraph StageB["Stage B :: Isolated Clean-Room Builder"]
        Penelope["🧵 penelope (Penelope)\nIdiomatic Modernization (Rust/Go/C23/TS)"]
    end

    subgraph SpecialistLands["Odyssey Specialist Lands (Domain Engines)"]
        Itaca["🏝️ itaca (Ithaca)\nLegacy ARM/SBC/PC Hardware Preservation & Mainline BSP"]
        Ea["🏝️ ea (Aeaea)\nFirst-Party Source Recovery & Language Transmutation"]
        Ogigia["🏝️ ogigia (Ogygia)\nAbandonware, Database Rescue & User-Space Drivers"]
        Eolia["🏝️ eolia (Aeolia)\nNetwork Protocols, PCAP & Logic Analyzer Signals"]
        Scheria["🏝️ scheria (Scheria)\nMobile (Android/iOS), Managed (.NET) & Web/Electron"]
        Proteo["🌊 proteo (Proteus)\nMulti-Engine Adapter (Ghidra/IDA/Rizin/Frida/GDB/ADB)"]
    end

    Ulisse --> Outis
    Ulisse --> Atena
    Ulisse --> SpecialistLands
    Outis --> Ermes
    Atena --> Ermes
    Ermes --> Penelope
    Penelope --> Verify["✅ REA Parity Gate\nverify_reconstruction"]
    SpecialistLands --> Verify
```

| Skill | Classical Archetype | Universal Engineering Scope |
|---|---|---|
| **[`odissrea`](skills/odissrea/SKILL.md)** | **Odysseus (*Polytropos*)** | Master Orchestrator, universal target router across all 207 REA tools, and iterative `/goal` verification coordinator. |
| **[`telemaco`](skills/telemaco/SKILL.md)** | **Telemachus (*The Telemachy*)** | Default first move: the scouting journey ahead of the full odyssey. Plain Bash/CLI tools (`file`, `readelf`/`otool`, `nm`, `strings`, `jq`, `rg -uu`, `go version -m`, `sqlite3`, `tshark`, `binwalk`) route and inventory any target in 2-4 turns. Escalates to the MCP lands only on a real gap. Distilled from [leanrea](https://github.com/aicodeking/leanrea) (MIT), adapted to Linux-native tooling. |
| **[`outis`](skills/outis/SKILL.md)** | **Outis (*External Observer*)** | `Stage_0` Black-Box Behavioral & Protocol Analyst: inspects HTTP/HAR/SAZ/PCAP, CLI/UI scenarios, SQLite schemas, and logic signals without decompilation. |
| **[`atena`](skills/atena/SKILL.md)** | **Athena (*Metis & Techne*)** | `Stage_A` REA Diagnostic Microscope: extracts hidden domain invariants, contextual edge-cases, data schemas, and formal obligation ledgers (`build_reconstruction_obligation_ledger`). |
| **[`ermes`](skills/ermes/SKILL.md)** | **Hermes (*Boundary Monitor*)** | `Stage_M` Specification Gate: normalizes `Stage_A` findings into a functional `CLEAN_SPEC.md` + timestamped `AUDIT_LOG` (`ev_...`), keeping out code and internal names. |
| **[`penelope`](skills/penelope/SKILL.md)** | **Penelope (*The Weaver*)** | `Stage_B` Isolated Clean-Room Builder: consumes **only** `CLEAN_SPEC.md` to architect and test original code (`Rust`, `Go`, `C23`, `Zig`, `Python`, `TS`, `Swift`, `Kotlin`, `UCI`, `libusb`). |
| **[`proteo`](skills/proteo/SKILL.md)** | **Proteus (*Multi-Engine*)** | Multi-Engine Adapter (`Ghidra` <-> `IDA` <-> `Hopper` <-> `Rizin` <-> `JEB` <-> `Frida` <-> `GDB` <-> `ADB`) & First-Party Legacy Source Recovery. |
| **[`itaca`](skills/itaca/SKILL.md)** | **Ithaca (*Homeland Hardware*)** | Legacy ARM, Mobile, SBC & PC Hardware Preservation: DTB/DTS reconstruction, vendor `.ko`/HAL interoperability, and mainline Linux/postmarketOS/LineageOS porting. |
| **[`ea`](skills/ea/SKILL.md)** | **Aeaea (*Transmutation Island*)** | First-Party Source Recovery & Cross-Language Transmutation: decompile and translate owned C/C++/ASM binaries into modern `Rust`, `Go`, `C23`, or `TypeScript`. |
| **[`ogigia`](skills/ogigia/SKILL.md)** | **Ogygia (*Orphaned Systems*)** | Abandonware, Database & Peripheral Rescue: recover SQLite schemas, crash dumps, proprietary archives, and synthesize user-space drivers (`libusb`/`hidapi`). |
| **[`eolia`](skills/eolia/SKILL.md)** | **Aeolia (*Winds & Flows*)** | Network Protocol, Packet (`PCAP`/`HAR`/`SAZ`/`qlog`) & Hardware Bus Signal (`UART`/`SPI`/`I2C`/`USB`) Interoperability Analysis. |
| **[`scheria`](skills/scheria/SKILL.md)** | **Scheria (*Phaeacian Port*)** | Mobile (`Android APK`/`DEX`/`Flutter`, `Apple IPA`/`Swift`), Managed (`.NET`), and `Electron`/`Web`/`WASM` Application Graph Modernization. |
| **[`tiresia`](skills/tiresia/SKILL.md)** | **Tiresias (*The Seer*)** | All-in-One Tri-Stage Clean-Room Specification & Modernization Engine: reveals the complete path (Stage A→M→B) in one standalone skill. |
| **[`demodoco`](skills/demodoco/SKILL.md)** | **Demodocus (*The Bard*)** | All-in-One First-Party Legacy Source Recovery & Modernization Engine: reconstructs and re-sings the whole lost tale (the original source) standalone. |
| **[`antirez-cleanroom`](skills/antirez-cleanroom/SKILL.md)** | **Clean-Room Process** | Reimplementation from specifications and test oracles, with separated contexts, hidden tests and provenance logging, using the `odissrea-cleanroom-mcp` tools. Includes a path for third-party `.exe`/`.apk` targets, observed from outside. Inspired by [antirez's Z80 experiment](https://antirez.com/news/160); not affiliated with or endorsed by him. |

---

## 3. INSTALLATION
```bash
git clone https://github.com/mich-de/OdissRea.git ~/.local/share/odissrea && ~/.local/share/odissrea/install.sh
```
Keep the clone: the MCP configuration points to the server inside it. On Windows, run `install_cleanroom.ps1` from the clone.

Target directories automatically populated:
- `~/.gemini/config/skills/`
- `~/.claude/skills/`
- `~/.config/opencode/skills/`

The installer merges `odissrea-cleanroom-mcp` into `~/.gemini/config/mcp_config.json`, keeping other servers and saving a timestamped backup.

### Clean-room MCP server
`mcp/odissrea_cleanroom_server.py` and the [`antirez-cleanroom`](skills/antirez-cleanroom/SKILL.md) skill provide process tooling. They do not grant authorization, prove independent creation or replace legal advice. Python 3.12 standard library only.

| Tool | Purpose | Limit |
|---|---|---|
| `assess_legal_posture` | Blockers, conditions and risks for a planned reimplementation | Self-declared inputs, no clearance |
| `scaffold_clean_spec` | Spec template by system type | Unfilled, never overwrites |
| `validate_boundary_hygiene` | Known decompiler residue and copyright notices | Cannot detect renamed or paraphrased copying |
| `setup_parity_oracle` | Golden vector harness | Proves only what the vectors cover; text stdin/stdout |
| `record_audit_provenance` | Hash-chained log with a Stage B separation check | Self-declared; a full rewrite is not detected |
| `verify_audit_chain` | Chain check and last hash | Needs an external anchor to catch a full rewrite |

- **Configuration**: paths are confined to `ODISSREA_WORKSPACE` (default: the server's working directory).
- **Tests**: `python -m unittest discover tests`.
- **Oracle discipline**: visible test vectors can be passed by a program that only replays them. The skill also requires hidden tests, live comparison with the original where it can be run, a fake candidate that must fail, and injected defects.

**Field test**: `tree.com` on Windows 11 ARM64 was observed from outside only, specified, and rebuilt in a separate context as a new program with its own wording.

| Check | Result |
|---|---|
| Output body against the live original, on random trees unseen by the builder, plus targeted cases | 99/99 |
| Fake candidate replaying the public examples | Stopped, 4/99 |
| Injected defects, run before the final fixes | 25 of 26 stopped |
| 20,400 entries, redirected output | 0.067 s against 0.160 s |

One small tool on one machine: Italian locale, code page 1252, NTFS. Headers, messages and some behaviors differ on purpose. Isolation was instructed, not enforced: the builder's own tests walked drive `C:` against its rules, so use a sandbox when separation matters. Larger or server-dependent software has not been tested.

### How to recreate an existing program: practical guide
You can use this for a program you have a lawful right to use. The new program reproduces behavior, not code, assets, name or branding. It does not bypass license checks or DRM, and it cannot give access to a vendor's servers.

**How the analysis works**

| Step | Session | Sees | Produces |
|---|---|---|---|
| 1. Intake | Main | Your facts, license terms | Blockers and risks from `assess_legal_posture` |
| 2. Observation | Observer, in a disposable VM or emulator | The program running: UI, files, formats, network | Notes on external behavior |
| 3. Specification | Main | The observer's notes | `CLEAN_SPEC.md`, public vectors, hidden tests |
| 4. Build | **New session** | Only the spec and public vectors | The new program |
| 5. Verification | **Separate session** | Program, spec, hidden tests | Test results, bugs, signs of copying |

By default the program is not decompiled. Use one folder for the new project and a different one for hidden tests and observation notes. Prompts are in Italian: replace every `<placeholder>` with true facts, and say so when a fact is unknown.

**Prompt 1, intake and plan.** Start here, in a folder for the analysis:
```text
Usa la skill antirez-cleanroom. Voglio ricreare da zero <programma, versione>, per uso personale.
Copia: <licenza acquistata / gratuita> da <sito ufficiale>. Giurisdizione: UE.
Licenza: <testo o link, oppure "non letta">.
Uso solo queste funzioni: <funzione 1>, <funzione 2>.
Voglio migliorare: <velocità, consumi, interfaccia...>. Stack preferito: <linguaggio, oppure "scegli tu">.
Esegui assess_legal_posture, elenca blocchi e rischi e proponi un piano. Non iniziare finché non confermo.
```

**Prompt 2, observation:**
```text
Fase di osservazione: lancia un subagent che analizzi <programma> solo dall'esterno, in <VM o emulatore>,
senza dati personali. Può usarlo e registrare interfaccia, file scritti, formati e traffico per <funzioni>.
Non deve decompilare, leggere i byte del programma né aggirare protezioni: se servisse, si ferma e me lo chiede.
Output: note con il comportamento, separando fatti osservati e ipotesi, senza testi copiati dai manuali.
```

**Prompt 3, specification and tests:**
```text
Dalle note scrivi CLEAN_SPEC.md in <cartella progetto> con scaffold_clean_spec, solo per <funzioni>, con parole
tue e nessun testo, codice o nome interno dell'originale. Aggiungi le mie modifiche volute: <elenco>.
Crea vettori pubblici con setup_parity_oracle e test nascosti in <altra cartella>.
Se il programma si può eseguire in sicurezza, confronta dal vivo su input generati al momento.
Verifica che tutti i test falliscano senza programma, poi esegui validate_boundary_hygiene.
```

**Prompt 4, build.** Open a **new** session in the project folder, not `/clear` in a session that has seen the notes:
```text
Implementa il programma leggendo solo CLEAN_SPEC.md e oracle/. Non usare internet, non eseguire o cercare
<programma originale> né codice simile, non leggere altre cartelle e non modificare spec o test.
Altri test che non puoi vedere giudicheranno il risultato. Se la spec è incompleta, fermati e dimmelo.
```

**Prompt 5, verification.** Back in the analysis session:
```text
Esegui vettori pubblici e test nascosti su <cartella progetto>. Verifica l'oracolo con un programma finto che
ripete i vettori e con difetti iniettati su una copia. Poi lancia una revisione in un contesto separato per
bug e segni di copia. Registra le fasi con record_audit_provenance e chiudi con verify_audit_chain.
Riporta cosa non è stato testato o riprodotto.
```

**Worked example, `tree.com`.** Prompt 1 becomes:
```text
Usa la skill antirez-cleanroom. Voglio ricreare da zero tree.com di Windows 11, con un nome nuovo.
Copia: inclusa nella mia licenza Windows. Giurisdizione: UE. Licenza: non letta.
Uso: elenco cartelle con /F e /A. Voglio migliorare: exit code sugli errori e path oltre 260 caratteri.
Esegui assess_legal_posture, elenca blocchi e rischi e proponi un piano. Non iniziare finché non confermo.
```
Observation ran the command on generated folders and captured raw output. The hidden test then compared the new program with the real command on random trees. See the results in the field test above.

**Worked example, an archiver inspired by WinRAR.** Not yet run end to end. The result is your own archiver with its own name and design, compatible on open formats and able to read RAR files. It does not create RAR files or look like the original, and it reuses no code, icons, text or key generator. WinRAR and RAR are the property of their owners; this project is not affiliated with them.

Intake:
```text
Usa la skill antirez-cleanroom. Voglio creare da zero un archiver per uso personale, ispirato alle funzioni
di WinRAR <versione>, con nome e grafica propri. Copia: <licenza acquistata / trial> da win-rar.com.
Giurisdizione: UE. Licenza: <testo o link, oppure "non letta">.
Uso solo: creare ed estrarre ZIP e 7z, estrarre RAR, test archivi, menu contestuale.
Voglio migliorare: multi-thread su Windows ARM64, interfaccia essenziale.
Esegui assess_legal_posture, elenca blocchi e rischi, compresa la licenza di UnRAR, e proponi un piano.
Non iniziare finché non confermo.
```

Observation:
```text
Lancia un subagent che osservi WinRAR dall'esterno, in una VM senza dati personali: flussi d'uso, opzioni che uso,
messaggi di stato, comportamento su archivi corrotti. Non deve decompilare, leggere i byte del programma,
copiare testi o grafica, né toccare licenza e attivazione. Se servisse, si ferma e me lo chiede.
Output: note sul comportamento, separando fatti osservati e ipotesi.
```

Specification and tests:
```text
Dalle note scrivi CLEAN_SPEC.md con parole tue. Formati: usa solo specifiche ZIP e 7z pubbliche.
RAR: sola estrazione, tramite una libreria di cui hai controllato la licenza.
Crea vettori pubblici e test nascosti in un'altra cartella. Confronta il contenuto estratto con quello
di WinRAR su archivi generati al momento. Non puntare a un'interfaccia uguale.
```

Build, in a new session:
```text
Implementa leggendo solo CLEAN_SPEC.md e oracle/. Non usare internet, non eseguire WinRAR, non cercare codice
simile e non leggere altre cartelle. Se la spec è incompleta, fermati e dimmelo.
```

Then verify with prompt 5. Check the UnRAR license text yourself before relying on any RAR library.

**What to expect**
- Good fit: local tools and documented formats. Rebuild a subset of large products.
- Features that need vendor servers need your own compatible backend, or are dropped.
- Stop and ask a lawyer when rights are unclear or the program will be distributed or sold.
- A separate session is instructed, not enforced, so use a sandbox when separation matters.

The film *Automata* (2014) inspired the framing: a rule forbidding independent repair resembles vendor lock-in. The metaphor stops there: it does not apply to the safety limits of AI models, and it is not a legal argument.

---

## 4. STANDARD 5-PHASE FIRMWARE & HARDWARE REVERSE ENGINEERING PIPELINE

```mermaid
flowchart LR
    P1["Phase 1: Physical Access & UART"] --> P2["Phase 2: Firmware Acquisition"]
    P2 --> P3["Phase 3: Static Analysis"]
    P3 --> P4["Phase 4: Dynamic Reversing & Emulation"]
    P4 --> P5["Phase 5: HIL Validation & Deploy"]
```

### PHASE 1 :: PHYSICAL ACCESS & DEBUG HEADERS
1. Visually inspect PCB under microscope/magnifier for unpopulated 3-pin or 4-pin headers and test pads.
2. Probe pads with digital multimeter (continuity test to ground for GND, identify TX with fluctuating voltage on boot, RX high impedance, VCC steady 3.3V/5V — DO NOT connect VCC to USB serial adapter).
3. Connect 3.3V USB-to-TTL adapter (FTDI FT232H / CP2102). Set serial parameters (default `115200 8N1`, try `57600`, `38400`, `9600`).
4. Read boot log. Send keystroke (Space / Enter / `Ctrl+C`) during boot countdown to drop into **U-Boot shell**.
5. Inside U-Boot:
   ```bash
   printenv            # inspect bootcmd, bootargs, load addresses
   md.b <addr> <len>   # inspect memory contents
   sf probe 0          # initialize SPI flash
   ```

### PHASE 2 :: FIRMWARE ACQUISITION
1. If serial disabled or locked: locate SPI NOR/NAND flash (e.g. Winbond W25Q128, Macronix MX25L).
2. Attach 3.3V SOIC-8 clip directly to chip in-circuit. If pull-up resistors cause bus contention, desolder chip using hot-air rework station (350°C).
3. Connect to CH341A / Bus Pirate / FT232H programmer.
4. Dump full flash image with `flashrom`:
   ```bash
   flashrom -p ch341a_spi -r dump1.bin
   flashrom -p ch341a_spi -r dump2.bin
   cmp dump1.bin dump2.bin   # ensure byte-perfect parity
   ```

### PHASE 3 :: STATIC ANALYSIS & EXTRACTION
1. Scan strings, file headers, and certificates:
   ```bash
   file dump1.bin
   strings -n 10 dump1.bin | grep -Ei "admin|root|password|http|dropbear|secret|board"
   ```
2. Measure entropy and extract filesystems:
   ```bash
   binwalk -E dump1.bin      # high entropy = compressed/encrypted; low = plaintext/code
   binwalk -Me dump1.bin     # recursively unpack SquashFS, CramFS, JFFS2, Ext4, kernel
   ```
3. Inspect unpacked root filesystem: examine `/etc/shadow`, `/etc/passwd`, `/etc/init.d/*`, web server CGI scripts, NVRAM utility binaries.

### PHASE 4 :: DYNAMIC REVERSING, EMULATION & INSTRUMENTATION
1. Load target binaries into Ghidra / IDA Pro / Rizin via OdissRea (`atena`, `proteo`, `ea`).
2. Identify CPU architecture (ARMv7, ARM64, MIPS, RISC-V), endianness, base address.
3. Locate authentication routines, checksum verifiers, firmware update signature checks.
4. **Full-System Emulation**:
   ```bash
   qemu-system-mips -M malta -kernel vmlinux -drive file=rootfs.ext4,format=raw -append "root=/dev/sda console=ttyS0"
   ```
5. **User-Space Emulation**:
   ```bash
   qemu-arm-static -L ./extracted_rootfs ./extracted_rootfs/usr/sbin/httpd
   ```
6. **Simulation**: Use **Renode** for bare-metal microcontroller simulation (Cortex-M) and synthetic sensor feeds.
7. **Runtime Tracing**: Hook procedures via **Frida** (`instrument_with_frida`) or **GDB** (`start_gdb_session`) to log arguments, unpack encrypted payloads, and verify state machines.

### PHASE 5 :: VALIDATION & HARDWARE-IN-THE-LOOP (HIL)
1. Verify patches or modernized firmware in emulator/simulator before flashing physical hardware.
2. For industrial PLCs and safety-critical controllers: execute automated HIL tests with microcontrollers generating synthetic sensor inputs.
3. Rebuild firmware image (`mksquashfs`, `mkimage`) and flash via U-Boot TFTP or external programmer.

---

## 5. THE CAVEMAN WORKBENCH [ESSENTIAL BOM & LAB SETUP]

Bill of Materials for modern digital repair lab. Buy cheap, buy twice. Buy quality, buy once.

- **Vision & Magnification**: Stereo microscope (AmScope / Trinocular), digital USB microscope, adjustable LED ring light.
- **Probing & Logic**: Saleae Logic Pro 16 / DSLogic Plus, Rigol DS1054Z oscilloscope, digital multimeter with audible continuity buzzer.
- **Solder & Rework**: Hakko FX-888D soldering station, 858D hot-air rework station, Chip Quik low-temp removal alloy, tacky flux gel, Kapton high-temperature tape, 99.9% isopropyl alcohol (IPA).
- **Programmers & Adapters**:
  - **CH341A** (with **1.8V adapter module** — CRITICAL for modern 1.8V NAND/NOR flash).
  - **FT232H / FT2232H** breakout boards (high-speed UART/SPI/JTAG/Bitbang).
  - **J-Link / ST-Link V2 / Raspberry Pi** (for OpenOCD SWD/JTAG).
  - **CANable / PCAN-USB** (for automotive/industrial CAN-Bus).
  - **HackRF One / Yard Stick One** (for Sub-GHz / RF analysis).
- **Software Stack**: Linux host (Debian/Ubuntu/Parrot/Kali), `flashrom`, `binwalk`, `Ghidra`, `QEMU`, `Renode`, `Wireshark`, `PlatformIO`, REA MCP server.

---

## 6. ANYTHINK FIELD DIRECTIVES [CAVEMAN ULTRA SURVIVAL GUIDE]

- **Rule 1: Trust No Silicon.** Assume every pin is debug. Probe everything. Multimeter && logic analyzer are primary weapons.
- **Rule 2: Cloud is Lie.** Local control > Vendor cloud. If cloud dead == device dead. Cut cord. Build local bridge.
- **Rule 3: Binary is Truth.** Marketing lies. Code doesn't. Strings dump reveals secrets. Entropy map reveals crypto.
- **Rule 4: Emulate Before Flash.** Bricked hardware == sad caveman. QEMU/Renode first. HIL second. Flash last.
- **Rule 5: Clean-Room is Shield.** Copying code == copyright risk. Copying functional logic == freedom. `ermes` spec -> `penelope` build. Zero IP contamination.
- **Rule 6: Right to Repair is Law.** EU Directive 2009/24/EC && US DMCA 1201(f) are shields. Wield them. Document everything.

---

## 7. REAL-WORLD MISSIONS & ACTION QUESTS [THE 20 ANYTHINK CASE STUDIES]

### MISSION 1: MIKROTIK mAP2n ROUTER — RESTORE SSH ON ABANDONED BOX
- **PROBLEM**: Abandoned router. Vendor firmware obsolete. Wi-Fi dead. No SSH access.
- **ACTION**:
  1. Open casing. Identify UART test pads on PCB.
  2. Solder wires to TX/RX/GND. Connect FTDI adapter at 115200 baud.
  3. Power on. Hit spacebar inside 2s countdown. Enter U-Boot shell.
  4. Inspect environment: `printenv bootcmd`.
  5. Dump SPI flash: `sf probe 0 && sf read 0x80600000 0x0 0x1000000`.
  6. Dump memory to host via TFTP or serial hex dump (`router.bin`).
  7. Unpack: `binwalk -Me router.bin`. Locate rootfs.
  8. Inject modern public SSH key into `/etc/dropbear/authorized_keys`.
  9. Rebuild clean OpenWrt image via ImageBuilder.
  10. Load image via TFTP: `tftpboot 0x80600000 openwrt-ramips.bin`. Flash and reboot.
- **RESULT**: Orphaned router salvaged. Modern SSH access restored. Zero e-waste.

### MISSION 2: TP-LINK TL-WR340GD — BYPASS HARDCODED ADMIN PASSWORD
- **PROBLEM**: No exposed serial shell. Vendor discontinued support. Default admin password leaked/locked.
- **ACTION**:
  1. Identify Atheros SoC + Winbond W25Q128 SPI NOR flash chip.
  2. Desolder SPI chip with hot-air rework station (350°C).
  3. Mount chip into CH341A socket. Run `flashrom -p ch341a_spi -r firmware.bin`.
  4. Run `strings -n 16 firmware.bin | grep "TP-LINK"`.
  5. Locate plaintext administrative credentials in web server string table.
  6. Open HTTP server binary in Ghidra via `atena`.
  7. Find function comparing credentials via `strcmp`.
  8. Patch conditional jump / force return code 0 (success).
  9. Repack rootfs with `mksquashfs`. Splice patched filesystem into firmware binary.
  10. Write patched image back to SPI flash with `flashrom`. Resolder chip to board.
- **RESULT**: Administrative root access restored. Hardcoded password flaw eliminated.

### MISSION 3: INDUSTRIAL PLC CONTROLLER — EXTEND CRITICAL LIFECYCLE
- **PROBLEM**: Legacy factory PLC controller. Vendor defunct. New controller costs $50,000 + recertification downtime.
- **ACTION**:
  1. Connect Saleae Logic Analyzer to internal SPI bus lines between MCU and EEPROM.
  2. Capture transaction frames during power-on and sensor read cycles.
  3. Load PLC binary into Renode simulator. Map MMIO registers.
  4. Hook sensor reading functions to trace calibration calculations.
  5. Modify firmware to accept modern digital sensor calibration values stored in EEPROM.
  6. Run HIL testbed with RP2040 generating simulated sensor voltages.
  7. Flash verified patch back to physical controller.
- **RESULT**: Machine lifespan extended 10+ years. $50k replacement cost avoided. Safety certification maintained.

### MISSION 4: FITNESS TRACKER (BRAND X) — LIBERATE PROPRIETARY DATA TO LOCAL API
- **PROBLEM**: Proprietary wearable. Cloud servers decommissioned. Device unusable without vendor backend.
- **ACTION**:
  1. Sniff Bluetooth Low Energy (BLE) GATT packets with Wireshark + nRF Sniffer.
  2. Decompile companion Android APK with OdissRea `scheria` (`inspect_android_package`, `decompile_jeb_item`).
  3. Extract AES encryption key and session handshake from native library (`libtracker.so`).
  4. Write standalone Python daemon with `bleak` to emulate mobile app BLE handshake.
  5. Decrypt binary GATT notifications. Parse heart rate, step count, and sleep frames.
  6 forward decoded metrics directly to local Home Assistant / InfluxDB instance.
- **RESULT**: Device liberated from defunct cloud. Works 100% locally with zero data leakage.

### MISSION 5: SMART HOME LIGHT BULB — LOCAL OTA & SECURITY HARDENING
- **PROBLEM**: IoT light bulb queries closed cloud update server. Firm shutdown leaves bulb exposed to network attacks.
- **ACTION**:
  1. Intercept outbound firmware check with `mitmproxy`.
  2. Capture signed update payload. Extract archive (tar containing SquashFS).
  3. Unpack SquashFS. Locate update verification script.
  4. Patch script to disable cloud TLS signature enforcement or trust internal root CA.
  5. Repack rootfs. Flash patched firmware via UART test header.
  6. Reconfigure device to point to internal LAN OTA server (ESPHome / local MQTT broker).
- **RESULT**: Network vulnerability closed. Bulb managed entirely on private LAN.

### MISSION 6: ABANDONWARE ARM SMARTPHONE / SBC -> MAINLINE LINUX (`itaca`)
- **PROBLEM**: EoL ARMv7/AArch64 phone or SBC stuck on vendor Android 5/6 (kernel 3.4/3.10); vendor dropped support.
- **ACTION**:
  1. `inspect_firmware_regions` -> `extract_firmware` (`boot.img`, `vendor.img`, `dtbo.img`, `super.img`).
  2. Extract `/sys/firmware/fdt` or `boot.img` DTB -> `dtc -I dtb -O dts -o board.dts`.
  3. `open_binary` on vendor `.ko` modules & `hardware/*.so` -> `batch_decompile`, `inspect_native_data_type`. Recover MMIO base addresses, GIC interrupts, pinctrl states, regmap sequences, PMIC voltage rails, MIPI-DSI panel timings.
  4. `list_adb_devices` -> `pull_adb_file` (`/proc/iomem`, `/proc/interrupts`, `/sys/kernel/debug/clk/clk_summary`, `/sys/kernel/debug/gpio`).
  5. `build_reconstruction_obligation_ledger` -> synthesize clean mainline `.dts`/`.dtsi`, U-Boot defconfig, `postmarketOS` APKBUILD or `LineageOS` device tree -> `verify_reconstruction`.
- **RESULT**: Phone runs modern mainline Linux 6.x / postmarketOS with upstream security patches.

### MISSION 7: ORPHANED USB / SERIAL PERIPHERAL -> USER-SPACE DRIVER (`ogigia` + `eolia`)
- **PROBLEM**: Scientific instrument, audio interface, or industrial scanner only has 32-bit Windows XP/7 `.sys` driver; modern OS blocks unsigned/legacy kernel driver.
- **ACTION**:
  1. `open_binary` on legacy `.sys`/`.dll` -> `list_procedures`, `find_xrefs_to_name` (`IoCallDriver`, `UsbBuildInterruptOrBulkTransferRequest`, `DeviceIoControl`).
  2. `procedure_pseudo_code` + `inspect_native_data_type` -> extract USB control transfers (`bmRequestType`, `bRequest`, `wValue`, `wIndex`), bulk endpoints, and command/response structs.
  3. `decode_signal_recording` on USB/UART/SPI logic capture -> cross-check initialization handshake and timing invariants.
  4. Synthesize portable zero-kernel-dependency driver in `Rust` (`rusb`/`hidapi`), `C` (`libusb-1.0`), or `TypeScript` (`WebUSB`/`WebHID`) -> validate via `compare_process_captures`.
- **RESULT**: Hardware functions natively on modern Linux/macOS/Windows without kernel drivers.

### MISSION 8: LOST-SOURCE NATIVE DAEMON -> MEMORY-SAFE RUST / GO (`ea` + `proteo`)
- **PROBLEM**: Critical proprietary daemon or CLI tool has no surviving source code; needs security hardening, ARM64 port, or memory-safety migration.
- **ACTION**:
  1. `open_binary`(`provider_id:"ghidra"|"ida"|"hopper"`) -> `binary_overview`, `get_call_graph`, `list_procedures`.
  2. `batch_decompile` + `inspect_native_data_type` + `inspect_native_dispatch_metadata` -> recover structs, enums, vtables, state machines, lookup tables (`read_bytes`).
  3. Resolve indirect calls via `record_unknown` -> `instrument_with_frida` / `start_gdb_session` -> `correlate_static_and_runtime` -> `update_unknown`.
  4. Translate into idiomatic `Rust`/`Go`/`C23`, compile (`caveman shrink -- cargo test`), and prove 1:1 parity via `compare_functions` + `verify_reconstruction`.
- **RESULT**: Memory-safe, compilable source code recovered and verified.

### MISSION 9: LEGACY DESKTOP / SAAS SUITE -> CLEAN-ROOM RE-ARCHITECTURE (`outis` -> `atena` -> `ermes` -> `penelope`)
- **PROBLEM**: Bloated legacy Electron/.NET/native software suite needs an original, high-performance modern replacement that reuses none of its code or assets.
- **ACTION**:
  1. **`outis` (`Stage_0`)**: `capture_process_scenario` / `capture_browser_scenario` + `inspect_sqlite_database`(`schema_scope:"database"`) + `inspect_web_network_capture` (`HAR`).
  2. **`atena` (`Stage_A`)**: Extract hidden domain invariants (contextual edge-case branches, exact decimal rounding/reconciliation rules, state-cleanup paths, legacy bugs tagged `DO_NOT_REPLICATE`) -> `build_reconstruction_obligation_ledger`.
  3. **`ermes` (`Stage_M`)**: Remove code and internal names -> emit formal mathematical `CLEAN_SPEC.md` + timestamped `AUDIT_LOG` (`ev_...`).
  4. **`penelope` (`Stage_B`)**: Consume **only** `CLEAN_SPEC.md` -> weave clean modern codebase + property-based test suite -> verify `100%` ledger coverage via `evaluate_reconstruction_coverage`.
- **RESULT**: Completely independent, high-performance clean-room software with a provenance log.

### MISSION 10: EMBEDDED ROUTER & LAN FIREWALL PROFILING (`itaca` + `eolia`)
- **PROBLEM**: Constrained router (e.g. 16 MB Flash / 128 MB RAM) needs custom OpenWrt firmware, RAM-backed DNS sinkhole, VPN client tunnel, and deterministic LAN device egress firewall rules.
- **ACTION**:
  1. `inspect_firmware_regions` -> `extract_firmware` -> verify flash partition layout (`u-boot`, `factory` RF calibration, `firmware` SquashFS) and hardware offload path (`flow_offloading_hw`).
  2. `inspect_pcap_capture` -> `inspect_packet_fields` on appliance/LAN device traffic -> map exact DNS queries, SNI/endpoints, L4 ports, and keepalive intervals.
  3. Synthesize declarative `UCI` / `nftables` (`fw4`) configuration, tmpfs-backed `dnsmasq` blocklists, and `wireguard` policy routing -> verify zero flash wear and deterministic packet forwarding.
- **RESULT**: Hardened custom router running modern OpenWrt with zero-waste RAM storage and granular egress controls.

### MISSION 11: MOBILE & CROSS-PLATFORM APP MODERNIZATION (`scheria`)
- **PROBLEM**: Orphaned Android (`APK`/`DEX`/`Flutter`), iOS (`Mach-O`/`Swift`), or `.NET` client needs API/bridge recovery to keep working with self-hosted backend or modern OS.
- **ACTION**:
  1. `project_android_application_graph` / `project_apple_application_graph` / `project_managed_application_graph`.
  2. `decompile_jeb_item` / `inspect_dart_aot` / `analyze_swift_types` / `inspect_managed_native_boundaries` -> map JNI/FFI/P-Invoke contracts, certificate pinning config, protobuf/JSON payloads, and local encrypted storage schemas.
  3. Build compatible self-hosted server or modernized client -> verify via `compare_artifacts` and `verify_reconstruction`.
- **RESULT**: Full client/server interoperability maintained without relying on defunct cloud backends.

### MISSION 12: AUTOMOTIVE CAN-BUS INFOTAINMENT / ECU — LIBERATE FROM DEALER LOCK
- **PROBLEM**: EoL vehicle head unit. Map updates discontinued. Dealer demands $2k replacement. Component Protection (CP) locks aftermarket parts.
- **ACTION**:
  1. Tap CAN-H / CAN-L on OBD-II. Sniff with SavvyCAN / PCAN.
  2. `eolia` -> `decode_signal_recording` -> isolate UDS (ISO 14229) diagnostic sessions.
  3. Identify Security Access (Service 0x27) seed/key algorithm via ECU firmware dump.
  4. `atena` + `proteo` -> decompile `SecurityAccess.dll` / native ECU binary. Extract crypto primitive (custom XOR/LFSR or AES-CMAC).
  5. Write Python/CANable script to unlock ECU.
  6. Read/write EEPROM via K-Line or SPI. Patch CP bytes.
  7. Inject open-source nav stack (Navit / OsmAnd) via Android Automotive root access or custom Linux payload.
- **RESULT**: Head unit unlocked. Free map updates. Aftermarket parts coded. Zero dealer dependency.

### MISSION 13: LEGACY MEDICAL IMAGING WORKSTATION (DICOM) — DATA RESCUE AFTER VENDOR LOSS
- **PROBLEM**: High-end ultrasound / MRI console. Vendor bankrupt. Software license dongle dead. Machine no longer boots.
- **ACTION**:
  1. Ask the vendor's successor or receiver for a replacement license. Do not emulate or patch the license check.
  2. Image the internal disk read-only, under the operator's data protection rules.
  3. `ogigia` -> identify the local database and image formats in order to export studies.
  4. Import the studies into a modern open-source PACS (Orthanc / dcm4chee).
  5. Keep clinical use on certified equipment: changing a medical device's software can affect its regulatory status.
- **RESULT**: Patient data accessible via a modern web UI. Replacement path planned.

### MISSION 14: PROSUMER DRONE / GIMBAL — LOCAL TELEMETRY AFTER VENDOR CLOUD LOSS
- **PROBLEM**: Vendor cloud dead. Telemetry locked to a proprietary app.
- **ACTION**:
  1. Do not alter no-fly zones or other flight limits: they are safety controls, and aviation law applies.
  2. `eolia` -> observe the MAVLink / proprietary RF link between your own RC && drone.
  3. Write a custom Python decoder for the telemetry stream. Pipe to QGroundControl / Mission Planner.
- **RESULT**: Local telemetry control established. Flight limits unchanged.

### MISSION 15: PROPRIETARY NAS / SAN APPLIANCE — RESCUE RAID METADATA & BYPASS VENDOR LOCK
- **PROBLEM**: Enterprise NAS chassis. Motherboard dead. Vendor demands $10k proprietary replacement. Drives contain critical data in custom RAID layout.
- **ACTION**:
  1. Pull SATA/SAS drives. Connect to standard Linux rig via HBA.
  2. `outis` -> `inspect_firmware_regions` on drive headers. Identify custom metadata signatures (LSI MegaRAID, Synology SHR, QNAP mdadm).
  3. Map chunk size, stripe order, parity scheme.
  4. Reconstruct array using standard `mdadm` || `dmsetup` with custom mapping tables.
  5. Mount Btrfs/ZFS/Ext4 volumes.
  6. Extract vendor OS image from USB DOM. `itaca` -> compile generic Linux kernel with vendor's proprietary `.ko` for backplane LED/buzzer control.
  7. Flash generic TrueNAS / Unraid to standard ITX board. Re-seat drives.
- **RESULT**: $10k hardware cost avoided. 100% data recovered. NAS runs on commodity hardware.

### MISSION 16: RETRO ARCADE / PINBALL MACHINE — FPGA & ROM PRESERVATION
- **PROBLEM**: Custom 90s arcade PCB || solid-state pinball CPU. EPROMs rotting (bit rot). ASICs failing. No schematics.
- **ACTION**:
  1. Desolder UV-EPROMs / masked ROMs. Read via TL866II+ programmer.
  2. Dump custom ASICs / GALs / PALs using logic analyzer + custom stimulus rig.
  3. `eolia` -> reverse engineer GAL equations from truth tables.
  4. Write Verilog/VHDL behavioral models. Synthesize to modern FPGA (Lattice iCE40 / Xilinx Spartan).
  5. Design drop-in interposer PCB -> adapt 5V legacy logic to 3.3V FPGA I/O.
  6. Archive dumps to MAME / PinMAME project.
- **RESULT**: Silicon decay halted. Hardware preserved indefinitely in silicon && code.

### MISSION 17: SMART GRID / UTILITY METER — READ-ONLY LOCAL READOUT OF YOUR OWN CONSUMPTION
- **PROBLEM**: Utility meter uses proprietary RF mesh (Zigbee Smart Energy, LoRaWAN) or PLC. Vendor API locked. Data held hostage.
- **ACTION**:
  1. Sniff RF with HackRF One / Yard Stick One. Decode O-QPSK / LoRa PHY layer.
  2. Reverse MAC layer payload structure.
  3. Use the network keys of your own installation, where your provider and local rules allow it. Never transmit on the mesh or alter readings.
  4. Write local Python MQTT bridge to decrypt and parse payload.
  5. Pipe metrics to local Grafana dashboard.
- **RESULT**: Real-time power/water/gas consumption on local LAN. Zero cloud dependency. Privacy restored.

### MISSION 18: MODERN LAPTOP UEFI/BIOS — INTEL ME / AMD PSP NEUTRALIZATION & WHITELIST BYPASS
- **PROBLEM**: UEFI locks out custom Wi-Fi cards (WLAN whitelist). Intel ME / AMD PSP acts as black-box rootkit with out-of-band network access.
- **ACTION**:
  1. Dump SPI BIOS via hardware flasher (SOIC-8 clip).
  2. Use `UEFITool` to map firmware volumes.
  3. Run `me_cleaner` to neutralize ME / set HAP (High Assurance Platform) bit. Disable AMD PSP modules.
  4. Extract ACPI tables (DSDT/SSDT). Decompile to DSL. Patch out Wi-Fi whitelist checks (remove `_WAK` / `_PTS` validation routines). Recompile to AML.
  5. Inject patched ACPI back into BIOS image. Flash via hardware programmer.
- **RESULT**: Full hardware sovereignty. Subverted black-box CPU. Unlocked hardware expansion slots.

### MISSION 19: PROPRIETARY 3D PRINTER / CNC MOTHERBOARD — KLIPPER FIRMWARE PORT
- **PROBLEM**: Vendor locks down STM32 / LPC MCU with encrypted bootloader. Proprietary motion control limits speed and quality.
- **ACTION**:
  1. Dump MCU flash via SWD (ST-Link V2). Analyze vector table.
  2. Find bootloader entry point. Patch out signature check or locate mass storage boot pin.
  3. Compile open-source Klipper firmware for specific MCU architecture.
  4. Flash via custom DFU payload or hardware SWD programmer.
  5. Wire up Raspberry Pi host. Map stepper pins and thermistors.
- **RESULT**: Sub-millisecond motion control. Web UI (Mainsail/Fluidd). Vendor lock destroyed. Print speeds doubled.

### MISSION 20: VINTAGE SYNTHESIZER / DRUM MACHINE — MIDI RETROFIT & SAMPLE INJECTION
- **PROBLEM**: 80s analog/digital hybrid synth. No MIDI. Dead floppy drive for sample loading. Unobtainium parts.
- **ACTION**:
  1. Tap internal data bus / DAC inputs with logic analyzer. Map memory addresses for sample RAM.
  2. Design Raspberry Pi Pico (RP2040) USB-MIDI to parallel bus interposer PCB.
  3. Write PIO (Programmable I/O) assembly to match vintage bus timing constraints.
  4. Emulate floppy controller via `HxC` firmware / Gotek clone or inject samples directly into SRAM via interposer.
- **RESULT**: Vintage analog warmth + modern digital control. Anythink bridged across decades. Hardware saved from landfill.

---

## 8. ADVANCED STRATEGIES & OPERATIONAL IMPACT MAPPING

1. **Mapping Findings to Operational Impact**:
   - Technical finding: *"Unprotected UART pads exposed on PCB"* -> Operational impact: *"Direct U-Boot access obtained; zero-soldering firmware extraction enabled."*
   - Technical finding: *"Hardcoded AES key inside JNI shared library"* -> Operational impact: *"Local BLE communication liberated; cloud server dependency terminated."*
   - Technical finding: *"Device Tree defines MMIO addresses for undocumented display controller"* -> Operational impact: *"Mainline DRM/KMS driver ported; modern Linux display server functional."*
2. **Clean-Room Enforcement**:
   - Never paste decompiled assembly or proprietary C pseudo-code directly into production repository.
   - Filter all reverse engineering evidence through `ermes` (`Stage_M`) to produce formal mathematical specifications (`CLEAN_SPEC.md`).
   - Implement only from `CLEAN_SPEC.md` via `penelope` (`Stage_B`).
3. **The Autonomous `/goal` Loop**:
   - Set execution target.
   - Iterate across OdissRea skills until parity gate confirms:
     $$\text{unresolved\_obligations} = 0 \quad \land \quad \text{unknowns} = 0 \quad \land \quad \text{build} = \text{PASS}$$

---

## 9. CAVE TROUBLESHOOTING [FAQ & RECOVERY PROTOCOLS]

When silicon fights back, adapt and overcome. Standard operating procedures for common hardware/software roadblocks:

- **SYMPTOM**: `flashrom` fails with `Read/Write timeout` or `Chip not found`.
  - **CAUSE**: Bus contention. Main MCU holding SPI `MISO`/`MOSI` lines low/high.
  - **FIX**: Lift `WP#` / `HOLD#` pins with 3.3V pull-up resistors. Use `flashrom --ignore-safety`. If fail: desolder chip completely (hot-air 350°C).
- **SYMPTOM**: UART terminal spits gibberish (garbage characters / squares).
  - **CAUSE**: Wrong baud rate, swapped TX/RX, or inverted logic.
  - **FIX**: Swap TX/RX wires. Try standard rates (`9600`, `38400`, `57600`, `115200`). Hook logic analyzer to measure bit-width (`1 / bit-width = baud`). Check for inverted serial (common in Broadcom/MediaTek routers); invert signal via transistor or adapter.
- **SYMPTOM**: Bootloop after custom firmware flash.
  - **CAUSE**: Bad checksum, missing MAC/calibration partition, or wrong endianness in kernel header.
  - **FIX**: Interrupt bootloader. Re-flash `factory` / `art` / `eeprom` calibration partitions. Verify `mkimage` headers (magic numbers). Check if bootloader requires specific RSA signature.
- **SYMPTOM**: Firmware entirely encrypted (`binwalk -E` shows 99% high entropy everywhere).
  - **CAUSE**: Vendor uses AES-CBC/RSA for payload encryption.
  - **FIX**: Find decryption routine in bootloader (U-Boot) or RAM. Dump RAM via JTAG/UART. Extract key from memory. Patch bootloader assembly to skip signature check or dump decrypted payload from RAM post-boot.
- **SYMPTOM**: JTAG/SWD connection fails (`OpenOCD` halts).
  - **CAUSE**: Debug port disabled in eFuses, or low-power sleep mode locking MCU.
  - **FIX**: Hold reset button while connecting. Supply external clock signal. Use `connect_assert_srst`. If eFuses blown: hardware debug is dead; pivot to peripheral bus sniffing (SPI/I2C).

---

## 10. FORGING NEW SKILLS [CONTRIBUTOR PROTOCOL]

OdissRea is modular. You find new target class? You build new agent.

1. **DEFINE DOMAIN**: What is target? (e.g., `Automotive ECU`, `Smart Grid Meter`, `Spacecraft Avionics`).
2. **MAP TO REA**: Which of 207 MCP tools apply? (e.g., `inspect_packet_capture`, `decode_signal_recording`, `procedure_pseudo_code`).
3. **WRITE `SKILL.md`**: Use standard template.
   - `GOAL`: One sentence outcome.
   - `PREREQUISITES`: Hardware/Software needed.
   - `EXECUTION_STEPS`: Telegraphic, numbered actions.
   - `EXPECTED_OUTPUT`: Artifacts generated.
4. **REGISTER IN PANTHEON**: Add to `odissrea` router logic. Assign Greek/Odyssey archetype if applicable. Submit PR.

---

## 11. THE ODISSREA MANIFESTO

We do not accept "End of Life".  
We do not accept "Cloud Only".  
We do not accept "Planned Obsolescence".  

Silicon does not age. Logic does not rot. Only artificial barriers decay.  
When the vendor walks away, the hardware becomes ours.  
When the server shuts down, the protocol becomes ours.  

**OdissRea** is not just a tool. It is the crowbar for the digital age.  
Use it to pry open the black boxes.  
Use it to reclaim your property.  
Use it to build the bridge they refused to build.  

**Anythink. Anytime. Anywhere.**

---

## 12. LICENSE
MIT © [mich-de](https://github.com/mich-de)
