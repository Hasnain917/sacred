import os
import json
import uuid
import zipfile
from pathlib import Path

OUTPUT_DIR = Path('elementor_package')
TEMPLATES_DIR = OUTPUT_DIR / 'elementor_templates'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)

def uid():
    return uuid.uuid4().hex[:7]

def make_widget(widget_type, settings):
    return {
        "id": uid(),
        "elType": "widget",
        "widgetType": widget_type,
        "settings": settings,
        "elements": []
    }

def make_column(elements, size=100, settings=None):
    return {
        "id": uid(),
        "elType": "column",
        "settings": settings or {"_column_size": size},
        "elements": elements
    }

def make_section(columns, settings=None):
    return {
        "id": uid(),
        "elType": "section",
        "settings": settings or {"layout": "boxed"},
        "elements": columns
    }

# Load scraped & curated site data from generate.py
from generate import products, offerings_data, testimonials_data, faqs_data, blog_posts

# -----------------------------------------------------------------------------
# 1. ELEMENTOR TEMPLATE: HOME
# -----------------------------------------------------------------------------
home_sections = []

# Hero Section
home_sections.append(make_section([
    make_column([
        make_widget("heading", {
            "title": "A SPACE FOR COMING BACK TO YOURSELF — NYC",
            "header_size": "h5",
            "custom_css": "color: #bfa677; letter-spacing: 0.2em; text-transform: uppercase;"
        }),
        make_widget("heading", {
            "title": "Where healing is a collective journey.",
            "header_size": "h1",
            "custom_css": "font-family: 'Playfair Display', serif; color: #f5eedf; font-size: 56px;"
        }),
        make_widget("text-editor", {
            "editor": "<p style='color: #cad7c8; font-size: 18px; line-height: 1.8;'>Welcome to Sacred Origins. We offer heart-centered Kambo ceremonies, Reiki healing, retreats, and ancestral Earth medicine to empower our community and guide your personal transformation.</p>"
        }),
        make_widget("button", {
            "text": "Schedule a Call ↗",
            "link": {"url": "/contact/"},
            "button_type": "default"
        })
    ], 60),
    make_column([
        make_widget("image", {
            "image": {
                "url": "https://images.squarespace-cdn.com/content/v1/66eb0f36a4f6604238c67319/cbd523b2-f7d5-48c2-b4e4-ad731829fdb8/juli-kosolapova-pZ-XFIrJMtE-unsplash.jpg",
                "alt": "Sacred Origins sanctuary"
            }
        })
    ], 40)
], {
    "background_background": "classic",
    "background_color": "#173328",
    "padding": {"unit": "px", "top": "100", "bottom": "100", "left": "40", "right": "40", "isLinked": False}
}))

# Ethos Section
home_sections.append(make_section([
    make_column([
        make_widget("heading", {
            "title": "01 / THE ETHOS — NEW YORK CITY",
            "header_size": "h6",
            "custom_css": "color: #bfa677; letter-spacing: 0.2em;"
        }),
        make_widget("heading", {
            "title": "A space to feel seen and supported.",
            "header_size": "h2",
            "custom_css": "font-family: 'Playfair Display', serif; color: #183126;"
        })
    ], 45),
    make_column([
        make_widget("text-editor", {
            "editor": "<p style='color: #576059; font-size: 16px; line-height: 1.85;'>At Sacred Origins NYC, we are a collective deeply rooted in empowering BIPOC communities through sacred healing practices. We understand that healing is not just a personal journey but a collective one that reconnects us with the wisdom and resilience of our ancestors.</p><p style='color: #576059; font-size: 16px; line-height: 1.85;'>Our mission is to provide a safe and transformative space where individuals can explore deep healing through a variety of modalities, including Kambo, Reiki, Earth Medicine Ceremonies, and Retreats.</p>"
        }),
        make_widget("button", {
            "text": "The Story Behind Sacred Origins ↗",
            "link": {"url": "/about/"}
        })
    ], 55)
], {
    "background_background": "classic",
    "background_color": "#f5f2ea",
    "padding": {"unit": "px", "top": "80", "bottom": "80", "left": "40", "right": "40", "isLinked": False}
}))

# Offerings Grid Section
off_columns = []
for off in offerings_data:
    off_columns.append(make_column([
        make_widget("image", {
            "image": {"url": "https://sacred-nu.vercel.app" + off['image'], "alt": off['title']}
        }),
        make_widget("heading", {
            "title": off['tag'].split('·')[0].strip(),
            "header_size": "h6",
            "custom_css": "color: #9a794a; letter-spacing: 0.15em;"
        }),
        make_widget("heading", {
            "title": off['title'],
            "header_size": "h3",
            "custom_css": "font-family: 'Playfair Display', serif; margin-top: 5px;"
        }),
        make_widget("text-editor", {
            "editor": f"<p style='color: #576059; font-size: 14px; line-height: 1.7;'>{off['desc'][:160]}...</p>"
        }),
        make_widget("button", {
            "text": "Learn More ↗",
            "link": {"url": "/offerings/"}
        })
    ], 33))

