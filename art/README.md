# The art library

One picture per seat per set — no variants, no duplicate formats. The pack ships the
house art here:

| Set | Files | What |
| --- | --- | --- |
| `dossiers/` | 8 | one dossier card per seat, clean public render |
| `sheets/` | 8 | one character card per seat: name, title, sin, one sentence |
| `wallpapers/` | 8 | one poster wallpaper per seat, 2048x1152 |

The base set — portraits, roster cards, the team composite, the loop diagram, the social
card — lives once in `assets/img/` and is what the site and the README render. The lore
the agents read lives in `docs/seats/` and `docs/lore/`; this directory is only the
pictures.

Seat slugs: `reika`, `yui`, `rin`, `niko`, `mei`, `aria`, `elo`, `mechapip` (leadership order, founder first; the loop order is separate).

## The clean render

The v2.0.0 set is a clean public render from the house's own character art. The
private-stamped HUD, the money copy, and the brand marks are gone: each card carries
only the public name, the title, the sin, and the seat's one sentence. The two
burned-in renders were replaced with clean renders, and the set is complete at
8/8/8. The visual pass re-rendered the cards, the full-bleed portraits, the roster
cards, the lineup, the loop, and the social card from the same clean crops.

The asset review in `assets/REVIEW.md` holds the rule and the manifest: the review is
human, the manifest is machine-checked, and the chair signs the pass. A clean render
takes its row and its hash in the same commit as the file.

## The tour

The seat pages carry each seat's roster card; the full library lives in this directory.
The thumbnails live in `assets/thumbs/`, generated from these files and the site set;
they are display copies, not a second library.

## Provenance

Generated house art for AnimeStack, rendered from the house's own character art. The
pack ships it under the repository's AGPL-3.0-or-later license (`LICENSE`, `NOTICE`;
commercial terms in `COMMERCIAL.md`). Variants, alternates, sprites, and web exports
are not part of this release; this directory carries one copy of each shipped image
and nothing else.
