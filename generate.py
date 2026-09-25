import os
from pathlib import Path
from html import escape
from urllib.parse import quote

root = Path(__file__).parent / 'dist'

# Navigation links
nav = [
    ('Home', '/'),
    ('About Us', '/about/'),
    ('Offerings', '/offerings/'),
    ('Scheduling', '/scheduling/'),
    ('Shop', '/shop/'),
    ('Blog', '/blog/'),
    ('Contact', '/contact/')
]

# Apothecary Products
products = [
    ('cacao-hape', 'Cacao Hapé', 'Hapé', 'Warm · Heart-centered · Gentle',
     'Cacao Hapé carries a warm, nurturing quality that invites you inward. Traditionally associated with the heart, cacao complements Hapé with a softer, more expansive energy—beautiful for meditation, emotional reflection, prayer, and moments when you want to reconnect with yourself from a place of openness.'),
    ('murici-hape', 'Murici Hapé', 'Hapé', 'Grounding · Clearing · Protective',
     'Murici is a deeply grounding Hapé traditionally prepared using the Murici tree. Its energy is often described as steady, cleansing, and centering—supporting moments of release while bringing awareness back into the body. A beautiful medicine for clearing heaviness, grounding your energy, and returning to center.'),
    ('samauma-flower-hape', 'Samaúma Flower Hapé', 'Hapé', 'Expansive · Uplifting · Prayerful',
     'Known as the Mother of Trees, the great Samaúma is one of the towering beings of the Amazon rainforest. This flower blend carries a lighter, more expansive quality—inviting openness of the heart, prayer, meditation, and connection to something greater than ourselves. Rooted yet spacious, Samaúma Flower is medicine for opening upward while remaining connected to the Earth.'),
    ('kuripe', 'Kuripe', 'Applicator', 'For self-application',
     'A Kuripe is a traditional V-shaped applicator used to serve Hapé to yourself. Connecting the mouth to the nostril, it allows the medicine to be received through your own breath and intention. More than simply a tool, the Kuripe can become a personal ceremonial object—an extension of your relationship with the medicine and your individual practice.'),
    ('tepi', 'Tepi', 'Applicator', 'For serving another',
     'A Tepi is a longer ceremonial applicator used to serve Hapé from one person to another. Traditionally used within shared or guided practice, the Tepi brings relationship, trust, intention, and responsibility into the serving of the medicine. It is a tool for those called to hold space and work with Hapé in community or ceremony.')
]

# Core Offerings from Sacred Origins
offerings_data = [
    {
        'title': 'Kambo Ceremony',
        'tag': 'Amazonian Medicine · Detoxification · Immunity',
        'desc': 'Kambo is a traditional Amazonian medicine that comes from the secretion of the Phyllomedusa bicolor frog. It is used to cleanse the body, mind, and spirit. This powerful frog secretion helps detoxify, boost immunity, and release deep-seated emotional blockages. Our ceremonies honor the indigenous roots of Kambo, offering a safe, deeply held, and supportive space for renewal.',
        'image': '/assets/images/kambo_image.png',
        'link_tag': 'Kambo Ceremony'
    },
    {
        'title': 'Reiki Healing',
        'tag': 'Energy Work · Relaxation · Alignment',
        'desc': 'Reiki is a gentle, energy-based healing practice that promotes relaxation, balance, and emotional well-being. Using universal life force energy, Reiki clears energetic blockages and supports the body’s innate healing capacity. Guided by a Reiki Master with over a decade of dedicated practice, experience deep peace and cellular restoration.',
        'image': '/assets/images/reiki_.png',
        'link_tag': 'Reiki'
    },
    {
        'title': 'Retreats & Group Journeys',
        'tag': 'Community · Deep Immersion · Nature',
        'desc': 'Our Sacred Healing Retreats offer immersive experiences in indigenous plant medicine, energy healing, and holistic practices. These retreats are designed to foster deep personal transformation, spiritual growth, and genuine community connection, all within a nurturing, intentional sanctuary away from the noise.',
        'image': '/assets/images/1eddb259-b0aa-4161-9d1a-72880a781f4f.jpg',
        'link_tag': 'Retreats'
    },
    {
        'title': 'Hapé and Sananga Circles',
        'tag': 'Sacred Snuff · Inner Vision · Grounding',
        'desc': 'Join our Hapé and Sananga Circles to connect with sacred Amazonian plant medicines. Hapé, an intentional sacred blend, grounds and clears the mind, while Sananga, sacred eye medicine, sharpens inner vision and releases emotional stagnation. Together, these ceremonies foster clarity and spiritual alignment.',
        'image': '/assets/images/_dsc7634.jpg',
        'link_tag': 'Hapé and Sananga Circles'
    },
    {
        'title': 'Psychedelic Preparation & Integration',
        'tag': 'Guidance · Grounding · Embodiment',
        'desc': 'We offer compassionate guidance and clinical insight for those working with expanded states of consciousness, helping you prepare for transformative experiences and integrate the insights gained. Through personalized sessions led by licensed psychotherapy and somatic care, we help you embody your journey’s wisdom.',
        'image': '/assets/images/unsplash-image-betmvwgycly.jpg',
        'link_tag': 'Preparation and Integration'
    },
    {
        'title': 'House Cleansings / Limpias',
        'tag': 'Space Clearing · Protection · Sacred Herbs',
        'desc': 'Our House Cleansings, or Limpias, are sacred rituals designed to clear negative energy and restore balance to your home or workspace. Using traditional tools like sacred copal, herbs, smoke, sound, and prayer, we purify the environment, inviting harmony, protection, and positive energy to flow freely.',
        'image': '/assets/images/house_cleansing_.png',
        'link_tag': 'House Cleansings'
    }
]

# Client Testimonials from Sacred Origins
testimonials_data = [
    {
        'name': 'Clarimar',
        'quote': "If you're looking to start your healing journey or continue it, I highly recommend Sacred Origins NYC. The care and hard work I saw and experienced both through the retreat and local group work is admirable. There's a lot of care and intentionality that went into ensuring that the practices remain sacred and that the journey feels safe. It's suitable for those who are less outgoing and for those who are more comfortable taking up space since there is a balance of group and private time. I was able to receive/grow not only from the moments I engaged with the practices, but also from the private moments and curated group ones. Looking forward to the next retreat!",
        'badge': 'Retreat & Group Work'
    },
    {
        'name': 'Alexander',
        'quote': "I have no words to describe how amazing my spiritual retreat experience was with Sacred Origins, I am deeply thankful for everything. I can’t wait for the next retreat.",
        'badge': 'Spiritual Retreat'
    },
    {
        'name': 'Lauren O.',
        'quote': 'Kaira & Bryant have played a role in helping me change my life. They take the time to get to know you and create an environment that is safe, and simply feels like home. As someone who approaches the unfamiliar with precaution, it’s been a breath of fresh air to come across people so patient, understanding and knowledgable. I look forward to more opportunities to work with them as I continue down my own journey of exploration and growth.',
        'badge': 'Retreat & Ceremony'
    },
    {
        'name': 'Piri J.',
        'quote': 'I have had the pleasure of attending one of the retreats and receiving the guidance from both Kaira and Bryant. It was truly an enlightening experience and was the catalyst of my transformation in many areas of my life. On another occasion, I was educated about Hapè and was served for the 1st time by Kaira. She was gentle and patient during this experience. I sat with this medicine for about 10 minutes. It felt as though my energy was renewed and protected. It shifted my perspective and I also felt a lot lighter afterwards. Thank you for continuing to help and heal our community!',
        'badge': 'Retreat & Hapé'
    },
    {
        'name': 'Omar M.',
        'quote': 'This has been the most incredible and transformative experience I have ever had in my life - a milestone in my life that has brought clarity. I have spent these past 4 years between all types of mediations/therapists/solo travels etc. but nothing compares to setting an intention with what is earthly grown. I stand on the other side of this experience another person and a proud advocate of this experience. Being a human is tricky but can be so beautiful the further you explore.',
        'badge': 'Plant Medicine Journey'
    },
    {
        'name': 'Sydney R.',
        'quote': 'Finding Kaira and Bryant at Sacred Origins NYC was such a gift! As someone from the city, it’s rare to see people of color leading sacred medicine work, and they made my first experience with Kambo, Hape, and Sananga feel so natural and welcoming. Their passion and care are undeniable—you feel it in everything they do. Kaira’s warm, grounding presence and Bryant’s calm, steady energy are the perfect duo. Together, they create a space that feels safe, intentional, and deeply respectful.',
        'badge': 'Kambo & Circles'
    },
    {
        'name': 'Ana L.',
        'quote': 'Bryant and Kaira are truly life-changing. I worked with Kai during a therapeutic training in Colorado, and the experience was pivotal to my post-traumatic growth. Having participated in other ceremonies, none compare to the transformation I experienced with them. Since then, I’ve attended two more retreats that have profoundly impacted me. I no longer rely on psychotropic medication, have broken free from self-limiting patterns, and am now in a loving relationship while living more authentically.',
        'badge': 'Retreat & Integration'
    },
    {
        'name': 'Chris S.L.',
        'quote': 'I wasn’t sure what to expect going into my first experience with earth medicine, but I’m so glad I trusted my gut and joined Sacred Origins. Kaira and Bryant created such a warm, intentional space that any nerves I had quickly disappeared. They were so thoughtful in every detail, from the setup to the guidance they gave before and after, making it easy to connect with myself and the group. They worked seamlessly together, making everyone feel supported and heard.',
        'badge': 'Retreat Journey'
    },
    {
        'name': 'Alexa F.',
        'quote': 'I recently had a very profound and healing experience through a combined Reiki session and plant medicine ceremony, hosted by Sacred Origins NYC. From the moment I entered the healing space, I felt an overwhelming sense of calm and safety. Kaira and Bryant were deeply intuitive, warm, and welcoming - all of which immediately put me at ease. The session began with intention setting, followed by the introduction of a sacred plant medicine, and then the reiki ceremony. Throughout the experience, l could feel my heart soften and a deep emotional release bubbling up.',
        'badge': 'Reiki & Ceremony'
    },
    {
        'name': 'Alyssa M.',
        'quote': 'Kaira & Bryant have shed much light into my life with their blessings. Every experience has been memorable, transformative and in alignment with my personal journey of inner work. We’ve shared moments together in community sitting with medicine during a retreat, receiving reiki and my personal favorite, Hapè circles. I’ve also had the pleasure of receiving a revitalizing limpia in my home. A safe, warm & loving energy is truly a part of every experience.',
        'badge': 'Reiki, Hapé & Limpia'
    },
    {
        'name': 'Chris S.',
        'quote': 'Kaira and Bryant made my experience with earth medicine incredibly memorable, and their guidance through everything was treated with patience and immense care. I would strongly suggest anyone looking to experience a spiritual retreat with Kaira and Bryant!',
        'badge': 'Earth Medicine'
    },
    {
        'name': 'Brandon F.',
        'quote': 'Have had several great, meditative, and healing experiences with the team here while practicing with earth medicines under expert supervision. Definitely recommend!',
        'badge': 'Supervised Ceremony'
    }
]