# Group offerings into 2 rows of 3 columns
home_sections.append(make_section([
    make_column([
        make_widget("heading", {
            "title": "02 / SACRED PATHWAYS",
            "header_size": "h6",
            "custom_css": "color: #9a794a; letter-spacing: 0.2em; text-align: center;"
        }),
        make_widget("heading", {
            "title": "Our Core Ceremonial Offerings",
            "header_size": "h2",
            "custom_css": "font-family: 'Playfair Display', serif; text-align: center; margin-bottom: 40px;"
        })
    ], 100)
], {"background_color": "#ebe6d8", "padding": {"unit": "px", "top": "80", "bottom": "20"}}))

home_sections.append(make_section(off_columns[:3], {"background_color": "#ebe6d8", "padding": {"unit": "px", "top": "0", "bottom": "30"}}))
home_sections.append(make_section(off_columns[3:], {"background_color": "#ebe6d8", "padding": {"unit": "px", "top": "0", "bottom": "80"}}))

# Testimonials Section
test_columns = []
for t in testimonials_data[:3]:
    test_columns.append(make_column([
        make_widget("testimonial", {
            "testimonial_content": t['quote'],
            "testimonial_name": t['name'],
            "testimonial_job": t['badge']
        })
    ], 33))

home_sections.append(make_section([
    make_column([
        make_widget("heading", {
            "title": "VOICES FROM OUR COMMUNITY",
            "header_size": "h6",
            "custom_css": "color: #bfa677; letter-spacing: 0.2em; text-align: center;"
        }),
        make_widget("heading", {
            "title": "Words from the Circle",
            "header_size": "h2",
            "custom_css": "font-family: 'Playfair Display', serif; color: #f5eedf; text-align: center; margin-bottom: 40px;"
        })
    ], 100)
], {"background_color": "#162e24", "padding": {"unit": "px", "top": "80", "bottom": "20"}}))
home_sections.append(make_section(test_columns, {"background_color": "#162e24", "padding": {"unit": "px", "top": "0", "bottom": "80"}}))

home_template = {
    "version": "0.4",
    "title": "Sacred Origins - Home",
    "type": "page",
    "content": home_sections
}
with open(TEMPLATES_DIR / "elementor-home.json", "w", encoding="utf-8") as f:
    json.dump(home_template, f, indent=2)

# -----------------------------------------------------------------------------
# 2. ELEMENTOR TEMPLATE: ABOUT US
# -----------------------------------------------------------------------------
about_sections = []

about_sections.append(make_section([
    make_column([
        make_widget("heading", {
            "title": "THE PEOPLE & PURPOSE",
            "header_size": "h6",
            "custom_css": "color: #765f40; letter-spacing: 0.2em; text-align: center;"
        }),
        make_widget("heading", {
            "title": "Rooted in connection. Open to possibility.",
            "header_size": "h1",
            "custom_css": "font-family: 'Playfair Display', serif; text-align: center;"
        }),
        make_widget("text-editor", {
            "editor": "<p style='text-align: center; color: #576059; font-size: 18px; max-width: 700px; margin: auto;'>Our story begins with the belief that healing is a collective journey reconnecting us with ancestral wisdom.</p>"
        })
    ], 100)
], {"background_color": "#ddd6c5", "padding": {"unit": "px", "top": "80", "bottom": "80"}}))

# Founders Section
about_sections.append(make_section([
    make_column([
        make_widget("image", {
            "image": {"url": "https://sacred-nu.vercel.app/assets/images/for_website_2.jpg", "alt": "Kai - Kaira Otero"}
        }),
        make_widget("heading", {
            "title": "Meet Kai (Kaira Otero)",
            "header_size": "h3",
            "custom_css": "font-family: 'Playfair Display', serif; margin-top: 15px;"
        }),
        make_widget("heading", {
            "title": "LCSW Psychotherapist · Reiki Level II · Certified Kambo Practitioner",
            "header_size": "h6",
            "custom_css": "color: #9a794a;"
        }),
        make_widget("text-editor", {
            "editor": "<p style='color: #576059; line-height: 1.8;'>Kai was shaped by her early years in a working-class home led by her single immigrant mother. Over seven years as a psychotherapist have deepened her understanding of generational traumas. She became an LCSW, Reiki Level II, and Kambo practitioner, offering a sanctuary of compassion especially for adult children of immigrants and BIPOC women.</p>"
        })
    ], 50),
    make_column([
        make_widget("image", {
            "image": {"url": "https://sacred-nu.vercel.app/assets/images/333.jpg", "alt": "Bryant"}
        }),
        make_widget("heading", {
            "title": "Meet Bryant",
            "header_size": "h3",
            "custom_css": "font-family: 'Playfair Display', serif; margin-top: 15px;"
        }),
        make_widget("heading", {
            "title": "Reiki Master Teacher (10+ Years) · Kambo Practitioner · Earth Medicine Facilitator",
            "header_size": "h6",
            "custom_css": "color: #9a794a;"
        }),
        make_widget("text-editor", {
            "editor": "<p style='color: #576059; line-height: 1.8;'>Bryant’s journey was forged through profound personal transformation. Reconnecting with ancestral heritage and plant medicine gave him grounding and purpose. With over a decade as a Reiki Master Teacher and Kambo practitioner, Bryant fosters spaces for genuine connection and renewal, especially with BIPOC men and athletes.</p>"
        })
    ], 50)
], {"background_color": "#f5f2ea", "padding": {"unit": "px", "top": "80", "bottom": "80"}}))

