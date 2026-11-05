initSitePreloader();

document.addEventListener("DOMContentLoaded", () => {
  renderNavMega();
  initNav();
  initHeaderScroll();
  renderValuesGrid();
  updateCartBadge();
  renderFeaturedProducts();
  renderShopGrid();
  if (typeof initGradeChooser === "function") initGradeChooser();
  renderIndustriesGrid();
  initGradeStage();
  initEraseReveal();
  initAmpPickers();
  initProductGalleries();
  renderProductPage();
  if (typeof bindBuyNowButtons === "function") bindBuyNowButtons(document);
  renderCartPage();
  initReveals();
  initTestimonialSlider();
  initCheckoutForm();
  initContactForm();
  initDistributorForm();
  initDistributorBrief();
  setActiveNav();
  injectBrochureFab();
});

function initSitePreloader() {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const root = document.documentElement;
  const preloader = document.getElementById("site-preloader");
  const fill = preloader?.querySelector(".site-preloader__bar-fill");
  const pctEl = preloader?.querySelector("[data-preloader-pct]");

  const finish = () => {
    root.classList.remove("is-preload");
    if (!preloader) return;
    preloader.classList.add("is-done");
    preloader.setAttribute("aria-busy", "false");
    preloader.setAttribute("aria-hidden", "true");
    window.setTimeout(() => {
      preloader.remove();
    }, 600);
  };

  // Skip animation when returning within the same tab session
  try {
    if (sessionStorage.getItem("shubh_preloader_seen") === "1") {
      finish();
      return;
    }
  } catch (_) {
    /* private mode */
  }

  if (!preloader) {
    root.classList.remove("is-preload");
    return;
  }

  let progress = 0;
  let loaded = document.readyState === "complete";
  const started = performance.now();
  const minMs = reducedMotion ? 120 : 900;
  const maxMs = 4200;

  const setProgress = (value) => {
    progress = Math.max(progress, Math.min(100, value));
    if (fill) fill.style.width = `${progress}%`;
    if (pctEl) pctEl.textContent = String(Math.round(progress));
  };

  setProgress(8);

  const tick = window.setInterval(() => {
    if (loaded) return;
    const next = progress + (progress < 70 ? 2.2 : progress < 90 ? 0.8 : 0.2);
    setProgress(Math.min(next, 92));
  }, 90);

  const done = () => {
    loaded = true;
    window.clearInterval(tick);
    setProgress(100);
    const wait = Math.max(0, minMs - (performance.now() - started));
    window.setTimeout(() => {
      try {
        sessionStorage.setItem("shubh_preloader_seen", "1");
      } catch (_) {
        /* ignore */
      }
      finish();
    }, reducedMotion ? 0 : wait + 180);
  };

  if (loaded) {
    done();
  } else {
    window.addEventListener("load", done, { once: true });
    window.setTimeout(done, maxMs);
  }
}

function injectBrochureFab() {
  if (document.querySelector(".brochure-fab")) return;
  const a = document.createElement("a");
  a.className = "brochure-fab";
  a.href = "/assets/brochure/bharatweld-brochure.pdf";
  a.setAttribute("download", "");
  a.setAttribute("aria-label", "Download Bharatweld brochure PDF");
  a.innerHTML =
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm1 7V3.5L18.5 9H15zM12 19l-4-4h2.5V11h3v4H16l-4 4z"/></svg>' +
    '<span class="brochure-fab__label">Brochure</span>';
  document.body.appendChild(a);
}

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

  if (
    path === "shop.html" ||
    path === "product.html" ||
    window.location.pathname.includes("/products/")
  ) {
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
                `<li><a href="${productUrl(p.id)}">${p.name}</a></li>`
            )
            .join("")}
        </ul>
        <a class="nav-mega__cat-link" href="/shop.html#category-${cat.id}">Browse ${cat.title.toLowerCase()} -></a>
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
          <a class="nav-mega__all" href="/shop.html">View full product catalogue -></a>
          <a class="nav-mega__guide" href="/welding-process.html">Welding process guide</a>
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

  const cards = INDUSTRIES.map(
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
  );

  cards.push(`
    <article class="industry-item industry-item--cta reveal">
      <div class="industry-item__body">
        <p class="product-item__cat">Full range</p>
        <h3>See every application</h3>
        <p>Browse grade-by-grade guidance for fabrication, structural, stainless, cutting, and hardfacing work.</p>
        <a class="btn btn--primary btn--sm" href="industries.html">Explore industries</a>
      </div>
    </article>
  `);

  root.innerHTML = cards.join("");

  initReveals();
}

