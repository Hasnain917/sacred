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

## Pages & Structure

- **Home** (`/` & `/home/`): Hero, Ethos, 6 Core Offerings, 10 Community Testimonials, Apothecary highlights, and Journal preview.
- **About Us** (`/about/` & `/about-us/`): Bryant & Kai's journey, detailed co-founder bios with credentials, ancestral roots, core values, and comprehensive FAQ accordion.
- **Offerings** (`/offerings/`): Kambo Ceremonies, Reiki, Retreats/Group Journeys, Hapé & Sananga Circles, Psychedelic Integration, and House Cleansings/Limpias with authentic imagery.
- **Scheduling** (`/scheduling/`): Direct Calendly consultation booking (`sacredoriginsnyc/15`) and intake preparation notes.
- **Journal / Blog** (`/blog/`): All in-depth medicine guides & pharmacology articles:
  - *The Pharmacology of Kambo: How Its Compounds Affect the Human Body*
  - *The Sacred Origins of Sananga: History, Benefits, and Usage*
  - *Hapé: A Sacred Medicine for Spiritual Healing and Grounding*
  - *Getting Ready for Your Kambo Ceremony: A Friendly Guide*
  - *Discovering Kambo: A Sacred Healing Tradition for Modern Times*
- **Apothecary / Shop** (`/shop/`): 5 curated botanical items (Cacao Hapé, Murici Hapé, Samaúma Flower Hapé, Kuripe, Tepi) with inquiry flow.
- **Contact** (`/contact/`): Direct messaging form, email contact, and ceremonial space location.

All images from `https://www.sacredorigins.org/` have been downloaded locally to `dist/assets/images/` and integrated into the site's rich aesthetic.