# FAQ Section
faq_tabs = [{"tab_title": q, "tab_content": a} for q, a in faqs_data]
about_sections.append(make_section([
    make_column([
        make_widget("heading", {
            "title": "COMMON INQUIRIES",
            "header_size": "h6",
            "custom_css": "color: #9a794a; letter-spacing: 0.2em; text-align: center;"
        }),
        make_widget("heading", {
            "title": "Frequently Asked Questions",
            "header_size": "h2",
            "custom_css": "font-family: 'Playfair Display', serif; text-align: center; margin-bottom: 30px;"
        }),
        make_widget("accordion", {
            "tabs": faq_tabs
        })
    ], 100)
], {"background_color": "#ebe6d8", "padding": {"unit": "px", "top": "80", "bottom": "80"}}))

about_template = {
    "version": "0.4",
    "title": "Sacred Origins - About Us",
    "type": "page",
    "content": about_sections
}
with open(TEMPLATES_DIR / "elementor-about.json", "w", encoding="utf-8") as f:
    json.dump(about_template, f, indent=2)

# -----------------------------------------------------------------------------
# 3. ELEMENTOR TEMPLATE: OFFERINGS
# -----------------------------------------------------------------------------
off_sections = [
    make_section([
        make_column([
            make_widget("heading", {
                "title": "GATHER · REFLECT · TRANSFORM",
                "header_size": "h6",
                "custom_css": "color: #765f40; letter-spacing: 0.2em; text-align: center;"
            }),
            make_widget("heading", {
                "title": "Our Sacred Offerings",
                "header_size": "h1",
                "custom_css": "font-family: 'Playfair Display', serif; text-align: center;"
            })
        ], 100)
    ], {"background_color": "#ddd6c5", "padding": {"unit": "px", "top": "80", "bottom": "80"}})
]

for i, off in enumerate(offerings_data):
    col_img = make_column([
        make_widget("image", {
            "image": {"url": "https://sacred-nu.vercel.app" + off['image'], "alt": off['title']}
        })
    ], 40)
    col_text = make_column([
        make_widget("heading", {
            "title": off['tag'],
            "header_size": "h6",
            "custom_css": "color: #9a794a; letter-spacing: 0.15em;"
        }),
        make_widget("heading", {
            "title": off['title'],
            "header_size": "h2",
            "custom_css": "font-family: 'Playfair Display', serif;"
        }),
        make_widget("text-editor", {
            "editor": f"<p style='color: #576059; font-size: 16px; line-height: 1.85;'>{off['desc']}</p>"
        }),
        make_widget("button", {
            "text": "Inquire via Contact Form ↗",
            "link": {"url": "/contact/"}
        })
    ], 60)
    
    cols = [col_img, col_text] if i % 2 == 0 else [col_text, col_img]
    off_sections.append(make_section(cols, {
        "background_color": "#f5f2ea" if i % 2 == 0 else "#ebe6d8",
        "padding": {"unit": "px", "top": "70", "bottom": "70"}
    }))

offerings_template = {
    "version": "0.4",
    "title": "Sacred Origins - Offerings",
    "type": "page",
    "content": off_sections
}
with open(TEMPLATES_DIR / "elementor-offerings.json", "w", encoding="utf-8") as f:
    json.dump(offerings_template, f, indent=2)

# -----------------------------------------------------------------------------
# 4. ELEMENTOR TEMPLATE: CONTACT
# -----------------------------------------------------------------------------
contact_sections = [
    make_section([
        make_column([
            make_widget("heading", {
                "title": "WE WOULD LOVE TO HEAR FROM YOU",
                "header_size": "h6",
                "custom_css": "color: #765f40; letter-spacing: 0.2em; text-align: center;"
            }),
            make_widget("heading", {
                "title": "Let's Connect",
                "header_size": "h1",
                "custom_css": "font-family: 'Playfair Display', serif; text-align: center;"
            })
        ], 100)
    ], {"background_color": "#ddd6c5", "padding": {"unit": "px", "top": "80", "bottom": "80"}}),
    
    make_section([
        make_column([
            make_widget("heading", {
                "title": "Sacred Origins NYC",
                "header_size": "h3",
                "custom_css": "font-family: 'Playfair Display', serif;"
            }),
            make_widget("text-editor", {
                "editor": "<p style='color: #576059; line-height: 1.8;'>We’re Bryant and Kai. Whether you have questions about our offerings, want to join a ceremony, or are seeking guidance on your healing path, reach out to us!</p><p><strong>Email:</strong> <a href='mailto:sacredoriginsnyc@gmail.com' style='color:#9a794a;'>sacredoriginsnyc@gmail.com</a></p><p><strong>Location:</strong> New York City · Lenapehoking</p>"
            }),
            make_widget("image", {
                "image": {"url": "https://sacred-nu.vercel.app/assets/images/_dsc7710.jpg", "alt": "Sacred Origins Ceremony Space"}
            })
        ], 45),
        make_column([
            make_widget("heading", {
                "title": "Send a Message",
                "header_size": "h3",
                "custom_css": "font-family: 'Playfair Display', serif; margin-bottom: 20px;"
            }),
            make_widget("html", {
                "html": """
<form id="wp-contact-form" style="display:flex; flex-direction:column; gap:16px;">
  <label style="font-size:12px; font-weight:600; text-transform:uppercase;">Your Name *</label>
  <input type="text" name="name" required style="padding:14px; border:1px solid #ccc; background:#fff;">
  <label style="font-size:12px; font-weight:600; text-transform:uppercase;">Email Address *</label>
  <input type="email" name="email" required style="padding:14px; border:1px solid #ccc; background:#fff;">
  <label style="font-size:12px; font-weight:600; text-transform:uppercase;">Topic</label>
  <select name="subject" style="padding:14px; border:1px solid #ccc; background:#fff;">
    <option>General Inquiry</option>
    <option>Kambo Ceremony</option>
    <option>Reiki Healing</option>
    <option>Retreats & Group Journeys</option>
    <option>Hapé & Sananga Circles</option>
    <option>Psychedelic Integration</option>
    <option>Shop & Products</option>
  </select>
  <label style="font-size:12px; font-weight:600; text-transform:uppercase;">Your Message *</label>
  <textarea name="message" rows="5" required style="padding:14px; border:1px solid #ccc; background:#fff;"></textarea>
  <button type="submit" style="background:#183126; color:#fff; padding:16px 24px; border:none; cursor:pointer; font-weight:600; letter-spacing:0.1em; text-transform:uppercase;">Send Message ↗</button>
</form>
"""
            })
        ], 55)
    ], {"background_color": "#f5f2ea", "padding": {"unit": "px", "top": "80", "bottom": "80"}})
]