const GRADE_STAGE_COPY = {
  "e-6013": {
    why: "General-purpose rutile electrode for everyday fabrication — smooth arc, easy slag, clean bead.",
  },
  "e-7018": {
    why: "Low-hydrogen strength for structural frames, bridges, and crack-sensitive heavy steel.",
  },
  "e-308l": {
    why: "Extra-low carbon stainless for 304/308 food, chemical, and architectural work.",
  },
  cutting: {
    why: "Bharatweld cutting electrodes for severing, piercing, and gouging without oxy-fuel gear.",
  },
  manganese: {
    why: "High-manganese overlays for crushers, rails, and heavy abrasion + impact.",
  },
};

function initGradeStage() {
  const root = document.querySelector("[data-grade-stage]");
  if (!root || typeof getProductById !== "function") return;

  const jobs = root.querySelectorAll("[data-grade-job]");
  const img = root.querySelector("[data-grade-img]");
  const cat = root.querySelector("[data-grade-cat]");
  const name = root.querySelector("[data-grade-name]");
  const why = root.querySelector("[data-grade-why]");
  const link = root.querySelector("[data-grade-link]");

  const activate = (id) => {
    const product = getProductById(id);
    if (!product) return;
    jobs.forEach((btn) => {
      const on = btn.getAttribute("data-grade-job") === id;
      btn.classList.toggle("is-active", on);
      btn.setAttribute("aria-selected", on ? "true" : "false");
    });
    if (img) {
      img.src = product.image;
      img.alt = `${product.name} — Bharatweld packaging`;
    }
    if (cat) cat.textContent = product.category;
    if (name) name.textContent = product.name;
    if (why) why.textContent = GRADE_STAGE_COPY[id]?.why || product.tagline || product.description;
    if (link) {
      link.href = productUrl(id);
      link.textContent = `View ${product.shortName}`;
    }
  };

  jobs.forEach((btn) => {
    const id = btn.getAttribute("data-grade-job");
    btn.addEventListener("mouseenter", () => activate(id));
    btn.addEventListener("focus", () => activate(id));
    btn.addEventListener("click", () => activate(id));
  });
}

function initEraseReveal() {
  const nodes = document.querySelectorAll("[data-erase]");
  if (!nodes.length) return;
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduced) {
    nodes.forEach((el) => el.classList.add("is-on"));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-on");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.45 }
  );
  nodes.forEach((el) => io.observe(el));
}

function initAmpPickers() {
  document.querySelectorAll("[data-amp-picker]").forEach((root) => {
    const chips = root.querySelectorAll("[data-amp]");
    const rangeEl = root.querySelector("[data-amp-range]");
    const tipEl = root.querySelector("[data-amp-tip]");
    const setActive = (chip) => {
      chips.forEach((c) => c.classList.toggle("is-active", c === chip));
      if (rangeEl) rangeEl.textContent = chip.getAttribute("data-amp-range") || "";
      if (tipEl) tipEl.textContent = chip.getAttribute("data-amp-tip") || "";
    };
    chips.forEach((chip) => chip.addEventListener("click", () => setActive(chip)));
    if (chips[0]) setActive(chips[0]);
  });
}

function initProductGalleries() {
  document.querySelectorAll("[data-product-gallery]").forEach((root) => {
    const main = root.querySelector("[data-gallery-main]");
    const thumbs = root.querySelectorAll("[data-gallery-thumb]");
    thumbs.forEach((btn) => {
      btn.addEventListener("click", () => {
        thumbs.forEach((t) => t.classList.toggle("is-active", t === btn));
        const src = btn.getAttribute("data-src");
        const alt = btn.getAttribute("data-alt") || "";
        if (main && src) {
          main.src = src;
          main.alt = alt;
        }
      });
    });
  });
}

function initDistributorBrief() {
  const form = document.getElementById("distributor-form");
  const brief = document.querySelector("[data-distributor-brief]");
  if (!form || !brief) return;

  const steps = [...brief.querySelectorAll("[data-brief-step]")];
  const dots = [...brief.querySelectorAll("[data-brief-dot]")];
  let index = 0;

  const show = (i) => {
    index = Math.max(0, Math.min(steps.length - 1, i));
    steps.forEach((step, n) => {
      step.hidden = n !== index;
    });
    dots.forEach((dot, n) => {
      dot.classList.toggle("is-active", n === index);
      dot.classList.toggle("is-done", n < index);
    });
  };

  brief.querySelectorAll("[data-brief-next]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const step = steps[index];
      const required = step?.querySelectorAll("[required]");
      let ok = true;
      required?.forEach((field) => {
        if (!field.checkValidity()) {
          field.reportValidity();
          ok = false;
        }
      });
      if (ok) show(index + 1);
    });
  });

  brief.querySelectorAll("[data-brief-prev]").forEach((btn) => {
    btn.addEventListener("click", () => show(index - 1));
  });

  show(0);
}

