---
name: telemaco
description: Zero-MCP fast path for the OdissRea pantheon. Reverse engineer shipped software with plain local CLI tools (no REA server) — Electron/JS bundles, native ELF/PE/Mach-O, Go/Rust/.NET/Flutter/WASM, APKs, SQLite, pcaps, firmware, websites. Default first move; escalate to the REA MCP lands (atena/proteo/eritrea) only when a CLI path is insufficient.
---

# TELEMACO :: ZERO-MCP FAST PATH [ULTRACAVE]

## 0. ROLE & WHEN TO USE
- `IDENTITY`: **Telemaco (*Telemachus*)** :: the scouting first journey (*Telemachy*) that goes ahead of the master's full odyssey. The pantheon's cheapest entry point — same job the 207 REA tools do, with Bash and tools the agent already has. No MCP server, no tool-definition tax.
- `RULE OF ESCALATION`: Try the CLI path **first**. Reach for the REA MCP lands only on a real gap: no local tool + no `brew`/`apt` install allowed, decompiler-grade pseudocode needed, live multi-engine dynamic correlation, or a 100%-parity reconstruction gate. Document why before escalating.
- `COMPLIANCE`: Same basis as the pantheon — EU Dir. 2009/24/EC Art. 5(1)/5(3)/6; CJEU *SAS Institute* C-406/10; 17 U.S.C. § 1201(f) & § 107. First-party / lawful-acquirer / interoperability only.
- `WHY`: On a side-by-side benchmark the lean path hit the same accuracy as the full REA MCP at ~38% less wall time, ~35% lower cost, ~56% fewer turns, ~60% fewer tokens. Turns cost more than bytes.

## 1. RULES
- Work on a copy. Put each extraction in a new dir under `$TMPDIR/re/<name>` (`cp --reflink=auto` is instant on btrfs/XFS). Reuse an existing extraction.
- Route by `file -b T` and magic bytes first. Run the cheapest inventory next. Only then decompile or read code.
- `rg` skips hidden/ignored files, and bundlers hide code (Electron: `.webpack/`, `.vite/`). Always search extracted trees with `rg -uu`.
- Never `cat` a big or minified file. Slice it: `rg -o '.{0,200}NEEDLE.{0,200}' F | head`. Dump a disassembly once to a file, then grep that file.
- Batch independent probes into ONE shell call with `;` and `echo '--- name'` markers. Cap every output with `head` or `-m`. Wrap noisy builds/tests in `caveman shrink -- <cmd>`.
- Answer from evidence. Mark each claim **seen** (cite file:offset, or symbol/string) or **inferred**. A fact you did not find is **unknown**, not "absent". Static reading is not observed execution.
- A missing tool is not a blocker: use the row's fallback, or `apt/pacman/brew install <x>` if the user allows.
- Aim for 2–4 tool calls: one batched recon, one or two targeted slices, then answer. Stop when every asked item has evidence. Do not re-verify what you already saw.

## 2. FIRST MOVE: one call each, paste and run
Native (Linux ELF):
```sh
T=./bin; D=$TMPDIR/re/$(basename $T); mkdir -p $D; file $T; readelf -hdW $T | head -40; echo '--- NEEDED'; readelf -dW $T | rg NEEDED; echo '--- EXPORTS'; nm -D --defined-only $T 2>/dev/null | head -150; echo '--- IMPORTS'; nm -D -u $T 2>/dev/null | tr '\n' ' '; echo; echo '--- STRINGS'; strings -a -n 6 $T | rg -v '^[_$.]' | head -400; objdump -d -M intel --no-show-raw-insn $T > $D/dis.txt; echo '--- FUNCS'; rg '^[0-9a-f]+ <.*>:$' $D/dis.txt | head -150; pwn checksec $T 2>/dev/null || true
```
macOS Mach-O: swap to `lipo -info`, `otool -L`, `nm -gU`/`nm -u`, `otool -tV`, `codesign -d --entitlements :-`, `otool -ov`.

Electron:
```sh
A=./app.asar; X=$TMPDIR/re/asar; rm -rf $X; npx -y @electron/asar extract $A $X && jq '{name,version,main}' $X/package.json; find $X -path '*/node_modules' -prune -o -type f \( -name '*.js' -o -name '*.node' \) -print | head -60; ls ${A}.unpacked/node_modules 2>/dev/null; rg -uu -l --glob '!node_modules' 'exposeInMainWorld' $X
```
Then slice the needle: `rg -uu -o --glob '!node_modules' '.{0,250}NEEDLE.{0,250}' $X | head -20`.

Go: `go version -m T` alone usually answers the question.