contact_template = {
    "version": "0.4",
    "title": "Sacred Origins - Contact",
    "type": "page",
    "content": contact_sections
}
with open(TEMPLATES_DIR / "elementor-contact.json", "w", encoding="utf-8") as f:
    json.dump(contact_template, f, indent=2)

# -----------------------------------------------------------------------------
# 4b. ELEMENTOR TEMPLATE: SCHEDULING
# -----------------------------------------------------------------------------
scheduling_sections = [
    make_section([
        make_column([
            make_widget("heading", {
                "title": "INTAKE & CONSULTATION",
                "header_size": "h6",
                "custom_css": "color: #765f40; letter-spacing: 0.2em; text-align: center;"
            }),
            make_widget("heading", {
                "title": "Begin your healing journey.",
                "header_size": "h1",
                "custom_css": "font-family: 'Playfair Display', serif; text-align: center;"
            }),
            make_widget("text-editor", {
                "editor": "<p style='text-align: center; color: #576059; font-size: 18px; max-width: 650px; margin: auto;'>Schedule a 15-minute consultation with Bryant or Kai to discuss your intentions, answer questions, and prepare for ceremony.</p>"
            })
        ], 100)
    ], {"background_color": "#ded7c5", "padding": {"unit": "px", "top": "80", "bottom": "80"}}),

    make_section([
        make_column([
            make_widget("heading", {
                "title": "DIRECT ONLINE BOOKING",
                "header_size": "h6",
                "custom_css": "color: #9a794a; letter-spacing: 0.15em;"
            }),
            make_widget("heading", {
                "title": "Select a time that works for you.",
                "header_size": "h2",
                "custom_css": "font-family: 'Playfair Display', serif; margin: 10px 0 20px;"
            }),
            make_widget("text-editor", {
                "editor": "<p style='color: #576059; line-height: 1.8; font-size: 15px;'>Our complimentary consultation is a safe, no-pressure space where we get to know you, understand any health considerations, and help determine whether Kambo, Reiki, or our retreats are the right fit for your path.</p>"
            }),
            make_widget("html", {
                "html": """<div class="calendly-box">
  <div class="calendly-inline-widget" data-url="https://calendly.com/sacredoriginsnyc/15" style="width:100%;height:700px;"></div>
  <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
</div>
<div class="calendly-fallback">
  <p style="margin-bottom:12px;color:#576059;">Having trouble loading the calendar?</p>
  <a class="button button-dark" href="https://calendly.com/sacredoriginsnyc/15" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:12px;background:#183126;color:#fff;padding:14px 22px;text-decoration:none;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;">Open Calendly in New Tab <span>↗</span></a>
</div>"""
            })
        ], 60),
        make_column([
            make_widget("html", {
                "html": """<div style="background:#f5f2ea;border:1px solid #d5cfbe;overflow:hidden;margin-bottom:30px;">
  <img src="https://sacred-nu.vercel.app/assets/images/unsplash-image-rrnhdu2jokq.jpg" style="width:100%;height:300px;object-fit:cover;display:block;" alt="Sacred space reflection">
  <div style="padding:30px 25px;">
    <h3 style="font-family:'Playfair Display',serif;font-size:24px;margin:0 0 12px;">What to Expect on the Call</h3>
    <ul style="color:#556057;line-height:1.8;padding-left:20px;font-size:14px;margin-bottom:0;">
      <li>A welcoming conversation with Bryant or Kaira.</li>
      <li>Discussion of your personal intentions, background, and goals.</li>
      <li>Confidential medical review and contraindication check for Kambo.</li>
      <li>Guidance on ceremony location, preparation diet, and dates.</li>
    </ul>
  </div>
</div>

<div style="background:#ebe6d8;border:1px solid #d5cfbe;padding:30px 25px;">
  <h3 style="font-family:'Playfair Display',serif;font-size:20px;margin:0 0 10px;">Prefer Email or Custom Inquiries?</h3>
  <p style="color:#5f6b60;font-size:14px;line-height:1.7;margin-bottom:20px;">If you have a private group request, house limpia inquiry, or would prefer to connect via writing first, feel free to reach out directly.</p>
  <a href="mailto:sacredoriginsnyc@gmail.com" style="font-weight:600;color:#183126;text-transform:uppercase;font-size:12px;letter-spacing:0.1em;border-bottom:1px solid currentColor;padding-bottom:4px;text-decoration:none;">sacredoriginsnyc@gmail.com ↗</a>
</div>"""
            })
        ], 40)
    ], {"background_color": "#f5f2ea", "padding": {"unit": "px", "top": "80", "bottom": "90"}}),

    make_section([
        make_column([
            make_widget("heading", {
                "title": "A CONVERSATION IS A BEGINNING",
                "header_size": "h6",
                "custom_css": "color: #bfa677; letter-spacing: 0.15em;"
            }),
            make_widget("heading", {
                "title": "Questions before booking?",
                "header_size": "h2",
                "custom_css": "font-family: 'Playfair Display', serif; color: #f5eedf;"
            })
        ], 70),
        make_column([
            make_widget("button", {
                "text": "Send a Message ↗",
                "link": {"url": "/contact/"},
                "button_type": "default"
            })
        ], 30)
    ], {"background_color": "#183126", "padding": {"unit": "px", "top": "70", "bottom": "70"}})
]

