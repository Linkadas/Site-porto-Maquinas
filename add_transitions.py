import os

# 1. Add CSS for page transitions
css_to_add = """
/* Page Transition Animations */
body {
    animation: fadeInPage 0.4s ease-out forwards;
}

body.page-exit {
    animation: fadeOutPage 0.3s ease-in forwards;
}

@keyframes fadeInPage {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeOutPage {
    from { opacity: 1; transform: translateY(0); }
    to { opacity: 0; transform: translateY(-10px); }
}
"""

with open('css/animations.css', 'a', encoding='utf-8') as f:
    f.write(css_to_add)

# 2. Add JS for intercepting link clicks
js_to_add = """
// Page Transitions
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a[href]').forEach(link => {
        // Only internal links, not hash links, no target="_blank"
        if (link.hostname === window.location.hostname && !link.hash && link.getAttribute('target') !== '_blank' && !link.href.includes('mailto:') && !link.href.includes('tel:')) {
            link.addEventListener('click', function(e) {
                // Ignore if opening in new tab (ctrl/cmd click)
                if (e.ctrlKey || e.metaKey || e.shiftKey || e.button !== 0) return;
                
                e.preventDefault();
                const targetUrl = this.href;
                document.body.classList.add('page-exit');
                setTimeout(() => {
                    window.location.href = targetUrl;
                }, 300); // matches the 0.3s CSS animation
            });
        }
    });
});
"""

with open('js/main.js', 'a', encoding='utf-8') as f:
    f.write(js_to_add)

print("Page transitions added.")
