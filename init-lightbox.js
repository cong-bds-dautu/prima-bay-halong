// GLightbox initialization - placed at end of body
document.addEventListener('DOMContentLoaded', function() {
    // Add glightbox class to all image links
    document.querySelectorAll('a[href*=".jpg"]').forEach(link => {
        if (link.href.includes('assets/')) {
            link.classList.add('glightbox');
        }
    });

    // Initialize GLightbox with default settings
    const lightbox = GLightbox({
        selector: 'a.glightbox',
        touchNavigation: true,
        loop: true,
        autoplayVideos: false,
        closeOnOutsideClick: true,
        zoomable: true,
        draggable: true,
        openEffect: 'zoom',
        closeEffect: 'fade',
        slideEffect: 'slide',
        svg: {
            close: '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',
            next: '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>',
            prev: '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>'
        }
    });
    
    console.log('GLightbox initialized successfully with', document.querySelectorAll('a.glightbox').length, 'images');
});