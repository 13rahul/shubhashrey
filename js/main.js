document.addEventListener("DOMContentLoaded", () => {
  renderNavMega();
  initNav();
  initHeaderScroll();
  renderValuesGrid();
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
      nav.querySelectorAll(".nav-dropdown.is-open, .nav-mega.is-open").forEach((dropdown) => {
        dropdown.classList.remove("is-open");
        const btn = dropdown.querySelector(".nav-dropdown__toggle, .nav-mega__toggle");
        if (btn) btn.setAttribute("aria-expanded", "false");
      });
    });
  });

  nav.querySelectorAll(".nav-dropdown").forEach((dropdown) => {
    const btn = dropdown.querySelector(".nav-dropdown__toggle");
    if (!btn) return;

    btn.addEventListener("click", (event) => {
      event.stopPropagation();
      const open = dropdown.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  document.addEventListener("click", (event) => {
    if (!event.target.closest(".nav-dropdown, .nav-mega")) {
      nav.querySelectorAll(".nav-dropdown.is-open, .nav-mega.is-open").forEach((dropdown) => {
        dropdown.classList.remove("is-open");
        const btn = dropdown.querySelector(".nav-dropdown__toggle, .nav-mega__toggle");
        if (btn) btn.setAttribute("aria-expanded", "false");
      });
    }
  });

  nav.querySelectorAll(".nav-mega").forEach((mega) => {
    const btn = mega.querySelector(".nav-mega__toggle");
    if (!btn) return;

    btn.addEventListener("click", (event) => {
      event.stopPropagation();
      const open = mega.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
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

  if (path === "shop.html" || path === "product.html") {
    const megaToggle = document.querySelector(".nav-mega__toggle");
    if (megaToggle) megaToggle.setAttribute("aria-current", "page");
  }
}

function renderNavMega() {
  const roots = document.querySelectorAll("[data-nav-mega]");
  if (!roots.length || typeof PRODUCT_CATEGORIES === "undefined") return;

  const chevron = `<svg class="nav-mega__chevron" viewBox="0 0 24 24" aria-hidden="true" width="16" height="16"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>`;

  const panelCols = PRODUCT_CATEGORIES.map((cat) => {
    const products = getProductsByCategory(cat.id);
    return `
      <div class="nav-mega__col">
        <h3 class="nav-mega__col-title">${cat.title}</h3>
        <p class="nav-mega__col-sub">${cat.subtitle}</p>
        <ul class="nav-mega__list">
          ${products
            .map(
              (p) =>
                `<li><a href="product.html?id=${p.id}">${p.name}</a></li>`
            )
            .join("")}
        </ul>
        <a class="nav-mega__cat-link" href="shop.html#category-${cat.id}">Browse ${cat.title.toLowerCase()} →</a>
      </div>
    `;
  }).join("");

  const html = `
    <button class="nav-mega__toggle" type="button" aria-expanded="false" aria-haspopup="true" aria-controls="products-mega">
      Products
      ${chevron}
    </button>
    <div class="nav-mega__panel" id="products-mega">
      <div class="nav-mega__inner">
        <div class="nav-mega__cols">${panelCols}</div>
        <div class="nav-mega__footer">
          <a class="nav-mega__all" href="shop.html">View full product catalogue →</a>
          <a class="nav-mega__guide" href="welding-process.html">Welding process guide</a>
        </div>
      </div>
    </div>
  `;

  roots.forEach((root) => {
    root.classList.add("nav-mega");
    root.innerHTML = html;
  });
}

function renderValuesGrid() {
  const root = document.getElementById("values-grid");
  if (!root || typeof COMPANY_VALUES === "undefined") return;

  root.innerHTML = COMPANY_VALUES.map(
    (item) => `
    <article class="value-card">
      <h3>${item.title}</h3>
      <p>${item.text}</p>
    </article>
  `
  ).join("");
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

  const related = PRODUCTS.filter(
    (p) => p.categoryGroup === product.categoryGroup && p.id !== product.id
  );

  root.innerHTML = `
    <div class="product-detail">
      <div class="product-detail__media reveal">
        <img src="${product.image}" alt="${product.name} — Bharatweld welding electrodes with packaging" width="1200" height="900" />
      </div>
      <div class="product-detail__info reveal">
        <p class="eyebrow">${product.category}</p>
        <h1>${product.name}</h1>
        <p class="product-detail__tagline">${product.tagline || ""}</p>
        <p class="product-detail__sku">SKU: ${product.sku} · AWS ${product.aws || "—"}</p>
        <p>${product.description}</p>
        <div class="cta-row">
          <button type="button" class="btn btn--primary" data-buy-now="${product.id}">Buy now</button>
          <a class="btn btn--ghost" href="contact.html">Enquire</a>
        </div>
        <table class="spec-table">
          <tbody>
            <tr><th>AWS classification</th><td>${product.aws || "—"}</td></tr>
            <tr><th>Coating type</th><td>${product.coating || "—"}</td></tr>
            <tr><th>Welding positions</th><td>${product.positions || "—"}</td></tr>
            <tr><th>Current / polarity</th><td>${product.polarity || product.current || "—"}</td></tr>
            <tr><th>Diameters</th><td>${product.diameters || "—"}</td></tr>
            <tr><th>Industries</th><td>${(product.industries || []).join(", ")}</td></tr>
            <tr><th>Applications</th><td>${(product.applications || []).join("; ")}</td></tr>
          </tbody>
        </table>
        ${
          related.length
            ? `<div class="product-related">
            <h2>Related products</h2>
            <ul>${related.map((p) => `<li><a href="product.html?id=${p.id}">${p.name}</a></li>`).join("")}</ul>
          </div>`
            : ""
        }
        <p><a href="shop.html#category-${product.categoryGroup}" class="back-link">← Back to ${product.category}</a></p>
      </div>
    </div>
  `;

  bindBuyNowButtons(root);
  initReveals();
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