# FAQs from Sacred Origins
faqs_data = [
    (
        "What is Kambo, and how can it help me?",
        "Kambo is a traditional Amazonian medicine that comes from the secretion of the Phyllomedusa bicolor frog. It's used to cleanse the body, mind, and spirit. Kambo can help clear toxins, boost immunity, and release emotional blockages. Many people also experience greater clarity, focus, and a sense of alignment after a Kambo session. It’s a powerful medicine for those seeking deep healing and transformation."
    ),
    (
        "What are Hapé and Sananga, and what should I expect in a ceremony?",
        "Hapé (also known as Rapé) is a sacred tobacco snuff used by indigenous Amazonian tribes for grounding, clarity, and connection to spirit. Sananga is an eye drop made from a sacred Amazonian plant, used to enhance vision (both physical and spiritual) and clear energetic blockages. During a ceremony, you'll be guided through a meditative process, and we’ll support you in connecting with these plant medicines in a safe and sacred space."
    ),
    (
        "Do I need to have previous experience with plant medicine to participate?",
        "Not at all! We welcome everyone, whether you're new to these practices or have prior experience. Our ceremonies are designed to meet you where you are, and we’ll guide you every step of the way. Your safety, comfort, and transformation are our top priorities."
    ),
    (
        "What should I do to prepare for a Kambo, Hapé, or Sananga ceremony?",
        "Preparation is key to having a meaningful and safe experience. We recommend following a clean diet for a few days before the ceremony, avoiding alcohol, processed foods, and other toxins. Stay hydrated and set a clear intention for your healing journey. We’ll provide you with detailed guidance on how to prepare beforehand, so you’ll feel ready and supported."
    ),
    (
        "What are the benefits of Reiki?",
        "Reiki is a gentle yet powerful energy healing practice that promotes balance and well-being on all levels—physical, emotional, mental, and spiritual. Many people feel relaxed, lighter, and more centered after a session. It can help release stress, alleviate pain, and support emotional healing. Reiki is a beautiful complement to the plant medicine work we do, as it supports full holistic healing."
    ),
    (
        "How can I book a session or ceremony?",
        "Booking a session is easy! You can schedule directly through our <a href='/scheduling/' style='color:#b7955e;text-decoration:underline;'>Scheduling page</a>, reach out to us through our <a href='/contact/' style='color:#b7955e;text-decoration:underline;'>Contact page</a>, or email us directly at <a href='mailto:sacredoriginsnyc@gmail.com' style='color:#b7955e;text-decoration:underline;'>sacredoriginsnyc@gmail.com</a>. We’ll work with you to find a time and space that aligns with your needs."
    )
]

