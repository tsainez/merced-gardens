var body = document.querySelector('body')
var menuTrigger = document.querySelector('#toggle-main-menu-mobile');
var menuContainer = document.querySelector('#main-menu-mobile');

menuTrigger.onclick = function() {
    menuContainer.classList.toggle('open');
    menuTrigger.classList.toggle('is-active');
    body.classList.toggle('lock-scroll');

    // Toggle aria-expanded
    var isExpanded = menuTrigger.getAttribute('aria-expanded') === 'true';
    menuTrigger.setAttribute('aria-expanded', !isExpanded);
}

document.addEventListener('keydown', function(event) {
  var isExpanded = menuTrigger.getAttribute('aria-expanded') === 'true';
  if (event.key === 'Escape' && isExpanded) {
    menuTrigger.click();
    menuTrigger.focus();
  }
});
