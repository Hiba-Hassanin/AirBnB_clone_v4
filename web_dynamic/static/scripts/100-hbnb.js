document.addEventListener('DOMContentLoaded', function () {
    const statesCheckboxes = document.querySelectorAll('.states input[type="checkbox"]');
    const citiesCheckboxes = document.querySelectorAll('.cities input[type="checkbox"]');
    const locationsList = document.getElementById('locations-list');

    statesCheckboxes.forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            updateLocationsList(this);
        });
    });

    citiesCheckboxes.forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            updateLocationsList(this);
        });
    });

    function updateLocationsList(checkbox) {
        const locationId = checkbox.getAttribute('data-id');
        const locationName = checkbox.getAttribute('data-name');
        if (checkbox.checked) {
            locationsList.textContent += locationName + ', ';
            // Store the State or City ID
            // You can implement your own logic here
        } else {
            locationsList.textContent = locationsList.textContent.replace(locationName + ', ', '');
            // Remove the State or City ID
            // You can implement your own logic here
        }
    }
});
