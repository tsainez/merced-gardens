var body = document.querySelector('body')
var menuTrigger = document.querySelector('#toggle-main-menu-mobile');
var menuContainer = document.querySelector('#main-menu-mobile');

function handleEscape(event) {
  if (event.key === 'Escape') {
    menuTrigger.click();
    menuTrigger.focus();
  }
}

menuTrigger.onclick = function() {
    menuContainer.classList.toggle('open');
    menuTrigger.classList.toggle('is-active');
    body.classList.toggle('lock-scroll');

    // Toggle aria-expanded
    var isExpanded = menuTrigger.getAttribute('aria-expanded') === 'true';
    menuTrigger.setAttribute('aria-expanded', !isExpanded);

    if (!isExpanded) {
        // Menu was closed, now it's open
        document.addEventListener('keydown', handleEscape);
    } else {
        // Menu was open, now it's closed
        document.removeEventListener('keydown', handleEscape);
    }
}
