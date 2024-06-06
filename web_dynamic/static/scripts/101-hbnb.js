document.addEventListener('DOMContentLoaded', function () {
    const toggleReviews = document.getElementById('toggle-reviews');
    toggleReviews.addEventListener('click', function () {
        const reviewsContainer = document.getElementById('reviews-container');
        if (toggleReviews.textContent === 'Show') {
            // Fetch and display reviews
            fetchReviews().then(reviews => {
                reviewsContainer.innerHTML = ''; // Clear existing reviews
                reviews.forEach(review => {
                    const reviewElement = document.createElement('div');
                    reviewElement.textContent = review;
                    reviewsContainer.appendChild(reviewElement);
                });
            });
            toggleReviews.textContent = 'Hide';
        } else {
            // Hide reviews
            reviewsContainer.innerHTML = '';
            toggleReviews.textContent = 'Show';
        }
    });
});

function fetchReviews() {
    return fetch('/get_reviews') // Adjust the route accordingly
        .then(response => response.json())
        .catch(error => console.error('Error fetching reviews:', error));
}
