# NUCALORIC

Website, editable promotional video projects, and product/design documentation collected from the October 4, 2026 work sessions.

- `website/`: current website source, local assets, motion loop, and integration notes.
- `promo/`: original promo, v2, and approved v3 motion reel; render source, audio, Resolve timelines, storyboards, and masters.
- `vault/`: Obsidian Markdown vault and evidence; open this folder as a vault.
- `FILE_MANIFEST.json`: inventory of included project files and sizes.

## Preview the website

```sh
python -m http.server 8080 --directory website
```

Open http://localhost:8080. Paymenter purchases, hosting provisioning, and terminal access require a configured backend; see `website/docs/paymenter-integration.md`.

## Approved video

`promo/v3/output/NUCALORIC-motion-reel-16s-60fps.mp4` is the approved 1920×1080, 60 fps, 16-second reel. Editable render source and rebuild instructions are in `promo/v3/`.

## Large media

This repository is prepared for Git LFS for video, audio, and ZIP assets. Install Git LFS and run `git lfs install` before staging or uploading. Source files remain standard Git files.

Private chat histories, credentials, editor caches, and logs are excluded.

## October 5 creative refresh

The current website adds a creative Project Studio, a capability shortlist, purpose-based project kits, project discovery filters, monochrome chapter transitions, and quieter dot motion. See `website/docs/CREATIVE_REFRESH.md` and `website/docs/LAUNCHPAD_RESEARCH.md`.

`ad-assets/creative-refresh-2026-10-05/` contains nine editable SVGs, nine PNGs, three silent motion clips, source files, and an asset gallery. A ZIP of that pack is alongside the folder.