scheduling_template = {
    "version": "0.4",
    "title": "Sacred Origins - Scheduling",
    "type": "page",
    "content": scheduling_sections
}
with open(TEMPLATES_DIR / "elementor-scheduling.json", "w", encoding="utf-8") as f:
    json.dump(scheduling_template, f, indent=2)

# -----------------------------------------------------------------------------
# 5. ELEMENTOR TEMPLATE: SHOP
# -----------------------------------------------------------------------------
shop_sections = [
    make_section([
        make_column([
            make_widget("heading", {
                "title": "THE SACRED ORIGINS APOTHECARY",
                "header_size": "h6",
                "custom_css": "color: #765f40; letter-spacing: 0.2em; text-align: center;"
            }),
            make_widget("heading", {
                "title": "Gather your ritual.",
                "header_size": "h1",
                "custom_css": "font-family: 'Playfair Display', serif; text-align: center;"
            }),
            make_widget("text-editor", {
                "editor": "<p style='text-align: center; color: #576059; font-size: 18px;'>Hapé blends and traditional applicators, selected for intentional practice and ancestral connection.</p>"
            })
        ], 100)
    ], {"background_color": "#ddd6c5", "padding": {"unit": "px", "top": "80", "bottom": "80"}}),
    
    make_section([
        make_column([
            make_widget("shortcode", {
                "shortcode": "[products columns='3' limit='12']"
            })
        ], 100)
    ], {"background_color": "#f5f2ea", "padding": {"unit": "px", "top": "60", "bottom": "80"}})
]

shop_template = {
    "version": "0.4",
    "title": "Sacred Origins - Shop",
    "type": "page",
    "content": shop_sections
}
with open(TEMPLATES_DIR / "elementor-shop.json", "w", encoding="utf-8") as f:
    json.dump(shop_template, f, indent=2)

# -----------------------------------------------------------------------------
# 5a. ELEMENTOR TEMPLATE: BLOG HUB
# -----------------------------------------------------------------------------
blog_cards_html = """<div class="blog-grid">
  <a class="blog-card" href="/the-pharmacology-of-kambo-how-its-compounds-affect-the-human-body/">
    <div class="blog-thumb" style="background-image:url('https://sacred-nu.vercel.app/assets/images/kambo_dots.jpg');">
      <span class="blog-tag">Kambo Science</span>
    </div>
    <div class="blog-card-content">
      <div class="blog-meta"><span>Kaira Otero, LCSW</span><span>7 min read</span></div>
      <h3>The Pharmacology of Kambo: How Its Compounds Affect the Human Body</h3>
      <p>Explore the science of Kambo, a powerful Amazonian healing tradition. Learn how its unique bioactive peptides work to purify the body, calm the mind, and uplift the spirit.</p>
      <span class="blog-readmore">Read Article <span>↗</span></span>
    </div>
  </a>

  <a class="blog-card" href="/the-sacred-origins-of-sananga-history-benefits-and-usage/">
    <div class="blog-thumb" style="background-image:url('https://sacred-nu.vercel.app/assets/images/sananga_.jpeg');">
      <span class="blog-tag">Plant Medicine</span>
    </div>
    <div class="blog-card-content">
      <div class="blog-meta"><span>Kaira Otero, LCSW</span><span>6 min read</span></div>
      <h3>The Sacred Origins of Sananga: History, Benefits, and Usage</h3>
      <p>Discover the sacred origins of Sananga, an Amazonian eye medicine used for centuries to enhance vision, cleanse negative energy, and promote spiritual alignment.</p>
      <span class="blog-readmore">Read Article <span>↗</span></span>
    </div>
  </a>

  <a class="blog-card" href="/getting-ready-for-your-kambo-ceremony-a-friendly-guide/">
    <div class="blog-thumb" style="background-image:url('https://sacred-nu.vercel.app/assets/images/kambo_2.jpg');">
      <span class="blog-tag">Ceremony Prep</span>
    </div>
    <div class="blog-card-content">
      <div class="blog-meta"><span>Kaira Otero, LCSW</span><span>5 min read</span></div>
      <h3>Getting Ready for Your Kambo Ceremony: A Friendly Guide</h3>
      <p>Preparing for your first Kambo session? Follow these essential steps for diet, mindset, hydration, and intention-setting to ensure a grounded experience.</p>
      <span class="blog-readmore">Read Article <span>↗</span></span>
    </div>
  </a>

  <a class="blog-card" href="/discovering-kambo-a-sacred-healing-tradition-for-modern-times/">
    <div class="blog-thumb" style="background-image:url('https://sacred-nu.vercel.app/assets/images/kambo_1.png');">
      <span class="blog-tag">Amazonian Medicine</span>
    </div>
    <div class="blog-card-content">
      <div class="blog-meta"><span>Kaira Otero, LCSW</span><span>6 min read</span></div>
      <h3>Discovering Kambo: A Sacred Healing Tradition for Modern Times</h3>
      <p>Discover the transformative power of Kambo, a sacred healing practice rooted in Amazonian indigenous traditions. Learn about its cultural significance and holistic benefits.</p>
      <span class="blog-readmore">Read Article <span>↗</span></span>
    </div>
  </a>
</div>"""

