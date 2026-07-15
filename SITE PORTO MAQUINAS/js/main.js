document.addEventListener("DOMContentLoaded", () => {
    /* 1. Scroll Animations (Fade In / Slide Up) */
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Seleciona elementos para animar
    const animateElements = document.querySelectorAll('.hero-content, .about-grid, .product-card, .service-grid article, .catalog-choice, .contact-layout');
    animateElements.forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });

    /* 2. Catalog Search (Linha Acessório Panificação) */
    const searchInput = document.querySelector('.search-field input');
    const catalogItems = document.querySelectorAll('.catalog-choice');
    if (searchInput && catalogItems.length > 0) {
        searchInput.addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase().trim();
            catalogItems.forEach(item => {
                const text = item.textContent.toLowerCase();
                if (text.includes(term)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }

    /* 3. WhatsApp Form (Orçamento) */
    const contactForm = document.querySelector('.contact-layout form');
    if (contactForm) {
        // Remover o 'onsubmit' inline que estava na tag HTML
        contactForm.removeAttribute('onsubmit');
        
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const formData = new FormData(contactForm);
            const destino = formData.get('destino');
            
            if (!destino) {
                alert("Por favor, selecione para qual cidade deseja enviar o orçamento.");
                return;
            }

            const nome = formData.get('nome') || '';
            const email = formData.get('email') || '';
            const telefone = formData.get('telefone') || 'Não informado';
            const interesse = formData.get('interesse') || 'Não especificado';
            const mensagem = formData.get('mensagem') || '';

            const texto = `*Solicitação de orçamento — Porto Máquinas*\n\n` +
                          `*Nome:* ${nome}\n` +
                          `*E-mail:* ${email}\n` +
                          `*Telefone:* ${telefone}\n` +
                          `*Equipamento:* ${interesse}\n\n` +
                          `*Mensagem:*\n${mensagem}\n\n` +
                          `Enviado pelo site estático Porto Máquinas.`;

            const url = `https://wa.me/${destino}?text=${encodeURIComponent(texto)}`;
            window.open(url, '_blank');
        });
    /* 4. Splash Screen Logic */
    const isHomePage = document.querySelector('.hero') !== null;
    
    if (isHomePage) {
        if (!sessionStorage.getItem('splashShown')) {
            // First time loading in this session
            document.body.classList.add('splash-active');
            sessionStorage.setItem('splashShown', 'true');
            
            // Create splash screen dynamically
            const splashScreen = document.createElement('div');
            splashScreen.id = 'splash-screen';
            splashScreen.className = 'splash-screen';
            splashScreen.innerHTML = `
                <div class="splash-content">
                    <div class="splash-logo">Porto Máquinas</div>
                    <div class="splash-spinner"></div>
                </div>
            `;
            document.body.prepend(splashScreen);
            
            setTimeout(() => {
                document.body.classList.remove('splash-active');
                // Allow animation to finish
                setTimeout(() => splashScreen.remove(), 600);
            }, 2000); // 1.5s animation-delay + 0.5s fade out
        }
    }

    /* 5. Image Lightbox */
    const productImages = document.querySelectorAll('.product-visual img, .catalog-choice-visual img');
    if (productImages.length > 0) {
        // Create lightbox overlay
        const lightbox = document.createElement('div');
        lightbox.className = 'lightbox-overlay';
        const lightboxImg = document.createElement('img');
        lightbox.appendChild(lightboxImg);
        document.body.appendChild(lightbox);

        productImages.forEach(img => {
            img.style.cursor = 'zoom-in';
            img.addEventListener('click', (e) => {
                e.preventDefault();
                lightboxImg.src = img.src;
                lightbox.classList.add('show');
            });
        });

        lightbox.addEventListener('click', () => {
            lightbox.classList.remove('show');
        });
    }

    /* 6. Floating WhatsApp Button */
    const floatBtn = document.createElement('a');
    floatBtn.href = "https://wa.me/5511999999999?text=Ol%C3%A1%2C%20estou%20no%20site%20da%20Porto%20M%C3%A1quinas%20e%20gostaria%20de%20informa%C3%A7%C3%B5es.";
    floatBtn.className = 'whatsapp-float';
    floatBtn.target = '_blank';
    floatBtn.innerHTML = `<svg viewBox="0 0 24 24"><path d="M12.031 21.054c-1.579 0-3.125-.425-4.49-1.229l-5.04 1.32 1.34-4.912c-.883-1.425-1.35-3.076-1.35-4.78 0-4.935 4.015-8.95 8.95-8.95 4.935 0 8.95 4.015 8.95 8.95s-4.015 8.95-8.95 8.95zm0-16.142c-3.968 0-7.192 3.224-7.192 7.192 0 1.282.336 2.531.973 3.633l.112.193-.787 2.88 2.946-.773.187.111c1.077.64 2.308.977 3.58.977 3.968 0 7.192-3.224 7.192-7.192 0-3.968-3.224-7.192-7.192-7.192z"></path><path d="M15.82 13.676c-.225-.113-1.332-.656-1.538-.73-.205-.075-.355-.113-.505.113-.15.225-.58 .73-.711.881-.131.15-.262.169-.487.056-.225-.113-.951-.35-1.813-1.125-.671-.603-1.125-1.346-1.256-1.571-.131-.225-.014-.347.098-.46.101-.101.225-.262.337-.394.113-.131.15-.225.225-.375.075-.15.038-.281-.019-.394-.056-.113-.505-1.218-.693-1.668-.182-.437-.369-.379-.505-.386-.131-.007-.281-.007-.431-.007-.15 0-.394.056-.6.281-.205.225-.786.769-.786 1.875s.805 2.175.918 2.325c.113.15 1.583 2.419 3.834 3.389.536.231.954.369 1.28.472.537.17 1.025.146 1.411.088.432-.064 1.332-.544 1.519-1.069.187-.525.187-.975.131-1.069-.056-.094-.206-.15-.431-.262z"></path></svg>`;
    document.body.appendChild(floatBtn);
});
