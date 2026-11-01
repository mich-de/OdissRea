# Handover

## Stato
- `D:\Odisserea`: server MCP v3, skill, installer, README e test sul branch `Odissrea-cleanroom-mcp`, non ancora unito a `main`.
- `D:\ramo-cleanroom`: collaudo reale su `tree.com` (`ramo.py`), confronto dal vivo 99/99. Oracoli privati in `D:\tree-oracle-private`.
- `D:\arca-cleanroom`: pilota ZIP (`arca.py`), non è un repo git. L'oracolo dà 35/35, ma la revisione separata lo ha trovato aggirabile.

## Da fare: arca
Difetti riportati dal revisore, non ancora corretti:
1. H1: nessun limite contro le zip bomb (dimensione totale, rapporto, numero di entry).
2. H2: memoria quadratica in `plan_outputs` con nomi molto profondi.
3. H3: la fixture `evil_backslash.zip` non contiene backslash, perché `ZipInfo` li normalizza su Windows. Scrivere i byte a mano.
4. H4: oracolo aggirabile. Servono vettori nascosti al builder e test mutanti.
5. M1-M5: `RecursionError`, dimensione dichiarata non verificata, CRC saltato sulle directory con dati, distinzione corrupt/non-ZIP, flag di cifratura solo nel local header.
Report ripetibili in `arca-review` nello scratchpad della sessione, una cartella temporanea.

## Da fare: OdissRea
1. Revisione di un legale: testi riscontrati su fonti pubbliche, in parte secondarie (SAS, Top System, FTC).
2. Decidere sulle missioni 2, 12, 18 e 19 del README: aggirano protezioni e non sono state riscritte.
3. Valutare il nome della skill `antirez-cleanroom`. Citazioni di antirez verificate sull'originale.
4. Aggiungere alla skill: vettori nascosti al builder e test mutanti.
5. Reinstallare con `install_cleanroom.ps1`, riavviare Claude, rimuovere le directory annidate in home.

## Problemi aperti
- Se `mcp_config.json` conteneva altri server, il vecchio installer li ha persi.
- Decidere se proseguire `arca` o chiudere il pilota.
