# Routinekaart Opstaan

Interactieve routinekaart (positive discipline) voor de ochtend, gemaakt voor de iPad.
Elke stap is een tegel: tik erop en hij draait om naar "Gedaan!". De Klaar-tegel gaat pas open als alle stappen af zijn.

Online: https://opstaan.fldr.nl

## Hoe het werkt

Eén losse HTML-pagina met gewone HTML, CSS en JavaScript, zonder framework of bibliotheken.

- Omdraaien: CSS 3D-transform (`rotateY`), sterretjes via de Web Animations API, confetti op een canvas.
- Geluid: Web Audio API (belletjes worden live gemaakt, geen audiobestanden). Op iPhone en iPad speelt het ook als de stilschakelaar aan staat.
- Voortgang: `localStorage` op het apparaat, per dag. Elke ochtend begint de kaart leeg.
- Op het beginscherm van de iPad zetten via Deel > "Zet op beginscherm" geeft een eigen app-icoon (het zonnetje).

## Bestanden

| Pad | Wat |
| --- | --- |
| `src/opstaan.html` | De pagina. Iconen staan erin als `__ICON_<code>__`. |
| `src/icons/` | Iconen als SVG, op Unicode-code (bijvoorbeeld `23f0.svg` is de wekker). |
| `src/opstaan-icoon.png` | App-icoon voor het beginscherm (180×180). |
| `build.py` | Bouwt `dist/index.html`: zet de iconen als data-URI in de pagina. Alleen standaard-Python. |
| `wrangler.jsonc` | Cloudflare Worker met statische assets uit `dist/`, op opstaan.fldr.nl. |

## Aanpassen

1. Taken staan in `src/opstaan.html` in de lijst `TASKS` (label, icoon, kleur, eventueel `soms:true`). Pas ook `TOTAL` aan als het aantal stappen verandert.
2. Nieuw icoon nodig? Zet de SVG in `src/icons/` met de Unicode-code als naam, bijvoorbeeld van [Twemoji](https://github.com/jdecked/twemoji/tree/main/assets/svg).
3. Lokaal bekijken: `python3 build.py` en open `dist/index.html` in de browser.
4. Push naar main: Cloudflare bouwt en rolt hem automatisch uit.

## Cloudflare

De site draait als Cloudflare Worker met statische assets (zie `wrangler.jsonc`), gekoppeld aan deze repo via Workers Builds.

- Build command: `python3 build.py`
- Deploy command: `npx wrangler deploy`
- Worker-naam: `routinekaart` (moet gelijk zijn aan `name` in `wrangler.jsonc`)
- Domein: https://opstaan.fldr.nl (staat als custom domain in `wrangler.jsonc`; Cloudflare maakt de DNS-record bij de eerste uitrol)
- Terugrollen: in het dashboard onder Deployments.

## Licenties

Iconen: [Twemoji](https://github.com/jdecked/twemoji), CC BY 4.0. Lettertype: Fredoka (Google Fonts), SIL Open Font License.