# Blog Posts from Sacred Origins
blog_posts = [
    {
        'slug': 'the-pharmacology-of-kambo-how-its-compounds-affect-the-human-body',
        'title': 'The Pharmacology of Kambo: How Its Compounds Affect the Human Body',
        'meta_title': 'Kambo Explained: The Pharmacology Behind Amazonian Frog Medicine',
        'desc': 'Explore the science of Kambo, a powerful Amazonian healing tradition. Learn how its unique bioactive peptides work to purify the body, calm the mind, and uplift the spirit.',
        'image': '/assets/images/kambo_dots.jpg',
        'category': 'Kambo Science',
        'date': 'Published in Sacred Origins Blog',
        'read_time': '7 min read',
        'author': 'Kaira Otero, LCSW',
        'author_bio': 'Co-founder of Sacred Origins NYC, Licensed Clinical Social Worker (LCSW), Reiki Level II practitioner, and certified Kambo practitioner.',
        'content': '''
<p class="lead">Let’s get one thing straight: Kambo isn’t just some trendy wellness fad. This Amazonian frog medicine has been used for centuries by indigenous tribes for its profound healing properties. But what makes Kambo so powerful? Why does it leave people feeling like they’ve been hit by a spiritual freight train (in the best way possible)? The answer lies in its complex pharmacology—a cocktail of bioactive peptides that interact with the human body in ways that are both fascinating and mind-blowing.</p>

<div class="article-img-block">
  <img src="/assets/images/kambo.png" alt="Phyllomedusa bicolor giant monkey frog and Kambo medicine">
  <div class="article-img-caption">The Phyllomedusa bicolor frog from the Amazon rainforest</div>
</div>

<h3>What’s in the Frog Secretion?</h3>
<p>Kambo comes from the secretion of the <em>Phyllomedusa bicolor</em> frog, a bright green tree frog native to the Amazon rainforest. This secretion contains over 100 bioactive peptides—short chains of amino acids that act as messengers in the body. These peptides are the real MVPs of Kambo, and they’re responsible for its wide-ranging effects.</p>

<p>Many of these peptides are pharmacologically active, meaning they can interact with our cells, tissues, and organs in specific ways. Some of these peptides are so unique that they’ve caught the attention of scientists and pharmaceutical researchers alike.</p>

<div class="peptide-grid">
  <div class="peptide-card">
    <h4>1. Phyllomedusin (The Purge Master)</h4>
    <p>Stimulates the smooth muscles of the intestines, initiating a thorough cleanse. It acts on the gut-brain axis to trigger deep cellular and emotional detox.</p>
  </div>
  <div class="peptide-card">
    <h4>2. Dermorphin & Deltorphin (Natural Opioids)</h4>
    <p>Potent peptides binding to opioid receptors in the brain, offering deep pain relief up to 40 times stronger than morphine without synthetic addiction risks.</p>
  </div>
  <div class="peptide-card">
    <h4>3. Phyllokinin & Phyllocaerulein (Blood Flow)</h4>
    <p>Vasodilators widening blood vessels, lowering blood pressure safely, improving circulation, and stimulating adrenal/pituitary balance.</p>
  </div>
  <div class="peptide-card">
    <h4>4. Adenoregulin (Immune Booster)</h4>
    <p>Interacts with adenosine receptors to modulate immune health and cellular metabolism, showing profound antimicrobial and antiviral properties.</p>
  </div>
  <div class="peptide-card" style="grid-column: 1 / -1;">
    <h4>5. Sauvagine (Stress & HPA-Axis Reset)</h4>
    <p>Regulates the body’s hypothalamic-pituitary-adrenal axis, stimulating a controlled release of cortisol that resets systemic stress and fosters enduring clarity.</p>
  </div>
</div>

<div class="article-img-block">
  <img src="/assets/images/kambo_dots.jpg" alt="Traditional Kambo points application on skin">
  <div class="article-img-caption">Traditional Kambo points placed with sacred intention</div>
</div>

<h3>The Body-Mind Connection</h3>
<p>What’s truly remarkable about Kambo is how these peptides work together to create a holistic healing experience. It’s not just about physical detoxification—it’s about resetting the entire system. The peptides interact with the nervous system, the endocrine system, and the immune system, creating a cascade of effects that can lead to profound emotional and spiritual shifts.</p>

<p>For example, the purging process isn’t just physical. Many people report releasing emotional trauma during a Kambo ceremony, as if the medicine is helping them let go of what no longer serves them. This isn’t just anecdotal—there’s a growing body of scientific research suggesting that the gut-brain axis plays a key role in mental health.</p>

<h3>A Word of Caution & Reverence</h3>
<p>As fascinating as the science is, it’s important to remember that Kambo is a sacred medicine, not a recreational drug. It’s not something to be taken lightly or without proper guidance. The indigenous tribes who have used Kambo for generations treat it with deep respect, and so should we. Always work with an experienced, certified practitioner who holds safety and ethics as paramount.</p>

<div class="article-disclaimer">
  <strong>Scientific References:</strong><br>
  • Erspamer, V., et al. (1993). <em>Pharmacological Studies of Phyllomedusa bicolor Skin Secretion.</em> Journal of Ethnopharmacology.<br>
  • Daly, J. W., et al. (2005). <em>Bioactive Alkaloids from Amphibian Skin.</em> Proceedings of the National Academy of Sciences.<br><br>
  <strong>Medical Disclaimer:</strong> This article is for educational and informational purposes only and is not a substitute for medical advice. Consult with a qualified healthcare professional before undertaking any ceremonial or alternative therapy.
</div>
'''
    },
    {
        'slug': 'the-sacred-origins-of-sananga-history-benefits-and-usage',
        'title': 'The Sacred Origins of Sananga: History, Benefits, and Usage',
        'meta_title': 'What is Sananga? The Sacred Amazonian Medicine For Clear Vision',
        'desc': 'Discover the sacred origins of Sananga, an Amazonian eye medicine used for centuries to enhance vision, cleanse negative energy, and promote spiritual alignment.',
        'image': '/assets/images/sananga_.jpeg',
        'category': 'Plant Medicine',
        'date': 'Published in Sacred Origins Blog',
        'read_time': '6 min read',
        'author': 'Kaira Otero, LCSW',
        'author_bio': 'Co-founder of Sacred Origins NYC, Licensed Clinical Social Worker (LCSW), Reiki Level II practitioner, and certified Kambo practitioner.',
        'content': '''
<p class="lead">Sananga is a revered plant medicine from the Amazon Rainforest, long cherished by indigenous tribes for its profound healing properties. It is a natural remedy used to cleanse and enhance both physical and spiritual vision. At Sacred Origins, we honor the ancient traditions tied to Sananga and aim to share its benefits with those seeking holistic healing and spiritual alignment.</p>

<div class="article-img-block">
  <img src="/assets/images/sananga_.jpeg" alt="Sacred Sananga plant medicine bottle and drops">
  <div class="article-img-caption">Sananga: Sacred Amazonian botanical eye drops</div>
</div>

<h3>The Rich History of Sananga</h3>
<p>For generations, tribes such as the Kaxinawá (Huni Kuin) and Yawanawá have used Sananga in their rituals and daily practices. This sacred eye medicine is derived from the roots and bark of shrubs in the <em>Tabernaemontana</em> genus. Prepared in ceremonies by skilled shamans, the medicine is infused with prayers and intentions to enhance its healing power.</p>

<p>In tribal culture, Sananga is considered essential for sharpening vision—both literally and spiritually. Hunters often use it to improve focus and clarity during their pursuits in the dense forest. Beyond its practical uses, Sananga is deeply valued as a tool to cleanse negative energy (known as <em>panema</em>) and realign one’s spiritual path.</p>

<h3>The Many Benefits of Sananga</h3>
<p>Sananga’s healing effects are broad, offering support for physical, emotional, and spiritual well-being:</p>

<div class="peptide-grid">
  <div class="peptide-card">
    <h4>Physical Benefits</h4>
    <p>• Supports Eye Health: Traditionally used to alleviate vision strain, glaucoma, and ocular tension.<br>• Reduces Inflammation: Powerful natural anti-inflammatory compounds ease chronic eye fatigue.<br>• Alleviates Stored Pain: Relaxes facial tension and muscular holding around the head and neck.</p>
  </div>
  <div class="peptide-card">
    <h4>Emotional & Mental Benefits</h4>
    <p>• Cleanses Negative Energies: Assists in releasing stagnant sadness, anxiety, and mental congestion.<br>• Sharpens Focus: Quiets mind chatter and grounds attention firmly in the present moment.<br>• Somatic Release: Allows unexpressed tears and blocked feelings to gently flow.</p>
  </div>
  <div class="peptide-card" style="grid-column: 1 / -1;">
    <h4>Spiritual & Intuitive Alignment</h4>
    <p>• Clears Energetic Blockages: Unblocks the third eye chakra and cleanses the subtle energy body.<br>• Heightens Intuitive Guidance: Fosters a deeper connection to ancestral wisdom and inner sight.<br>• Amplifies Ceremony: Beautifully deepens meditation, Hapé, or sound journeys when received beforehand.</p>
  </div>
</div>

<h3>How to Receive Sananga</h3>
<p>Sananga is traditionally administered as eye drops. Receiving it with intention and conscious breath is essential to experiencing its medicine:</p>
<ol>
  <li><strong>Set Your Intention:</strong> Begin by grounding yourself in silence and establishing what you are asking the medicine to help you see or release.</li>
  <li><strong>Create a Calm Space:</strong> Lie down in a comfortable, dimly lit space with soothing sound and quiet breath.</li>
  <li><strong>Administer the Drops:</strong> A drop is placed in the corner of each eye. When you blink, a strong burning sensation arises for 2 to 5 minutes.</li>
  <li><strong>Breathe & Surrender:</strong> Rather than resisting the heat, breathe deeply into the sensation, allowing physical tears to wash away stagnation.</li>
  <li><strong>Rest & Integrate:</strong> As the heat subsides into a wave of serene calmness, rest and allow clarity to fill your awareness.</li>
</ol>

<div class="article-disclaimer">
  <strong>Important Notice:</strong> Sananga must always be sourced ethically and handled with ceremonial respect. Do not use if you wear contacts during administration, have open eye wounds, or suffer from serious eye detachment conditions.
</div>
'''
    },
    {
        'slug': '81aapg1ja12yc9wjolnnpckod4loeh',
        'alt_slug': 'hape-sacred-medicine-spiritual-healing',
        'title': 'Hapé: A Sacred Medicine for Spiritual Healing and Grounding',
        'meta_title': 'Hapé: A Sacred Medicine for Spiritual Healing and Grounding — Sacred Origins NYC',
        'desc': 'Explore Hapé (Rapé), the ancient Amazonian sacred tobacco snuff used for spiritual alignment, centering, and deep emotional release.',
        'image': '/assets/images/img_1543.jpg',
        'category': 'Ancestral Traditions',
        'date': 'Published in Sacred Origins Blog',
        'read_time': '8 min read',
        'author': 'Kaira Otero, LCSW',
        'author_bio': 'Co-founder of Sacred Origins NYC, Licensed Clinical Social Worker (LCSW), Reiki Level II practitioner, and certified Kambo practitioner.',
        'content': '''
<p class="lead">Hapé (or Rapé) is an ancient and sacred plant medicine, used by indigenous cultures for thousands of years to heal, cleanse, and foster deep connection with the Earth and spirit. Traditionally made from a blend of finely ground tobacco and medicinal tree ashes, hapé is a tool that helps align the mind, body, and spirit.</p>

<div class="article-img-block">
  <img src="/assets/images/img_1543.jpg" alt="Ceremonial Hapé serving with Tepi applicator">
  <div class="article-img-caption">Serving Hapé with prayer and intention during a Sacred Origins ceremony</div>
</div>

<h3>What is Hapé?</h3>
<p>Hapé is created by blending sacred jungle tobacco, known as <em>mapacho</em> (Nicotiana rustica), with medicinal plants, tree barks, and sacred ashes (such as Pau Pereira, Paricá, or Tsunu). Each blend is crafted through days of prayerful preparation, honoring both the plants and the healing lineage.</p>

<p>The practice of using hapé involves receiving the medicine through the nostrils using ceremonial pipes:</p>
<ul>
  <li><strong>The Tepi:</strong> A long two-person pipe used by a trained facilitator to serve another person, bringing relationship, trust, and shared intention into the space.</li>
  <li><strong>The Kuripe:</strong> A compact V-shaped applicator used for self-application, connecting your own breath and intention directly to your practice.</li>
</ul>

<div class="article-img-block">
  <img src="/assets/images/hape__1_.jpg" alt="Different blends of sacred Hapé">
  <div class="article-img-caption">Sacred botanical blends of Amazonian Hapé</div>
</div>

<h3>Amazonian Roots and Taíno Heritage</h3>
<p>While Hapé is internationally known through Amazonian tribal traditions (such as the Yawanawá, Kuntanawa, and Katukina), sacred tobacco snuffing also has deep roots in Caribbean and Taíno ancestral ceremonies known as <em>Cohoba</em> rituals. In both traditions, tobacco was never recreational—it was revered as the Master Plant of prayer, carrying intentions directly to the spirit world.</p>

<h3>Notable Hapé Blends & Their Energies</h3>
<div class="peptide-grid">
  <div class="peptide-card">
    <h4>1. Tsunu Hapé</h4>
    <p>Prepared with the ashes of the Pau Pereira tree. Renowned for its potent cleansing properties, clearing heaviness, releasing emotional tension, and resetting the nervous system.</p>
  </div>
  <div class="peptide-card">
    <h4>2. Murici Hapé</h4>
    <p>Made with ashes of the Murici tree. Deeply grounding, cleansing, and centering. Beautiful for clearing sluggish energies and restoring focus to the lower chakras.</p>
  </div>
  <div class="peptide-card">
    <h4>3. Caneleiro Hapé</h4>
    <p>A gentle, heart-opening medicine associated with compassion, emotional forgiveness, and melting protective armor around the heart center.</p>
  </div>
  <div class="peptide-card">
    <h4>4. Samaúma & Bobinsana</h4>
    <p>Blended with the Mother of Trees or Bobinsana flowers, opening subtle perception, dream work, spiritual insight, and gentle upliftment.</p>
  </div>
</div>

<h3>The Sacred Ritual of Reception</h3>
<p>When working with hapé, respect and presence are paramount. Take time before receiving to breathe, quiet your thoughts, and set an intention. Allow the breath of the pipe to enter not as a force, but as an offering that anchors you back into your center.</p>
'''
    },
    {
        'slug': 'getting-ready-for-your-kambo-ceremony-a-friendly-guide',
        'title': 'Getting Ready for Your Kambo Ceremony: A Friendly Guide',
        'meta_title': 'Preparing for Kambo: Your Friendly Step-by-Step Guide to a Transformative Ceremony',
        'desc': 'Discover the essential steps to prepare for your Kambo ceremony in this comprehensive guide. Learn about dietary adjustments, hydration, and setting intentions.',
        'image': '/assets/images/6.png',
        'category': 'Ceremony Prep',
        'date': 'Published in Sacred Origins Blog',
        'read_time': '5 min read',
        'author': 'Kaira Otero, LCSW',
        'author_bio': 'Co-founder of Sacred Origins NYC, Licensed Clinical Social Worker (LCSW), Reiki Level II practitioner, and certified Kambo practitioner.',
        'content': '''
<p class="lead">Welcome to Sacred Origins! If you’re considering a Kambo ceremony, you’re about to embark on a unique journey of healing and transformation. Kambo, the sacred medicine from the Amazonian giant monkey frog, has been cherished for centuries for its purifying and revitalizing effects. Here’s a cozy, friendly guide to help you prepare your mind, body, and spirit.</p>

<div class="article-img-block">
  <img src="/assets/images/6.png" alt="Preparation guide for your Kambo journey">
  <div class="article-img-caption">Preparing with care, intention, and gentle mindfulness</div>
</div>

<h3>1. Nourishing Your Body</h3>
<p><strong>Watch Your Diet:</strong></p>
<ul>
  <li><strong>A Few Days Ahead:</strong> Shift toward clean, whole foods. Emphasize fresh vegetables, fruit, wholesome grains, and light proteins. It’s an ideal time to minimize caffeine, alcohol, processed sugars, and heavy oils.</li>
  <li><strong>The Day Before:</strong> Eat light meals for breakfast and lunch. For dinner, enjoy a simple vegetable broth or herbal tea. This gently prepares your digestive system for the cleansing process.</li>
  <li><strong>Fast Before Ceremony:</strong> On the morning of your ceremony, come on a fasting stomach (no solid food for 8 to 10 hours prior).</li>
</ul>

<p><strong>Hydration Guidelines:</strong></p>
<p>Drink plenty of water in the days leading up to your session. However, <em>do not force-drink massive quantities of water on your own beforehand</em>—water intake during ceremony must always be guided step-by-step by your certified practitioner to maintain safe electrolyte balance.</p>

<h3>2. Preparing Your Mind & Heart</h3>
<p><strong>Set Clear Intentions:</strong> Spend quiet time journaling about what you are seeking to release and what qualities you wish to cultivate—whether that is mental clarity, physical vitality, emotional freedom, or renewed direction.</p>
<p><strong>Embrace Grounding:</strong> Practice gentle stretching, nature walks, or meditation in the days preceding the circle. Approaching the medicine from a calm, centered state allows you to surrender with trust.</p>

<h3>3. Communicating with Your Practitioner</h3>
<p>Honest communication is the cornerstone of safe ceremonial care. Always inform your practitioner of your full medical history, prescription medications, supplements, or past conditions. At Sacred Origins, every participant completes a thorough health intake to ensure absolute safety.</p>

<h3>4. Post-Ceremony Integration</h3>
<p>Plan a slow, restful schedule for the rest of the day following your session. Nourish yourself with warm soup, rest in cozy clothing, and give yourself space to absorb the energetic lightness and mental clarity that Kambo leaves in its wake.</p>
'''
    },
    {
        'slug': 'discovering-kambo-a-sacred-healing-tradition-for-modern-times',
        'title': 'Discovering Kambo: A Sacred Healing Tradition for Modern Times',
        'meta_title': 'Unlocking Healing with Kambo: A Journey Through Ancient Traditions and Modern Science',
        'desc': 'Discover the transformative power of Kambo, a sacred healing practice rooted in Amazonian indigenous traditions. Learn about its cultural significance and holistic benefits.',
        'image': '/assets/images/kambo_1.png',
        'category': 'Amazonian Medicine',
        'date': 'Published in Sacred Origins Blog',
        'read_time': '6 min read',
        'author': 'Kaira Otero, LCSW',
        'author_bio': 'Co-founder of Sacred Origins NYC, Licensed Clinical Social Worker (LCSW), Reiki Level II practitioner, and certified Kambo practitioner.',
        'content': '''
<p class="lead">At Sacred Origins, we honor the ancient healing traditions that have been passed down through generations. One of the most potent medicines we work with is Kambo—a sacred ritual and healing practice that originates from indigenous tribes of the Amazon basin. Used for centuries, Kambo is renowned for its deep cleansing properties and its ability to support physical, emotional, and spiritual renewal.</p>

<div class="article-img-block">
  <img src="/assets/images/kambo_1.png" alt="Sacred Kambo medicine on stick with traditional applicator">
  <div class="article-img-caption">Harvested sustainably and served with traditional reverence</div>
</div>

<h3>The Indigenous Roots of Kambo</h3>
<p>For tribes such as the Matsés and Katukina, Kambo is far more than medicine. It is considered a protective spiritual teacher. Historically, warriors and hunters received Kambo to dispel <em>panema</em> (a cloudy energetic state of bad luck or sluggishness), heighten sensory perception, sharpen stamina, and fortify immunity against jungle diseases.</p>

<p>The medicine is harvested without harming the frog, treating the amphibian with deep gratitude and prayer before releasing it back into its rainforest canopy.</p>

<h3>Bridging Ancient Wisdom & Modern Science</h3>
<p>In modern times, research has revealed why Kambo produces such profound physiological effects: the frog secretion is rich in bioactive peptides that cross the blood-brain barrier, stimulating cellular repair, immune response, and circulation.</p>

<p>For those living in urban environments like New York City, where chronic stress, screen overload, and emotional fatigue take a toll on the nervous system, Kambo acts as an elemental reset—clearing accumulated density and returning you to a grounded, vibrant baseline.</p>

<h3>A Sacred Space for Personal Transformation</h3>
<p>At Sacred Origins NYC, our ceremonies provide an intimate, safe, and heart-centered container. We combine traditional ritual elements—intention setting, sacred songs, palo santo, and reiki—with modern trauma-informed facilitation so that you feel fully held through every stage of your experience.</p>
'''
    }
]

