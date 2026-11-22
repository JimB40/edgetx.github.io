(()=>{
 const root=document.getElementById('etx-home')||document.body;
 const button=document.querySelector('button.theme-toggle');
 function apply(theme){root.style.colorScheme=theme;document.documentElement.style.colorScheme=theme;document.documentElement.dataset.etxTheme=theme;document.body.setAttribute('data-md-color-scheme',theme==='dark'?'slate':'default');if(button){button.setAttribute('aria-label',theme==='light'?'Switch to dark theme':'Switch to light theme');button.setAttribute('aria-pressed',String(theme==='light'));button.innerHTML='<i data-lucide="'+(theme==='light'?'moon':'sun')+'" aria-hidden="true"></i>'}if(window.lucide)lucide.createIcons();}
 apply(window.etxReviewTheme||'light');
 if(button)button.addEventListener('click',()=>{const next=document.documentElement.dataset.etxTheme==='dark'?'light':'dark';apply(next);try{localStorage.setItem('edgetx-review-theme',next)}catch{}});
 const menu=document.querySelector('.menu');if(menu)menu.addEventListener('click',()=>{const expanded=menu.getAttribute('aria-expanded')==='true';menu.setAttribute('aria-expanded',String(!expanded));document.getElementById('etx-nav').classList.toggle('open',!expanded)});
 const dismiss=document.querySelector('.noticeclose');if(dismiss)dismiss.addEventListener('click',()=>document.querySelector('.notice').hidden=true);
 const search=document.querySelector('.etx-search-button');if(search)search.addEventListener('keydown',event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();search.click()}});
})();
