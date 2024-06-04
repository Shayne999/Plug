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
    const container = document.getElementById('notification-container');
    
    if (container.classList.contains('d-none')) {
        container.classList.remove('d-none');
    } else {
        container.classList.add('d-none');
    }

}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function removeNotification(removeNotificationURL, redirectURL) {

    const csrftoken = getCookie('csrftoken');
    let xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readystate === XMLHttpRequest.DONE) {
            if (xmlhttp.status === 200) {
                window.location.replace = redirectURL;
            } else {
                alert('There was an error removing the notification.');
            }
        }
    };
    xmlhttp.open("DELETE", removeNotificationURL, true);
    xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xmlhttp.send();
}









