# RealDynLFV

Static project homepage for **RealDynLFV: A Large-Parallax Benchmark for Real-World Dynamic Light Field Video**, accepted at IEEE VCIP 2026.

The benchmark dataset and accompanying resources are being prepared for release. Availability updates will be provided on the project page. No dataset license or release date has been announced.

## Preview and build

Python 3 is sufficient; no framework, runtime JavaScript, external fonts or package installation is needed.

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000/ on the same computer. Stop the server with Ctrl+C.

## Files

- `content.json`: project description, statistics, resource states and URLs, media slots, authors, citation, license and versioned releases.
- `template.html`: semantic page layout and section copy.
- `assets/`: responsive CSS, favicon and future approved media.
- `scripts/build.py`: escaped, dependency-free static renderer.
- `scripts/check.py`: baseline checks for the current unreleased state.
- `index.html`: generated page; rebuild after source changes.
- `.nojekyll`: serve generated static files directly on GitHub Pages.
- `docs/DEPLOYMENT.md`: hosting and maintenance notes.

## Update content

A resource with a null `url` renders an availability label. Set a verified HTTPS URL only when that resource is publicly available. Update the accompanying availability text at the same time. Add version-specific records to `releases` using `version`, `label` and `url` keys; retain older versions when adding a new one. DOI records, Hugging Face downloads, GitHub code and regional mirrors can each have separate entries.

Set `authors`, `citation` and `license` only from confirmed metadata and permissions. The current overview is not the formal paper abstract. Do not invent publication details or results.

For approved still images, place web-sized derivatives under `assets/`, set the gallery item's relative `src` path and provide meaningful `alt` text. Keep master data outside this repository. Set `approved` to true only after publication permission is confirmed. Use `kind: "image"` for stills or `kind: "video"` for an MP4 clip, with an optional local `poster`. Videos use native controls, no autoplay and no preload. The required `alt` field supplies the image alternative or video description; add captions in the template if speech is present. Leave unapproved or missing assets unset. Gallery captions are configured through `title`, `spec` and `description`.

All assets use relative paths, supporting both root and project subdirectory hosting without a hardcoded account name. After editing, rebuild, run checks and inspect desktop/mobile layouts. The static checker deliberately rejects external resource links in the current unreleased preview; update that assertion when approved resources become available.