blog_sections = [
    make_section([
        make_column([
            make_widget("heading", {
                "title": "SACRED WRITINGS & SCIENCE",
                "header_size": "h6",
                "custom_css": "color: #765f40; letter-spacing: 0.2em; text-align: center;"
            }),
            make_widget("heading", {
                "title": "The Sacred Origins Journal.",
                "header_size": "h1",
                "custom_css": "font-family: 'Playfair Display', serif; text-align: center;"
            }),
            make_widget("text-editor", {
                "editor": "<p style='text-align: center; color: #576059; font-size: 18px; max-width: 650px; margin: auto;'>Exploring the cultural roots, pharmacology, and ceremonial wisdom of Kambo, Sananga, Hapé, and holistic healing.</p>"
            })
        ], 100)
    ], {"background_color": "#ded8c7", "padding": {"unit": "px", "top": "80", "bottom": "80"}}),

    make_section([
        make_column([
            make_widget("heading", {
                "title": "ARTICLES & GUIDES",
                "header_size": "h6",
                "custom_css": "color: #9a794a; letter-spacing: 0.15em;"
            }),
            make_widget("heading", {
                "title": "Deep dives & medicine notes.",
                "header_size": "h2",
                "custom_css": "font-family: 'Playfair Display', serif; margin: 10px 0 35px;"
            }),
            make_widget("html", {
                "html": blog_cards_html
            })
        ], 100)
    ], {"background_color": "#f5f2ea", "padding": {"unit": "px", "top": "80", "bottom": "90"}}),

    make_section([
        make_column([
            make_widget("heading", {
                "title": "CONTINUE THE CONVERSATION",
                "header_size": "h6",
                "custom_css": "color: #bfa677; letter-spacing: 0.15em;"
            }),
            make_widget("heading", {
                "title": "Have a question about one of the medicines?",
                "header_size": "h2",
                "custom_css": "font-family: 'Playfair Display', serif; color: #f5eedf;"
            })
        ], 70),
        make_column([
            make_widget("button", {
                "text": "Send us a Message ↗",
                "link": {"url": "/contact/"},
                "button_type": "default"
            })
        ], 30)
    ], {"background_color": "#183126", "padding": {"unit": "px", "top": "70", "bottom": "70"}})
]

blog_template = {
    "version": "0.4",
    "title": "Sacred Origins - Blog Journal",
    "type": "page",
    "content": blog_sections
}
with open(TEMPLATES_DIR / "elementor-blog.json", "w", encoding="utf-8") as f:
    json.dump(blog_template, f, indent=2)


# -----------------------------------------------------------------------------
# 5b. ELEMENTOR TEMPLATE: HEADER
# -----------------------------------------------------------------------------
header_html = """<div class="announcement">
  <span class="announcement-left">NYC · A PLACE TO RETURN TO</span>
  <span class="announcement-center">ROOTED IN COMMUNITY · GUIDED BY ANCESTRAL WISDOM</span>
  <span class="announcement-right">EST. IN CONNECTION <span aria-hidden="true">✳</span></span>
</div>
<header class="header">
  <div class="header-inner">
    <span class="header-loc">SACRED ORIGINS<br>NEW YORK CITY</span>
    <a class="brand" href="/" aria-label="Sacred Origins home">
      <img class="brand-logo" src="/wp-content/uploads/sacred-origins-official-logo.png" width="105" height="105" alt="Sacred Origins NYC">
    </a>
    <div class="header-actions">
      <a class="header-shop" href="/scheduling/">SCHEDULE CALL <span>↗</span></a>
      <button class="menu-toggle" aria-label="Open menu" aria-controls="nav" aria-expanded="false">
        <span></span><span></span>
      </button>
    </div>
  </div>
  <nav class="nav" id="nav" aria-label="Main navigation">
    <a href="/">Home</a>
    <a href="/about-us/">About Us</a>
    <a href="/offerings/">Offerings</a>
    <a href="/scheduling/">Scheduling</a>
    <a href="/shop/">Shop</a>
    <a href="/blog/">Blog</a>
    <a href="/contact/">Contact</a>
    <a class="nav-cta-mobile" href="/scheduling/">Schedule a Call <span>↗</span></a>
  </nav>
</header>"""