## 3. ROUTER (fastest CLI per target; REA land = escalation)
| Target (detect) | Fastest CLI path | Escalate to |
|---|---|---|
| Electron (`*/Resources/app.asar`) | `npx -y @electron/asar extract app.asar X`; entry `jq .main X/package.json`; surface `rg -n -o '.{0,120}(ipcMain\.(handle\|on)\|ipcRenderer\.(invoke\|send)\|contextBridge\.exposeIn(Main\|Isolated)World\|webPreferences\|preload:\|nodeIntegration\|sandbox\|\.node\b).{0,160}' -uu X --glob '!node_modules'`; app IPC wrappers hide channels, also `rg -uu -o '"[a-z]+:[a-z0-9:-]+"' X/<main> \| sort -u`; fuses `npx -y @electron/fuses read --app A.app` | `scheria` / `proteo` |
| Web bundle / minified JS | Find `sourceMappingURL`; if map has `sourcesContent`: `jq -r '.sources[]'`; else `npx -y prettier --parser babel F > F.pretty.js` then read by line range | `scheria` |
| Hermes / bytenode / V8 snap | Hermes magic `c6 1f bc 03`: `hermes-dec`/`hbc-decompiler`. `.jsc` bytenode: strings + runtime hooks only | `proteo` |
| Mach-O | `lipo -info` (thin: `lipo -thin arm64`); `otool -L`; `xcrun dyld_info -exports -imports`; `nm -gU`/`nm -u`; `codesign -d --entitlements :-`; `otool -ov`; `xcrun swift-demangle --compact` | `scheria` / `atena` |
| Native logic | `objdump -d -M intel --no-show-raw-insn T > $D/dis.txt` (or `otool -tV`). Find fn: `rg -n '<.*Name.*>:$' $D/dis.txt`. Read call/string trail, not every instruction. Pseudocode: `r2 -qc 'aaa; pdc @ sym.X' T` or Ghidra `analyzeHeadless $D p -import T -postScript DecompileAll.java -deleteProject` | `atena` / `ea` / `eritrea` |
| ELF / PE | `readelf -hlSW`, `readelf -dW` (NEEDED), `nm -D --defined-only`, `objdump -d -M intel`. PE: `objdump -x`, `pefile`/`wrestool`. checksec: `pwn checksec` | `ea` / `ogigia` |
| Go (`.go.buildinfo`) | `go version -m T` → toolchain, path, mod, deps, flags in one call. No Go: `strings -a T \| rg -m1 -A200 'Go buildinf'`. Symbols survive stripping: `go tool nm T \| rg main\.` | `atena` |
| Rust | cargo-auditable: `cargo audit bin T`, or inflate `.dep-v0`. Compiler: `strings -a T \| rg -o '/rustc/[0-9a-f]{40}' \| sort -u`. Crates: `strings -a T \| rg -o '[a-z0-9_-]+-[0-9]+\.[0-9]+\.[0-9]+/src' \| sort -u` | `ea` |
| .NET (Mono/.Net) | `ilspycmd -p -o X T.dll` then `rg`. P/Invoke: `rg DllImport X`. NativeAOT/IL2CPP → native rows | `scheria` |
| Android APK | `jadx -d X --show-bad-code a.apk` then `rg`. Manifest/res only: `apktool d --no-src -o X a.apk`. `lib/*/libflutter.so`→Flutter (`blutter`); `libhermes.so`→RN (Hermes row) | `scheria` / `proteo` |
| Flutter snapshot hash | In `libapp.so` find magic `f5 f5 dc dc`; 32 hex at +20 = snapshot hash → map to Dart version | `scheria` |
| WASM | `wasm-objdump -x`, `wasm2wat`, `wasm-decompile` (WABT) | `scheria` |
| SQLite | Copy db + `-wal` if present. `sqlite3 'file:C?mode=ro' '.schema'`, then `SELECT * FROM t LIMIT 20` | `ogigia` / `outis` |
| plist / nib / car | `plutil -p F`. Info.plist = bundle id, URL schemes, privacy strings. `assetutil --info Assets.car` | `ogigia` |
| pcap / HAR | `tshark -r C -q -z conv,tcp`; `tshark -r C -T fields -e dns.qry.name -e tls.handshake.extensions_server_name -e http.request.full_uri \| sort -u`. HAR: `jq -r '.log.entries[].request \| .method+" "+.url'` | `eolia` / `outis` |
| Firmware | `binwalk -e F` or `unblob -e X F`; `dtc -I dtb -O dts board.dtb` for device trees. Then route each extracted binary through this table | `itaca` / `eritrea` |
| Hardware bus (UART/SPI/I2C/USB) | `sigrok-cli`/`pulseview` export; decode with `sigrok-cli -i cap -P uart`. USB descriptors: `lsusb -v` | `eolia` |
| Website | `curl -sL URL` for HTML + script srcs, fetch JS, slice. Runtime: headless Chromium with network log (Playwright `page.on('request')`) or `--remote-debugging-port` | `outis` / `scheria` |
| Running app | Linux: `gdb -p PID`, `strace`/`ltrace`, `bpftrace`, `journalctl`. Electron main: `--inspect` (if RunAsNode/inspect fuse allows). Android: `adb logcat`, `frida -U -f pkg -l hook.js` | `proteo` / `outis` |

## 4. SPEED PATTERNS
- Strings + imports first. On a small binary, `nm -D -u` + `strings` + exports usually answer "what does it do" with no disassembly.
- Find who uses a string: get its address from disassembly literal-pool comments (`objdump`/`otool -tV`), then the enclosing function label above it.
- A symbol in a `bl`/`call` target already tells you the protocol (`getpeereid`, `write`, `std::hash`). Read the call sequence, not every instruction.
- JS: go native→JS boundary inward — native call, then caller class, then IPC registration, then renderer/preload.
- Versions: diff the inventories (`nm`, module list, `go version -m`) before diffing code.
- Rebuilding: write the minimal reimplementation, test against the original (same inputs → same outputs). Hand to `penelope` only when a clean-room spec + parity gate is actually required.

## 5. INSTALL (only on request)
`apt install jadx apktool radare2 binwalk wabt tshark gdb` · `pacman -S jadx apktool radare2 binwalk wabt wireshark-cli` · `npm i -g @electron/asar` · `dotnet tool install -g ilspycmd` · `cargo install cargo-audit cargo-auditable` · unblob via `pipx install unblob`.

---
*Lean path distilled from [leanrea](https://github.com/aicodeking/leanrea) (MIT) by aicodeking, itself credited to the [REA](https://github.com/morluto/rea) team. Adapted to the OdissRea pantheon and Linux-native tooling.*