def shell(title, body, active='', description='Sacred Origins NYC — Heart-centered Kambo ceremonies, Reiki healing, retreats, and ancestral botanical practices in New York City.'):
    links = ''.join(f'<a href="{href}" class="{"active" if active==label else ""}">{label}</a>' for label, href in nav)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#183126">
  <title>{escape(title)} | Sacred Origins NYC</title>
  <meta name="description" content="{escape(description, quote=True)}">
  <link rel="icon" href="/assets/images/sacred-origins-official-logo.png" type="image/png">
  <link rel="apple-touch-icon" href="/assets/images/sacred-origins-official-logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Manrope:wght@400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/style.css">
  <link rel="stylesheet" href="/assets/theme.css">
  <script defer src="/assets/site.js"></script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <div class="announcement">
    <span class="announcement-left">NYC · A PLACE TO RETURN TO</span>
    <span class="announcement-center">ROOTED IN COMMUNITY · GUIDED BY ANCESTRAL WISDOM</span>
    <span class="announcement-right">EST. IN CONNECTION <span aria-hidden="true">✳</span></span>
  </div>
  <header class="header">
    <div class="header-inner">
      <span class="header-loc">SACRED ORIGINS<br>NEW YORK CITY</span>
      <a class="brand" href="/" aria-label="Sacred Origins home">
        <img class="brand-logo" src="/assets/images/sacred-origins-official-logo.png" width="130" height="130" alt="Sacred Origins NYC">
      </a>
      <div class="header-actions">
        <a class="header-shop" href="/scheduling/">SCHEDULE CALL <span aria-hidden="true">↗</span></a>
        <button class="menu-toggle" aria-label="Open menu" aria-controls="nav" aria-expanded="false">
          <span></span><span></span>
        </button>
      </div>
    </div>
    <nav class="nav" id="nav" aria-label="Main navigation">
      {links}
      <a class="nav-cta-mobile" href="/scheduling/">Schedule a Call <span>↗</span></a>
    </nav>
  </header>
  <main id="main">
    {body}
  </main>
  <footer class="footer">
    <div class="footer-inner-wrap">
      <div class="footer-intro">
        <span class="eyebrow light">THE NEXT CHAPTER BEGINS HERE</span>
        <a href="/scheduling/">Begin your journey <span aria-hidden="true">↗</span></a>
      </div>
      <div class="footer-top">
        <div>
          <a class="footer-logo" href="/" aria-label="Sacred Origins home">
            <img src="/assets/images/sacred-origins-logo-light.png" width="160" height="160" alt="Sacred Origins NYC">
          </a>
          <p>A sacred sanctuary for healing, reflection, and ancestral reconnection.</p>
          <a href="mailto:sacredoriginsnyc@gmail.com" class="footer-mail">sacredoriginsnyc@gmail.com ↗</a>
        </div>
        <div>
          <h3>Explore</h3>
          <a href="/about/">About Us</a>
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
  </footer>
