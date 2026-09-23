const menu=document.querySelector('.menu-toggle');const nav=document.querySelector('.nav');if(menu&&nav){menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close menu':'Open menu')});nav.addEventListener('click',e=>{if(e.target.closest('a')){nav.classList.remove('open');menu.setAttribute('aria-expanded','false')}})}
const filters=document.querySelectorAll('.filter');filters.forEach(button=>button.addEventListener('click',()=>{filters.forEach(b=>{b.classList.remove('active');b.setAttribute('aria-pressed','false')});button.classList.add('active');button.setAttribute('aria-pressed','true');document.querySelectorAll('[data-category]').forEach(item=>{item.hidden=button.dataset.filter!=='all'&&item.dataset.category!==button.dataset.filter})}));
const form=document.querySelector('#contact-form');if(form){const params=new URLSearchParams(location.search);const product=params.get('product');const subject=params.get('subject');if(product){const name=product.replace(/-/g,' ').replace(/\b\w/g,m=>m.toUpperCase());form.subject.value='Product inquiry';form.message.value=`Hello, I would like to ask about ${name}.\n\n`;}else if(subject){form.subject.value='Offerings';form.message.value=`Hello, I would like to ask about ${subject}.\n\n`;}form.addEventListener('submit',event=>{event.preventDefault();if(!form.reportValidity())return;const data=new FormData(form);const body=`Name: ${data.get('name')}\nEmail: ${data.get('email')}\nTopic: ${data.get('subject')}\n\n${data.get('message')}`;location.href=`mailto:sacredoriginsnyc@gmail.com?subject=${encodeURIComponent('Sacred Origins — '+data.get('subject'))}&body=${encodeURIComponent(body)}`})}

// Section-aware entrances: image masks, alternating text directions and gentle card staggers.
if('IntersectionObserver' in window&&!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
  const candidates=[];
  document.querySelectorAll('main > section, footer').forEach((section,sectionIndex)=>{
    const items=section.querySelectorAll('h1,h2,h3,p,.button,.underline-link,.hero-visual,.editorial-photo,.about-image,.contact-art,.detail-image,.product-card,.offering-card,.offering-list a,.values-grid>div,.contact-form,.footer-intro,.footer-wordmark');
    let sequence=0;
    items.forEach(el=>{
      if(el.closest('.product-card,.offering-card,.contact-form,.values-grid>div,.offering-list a')!==el&&el.closest('.product-card,.offering-card,.contact-form,.values-grid>div,.offering-list a'))return;
      if(el.closest('.hero-visual,.editorial-photo')&&el.closest('.hero-visual,.editorial-photo')!==el)return;
      const isImage=el.matches('.hero-visual,.editorial-photo,.about-image,.contact-art,.detail-image,.product-card');
      el.classList.add('motion-target',isImage?'motion-image':((sectionIndex+sequence)%2?'motion-left':'motion-right'));
      el.style.setProperty('--entrance-delay',`${Math.min(sequence%5,4)*75}ms`);
      candidates.push(el);sequence++;
    });
  });
  document.documentElement.classList.add('motion-ready');
  const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('in-view');observer.unobserve(entry.target)}})},{rootMargin:'0px 0px -5% 0px',threshold:.08});
  candidates.forEach(el=>observer.observe(el));
  setTimeout(()=>{document.querySelectorAll('.motion-target:not(.in-view)').forEach(el=>el.classList.add('in-view'))},1000);
}
