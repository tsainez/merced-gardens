var body = document.querySelector('body');
var menuTrigger = document.querySelector('#toggle-main-menu-mobile');
var menuContainer = document.querySelector('#main-menu-mobile');

if (menuTrigger && menuContainer) {
    menuTrigger.onclick = function() {
        toggleMenu();
    }

    function toggleMenu() {
        menuContainer.classList.toggle('open');
        menuTrigger.classList.toggle('is-active');
        body.classList.toggle('lock-scroll');

        // Toggle aria-expanded
        var isExpanded = menuTrigger.getAttribute('aria-expanded') === 'true';
        menuTrigger.setAttribute('aria-expanded', !isExpanded);

        if (!isExpanded) {
            // Menu is opening
            document.addEventListener('keydown', handleEsc);
            setTimeout(function() {
                var firstLink = menuContainer.querySelector('a');
                if (firstLink) {
                    firstLink.focus();
                }
            }, 50);
        } else {
            // Menu is closing
            document.removeEventListener('keydown', handleEsc);
        }
    }

    function handleEsc(event) {
        if (event.key === 'Escape') {
            toggleMenu();
            menuTrigger.focus();
        }
    }
}