</body>
</html>'''

def write(path, content):
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')

def card(p):
    slug, name, cat, mood, _ = p
    return f'''<a class="product-card" href="/shop/{slug}/">
  <div class="product-image product-{slug}">
    <span class="image-stamp">SO / 0{products.index(p)+1}</span>
    <span class="product-arrow" aria-hidden="true">↗</span>
  </div>
  <div class="product-meta"><span>{cat}</span><span>Explore ↗</span></div>
  <h3>{name}</h3>
  <p>{mood}</p>
</a>'''

# ==============================================================================
# 1. HOME PAGE
# ==============================================================================
home_testimonials_html = ''.join(f'''
<div class="testimonial-card">
  <span class="testimonial-star">✺ ✺ ✺ ✺ ✺</span>
  <p class="testimonial-quote">“{escape(t['quote'])}”</p>
  <div class="testimonial-author">
    <strong>{escape(t['name'])}</strong>
    <span class="testimonial-badge">{escape(t['badge'])}</span>
  </div>
</div>
''' for t in testimonials_data[:6])

home_offerings_grid = ''.join(f'''
<div class="offering-card" style="background:#f5f2ea;border:1px solid #d5cfbe;overflow:hidden;padding:0;display:flex;flex-direction:column;">
  <div style="height:230px;background-image:url('{off['image']}');background-size:cover;background-position:center;position:relative;">
    <span style="position:absolute;bottom:15px;left:15px;background:rgba(20,43,34,.85);color:#ede6d6;font-size:9px;letter-spacing:.15em;text-transform:uppercase;padding:5px 10px;">SO / {i:02d}</span>
  </div>
  <div style="padding:28px 25px;display:flex;flex-direction:column;flex:1;">
    <span style="font-size:10px;letter-spacing:.15em;color:#9b7a48;text-transform:uppercase;margin-bottom:8px;">{off['tag'].split('·')[0].strip()}</span>
    <h3 style="font-size:24px;margin:0 0 12px;">{off['title']}</h3>
    <p style="color:#5f6a60;font-size:14px;line-height:1.7;margin-bottom:20px;flex:1;">{off['desc'][:165]}...</p>
    <a href="/offerings/" style="font:600 10px 'Manrope';text-transform:uppercase;letter-spacing:.14em;color:#183126;display:inline-flex;align-items:center;gap:6px;">Learn More <span>↗</span></a>
  </div>
</div>
''' for i, off in enumerate(offerings_data, 1))

home_blog_cards = ''.join(f'''
<a class="blog-card" href="/blog/{b['slug']}/">
  <div class="blog-thumb" style="background-image:url('{b['image']}');">
    <span class="blog-tag">{b['category']}</span>
  </div>
  <div class="blog-card-content">
    <div class="blog-meta"><span>{b['author']}</span><span>{b['read_time']}</span></div>
    <h3>{b['title']}</h3>
    <p>{b['desc']}</p>
    <span class="blog-readmore">Read Article <span>↗</span></span>
  </div>
</a>
''' for b in blog_posts[:3])

home_content = f'''
<section class="hero">
  <div class="hero-grain"></div>
  <div class="hero-content">
    <p class="eyebrow light">A SPACE FOR COMING BACK TO YOURSELF <span>— NYC</span></p>
    <h1>Where healing is a<br><em>collective journey.</em></h1>
    <p>Welcome to Sacred Origins. We offer heart-centered Kambo ceremonies, Reiki healing, retreats, and ancestral Earth medicine to empower our community and guide your personal transformation.</p>
    <div class="hero-buttons">
      <a class="button button-cream" href="/contact/">Contact Us <span>↗</span></a>
      <a class="text-link light-link" href="/shop/">Shop the Apothecary <span>↗</span></a>
    </div>
    <div class="hero-index">01 <span>/</span> 04 <i></i> DISCOVER THE STORY</div>
  </div>
  <div class="hero-visual">
    <div class="hero-picture" style="background-image:url('/assets/images/juli-kosolapova-pz-xfirjmte-unsplash.jpg');"></div>
    <div class="hero-visual-top">THE ART OF RETURNING <span>✺</span> SACRED ORIGINS</div>
    <div class="hero-visual-bottom">
      <span>EST. IN CONNECTION</span>
      <span>NEW YORK CITY</span>
    </div>
  </div>
  <div class="hero-vertical">INTENTION · COMMUNITY · ORIGIN · ANCESTRAL WISDOM</div>
</section>

<section class="ticker" aria-label="Our values">
  <div>GATHER WITH INTENTION <span>✺</span> RETURN TO ORIGIN <span>✺</span> HONOR ANCESTRAL WISDOM <span>✺</span> KAMBO & REIKI HEALING <span>✺</span> EMPOWERING COMMUNITY <span>✺</span></div>
</section>

<section class="intro section-wrap reveal">
  <div class="section-label"><span class="tiny-star">✺</span> 01 / THE ETHOS <span class="line"></span> NEW YORK CITY</div>
  <div class="intro-grid">
    <div>
      <span class="intro-overline">BEYOND THE EVERYDAY</span>
      <h2>A space to feel<br><em>seen and supported.</em></h2>
    </div>
    <div>
      <p>At Sacred Origins NYC, we are a collective deeply rooted in empowering BIPOC communities through sacred healing practices. We understand that healing is not just a personal journey but a collective one that reconnects us with the wisdom and resilience of our ancestors.</p>
      <p>Our mission is to provide a safe and transformative space where individuals can explore deep healing through a variety of modalities, including Kambo, Reiki, Earth Medicine Ceremonies, and Retreats.</p>
      <a class="underline-link" href="/about/">The story behind Sacred Origins <span>↗</span></a>
    </div>
  </div>
</section>

<section class="section-wrap" style="padding-top:20px;padding-bottom:80px;">
  <div class="section-heading">
    <div>
      <p class="eyebrow">02 / SACRED PATHWAYS</p>
      <h2>Our core<br><em>ceremonial offerings.</em></h2>
    </div>
    <a class="underline-link" href="/offerings/">View all offerings <span>↗</span></a>
  </div>
  <div class="offerings-grid">
    {home_offerings_grid}
  </div>
</section>

<section class="editorial">
  <div class="editorial-photo" style="background-image:url('/assets/images/green_minimalist_quote_of_nature_instagram_post.png');background-size:cover;background-position:center;">
    <div class="photo-caption">SO / ANCESTRAL CONNECTION <span>01—06</span></div>
  </div>
  <div class="editorial-copy">
    <span class="eyebrow">03 / IN THE SANCTUARY</span>
    <h2>Unlock the sacred<br><em>potential within.</em></h2>
    <p>In our safe and welcoming space, you will discover modalities designed to facilitate deep healing and personal growth. By engaging in these intentional practices, you will not only cultivate your own well-being but also contribute to the collective healing of our communities.</p>
    <a class="button button-dark" href="/scheduling/">Book an intake call <span>↗</span></a>
    <span class="editorial-numeral">✺</span>
  </div>
