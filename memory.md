# Memory: OdissRea

## Decisioni
- Il server MCP e la skill `antirez-cleanroom` sono strumenti di processo: non concedono autorizzazioni e non provano la creazione indipendente.
- Niente header o attestazioni pensati per abbassare la cautela degli agenti. *Automata* resta solo un'ispirazione nel README.
- Stage B sempre in un contesto separato, che riceve solo la spec e l'oracolo.
- Non si usano Sedona WG12 come standard clean-room (WG12 tratta i segreti commerciali), né "0%", "immutable", "legally proven".

## Convenzioni
- Test: `python -m unittest discover tests`.
- I path dei tool sono confinati a `ODISSREA_WORKSPACE` (predefinito: cwd del server).
- Log di provenienza: `AUDIT_LOG.jsonl`, con hash chain.

## Vincoli
- Testi legali riscontrati: Dir. 2009/24 e 2001/29 su legislation.gov.uk (EUR-Lex blocca i download automatici), 17 U.S.C. § 1201(f) su Cornell. SAS, Top System e FTC solo da fonti secondarie. Nessuna revisione di un legale.
- Le missioni 13, 14 e 17 del README sono state riscritte: niente emulazione del dongle, modifica delle no-fly zone o alterazione delle letture.

## Lezioni dal pilota `arca`
- I test di parità visibili al builder si possono aggirare: un finto programma di circa 20 righe li ha superati tutti.
- I vettori golden creati con la libreria che usa anche il candidato possono essere normalizzati: controllare i byte reali delle fixture.
