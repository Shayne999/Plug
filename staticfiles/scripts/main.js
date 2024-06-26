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




/*====================================================================

NOTIFICATIONS                                                         */

function showNotifications() {
    var container = document.getElementById('notification-container');
    if (container.classList.contains('d-none')) {
        container.classList.remove('d-none');
    } else {
        container.classList.add('d-none');
    }
}

function removeNotification(url, redirectUrl) {
    fetch(url, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => {
        if (response.ok) {
            // Optionally refresh the notifications
            window.location.href = redirectUrl;
            console.log
        } else {
            console.error('Failed to delete notification');
        }
    })
    .catch(error => console.error('Error:', error));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}