</section>

<section class="testimonials-section">
  <div class="testimonials-inner">
    <div class="testimonials-header">
      <div>
        <p class="eyebrow light">VOICES FROM THE CIRCLE</p>
        <h2>Words from our<br><em>community.</em></h2>
      </div>
      <a class="text-link light-link" href="/about/#testimonials">Read all reflections <span>↗</span></a>
    </div>
    <div class="testimonials-grid">
      {home_testimonials_html}
    </div>
  </div>
</section>

<section class="collection section-wrap">
  <div class="section-heading">
    <div>
      <p class="eyebrow">04 / THE APOTHECARY</p>
      <h2>Hand selected<br><em>ceremonial tools.</em></h2>
    </div>
    <a class="underline-link" href="/shop/">Enter the Apothecary <span>↗</span></a>
  </div>
  <div class="product-grid featured-grid">
    {''.join(card(p) for p in products[:3])}
  </div>
</section>

<section style="background:#ebe6d8;">
  <div class="section-wrap" style="padding-top:70px;padding-bottom:70px;">
    <div class="section-heading">
      <div>
        <p class="eyebrow">05 / KNOWLEDGE & MEDICINE</p>
        <h2>From the <em>journal.</em></h2>
      </div>
      <a class="underline-link" href="/blog/">Read all articles <span>↗</span></a>
    </div>
    <div class="blog-grid">
      {home_blog_cards}
    </div>
  </div>
</section>

<section class="manifesto">
  <div class="manifesto-top">
    <span>THE SACRED IS NOT FAR AWAY</span>
    <span>✺</span>
    <span>IT BEGINS WITH ATTENTION</span>
  </div>
  <p>Come as you are.<br><em>Leave more connected.</em></p>
  <a href="/scheduling/">SCHEDULE A 15-MINUTE CALL ↗</a>
</section>

<section class="contact-banner">
  <div class="contact-banner-inner">
    <div>
      <p class="eyebrow light">A CONVERSATION IS A BEGINNING</p>
      <h2>Find your way<br><em>back to your center.</em></h2>
    </div>
    <a class="button button-cream" href="/contact/">Get in touch <span>↗</span></a>
  </div>
</section>
'''

write('index.html', shell('Home: Kambo & Reiki Healing NYC', home_content, 'Home', 'Welcome to Sacred Origins NYC — heart-centered Kambo ceremonies, Reiki healing, retreats, and ancestral medicine in New York City.'))
write('home/index.html', shell('Home: Kambo & Reiki Healing NYC', home_content, 'Home'))

# ==============================================================================
# 2. ABOUT US PAGE
# ==============================================================================
about_faqs_html = ''.join(f'''
<details class="faq-item">
  <summary class="faq-summary">
    <span>{escape(q)}</span>
    <i class="faq-icon">+</i>
  </summary>
  <div class="faq-body">
    <p>{a}</p>
  </div>
</details>
''' for q, a in faqs_data)

all_testimonials_html = ''.join(f'''
<div class="testimonial-card">
  <span class="testimonial-star">✺ ✺ ✺ ✺ ✺</span>
  <p class="testimonial-quote">“{escape(t['quote'])}”</p>
  <div class="testimonial-author">
    <strong>{escape(t['name'])}</strong>
    <span class="testimonial-badge">{escape(t['badge'])}</span>
  </div>
</div>
''' for t in testimonials_data)

about_content = f'''
<section class="page-hero">
  <p class="eyebrow">THE PEOPLE & PURPOSE</p>
  <h1>Rooted in connection.<br><em>Open to possibility.</em></h1>
  <p>Our story begins with the belief that healing is a collective journey reconnecting us with ancestral wisdom.</p>
</section>

<section class="about-content section-wrap">
  <div class="about-image" style="background-image:url('/assets/images/111.jpg');background-size:cover;background-position:center;"></div>
  <div>
    <p class="eyebrow">OUR VISION & STORY</p>
    <h2>We’re Bryant & Kaira,<br><em>the heart of Sacred Origins.</em></h2>
    <p>Sacred Origins NYC is a vision that has been unfolding for years. It was born from a simple yet powerful dream: to create a sanctuary where our community can heal, reconnect, and dive deeper into their own ancestral wisdom—just as we’ve been doing on our own healing journeys.</p>
    <p>Bryant, from the Dominican Republic and raised in Lenapehoking (NYC), and Kaira, of Filipino and Puerto Rican descent from Lenapehoking, have spent many years working with plant medicine and carrying forward our ancestral traditions. We’ve witnessed the incredible healing that comes from remembering who we are, honoring our roots, and connecting with our community in deeper ways.</p>
    <p>Our offerings are all about supporting your journey back to yourself: from Plant Medicine Journeys, Kambo, Hapé and Sananga ceremonies, Reiki, to Psychedelic Preparation/Integration, Group and 1:1 sessions, and transformative retreats.</p>
    <a class="underline-link" href="/scheduling/">Schedule a consultation with us <span>↗</span></a>
  </div>
</section>

<section class="founders-section">
  <div class="section-heading">
    <div>
      <p class="eyebrow">THE FACILITATORS</p>
      <h2>Meet the <em>co-founders.</em></h2>
    </div>
  </div>
  <div class="founders-grid">
    <div class="founder-card">
      <div class="founder-img" style="background-image:url('/assets/images/for_website_2.jpg');"></div>
      <div class="founder-content">
        <span class="founder-tag">CO-FOUNDER & PRACTITIONER</span>
        <h3>Meet Kai (Kaira Otero)</h3>
        <span class="founder-role">LCSW Psychotherapist · Reiki Level II · Certified Kambo Practitioner</span>
        <p>Kai was shaped by her early years in a working-class home led by her single immigrant mother—a place of raw intensity and enduring hardship. Amid the echoes of generational pain and a turbulent upbringing, she wrestled with deep-seated rage and disconnection, unaware that her inner turmoil was born from ancestral wounds.</p>
        <p>This profound struggle sparked Kai’s transformative healing journey. Over seven years as a psychotherapist have deepened her understanding of how early life, generational, and ancestral traumas forge our identities. Embracing her calling, she became a licensed clinical social worker (LCSW), a Reiki Level II practitioner, and a Kambo practitioner, dedicating herself to healing the unseen scars of the soul.</p>
        <p>Today, Kai offers a sanctuary of compassion and transformation, especially for adult children of immigrants and BIPOC women. Through intimate one-on-one sessions and nurturing group work, she guides others to reconnect with their inner power, reclaim their wholeness, and transcend the legacies of pain.</p>
      </div>
    </div>
    <div class="founder-card">
      <div class="founder-img" style="background-image:url('/assets/images/333.jpg');"></div>
      <div class="founder-content">
        <span class="founder-tag">CO-FOUNDER & TEACHER</span>
        <h3>Meet Bryant</h3>
        <span class="founder-role">Reiki Master Teacher (10+ Years) · Kambo Practitioner · Earth Medicine Facilitator</span>
        <p>Bryant’s journey to transformation was deeply personal and forged through profound hardship. Growing up in a home where rigid religious expectations clashed with his inner truth, he endured a childhood marked by religious trauma. In his early twenties, Bryant found himself entangled in the struggles of deep addiction—a time when he felt lost, isolated, and overwhelmed by pain.</p>
        <p>During these dark moments, he reached a turning point: the discovery of plant medicine. This powerful, natural healing opened a door to the ancient wisdom of his ancestors, offering him solace and a path out of despair. The teachings of his heritage, combined with the healing energies of plant medicine, gave him grounding and purpose.</p>
        <p>Today, with over a decade of experience as a Reiki Master Teacher, along with his roles as a Kambo practitioner and Earth Medicine facilitator, Bryant brings an authenticity and empathy born from lived experience. His approach is straightforward and compassionate, particularly in his work with men—especially BIPOC individuals and martial arts fighters—fostering genuine connection and renewal.</p>
      </div>
    </div>
  </div>
</section>

<section class="values">
  <div class="section-wrap">
    <p class="eyebrow light">WHAT GUIDES US</p>
    <div class="values-grid">
      <div>
        <span>01</span>
        <h3>Community</h3>
        <p>We gather in a spirit of belonging, safety, and mutual support, honoring the collective strength of BIPOC lineages.</p>
      </div>
      <div>
        <span>02</span>
        <h3>Intention</h3>
        <p>We approach every ceremony and energy session with deep presence, ceremonial care, and sacred purpose.</p>
      </div>
      <div>
        <span>03</span>
        <h3>Respect</h3>
        <p>We honor the ancestral roots, traditions, and ecological stewards behind each medicine and practice we share.</p>
      </div>
    </div>
  </div>
</section>

