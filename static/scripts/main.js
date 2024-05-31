/*====================================================================

NAV BAR                                                              */


document.addEventListener('DOMContentLoaded', (event) => {
    const currentLocation = location.pathname;
    const menuItem = document.querySelectorAll('.nav-link');
    const menuLength = menuItem.length;
    for (let i = 0; i < menuLength; i++) {
        if (menuItem[i].getAttribute("href") === currentLocation) {
            menuItem[i].classList.add('active');
            menuItem[i].style.backgroundColor = '#007bff'; // Apply inline style
        }
    }
});

/*====================================================================*/