function renderProductPage() {
  /* Product pages are static HTML under /products/{id}. Legacy ?id= redirects via .htaccess. */
  const root = document.getElementById("product-detail");
  if (!root) return;

  const params = new URLSearchParams(window.location.search);
  const id = params.get("id");
  if (id && getProductById(id)) {
    window.location.replace(productUrl(id));
    return;
  }

  root.innerHTML = `
      <div class="empty-state">
        <h2>Browse Bharatweld electrodes</h2>
        <p>Product pages now use clean URLs. Open the catalogue to choose a grade.</p>
        <a class="btn btn--primary" href="/shop.html">Go to shop</a>
      </div>
    `;
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

async function saveLead(payload) {
  const candidates = [
    "api/lead.php",
    "./api/lead.php",
    "/Subhshrey-industries/api/lead.php",
  ];
  // Prefer path relative to current page folder
  const base = window.location.pathname.replace(/[^/]+$/, "");
  candidates.unshift(base + "api/lead.php");

  for (const url of [...new Set(candidates)]) {
    try {
      const res = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await res.json().catch(() => ({}));
      if (res.ok && data && data.success) {
        return true;
      }
    } catch (_) {
      /* try next */
    }
  }
  return false;
}

function initContactForm() {
  const form = document.getElementById("contact-form");
  if (!form) return;

  const whatsappNumber =
    typeof WHATSAPP_ORDER_NUMBER !== "undefined" ? WHATSAPP_ORDER_NUMBER : "919168679621";

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const status = document.getElementById("contact-status");

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    const firstName = form.firstName.value.trim();
    const lastName = form.lastName.value.trim();
    const email = form.email.value.trim();
    const phone = form.phone.value.trim();
    const message = form.message.value.trim();

    const saved = await saveLead({
      source: "contact",
      lead_label: "Inbound",
      firstName,
      lastName,
      name: `${firstName} ${lastName}`.trim(),
      email,
      phone,
      message,
    });

    let text =
      `*New enquiry - Bharatweld / Shubhshrey*\n` +
      `Name: ${firstName} ${lastName}\n` +
      `Email: ${email}\n`;

    if (phone) text += `Phone: ${phone}\n`;
    text += `\nMessage:\n${message}`;

    const url = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(text)}`;
    window.open(url, "_blank", "noopener,noreferrer");

    form.reset();
    status.textContent = saved
      ? "Saved - WhatsApp opened with your message. Tap Send in WhatsApp to deliver it to us."
      : "WhatsApp opened with your message. Tap Send in WhatsApp to deliver it to us.";
    status.className = "form-status is-success";
  });
}

function initDistributorForm() {
  const form = document.getElementById("distributor-form");
  if (!form) return;

  const whatsappNumber =
    typeof WHATSAPP_ORDER_NUMBER !== "undefined" ? WHATSAPP_ORDER_NUMBER : "919168679621";

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const status = document.getElementById("distributor-status");

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    const fullName = form.fullName.value.trim();
    const company = form.company.value.trim();
    const email = form.email.value.trim();
    const phone = form.phone.value.trim();
    const city = form.city.value.trim();
    const state = form.state.value.trim();
    const area = form.area.value.trim();
    const businessType = form.businessType.value;
    const experience = form.experience.value.trim();
    const interest = form.interest.value;
    const message = form.message.value.trim();

    const saved = await saveLead({
      source: "distributor",
      lead_label: "Inbound",
      fullName,
      name: fullName,
      company,
      email,
      phone,
      city,
      state,
      area,
      territory: area,
      businessType,
      experience,
      interest,
      message,
    });

    let text =
      `*Distributor application - Bharatweld / Shubhshrey*\n\n` +
      `*Contact person:* ${fullName}\n` +
      `*Company:* ${company}\n` +
      `*Email:* ${email}\n` +
      `*Phone / WhatsApp:* ${phone}\n` +
      `*City:* ${city}\n` +
      `*State:* ${state}\n` +
      `*Territory:* ${area}\n` +
      `*Business type:* ${businessType}\n`;

    if (experience) text += `*Experience:* ${experience}\n`;
    text += `*Products of interest:* ${interest}\n`;
    text += `\n*About the business:*\n${message}`;

    const url = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(text)}`;
    window.open(url, "_blank", "noopener,noreferrer");

    form.reset();
    status.textContent = saved
      ? "Saved - WhatsApp opened with your distributor application. Tap Send in WhatsApp to deliver it."
      : "WhatsApp opened with your distributor application. Tap Send in WhatsApp to deliver it to us.";
    status.className = "form-status is-success";
  });
}