<section class="testimonials-section" id="testimonials">
  <div class="testimonials-inner">
    <div class="testimonials-header">
      <div>
        <p class="eyebrow light">AUTHENTIC EXPERIENCES</p>
        <h2>Transformations from<br><em>our community.</em></h2>
      </div>
      <p style="color:#b5c4b8;max-width:400px;font-size:14px;">Every journey is unique. Read how our circles, Kambo sessions, and retreats have supported our participants.</p>
    </div>
    <div class="testimonials-grid">
      {all_testimonials_html}
    </div>
  </div>
</section>

<section class="faq-section">
  <div class="faq-intro">
    <p class="eyebrow">COMMON INQUIRIES</p>
    <h2>Frequently asked<br><em>questions.</em></h2>
    <p style="color:#606c61;max-width:550px;margin-top:10px;">Everything you need to know about our ceremonies, preparation, and approach to healing.</p>
  </div>
  <div class="faq-list">
    {about_faqs_html}
  </div>
</section>

<section class="contact-banner">
  <div>
    <p class="eyebrow light">WE ARE HERE TO WALK WITH YOU</p>
    <h2>Ready to begin your<br><em>journey of return?</em></h2>
  </div>
  <a class="button button-cream" href="/scheduling/">Schedule a call <span>↗</span></a>
</section>
'''

write('about/index.html', shell('About Us', about_content, 'About Us', 'Learn about Sacred Origins NYC, founders Bryant and Kai, our ancestral mission, and our holistic healing approach in NYC.'))
write('about-us/index.html', shell('About Us', about_content, 'About Us'))

# ==============================================================================
# 3. OFFERINGS PAGE
# ==============================================================================
offerings_page_html = ''.join(f'''
<div class="offering-detail-card">
  <div class="offering-detail-img" style="background-image:url('{off['image']}');"></div>
  <div class="offering-detail-body">
    <span style="font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#9a794a;margin-bottom:8px;font-weight:600;">{off['tag']}</span>
    <h3>{off['title']}</h3>
    <p>{off['desc']}</p>
    <div class="offering-detail-actions" style="display:flex;gap:20px;align-items:center;flex-wrap:wrap;margin-top:auto;">
      <a class="button button-dark" href="/scheduling/?offering={quote(off['title'])}">Schedule a Call <span>↗</span></a>
      <a class="underline-link" href="/contact/?subject={quote(off['title'])}">Inquire via message <span>↗</span></a>
    </div>
  </div>
</div>
''' for off in offerings_data)

offerings_page_content = f'''
<section class="page-hero">
  <p class="eyebrow">GATHER · REFLECT · TRANSFORM</p>
  <h1>Our sacred <em>offerings.</em></h1>
  <p>Heart-centered Kambo ceremonies, Reiki healing, retreats, Hapé & Sananga circles, and integration support in New York City.</p>
</section>

<section class="section-wrap" style="padding-top:70px;">
  <div class="section-heading">
    <div>
      <p class="eyebrow">MODALITIES OF HEALING</p>
      <h2>Spaces crafted for<br><em>deep return.</em></h2>
    </div>
    <p style="max-width:380px;color:#5f6b60;">Questions about which modality aligns with where you are right now? We invite you to connect with us for guidance.</p>
  </div>
  <div style="margin-top:50px;">
    {offerings_page_html}
  </div>
</section>

<section class="contact-banner">
  <div>
    <p class="eyebrow light">A PERSONAL CONNECTION</p>
    <h2>Curious about<br><em>working together?</em></h2>
  </div>
  <a class="button button-cream" href="/scheduling/">Book an intake call <span>↗</span></a>
</section>
'''

write('offerings/index.html', shell('Offerings', offerings_page_content, 'Offerings', 'Explore Kambo ceremonies, Reiki healing, transformative retreats, Hapé circles, and integration support at Sacred Origins NYC.'))

# ==============================================================================
# 4. SCHEDULING PAGE
# ==============================================================================
scheduling_content = f'''
<section class="page-hero scheduling-hero">
  <p class="eyebrow">INTAKE & CONSULTATION</p>
  <h1>Begin your <em>healing journey.</em></h1>
  <p>Schedule a 15-minute consultation with Bryant or Kai to discuss your intentions, answer questions, and prepare for ceremony.</p>
</section>

<section class="section-wrap" style="padding-top:70px;padding-bottom:90px;">
  <div class="scheduling-grid">
    <div>
      <p class="eyebrow">DIRECT ONLINE BOOKING</p>
      <h2 style="font-size:clamp(2.5rem,4vw,4rem);margin:10px 0 25px;">Select a time that<br><em>works for you.</em></h2>
      <p style="color:#576059;line-height:1.8;">Our complimentary consultation is a safe, no-pressure space where we get to know you, understand any health considerations, and help determine whether Kambo, Reiki, or our retreats are the right fit for your path.</p>
      
      <!-- Calendly inline widget -->
      <div class="calendly-box">
        <div class="calendly-inline-widget" data-url="https://calendly.com/sacredoriginsnyc/15" style="width:100%;height:700px;"></div>
        <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
      </div>
      
      <div class="calendly-fallback">
        <p>Having trouble loading the calendar?</p>
        <a class="button button-dark" href="https://calendly.com/sacredoriginsnyc/15" target="_blank" rel="noopener noreferrer">Open Calendly in New Tab <span>↗</span></a>
      </div>
    </div>
    
    <div>
      <div style="background:#f5f2ea;border:1px solid #d5cfbe;overflow:hidden;margin-bottom:30px;">
        <img src="/assets/images/unsplash-image-rrnhdu2jokq.jpg" style="width:100%;height:320px;object-fit:cover;" alt="Sacred space reflection">
        <div style="padding:30px 25px;">
          <h3 style="font-size:24px;margin-bottom:12px;">What to Expect on the Call</h3>
          <ul style="color:#556057;line-height:1.8;padding-left:20px;font-size:14px;margin-bottom:0;">
            <li>A welcoming conversation with Bryant or Kaira.</li>
            <li>Discussion of your personal intentions, background, and goals.</li>
            <li>Confidential medical review and contraindication check for Kambo.</li>
            <li>Guidance on ceremony location, preparation diet, and dates.</li>
          </ul>
        </div>
      </div>
      
      <div style="background:#ebe6d8;border:1px solid #d5cfbe;padding:30px 25px;">
        <h3 style="font-size:20px;margin-bottom:10px;">Prefer Email or Custom Inquiries?</h3>
        <p style="color:#5f6b60;font-size:14px;line-height:1.7;margin-bottom:20px;">If you have a private group request, house limpia inquiry, or would prefer to connect via writing first, feel free to reach out directly.</p>
        <a class="underline-link" href="mailto:sacredoriginsnyc@gmail.com">sacredoriginsnyc@gmail.com <span>↗</span></a>
      </div>
    </div>
  </div>
</section>
'''

write('scheduling/index.html', shell('Scheduling', scheduling_content, 'Scheduling', 'Schedule your healing session, Kambo intake call, or Reiki consultation with Sacred Origins NYC.'))

# ==============================================================================
# 5. BLOG INDEX PAGE
# ==============================================================================
blog_grid_html = ''.join(f'''
<a class="blog-card" href="/blog/{b['slug']}/">
  <div class="blog-thumb" style="background-image:url('{b['image']}');">
    <span class="blog-tag">{b['category']}</span>
  </div>
  <div class="blog-card-content">
    <div class="blog-meta">
      <span>{b['author']}</span>
      <span>{b['read_time']}</span>
    </div>
    <h3>{b['title']}</h3>
    <p>{b['desc']}</p>
    <span class="blog-readmore">Read Article <span>↗</span></span>
  </div>
</a>
''' for b in blog_posts)

blog_index_content = f'''
<section class="page-hero blog-hero">
  <p class="eyebrow">SACRED WRITINGS & SCIENCE</p>
  <h1>The Sacred Origins <em>Journal.</em></h1>
  <p>Exploring the cultural roots, pharmacology, and ceremonial wisdom of Kambo, Sananga, Hapé, and holistic healing.</p>
</section>

<section class="section-wrap" style="padding-top:70px;">
  <div class="section-heading">
    <div>
      <p class="eyebrow">ARTICLES & GUIDES</p>
      <h2>Deep dives & <em>medicine notes.</em></h2>
    </div>
    <p style="max-width:360px;color:#606b60;">Written by our practitioners to inform, ground, and support your journey with respect and safety.</p>
  </div>
  <div class="blog-grid">
    {blog_grid_html}
  </div>
</section>

<section class="contact-banner">
  <div>
    <p class="eyebrow light">CONTINUE THE CONVERSATION</p>
    <h2>Have a question about<br><em>one of the medicines?</em></h2>
  </div>
  <a class="button button-cream" href="/contact/">Send us a message <span>↗</span></a>
