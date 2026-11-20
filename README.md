# Mier’s portfolio

A static personal site. Open `index.html` directly, or preview with:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Experience and project content lives in `data/timeline.json`. After changing it, run:

```sh
python3 scripts/build.py
```

The generator updates only the marked regions in `index.html`. Edit its introduction, navigation, contact and metadata directly. Layout and spacing live in `css/styles.css`.

Deploy `index.html`, `css/`, `assets/` and `CV_Mier.pdf` to any static host. The site uses static HTML and CSS. The local voice sample comes from the [Pagehum v0.1.0 release](https://github.com/Mieraidihaimu/pagehum/releases/tag/v0.1.0). Keep the JSON and generator in source control for future edits.
