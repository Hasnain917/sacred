const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');
if (menu && nav) {
  menu.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    menu.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });

  nav.addEventListener('click', e => {
    if (e.target.closest('a')) {
      nav.classList.remove('open');
      menu.setAttribute('aria-expanded', 'false');
      menu.setAttribute('aria-label', 'Open menu');
    }
  });

  document.addEventListener('click', e => {
    if (!nav.contains(e.target) && !menu.contains(e.target) && nav.classList.contains('open')) {
      nav.classList.remove('open');
      menu.setAttribute('aria-expanded', 'false');
      menu.setAttribute('aria-label', 'Open menu');
    }
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && nav.classList.contains('open')) {
      nav.classList.remove('open');
      menu.setAttribute('aria-expanded', 'false');
      menu.setAttribute('aria-label', 'Open menu');
      menu.focus();
    }
  });
}

const filters = document.querySelectorAll('.filter');
filters.forEach(button => button.addEventListener('click', () => {
  filters.forEach(b => {
    b.classList.remove('active');
    b.setAttribute('aria-pressed', 'false');
  });
  button.classList.add('active');
  button.setAttribute('aria-pressed', 'true');
  document.querySelectorAll('[data-category]').forEach(item => {
    item.hidden = button.dataset.filter !== 'all' && item.dataset.category !== button.dataset.filter;
  });
}));

const form = document.querySelector('#contact-form');
if (form) {
  const params = new URLSearchParams(location.search);
  const product = params.get('product');
  const subject = params.get('subject');
  if (product) {
    const name = product.replace(/-/g, ' ').replace(/\b\w/g, m => m.toUpperCase());
    form.subject.value = 'Apothecary / Product Inquiry';
    form.message.value = `Hello, I would like to ask about ${name}.\n\n`;
  } else if (subject) {
    const options = Array.from(form.subject.options).map(o => o.value);
    if (options.includes(subject)) {
      form.subject.value = subject;
    } else {
      form.subject.value = 'General inquiry';
    }
    form.message.value = `Hello, I would like to ask about ${subject}.\n\n`;
  }
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const data = new FormData(form);
    const body = `Name: ${data.get('name')}\nEmail: ${data.get('email')}\nTopic: ${data.get('subject')}\n\n${data.get('message')}`;
    location.href = `mailto:sacredoriginsnyc@gmail.com?subject=${encodeURIComponent('Sacred Origins — ' + data.get('subject'))}&body=${encodeURIComponent(body)}`;
  });
}

// Section-aware entrances (Compatible with standard HTML and WordPress Elementor)
if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const candidates = [];
  const containerSelector = '.elementor-section, .e-con, section, article, .article-wrap, main > section, footer, .site-main, .entry-content';
  const sections = document.querySelectorAll(containerSelector);

  sections.forEach((section, sectionIndex) => {
    const itemSelector = 'h1,h2,h3,p,.button,.underline-link,.hero-visual,.editorial-photo,.about-image,.contact-art,.detail-image,.product-card,.offering-card,.offering-list a,.values-grid>div,.contact-form,.footer-intro,.footer-wordmark,.testimonial-card,.founder-card,.blog-card,.elementor-widget-heading,.elementor-widget-text-editor,.elementor-widget-button,.elementor-widget-image';
    const items = section.querySelectorAll(itemSelector);
    let sequence = 0;

    items.forEach(el => {
      if (el.closest('.product-card,.offering-card,.contact-form,.values-grid>div,.offering-list a,.testimonial-card,.founder-card,.blog-card') !== el && el.closest('.product-card,.offering-card,.contact-form,.values-grid>div,.offering-list a,.testimonial-card,.founder-card,.blog-card')) return;
      if (el.closest('.hero-visual,.editorial-photo') && el.closest('.hero-visual,.editorial-photo') !== el) return;
      
      const isImage = el.matches('.hero-visual,.editorial-photo,.about-image,.contact-art,.detail-image,.product-card,.testimonial-card,.founder-card,.blog-card,.elementor-widget-image');
      el.classList.add('motion-target', isImage ? 'motion-image' : ((sectionIndex + sequence) % 2 ? 'motion-left' : 'motion-right'));
      el.style.setProperty('--entrance-delay', `${Math.min(sequence % 5, 4) * 75}ms`);
      candidates.push(el);
      sequence++;
    });
  });

  document.documentElement.classList.add('motion-ready');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -5% 0px', threshold: .08 });

  candidates.forEach(el => observer.observe(el));
  setTimeout(() => {
    document.querySelectorAll('.motion-target:not(.in-view)').forEach(el => el.classList.add('in-view'));
  }, 1000);
}