</section>
'''

write('blog/index.html', shell('Journal & Blog', blog_index_content, 'Blog', 'Read in-depth articles on Kambo pharmacology, Sananga benefits, Hapé ceremonies, and holistic medicine from Sacred Origins NYC.'))

# ==============================================================================
# 6. INDIVIDUAL BLOG ARTICLES
# ==============================================================================
for post in blog_posts:
    slug = post['slug']
    related_posts = [p for p in blog_posts if p['slug'] != slug][:2]
    related_html = ''.join(f'''
    <a class="blog-card" href="/blog/{rp['slug']}/">
      <div class="blog-thumb" style="background-image:url('{rp['image']}');height:200px;">
        <span class="blog-tag">{rp['category']}</span>
      </div>
      <div class="blog-card-content">
        <div class="blog-meta"><span>{rp['author']}</span><span>{rp['read_time']}</span></div>
        <h3 style="font-size:20px;">{rp['title']}</h3>
        <span class="blog-readmore">Read Article <span>↗</span></span>
      </div>
    </a>
    ''' for rp in related_posts)
    
    article_html = f'''
    <article class="article-wrap">
      <div class="article-header">
        <a class="back-link" href="/blog/">← Back to all articles</a>
        <p class="eyebrow">{post['category']} · {post['read_time']}</p>
        <h1>{post['title']}</h1>
        <div class="article-byline">
          <img src="/assets/images/4a724d8e410b44279d628f7316a44301.jpeg" alt="{post['author']}">
          <div>
            <strong>By {post['author']}</strong><br>
            <span style="font-size:11px;color:#857866;">Co-founder, Sacred Origins NYC</span>
          </div>
        </div>
      </div>
      
      <div class="article-hero-banner" style="background-image:url('{post['image']}');"></div>
      
      <div class="article-content">
        {post['content']}
      </div>
      
      <div class="article-author-bio">
        <img src="/assets/images/4a724d8e410b44279d628f7316a44301.jpeg" alt="{post['author']}">
        <div>
          <h4>Written by {post['author']}</h4>
          <p>{post['author_bio']}</p>
          <a href="/about/">Learn more about our team ↗</a>
        </div>
      </div>
      
      <div style="margin-top:80px;border-top:1px solid #d5cfbe;padding-top:40px;">
        <h3 style="font-size:28px;margin-bottom:30px;">Continue Reading</h3>
        <div class="related-articles-grid">
          {related_html}
        </div>
      </div>
    </article>
    '''
    
    write(f'blog/{slug}/index.html', shell(post['title'], article_html, 'Blog', post['desc']))
    
    # If there's an alternate slug (e.g. for hape squarespace slug compatibility)
    if 'alt_slug' in post:
        write(f'blog/{post["alt_slug"]}/index.html', shell(post['title'], article_html, 'Blog', post['desc']))

# ==============================================================================
# 7. SHOP & PRODUCT DETAIL PAGES
# ==============================================================================
shop_content = f'''
<section class="page-hero shop-hero">
  <p class="eyebrow">THE SACRED ORIGINS APOTHECARY</p>
  <h1>Gather your <em>ritual.</em></h1>
  <p>Hapé blends and traditional applicators, selected for intentional practice and ancestral connection.</p>
</section>

<section class="shop-section section-wrap">
  <div class="shop-top">
    <div>
      <p class="eyebrow">EXPLORE THE COLLECTION</p>
      <h2>Objects with <em>intention.</em></h2>
    </div>
    <div class="filters" role="group" aria-label="Filter products">
      <button class="filter active" data-filter="all" aria-pressed="true">All <span>05</span></button>
      <button class="filter" data-filter="Hapé" aria-pressed="false">Hapé <span>03</span></button>
      <button class="filter" data-filter="Applicator" aria-pressed="false">Applicators <span>02</span></button>
    </div>
  </div>
  <div class="product-grid full-grid">
    {''.join(f'<div data-category="{p[2]}">{card(p)}</div>' for p in products)}
  </div>
  <p class="shop-note">These are the authentic botanical offerings shared within our community. Images are editorial representations; final product batches, sizes, and availability can be confirmed directly with our team.</p>
</section>
'''

write('shop/index.html', shell('Shop', shop_content, 'Shop', 'Explore Sacred Origins Hapé blends, Kuripe and Tepi applicators.'))

for p in products:
    slug, name, cat, mood, desc = p
    detail = f'''
<section class="detail section-wrap">
  <div class="detail-image product-{slug}" role="img" aria-label="Representation of {escape(name)}"></div>
  <div class="detail-copy">
    <a class="back-link" href="/shop/">← Back to the collection</a>
    <p class="eyebrow">THE APOTHECARY / {escape(cat.upper())}</p>
    <h1>{escape(name)}</h1>
    <p class="detail-mood">{escape(mood)}</p>
    <div class="detail-divider"></div>
    <p>{escape(desc)}</p>
    <div class="availability">
      <span>Availability & inquiries</span>
      <strong>Inquire for current batch & pricing</strong>
    </div>
    <a class="button button-dark" href="/contact/?product={slug}">Inquire about {escape(name)} <span>↗</span></a>
    <p class="detail-footnote">Botanical products are offered with reverence for educational, ceremonial, and traditional practice.</p>
  </div>
</section>

<section class="related section-wrap">
  <div class="section-heading">
    <h2>Continue <em>exploring.</em></h2>
    <a class="underline-link" href="/shop/">Shop all <span>↗</span></a>
  </div>
  <div class="product-grid">
    {''.join(card(q) for q in [q for q in products if q != p][:3])}
  </div>
</section>
'''
    write(f'shop/{slug}/index.html', shell(name, detail, 'Shop', desc[:155]))

# ==============================================================================
# 8. CONTACT PAGE
# ==============================================================================
contact_content = f'''
<section class="page-hero">
  <p class="eyebrow">WE’D LOVE TO HEAR FROM YOU</p>
  <h1>Let’s <em>connect.</em></h1>
  <p>Questions about an offering, a ceremony, scheduling, or simply where to begin? Send a note.</p>
</section>

<section class="contact-section section-wrap">
  <div>
    <p class="eyebrow">SACRED ORIGINS NYC</p>
    <h2>Start a<br><em>conversation.</em></h2>
    <p>We’re Bryant and Kai. We’ll be in touch as soon as we can to support you on your path.</p>
    <a class="contact-email" href="mailto:sacredoriginsnyc@gmail.com">sacredoriginsnyc@gmail.com ↗</a>
    <div style="margin:25px 0;">
      <p style="font-size:14px;color:#606b60;margin-bottom:8px;"><strong>Location:</strong> New York City · Lenapehoking</p>
      <p style="font-size:14px;color:#606b60;"><strong>Intake Booking:</strong> <a href="/scheduling/" style="color:#bfa677;text-decoration:underline;">Schedule a 15-min call</a></p>
    </div>
    <div class="contact-art" style="background-image:url('/assets/images/_dsc7710.jpg');background-size:cover;background-position:center;height:340px;" role="img" aria-label="Sacred Origins ceremony space"></div>
  </div>
  <form id="contact-form" class="contact-form">
    <label for="name">Your name *</label>
    <input id="name" name="name" autocomplete="name" required placeholder="Full name">
    <label for="email">Email address *</label>
    <input id="email" name="email" type="email" autocomplete="email" required placeholder="you@example.com">
    <label for="subject">What is this about?</label>
    <select id="subject" name="subject">
      <option>General inquiry</option>
      <option>Kambo Ceremony</option>
      <option>Reiki Healing</option>
      <option>Retreats & Group Journeys</option>
      <option>Hapé & Sananga Circles</option>
      <option>Psychedelic Integration</option>
      <option>House Cleansings / Limpias</option>
      <option>Apothecary / Product Inquiry</option>
      <option>Something else</option>
    </select>
    <label for="message">Your message *</label>
    <textarea id="message" name="message" rows="6" required placeholder="Tell us what is on your mind, your intentions, or any questions..."></textarea>
    <button class="button button-dark" type="submit">Compose email <span>↗</span></button>
    <p class="form-note">Submitting will open your email client addressed to sacredoriginsnyc@gmail.com with your message pre-filled. You can also email us directly above.</p>
  </form>
</section>
'''

write('contact/index.html', shell('Contact Us', contact_content, 'Contact', 'Get in touch with Sacred Origins NYC for Kambo ceremonies, Reiki healing, retreats, and integration support.'))

# ==============================================================================
# 9. META & STATICS
# ==============================================================================
write('assets/favicon.svg', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#183126"/><circle cx="32" cy="32" r="13" fill="none" stroke="#d6b678" stroke-width="2"/><path d="M32 8v11M32 45v11M8 32h11M45 32h11M15 15l8 8m18 18 8 8m0-34-8 8M23 41l-8 8" stroke="#d6b678" stroke-width="2"/></svg>')
write('robots.txt', 'User-agent: *\nAllow: /\n')

all_pages = list(root.rglob('*.html'))
print(f"Successfully generated {len(all_pages)} HTML pages across the entire site!")
for p in sorted(all_pages):
    print(f" - {p.relative_to(root)}")
