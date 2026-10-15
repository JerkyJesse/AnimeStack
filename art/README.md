# The art library

One picture per seat per set — no variants, no duplicate formats. The pack ships the
house art here:

| Set | Files | What |
| --- | --- | --- |
| `dossiers/` | 8 | one dossier card per seat — the machine's card landed with the eighth seat |
| `sheets/` | 7 | one character sheet per seat (the machine's sheet awaits the art pass) |
| `wallpapers/` | 7 | one 4K wallpaper per seat (stamped jpg; the machine's awaits the art pass) |

The base set — portraits, roster cards, the team composite, the loop diagram, the social
card — lives once in `assets/img/` and is what the site and the README render. The lore
the agents read lives in `docs/seats/` and `docs/lore/`; this directory is only the
pictures.

Seat slugs: `reika`, `yui`, `rin`, `niko`, `mei`, `aria`, `elo`, `mechapip` (leadership order, founder first; the loop order is separate).

## The tour

The seat pages carry each seat's roster card; the full library lives in this directory.
The thumbnails live in `assets/thumbs/`, generated from these files and the site set;
they are display copies, not a second library.

## Provenance

Generated house art for AnimeStack. The pack ships it under the repository's
AGPL-3.0-or-later license (`LICENSE`, `NOTICE`; commercial terms in
`COMMERCIAL.md`). Variants, alternates, sprites, web exports, and the
animated wallpaper packs stay in the source repo; this directory carries one copy of each
shipped image and nothing else.
