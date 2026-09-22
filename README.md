# Sacred Origins website

Complete static website source. No build dependencies are required.

## Preview locally

From this folder, run:

```sh
python -m http.server 8000 --directory dist
```

Open http://localhost:8000/ in your browser.

## Edit content

- `generate.py` contains page copy, navigation, and product data. Edit it, then run `python generate.py` to rebuild the HTML in `dist/`.
- `dist/assets/style.css` and `dist/assets/theme.css` control design, spacing, and responsive layout.
- `dist/assets/site.js` controls mobile navigation, filters, contact email composition, and scroll animations.
- `dist/assets/` contains the logo and optimized editorial images. Replace product images with approved product photos when available.

For Netlify or Vercel, publish `dist/` as the output directory. For traditional hosting, upload the contents of `dist/` into the site document root while preserving folder paths.

## Current shop status

The five product pages are an inquiry catalog. Prices, inventory, checkout, payment, and shipping are not connected. The contact form opens the visitor's email application; it does not submit to a server.
