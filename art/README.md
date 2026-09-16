# The art library

The AnimeStack pack ships the Phipps Predictions house art here: six still sets plus
seven Wallpaper Engine packs, 105 files. Everything is copied byte-for-byte from the
house art library; nothing is re-encoded here — the site thumbnails in
`assets/thumbs/` are generated *from* this directory, never the other way around.

| Set | Files | What |
| --- | --- | --- |
| `dossiers/` | 7 | one dossier card per seat — the seat's file, drawn |
| `portraits/` | 7 | alternate portraits (the primaries ship as `assets/img/<seat>-portrait.jpg` and `docs/images/portraits/`) |
| `sheets/` | 14 | two character sheets per seat |
| `sprites/` | 15 | seven transparent PNGs, seven nameplate composites, one extra nameplate variant |
| `team/` | 5 | full-house composites |
| `gallery/` | 15 | the webp exports: reference sheets, dossiers, the canon Rev 10 composite |
| `wallpapers/` | 14 + 7 packs | per seat: a 4K still (webp), a stamped jpg, and an animated pack |

Seat slugs: `mei`, `elo`, `yui`, `niko`, `rin`, `aria`, `reika` (loop order). The
roster cards already in the site set are the same art as the house's roster cards;
they are not duplicated here.

## Wallpaper Engine packs

`wallpapers/engine/<seat>/` carries `project.json`, `<seat>.mp4`, `preview.jpg`, and
`README_macOS.txt`. Import the folder in Wallpaper Engine, or use the mp4 directly as a
dynamic wallpaper on macOS Sonoma. The videos are slugged from the house's originals
and `project.json` points at them by name.

## The tour

[`gallery.html`](../gallery.html) is the tour of this directory on the site
(`animestack.jerkyjesse.com`): every piece as a thumbnail, linked to its full-size
file. The seat pages use the same thumbnails for their art strips so the tour stays
light; full files are one click away.

## Provenance

Generated house art for Phipps Predictions — the same library the house uses for its
public pages. The pack ships it under the repository's MIT license (`LICENSE`,
`NOTICE`). Originals, backups, and renders not shipped here stay in the source repo;
this is a frozen export, like the lore mirror beside it at `docs/lore/`.
