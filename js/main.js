document.addEventListener("DOMContentLoaded", () => {
  initNav();
  initHeaderScroll();
  updateCartBadge();
  renderFeaturedProducts();
  renderShopGrid();
  renderIndustriesGrid();
  renderProductPage();
  renderCartPage();
  initReveals();
  initTestimonialSlider();
  initCheckoutForm();
  initContactForm();
  setActiveNav();
});

function initNav() {
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".site-nav");
  if (!toggle || !nav) return;

  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("is-open");
    toggle.classList.toggle("is-active", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.classList.toggle("nav-open", open);
  });

  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.remove("is-open");
      toggle.classList.remove("is-active");
      toggle.setAttribute("aria-expanded", "false");
      document.body.classList.remove("nav-open");
    });
  });
}

function initHeaderScroll() {
  const header = document.querySelector(".site-header");
  if (!header) return;

  const onScroll = () => {
    header.classList.toggle("is-scrolled", window.scrollY > 20);
  };

  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

function setActiveNav() {
  const path = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".site-nav a[href]").forEach((link) => {
    const href = link.getAttribute("href");
    if (href === path || (path === "" && href === "index.html")) {
      link.setAttribute("aria-current", "page");
    }
  });
}

let revealObserver = null;

function initReveals() {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const items = document.querySelectorAll(".reveal:not([data-reveal-bound])");

  if (!items.length) return;

  items.forEach((el) => el.setAttribute("data-reveal-bound", "true"));

  if (reducedMotion || !("IntersectionObserver" in window)) {
    items.forEach((el) => el.classList.add("is-visible"));
    return;
  }

  if (!revealObserver) {
    revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: "0px 0px -30px 0px" }
    );
  }

  items.forEach((el, i) => {
    const parent = el.closest(".serve-grid, .product-grid, .industry-grid");
    const delay = parent ? Math.min(i * 80, 480) : Math.min(i * 60, 360);
    el.style.setProperty("--reveal-delay", `${delay}ms`);
    revealObserver.observe(el);
  });
}

function renderIndustriesGrid() {
  const root = document.getElementById("industries-grid");
  if (!root || typeof INDUSTRIES === "undefined") return;

  root.innerHTML = INDUSTRIES.map(
    (item) => `
    <article class="industry-item reveal">
      <a class="industry-item__media" href="industries.html#${item.id}">
        <img src="${item.image}" alt="${item.title}" width="640" height="400" loading="lazy" />
      </a>
      <div class="industry-item__body">
        <p class="product-item__cat">${item.grades}</p>
        <h3>${item.title}</h3>
        <p>${item.summary}</p>
        <a href="industries.html#${item.id}">View applications</a>
      </div>
    </article>
  `
  ).join("");

  initReveals();
}

function renderProductPage() {
  const root = document.getElementById("product-detail");
  if (!root) return;

  const params = new URLSearchParams(window.location.search);
  const id = params.get("id");
  const product = id ? getProductById(id) : null;

  if (!product) {
    root.innerHTML = `
      <div class="empty-state">
        <h2>Product not found</h2>
        <p>Browse the full Bharatweld electrode range.</p>
        <a class="btn btn--primary" href="shop.html">Go to shop</a>
      </div>
    `;
    return;
  }

  document.title = `${product.name} | Bharatweld | Shubhshrey Industries`;

  root.innerHTML = `
    <div class="product-detail">
      <div class="product-detail__media reveal">
        <img src="${product.image}" alt="${product.name} Bharatweld electrode" width="800" height="600" />
        <img class="product-detail__pack" src="assets/bharatweld-pack.png" alt="Bharatweld welding electrodes packaging" width="800" height="500" loading="lazy" />
      </div>
      <div class="product-detail__info reveal">
        <p class="eyebrow">${product.category}</p>
        <h1>${product.name}</h1>
        <p class="product-detail__sku">SKU: ${product.sku}</p>
        <p>${product.description}</p>
        <p class="product-item__price">${formatINR(product.price)}${product.unit ? ` <small>${product.unit}</small>` : ""}</p>
        <div class="cta-row">
          <button type="button" class="btn btn--primary" data-add-to-cart="${product.id}">Add to cart</button>
          <a class="btn btn--ghost" href="checkout.html" id="buy-now-link">Buy now via WhatsApp</a>
        </div>
        <table class="spec-table">
          <tbody>
            <tr><th>Current</th><td>${product.current || "—"}</td></tr>
            <tr><th>Industries</th><td>${(product.industries || []).join(", ")}</td></tr>
            <tr><th>Applications</th><td>${(product.applications || []).join("; ")}</td></tr>
          </tbody>
        </table>
        <p><a href="shop.html" class="back-link">← Back to shop</a></p>
      </div>
    </div>
  `;

  bindAddToCartButtons(root);
  initReveals();

  const buyNow = document.getElementById("buy-now-link");
  if (buyNow) {
    buyNow.addEventListener("click", (e) => {
      e.preventDefault();
      addToCart(product.id, 1);
      window.location.href = "checkout.html";
    });
  }
}

