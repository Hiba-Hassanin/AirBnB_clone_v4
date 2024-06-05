$(document).ready(function() {
    const selectedAmenities = {};

    $('input[type="checkbox"]').change(function() {
        const amenityId = $(this).attr('data-id');
        const amenityName = $(this).attr('data-name');

        if (this.checked) {
            selectedAmenities[amenityId] = amenityName;
        } else {
            delete selectedAmenities[amenityId];
        }

        updateAmenities();
    });

    function updateAmenities() {
        const amenityList = Object.values(selectedAmenities).join(', ');
        $('.filters h4').text(`Amenities: ${amenityList}`);
    }
});
