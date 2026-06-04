document.addEventListener('DOMContentLoaded', () => {
    // Create scroll progress bar dynamically
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    document.body.appendChild(progressBar);

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

    // Dynamic scroll tracking: progress bar, background parallax, and BOOM badge rotation
    const boom = document.querySelector('.comic-boom');
    const scrollIndicator = document.querySelector('.scroll-hint-left');
    window.addEventListener('scroll', () => {
        const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        
        // 1. Update progress bar
        if (height > 0) {
            const scrolledPercent = (winScroll / height) * 100;
            progressBar.style.width = `${scrolledPercent}%`;
        }

        // 2. Parallax background halftone shift
        document.body.style.backgroundPositionY = `${winScroll * 0.15}px`;

        // 3. Dynamic BOOM! badge rotation
        if (boom) {
            boom.style.transform = `scale(1) rotate(${15 + winScroll * 0.05}deg)`;
        }

        // 4. Fade out scroll indicator on scroll
        if (scrollIndicator) {
            const opacity = Math.max(1 - winScroll / 200, 0);
            scrollIndicator.style.opacity = opacity;
            scrollIndicator.style.visibility = opacity === 0 ? 'hidden' : 'visible';
        }
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