header_template = {
    "version": "0.4",
    "title": "Sacred Origins - Header",
    "type": "section",
    "content": [
        make_section([
            make_column([
                make_widget("html", {"html": header_html})
            ], 100)
        ], {"layout": "full_width", "gap": "no", "padding": {"unit": "px", "top": "0", "bottom": "0", "left": "0", "right": "0", "isLinked": True}})
    ]
}
with open(TEMPLATES_DIR / "elementor-header.json", "w", encoding="utf-8") as f:
    json.dump(header_template, f, indent=2)

# -----------------------------------------------------------------------------
# 5c. ELEMENTOR TEMPLATE: FOOTER
# -----------------------------------------------------------------------------
footer_html = """<footer class="footer">
  <div class="footer-inner-wrap">
    <div class="footer-intro">
      <span class="eyebrow light">THE NEXT CHAPTER BEGINS HERE</span>
      <a href="/scheduling/">Begin your journey <span>↗</span></a>
    </div>
    <div class="footer-top">
      <div>
        <a class="footer-logo" href="/" aria-label="Sacred Origins home">
          <img src="/wp-content/uploads/sacred-origins-logo-light.png" width="150" height="150" alt="Sacred Origins NYC">
        </a>
        <p>A sacred sanctuary for healing, reflection, and ancestral reconnection.</p>
        <a href="mailto:sacredoriginsnyc@gmail.com" class="footer-mail">sacredoriginsnyc@gmail.com ↗</a>
      </div>
      <div>
        <h3>Explore</h3>
        <a href="/about-us/">About Us</a>
        <a href="/offerings/">Offerings</a>
        <a href="/scheduling/">Scheduling</a>
        <a href="/shop/">Apothecary</a>
        <a href="/blog/">Journal & Articles</a>
      </div>
      <div>
        <h3>Connect</h3>
        <a href="/contact/">Contact Us</a>
        <a href="/scheduling/">Schedule a Consultation</a>
        <span>New York City · Lenapehoking</span>
      </div>
    </div>
    <a class="footer-wordmark" href="/" aria-label="Sacred Origins home">SACRED<span>✺</span>ORIGINS</a>
    <div class="footer-bottom">
      <span>© 2026 Sacred Origins NYC. All Rights Reserved.</span>
      <span>EMPOWERING BIPOC COMMUNITIES · GUIDED BY ANCESTRAL WISDOM</span>
      <a href="#main">BACK TO TOP ↑</a>
    </div>
  </div>
</footer>"""

footer_template = {
    "version": "0.4",
    "title": "Sacred Origins - Footer",
    "type": "section",
    "content": [
        make_section([
            make_column([
                make_widget("html", {"html": footer_html})
            ], 100)
        ], {"layout": "full_width", "gap": "no", "padding": {"unit": "px", "top": "0", "bottom": "0", "left": "0", "right": "0", "isLinked": True}})
    ]
}
with open(TEMPLATES_DIR / "elementor-footer.json", "w", encoding="utf-8") as f:
    json.dump(footer_template, f, indent=2)


# -----------------------------------------------------------------------------
# 6. WOOCOMMERCE PRODUCTS CSV EXPORT
# -----------------------------------------------------------------------------
import csv
csv_file = OUTPUT_DIR / "sacred-origins-woocommerce-products.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Type", "SKU", "Name", "Published", "Is featured?", "Visibility in catalog",
        "Short description", "Description", "In stock?", "Stock", "Regular price",
        "Categories", "Tags", "Images"
    ])
    
    # 5 client products
    items = [
        ("simple", "SO-CACAO", "Cacao Hapé", 1, 1, "visible", "Warm · Heart-Centered · Gentle", products[0][4], 1, 20, "35.00", "Hapé, Botanical Snuff", "hape, cacao, heart-opening", "https://sacred-nu.vercel.app/assets/apothecary.webp"),
        ("simple", "SO-MURICI", "Murici Hapé", 1, 1, "visible", "Grounding · Clearing · Protective", products[1][4], 1, 20, "35.00", "Hapé, Botanical Snuff", "hape, murici, grounding", "https://sacred-nu.vercel.app/assets/still-life.webp"),
        ("simple", "SO-SAMAUMA", "Samaúma Flower Hapé", 1, 1, "visible", "Expansive · Uplifting · Prayerful", products[2][4], 1, 20, "38.00", "Hapé, Botanical Snuff", "hape, samauma, prayerful", "https://sacred-nu.vercel.app/assets/apothecary.webp"),
        ("simple", "SO-KURIPE", "Kuripe Applicator", 1, 0, "visible", "For Self-Application", products[3][4], 1, 15, "45.00", "Applicators, Ceremony Tools", "kuripe, applicator, self-ceremony", "https://sacred-nu.vercel.app/assets/applicators.webp"),
        ("simple", "SO-TEPI", "Tepi Applicator", 1, 0, "visible", "For Serving Another", products[4][4], 1, 15, "65.00", "Applicators, Ceremony Tools", "tepi, applicator, space holder", "https://sacred-nu.vercel.app/assets/applicators.webp"),
    ]
    for row in items:
        writer.writerow(row)

