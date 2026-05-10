document.addEventListener('DOMContentLoaded', () => {
    // Intersection Observer for scroll animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
                // Optional: stop observing once animated
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Select all elements with animation classes
    const animatedElements = document.querySelectorAll(
        '.animate-slide-left, .animate-slide-right, .animate-slide-down, .animate-pop, .animate-fade-in, .animate-zoom'
    );

    animatedElements.forEach(el => {
        observer.observe(el);
    });

    // Add glitch effect interval to title
    const title = document.querySelector('.glitch');
    if (title) {
        setInterval(() => {
            title.style.transform = `translate(${Math.random() * 4 - 2}px, ${Math.random() * 4 - 2}px)`;
            setTimeout(() => {
                title.style.transform = 'translate(0, 0)';
            }, 50);
        }, 3000);
    }
    
    // Initial navbar animation trigger
    setTimeout(() => {
        const nav = document.querySelector('.navbar');
        if(nav) nav.classList.add('in-view');
    }, 100);
});
