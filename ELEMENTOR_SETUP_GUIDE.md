# Sacred Origins NYC — Elementor WordPress Setup Guide

This package contains everything needed to set up the **Sacred Origins** website on WordPress with **Elementor** and **WooCommerce**.

---

## 📦 Package Contents

1. **`elementor_templates/`**:
   - `elementor-home.json` — Homepage template (Hero, Ethos, 6 Offerings, Testimonials)
   - `elementor-about.json` — About Us template (Founders Kai & Bryant bios, full FAQs accordion)
   - `elementor-offerings.json` — Offerings template (All 6 modalities with photos & inquiry buttons)
   - `elementor-contact.json` — Contact template (Ceremony space, direct info, contact form)
   - `elementor-shop.json` — Apothecary template with WooCommerce shortcode catalog
2. **`sacred-origins-woocommerce-products.csv`**:
   - 5 client products ready for 1-click WooCommerce import (Cacao Hapé, Murici Hapé, Samaúma Flower Hapé, Kuripe, Tepi).
3. **`sacred-origins-wordpress-content.xml`**:
   - Complete WordPress export containing all 5 deep-dive Blog articles and pages.
4. **`sacred-origins-elementor-complete-package.zip`**:
   - All-in-one archive ready to download and share with client.

---

## 🚀 3-Step Setup Instructions

### Step 1: Install Theme & Plugins (WordPress Admin)
1. In WordPress Admin, go to **Appearance → Themes → Add New** and install:
   - **Hello Elementor** *(Recommended, free & ultra-fast)* or **Astra**.
2. Go to **Plugins → Add New** and install/activate:
   - **Elementor** *(Free page builder)*
   - **WooCommerce** *(Free store plugin for products)*
   - *(Optional)* **Elementor Header & Footer Builder** or **WPForms**

---

### Step 2: Import Products & Blog Content
1. **WooCommerce Products**:
   - Go to **WooCommerce → Products → Import**.
   - Select `sacred-origins-woocommerce-products.csv` and click **Continue → Run the Importer**.
   - All 5 products with categories, descriptions, and images will be created instantly.
2. **Blog Posts & Pages**:
   - Go to **Tools → Import → WordPress**.
   - Upload `sacred-origins-wordpress-content.xml`.
   - All 5 blog articles (Kambo Pharmacology, Sananga Origins, Hapé Ceremony, Prep Guide, Modern Kambo) will be created.

---

### Step 3: Import Elementor Templates
1. Go to **Templates → Saved Templates → Import Templates**.
2. Upload the JSON files from `elementor_templates/`:
   - `elementor-home.json`
   - `elementor-about.json`
   - `elementor-offerings.json`
   - `elementor-contact.json`
   - `elementor-shop.json`
3. Now create or edit any page (e.g. **Pages → Add New**):
   - Set Title (e.g. "Home"), click **Edit with Elementor**.
   - Click the **Folder Icon (Add Template) → My Templates**.
   - Click **Insert** next to `Sacred Origins - Home`.
   - Hit **Publish**!
