# Mier’s portfolio

A static personal site. Open `index.html` directly, or preview with:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Experience and project content lives in `data/timeline.json`. After changing it, run:

```sh
python3 scripts/build.py
```

The generator updates only the marked regions in `index.html`. Edit its introduction, navigation, contact and metadata directly. Styles live in `css/styles.css`; `js/app.js` only manages the saved light/dark preference.

Deploy `index.html`, `css/`, `js/` and `CV_Mier.pdf` to any static host. No build service, package installation or network access is required to use the site. Keep the JSON and generator in source control for future edits.