# -----------------------------------------------------------------------------
# 7. WORDPRESS WXR XML EXPORT FILE
# -----------------------------------------------------------------------------
xml_file = OUTPUT_DIR / "sacred-origins-wordpress-content.xml"
with open(xml_file, "w", encoding="utf-8") as f:
    f.write("""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
	xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:wp="http://wordpress.org/export/1.2/"
>
<channel>
	<title>Sacred Origins NYC</title>
	<link>https://www.sacredorigins.org</link>
	<description>Kambo &amp; Reiki Healing in New York City</description>
	<pubDate>Wed, 23 Sep 2026 10:00:00 +0000</pubDate>
	<language>en-US</language>
	<wp:wxr_version>1.2</wp:wxr_version>
	<wp:base_site_url>https://www.sacredorigins.org</wp:base_site_url>
	<wp:base_blog_url>https://www.sacredorigins.org</wp:base_blog_url>
""")
    
    # Write Blog Posts
    post_id = 100
    for bp in blog_posts:
        post_id += 1
        f.write(f"""
	<item>
		<title><![CDATA[{bp['title']}]]></title>
		<link>https://www.sacredorigins.org/blog/{bp['slug']}/</link>
		<pubDate>Wed, 23 Sep 2026 10:00:00 +0000</pubDate>
		<dc:creator><![CDATA[Kaira Otero]]></dc:creator>
		<category><![CDATA[{bp['category']}]]></category>
		<guid isPermaLink="false">https://www.sacredorigins.org/?p={post_id}</guid>
		<description></description>
		<content:encoded><![CDATA[{bp['content']}]]></content:encoded>
		<excerpt:encoded><![CDATA[{bp['desc']}]]></excerpt:encoded>
		<wp:post_id>{post_id}</wp:post_id>
		<wp:post_date><![CDATA[2026-09-23 10:00:00]]></wp:post_date>
		<wp:post_name><![CDATA[{bp['slug']}]]></wp:post_name>
		<wp:status><![CDATA[publish]]></wp:status>
		<wp:post_type><![CDATA[post]]></wp:post_type>
	</item>
""")

    # Write Core Pages
    pages_list = [
        ("Home", "home", "Sacred Origins NYC - Home"),
        ("About Us", "about-us", "About Sacred Origins"),
        ("Offerings", "offerings", "Offerings - Sacred Origins"),
        ("Scheduling", "scheduling", "Scheduling - Sacred Origins"),
        ("Contact", "contact", "Contact Us - Sacred Origins"),
        ("Shop", "shop", "Apothecary Shop - Sacred Origins")
    ]
    for p_title, p_slug, p_desc in pages_list:
        post_id += 1
        f.write(f"""
	<item>
		<title><![CDATA[{p_title}]]></title>
		<link>https://www.sacredorigins.org/{p_slug}/</link>
		<pubDate>Wed, 23 Sep 2026 10:00:00 +0000</pubDate>
		<dc:creator><![CDATA[admin]]></dc:creator>
		<guid isPermaLink="false">https://www.sacredorigins.org/?page_id={post_id}</guid>
		<description></description>
		<content:encoded><![CDATA[<!-- Edit with Elementor -->]]></content:encoded>
		<wp:post_id>{post_id}</wp:post_id>
		<wp:post_date><![CDATA[2026-09-23 10:00:00]]></wp:post_date>
		<wp:post_name><![CDATA[{p_slug}]]></wp:post_name>
		<wp:status><![CDATA[publish]]></wp:status>
		<wp:post_type><![CDATA[page]]></wp:post_type>
		<wp:postmeta>
			<wp:meta_key><![CDATA[_elementor_edit_mode]]></wp:meta_key>
			<wp:meta_value><![CDATA[builder]]></wp:meta_value>
		</wp:postmeta>
		<wp:postmeta>
			<wp:meta_key><![CDATA[_wp_page_template]]></wp:meta_key>
			<wp:meta_value><![CDATA[elementor_header_footer]]></wp:meta_value>
		</wp:postmeta>
	</item>
""")

    f.write("</channel>\n</rss>\n")

# -----------------------------------------------------------------------------
# 8. CREATE COMPLETE ZIP PACKAGE
# -----------------------------------------------------------------------------
zip_path = Path("sacred-origins-elementor-complete-package.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for root_dir, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            full_p = Path(root_dir) / file
            rel_p = full_p.relative_to(OUTPUT_DIR.parent)
            z.write(full_p, rel_p)

print(f"Successfully generated all Elementor JSON templates and packages in: {OUTPUT_DIR}")
print(f"Created ZIP bundle: {zip_path} (size: {zip_path.stat().st_size} bytes)")
