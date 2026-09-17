# The art library

One picture per seat per set — no variants, no duplicate formats. The pack ships the
house art here:

| Set | Files | What |
| --- | --- | --- |
| `dossiers/` | 7 | one dossier card per seat — shown on the seat pages |
| `sheets/` | 7 | one character sheet per seat — shown on the seat pages |
| `wallpapers/` | 7 | one 4K wallpaper per seat (stamped jpg) |

The base set — portraits, roster cards, the team composite, the loop diagram, the social
card — lives once in `assets/img/` and is what the site and the README render. The lore
the agents read lives in `docs/seats/` and `docs/lore/`; this directory is only the
pictures.

Seat slugs: `reika`, `yui`, `rin`, `niko`, `mei`, `aria`, `elo` (leadership order, founder first; the loop order is separate).

## The tour

Each seat page (`seats/<seat>.html`) shows that seat’s pieces at full size, linked from
their thumbnails. The thumbnails live in `assets/thumbs/`, generated from these files
and the site set; they are display copies, not a second library.

## Provenance

Generated house art for AnimeStack. The pack ships it under the repository's MIT
license (`LICENSE`, `NOTICE`). Variants, alternates, sprites, web exports, and the
animated wallpaper packs stay in the source repo; this directory carries one copy of each
shipped image and nothing else.
