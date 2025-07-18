// This file contains JavaScript code for interactive features on the website, such as form validation and dynamic content loading.

document.addEventListener('DOMContentLoaded', function() {
    // Example of form validation
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            if (!name || !email) {
                event.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    }

    // Example of dynamic content loading
    const loadDestinationsButton = document.getElementById('load-destinations');
    if (loadDestinationsButton) {
        loadDestinationsButton.addEventListener('click', function() {
            fetch('destinations.json')
                .then(response => response.json())
                .then(data => {
                    const destinationsList = document.getElementById('destinations-list');
                    destinationsList.innerHTML = '';
                    data.forEach(destination => {
                        const listItem = document.createElement('li');
                        listItem.textContent = destination.name;
                        destinationsList.appendChild(listItem);
                    });
                })
                .catch(error => console.error('Error loading destinations:', error));
        });
    }
});