function initTestimonialSlider() {
  const root = document.querySelector("[data-testimonial-slider]");
  if (!root) return;

  const viewport = root.querySelector(".testimonial-slider__viewport");
  const track = root.querySelector(".testimonial-slider__track");
  const slides = Array.from(root.querySelectorAll(".testimonial-slide"));
  const prevBtn = root.querySelector("[data-testimonial-prev]");
  const nextBtn = root.querySelector("[data-testimonial-next]");
  const dotsRoot = root.querySelector("[data-testimonial-dots]");
  let index = 0;
  let timer;

  if (!slides.length || !track || !viewport) return;

  function getVisibleCount() {
    if (window.innerWidth <= 640) return 1;
    if (window.innerWidth <= 900) return 2;
    return 3;
  }

  function getMaxIndex() {
    return Math.max(0, slides.length - getVisibleCount());
  }

  function buildDots() {
    const maxIndex = getMaxIndex();
    const count = maxIndex + 1;
    dotsRoot.innerHTML = Array.from({ length: count }, (_, i) =>
      `<button type="button" class="testimonial-slider__dot${i === index ? " is-active" : ""}" data-testimonial-dot="${i}" aria-label="Go to slide ${i + 1}"></button>`
    ).join("");
    dotsRoot.querySelectorAll("[data-testimonial-dot]").forEach((dot) => {
      dot.addEventListener("click", () => {
        index = Number(dot.getAttribute("data-testimonial-dot"));
        update();
        restartTimer();
      });
    });
  }

  function update() {
    const visible = getVisibleCount();
    const maxIndex = getMaxIndex();
    index = Math.min(index, maxIndex);

    root.style.setProperty("--testimonial-visible", String(visible));

    const slideWidth = viewport.offsetWidth / visible;
    track.style.transform = `translateX(-${index * slideWidth}px)`;

    dotsRoot.querySelectorAll("[data-testimonial-dot]").forEach((dot, i) => {
      dot.classList.toggle("is-active", i === index);
    });

    if (prevBtn) prevBtn.disabled = index === 0;
    if (nextBtn) nextBtn.disabled = index >= maxIndex;
  }

  function next() {
    index = Math.min(index + 1, getMaxIndex());
    update();
  }

  function prev() {
    index = Math.max(index - 1, 0);
    update();
  }

  function restartTimer() {
    clearInterval(timer);
    timer = setInterval(() => {
      if (index >= getMaxIndex()) index = 0;
      else index += 1;
      update();
    }, 6000);
  }

  buildDots();
  update();
  restartTimer();

  prevBtn?.addEventListener("click", () => {
    prev();
    restartTimer();
  });

  nextBtn?.addEventListener("click", () => {
    next();
    restartTimer();
  });

  window.addEventListener("resize", () => {
    buildDots();
    update();
  });
}

function initContactForm() {
  const form = document.getElementById("contact-form");
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const status = document.getElementById("contact-status");
    const submitBtn = form.querySelector('[type="submit"]');

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    const payload = {
      firstName: form.firstName.value.trim(),
      lastName: form.lastName.value.trim(),
      email: form.email.value.trim(),
      phone: form.phone.value.trim(),
      message: form.message.value.trim(),
    };

    submitBtn.disabled = true;
    status.textContent = "Sending…";
    status.className = "form-status";

    try {
      const res = await fetch("api/contact.php", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await res.json().catch(() => ({}));

      if (!res.ok || !data.success) {
        throw new Error(data.message || "Could not send message.");
      }

      form.reset();
      status.textContent = "Thank you. We will be in touch shortly.";
      status.className = "form-status is-success";
    } catch (err) {
      status.textContent =
        err.message || "Unable to send right now. Email us at contact@shubhshrey.com.";
      status.className = "form-status is-error";
    } finally {
      submitBtn.disabled = false;
    }
  });
}
