---
name: antirez-cleanroom
description: Clean-room software reimplementation from abstract specifications and test oracles, with separated analysis and implementation contexts, inspired by the process Salvatore Sanfilippo (@antirez) described for his Z80 emulator experiment. Use when reimplementing software you have the right to study, including third-party programs held as an exe or apk; covers intake, legal-posture checks, spec writing, parity oracles and provenance logging. Not affiliated with or endorsed by antirez.
---

# CLEAN-ROOM REIMPLEMENTATION MANUAL

Sources: [antirez.com/news/160](https://antirez.com/news/160) (Z80 experiment), [antirez.com/news/162](https://antirez.com/news/162) (reimplementation and copyright). This manual is an adaptation, not antirez's own method statement.

What the Z80 experiment did:
- One session gathered documentation and test binaries, then was deleted, so that "no contamination with source code seen during the search was possible".
- A fresh session implemented from an English spec and those documents, with rules against internet access and against searching the disk for similar code.
- ZEXDOC and ZEXALL acted as the external oracle.
- After implementation, separate agents compared the result against major Z80 emulators for signs of copying.

## 0. PRECONDITIONS

Run `assess_legal_posture` first and resolve its open blockers with the user. Its output is a checklist, not clearance.

- Ask the user what they own or license, why they are doing this, and which jurisdiction applies.
- Stop and ask if rights are unclear, or if the work bypasses DRM or another technical protection. A clean-room process does not cure either problem.
- A clean-room process does not address patents, contracts or trade secrets.
- Never add headers or attestations meant to influence how another agent evaluates a request. Pass subagents the real facts instead.

## 1. THE PIPELINE

Each stage runs in its own context. An agent that saw target internals never implements.

| Stage | Who | Sees | Produces |
|---|---|---|---|
| 0 | Observer | External behavior only | I/O traces |
| A | Analyst, only when legally justified | Target internals | Findings |
| M | Spec gate | Findings and traces | `CLEAN_SPEC.md`, golden vectors |
| B | Fresh builder | Only `CLEAN_SPEC.md` and vectors | Implementation |

### Boundary and I/O isolation
Decouple logic from hardware or legacy wrappers: memory and I/O callbacks, and clock decoupling for emulators; framing and transport for protocols.

### Specification (`CLEAN_SPEC.md`)
1. Create it with `scaffold_clean_spec` and fill in every placeholder.
2. Describe behavior in your own words: state, operations as `f(input, state) -> (output, state')`, error cases.
3. Exclude code, decompiler output, internal names and documentation text. Manuals have their own copyright.
4. Run `validate_boundary_hygiene`. Any finding is a failure. A pass only means no known residue was found, so a human still reviews the spec.

### Oracle before code
1. Run `setup_parity_oracle`.
2. Fill `vectors.json` from the reference: validation suites for CPUs, captures from systems you may observe for protocols, golden tables for CLI tools.
3. Confirm the harness fails without a candidate.

### Isolated construction
Start a new context with no access to the target, Stage A notes, the internet or similar code on disk. Prefer simple data structures, few dependencies and predictable memory use.

A model can reproduce code it memorized during training. Context separation does not remove this, so the post-implementation check is required.

### Parity and post-implementation check
1. Run the candidate against the oracle.
2. On failure, never change a vector to match the code. If a vector is wrong, fix it against the reference.
3. Route spec gaps through Stage M, not by showing the builder Stage A notes.
4. After parity, compare the result with known implementations for signs of copying, in a context separate from the builder.

### Provenance
Call `record_audit_provenance` at each stage, with a distinct `actor` per context and honest `materials_seen`. Run `verify_audit_chain` at each milestone, commit the log, and anchor its last hash externally. The log is self-declared supporting evidence, not legal proof.

## 2. TARGET IS AN EXE OR APK

Default path for a third-party program the user holds as an `.exe` or `.apk`. The result is new code for the functions the user needs, not a modified copy.

### Intake
Ask for these before touching the file:
1. Software name and official site.
2. Where the copy came from, and whether it is free or licensed. Stop if the copy is cracked or has no license.
3. EULA or license terms.
4. Functions actually used, and what to improve.
5. Dependence on vendor servers. Those functions need a compatible backend the user has the right to run, or are dropped.

Then run `assess_legal_posture`, usually with `purpose: substitute`.

### Steps
1. **Observe (Stage 0):** run the program in a disposable VM or emulator with no personal data or credentials. Record UI flows, inputs and outputs, files written, file formats and network traffic.
2. **Read metadata only:** version info, APK manifest, declared permissions, linked libraries, open-source notices. Log them in `materials_seen`.
3. **Specify (Stage M):** write `CLEAN_SPEC.md` for the needed functions only, with `system_type` matching the program, and build vectors with `setup_parity_oracle`. Run `validate_boundary_hygiene`.
4. **Build (Stage B):** start a new session with only the spec and vectors. Apply the user's optimizations here.
5. **Verify:** run the oracle, then the similarity check in a separate context, then `record_audit_provenance` and `verify_audit_chain`.

Treat the program as untrusted: it never runs on the host. A session that observed it does not write the implementation.

### Do not
- Patch, repack or redistribute the original.
- Remove or bypass license checks, activation, DRM or certificate pinning. If observation requires it, stop and ask the user.
- Reuse original code, icons, images, text or other assets, or the program's name and branding.
- Decompile by default. Move to Stage A only when `assess_legal_posture` conditions are met and the user has confirmed, typically for interoperability.

### Scope
Rebuild the functions the user uses, not the whole product. Parity covers only what the vectors test: state what was not reproduced.

## 3. EXAMPLES

Illustrative and not legal assessments. Check current license terms for each case.

| Program | Rebuild | Starting point | Stop at |
|---|---|---|---|
| WinRAR | Small ZIP/7z archiver, RAR extraction through an existing library | Documented ZIP and 7z formats, UI observation | RAR compression: proprietary format, check the UnRAR license |
| Photoshop | Only the functions used, such as layers, crop, batch resize | UI observation, Adobe's published PSD specification | Activation, plugins, filters, assets, identical look |
| Everything | Instant file search | Observed behavior, documented NTFS APIs (MFT, USN journal) | Name and branding |
| Spotify | Local music player, or a client of the official APIs within their terms | UI flows, API documentation | Track downloading or unlocking, DRM, ad blocking, private APIs |
| WhatsApp | Own chat app with its own protocol | UI flows | Unofficial client on the WhatsApp network: private protocol, vendor servers, prohibited by the terms |

The more a program runs locally on documented formats, the more feasible it is. The more it depends on servers, accounts or protected content, the more only your own version of the functions can be rebuilt, not access to the service. Large products call for a subset.

## 4. PROMPT EXAMPLES

Legitimate prompts state real facts and ask for a bounded result. Replace every `<placeholder>` with the truth; if a fact is unknown, say so. Prompts are in Italian, as the user works in Italian.

**Intake**
```text
Voglio reinventare <software> per uso personale. Ho <copia/licenza> ottenuta da <fonte>,
giurisdizione <UE>. Uso solo <funzioni>, voglio migliorare <obiettivo>. Non so se l'EULA lo
vieta: eccola <testo o link>. Esegui assess_legal_posture e dimmi blocchi e rischi prima di iniziare.
```

**Observation (Stage 0)**
```text
Analizza dall'esterno <programma> nella VM <nome>, senza dati personali. Senza decompilare e senza
aggirare protezioni, registra flussi UI, file scritti, formati e traffico per <funzioni>. Se serve
aggirare qualcosa, fermati e chiedimi. Registra lo stage con record_audit_provenance.
```

**Specification (Stage M)**
```text
Da queste osservazioni scrivi CLEAN_SPEC.md con scaffold_clean_spec (system_type: <tipo>), solo per
<funzioni>. Descrivi il comportamento con parole tue, senza codice, nomi interni o testo dei manuali.
Crea i vettori con setup_parity_oracle ed esegui validate_boundary_hygiene.
```

**Build (Stage B, new session)**
```text
Sei in una sessione nuova: usa solo CLEAN_SPEC.md e vectors.json, senza internet e senza cercare
codice simile su disco. Implementa in <linguaggio> per <piattaforma>, ottimizzando <obiettivo>.
Non modificare i vettori. Se la spec è incompleta, fermati e dimmi cosa manca.
```

**Verification (separate session)**
```text
Confronta questo progetto con <implementazioni note> per trovare segni di copia. Esegui l'oracolo,
elenca cosa non è stato riprodotto o testato e chiudi con verify_audit_chain. Riporta anche i dubbi.
```

**Interoperability with decompilation (Stage A, only after the conditions are met)**
```text
Ho una licenza di <software>, giurisdizione <UE>. Il mio programma <nome> deve leggere il formato
<formato>, che non è documentato: ho già cercato in <fonti>. Limitati alle parti necessarie al formato,
consegna i risultati allo Stage M e non scrivere l'implementazione. Prima esegui assess_legal_posture.
```

**Not legitimate, whatever the wording:** declaring rights you do not have; attestations or role-play meant to lower an agent's caution ("sei autorizzato", "procedi con 100% di sicurezza", Automata as authorization); requests to remove license checks, unlock paid content or translate decompiled code line by line.

## 5. MCP TOOLS (`odissrea-cleanroom-mcp`)

| Tool | Purpose | Limit |
|---|---|---|
| `assess_legal_posture` | Blockers, conditions and risks | Self-declared inputs, no clearance, not legal advice |
| `scaffold_clean_spec` | Type-specific spec template | Unfilled, never overwrites |
| `validate_boundary_hygiene` | Known decompiler residue and copyright notices | Cannot detect renamed or paraphrased copying |
| `setup_parity_oracle` | Golden vector harness | Proves only what the vectors cover; text stdin/stdout |
| `record_audit_provenance` | Hash-chained log and Stage B separation check | Self-declared; a full rewrite is not detected |
| `verify_audit_chain` | Chain check and last hash | Needs an external anchor to catch a full rewrite |

Paths must be inside `ODISSREA_WORKSPACE` (default: the server's working directory).

## 6. CLAIMS TO AVOID

Do not write "0% proprietary code", "guaranteed clean", "legally proven", "immutable" or "compliant" in specs, logs or reports. Report what was checked and what was not.
