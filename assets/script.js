// scripts.js
document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('header');
    header.style.transition = 'background-color 0.5s';

    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.style.backgroundColor = '#cc0000';
        } else {
            header.style.backgroundColor = '#ff0000';
        }
    });

    const videoItems = document.querySelectorAll('.video-item');
    videoItems.forEach(item => {
        item.addEventListener('mouseover', () => {
            item.style.transform = 'scale(1.05)';
        });

        item.addEventListener('mouseout', () => {
            item.style.transform = 'scale(1)';
        });
    });
});
