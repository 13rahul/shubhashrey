const CART_KEY = "shubhshrey_cart";

function getCart() {
  try {
    const raw = localStorage.getItem(CART_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveCart(cart) {
  localStorage.setItem(CART_KEY, JSON.stringify(cart));
  updateCartBadge();
  window.dispatchEvent(new CustomEvent("cart:updated"));
}

function addToCart(productId, qty = 1) {
  const cart = getCart();
  const existing = cart.find((item) => item.id === productId);
  if (existing) {
    existing.qty += qty;
  } else {
    cart.push({ id: productId, qty });
  }
  saveCart(cart);
  return cart;
}

function setCartQty(productId, qty) {
  let cart = getCart();
  if (qty <= 0) {
    cart = cart.filter((item) => item.id !== productId);
  } else {
    const item = cart.find((i) => i.id === productId);
    if (item) item.qty = qty;
  }
  saveCart(cart);
  return cart;
}

function removeFromCart(productId) {
  const cart = getCart().filter((item) => item.id !== productId);
  saveCart(cart);
  return cart;
}

function clearCart() {
  saveCart([]);
}

function getCartCount() {
  return getCart().reduce((sum, item) => sum + item.qty, 0);
}

function getCartLines() {
  return getCart()
    .map((item) => {
      const product = getProductById(item.id);
      if (!product) return null;
      return {
        ...item,
        product,
      };
    })
    .filter(Boolean);
}

function getCartSubtotal() {
  return 0;
}

function updateCartBadge() {
  const count = getCartCount();
  document.querySelectorAll("[data-cart-count]").forEach((el) => {
    el.textContent = String(count);
    el.hidden = count === 0;
  });
}

function renderProductCard(product, { featured = false } = {}) {
  return `
    <article class="product-item reveal" data-product-id="${product.id}">
      <a class="product-item__media" href="product.html?id=${product.id}">
        <img src="${product.image}" alt="${product.name} welding electrode" width="320" height="240" loading="lazy" />
      </a>
      <div class="product-item__body">
        <p class="product-item__cat">${product.category}</p>
        <h3 class="product-item__name"><a href="product.html?id=${product.id}">${product.name}</a></h3>
        <p class="product-item__desc">${product.description}</p>
        <div class="product-item__meta">
          <button type="button" class="btn btn--primary btn--sm" data-buy-now="${product.id}">
            Buy now
          </button>
        </div>
      </div>
    </article>
  `;
}

function buyNow(productId, qty = 1) {
  addToCart(productId, qty);
  window.location.href = "checkout.html";
}

function bindBuyNowButtons(root = document) {
  root.querySelectorAll("[data-buy-now]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = btn.getAttribute("data-buy-now");
      buyNow(id, 1);
    });
  });
}

function renderCartPage() {
  const root = document.getElementById("cart-root");
  if (!root) return;

  const lines = getCartLines();
  if (!lines.length) {
    root.innerHTML = `
      <div class="empty-state">
        <h2>Your cart is empty</h2>
        <p>Browse Bharatweld electrodes and buy a product to get started.</p>
        <a class="btn btn--primary" href="shop.html">Go to shop</a>
      </div>
    `;
    return;
  }

  const rows = lines
    .map(
      (line) => `
      <tr data-cart-row="${line.id}">
        <td class="cart-product">
          <img src="${line.product.image}" alt="" width="64" height="64" />
          <div>
            <strong>${line.product.name}</strong>
            <span>${line.product.sku}</span>
          </div>
        </td>
        <td>
          <div class="qty-control">
            <button type="button" data-qty-dec="${line.id}" aria-label="Decrease quantity">−</button>
            <input type="number" min="1" value="${line.qty}" data-qty-input="${line.id}" aria-label="Quantity" />
            <button type="button" data-qty-inc="${line.id}" aria-label="Increase quantity">+</button>
          </div>
        </td>
        <td>
          <button type="button" class="link-danger" data-remove="${line.id}">Remove</button>
        </td>
      </tr>
    `
    )
    .join("");

  root.innerHTML = `
    <div class="cart-layout">
      <div class="cart-table-wrap">
        <table class="cart-table">
          <thead>
            <tr>
              <th>Product</th>
              <th>Qty</th>
              <th></th>
            </tr>
          </thead>
          <tbody>${rows}</tbody>
        </table>
      </div>
      <aside class="cart-summary">
        <h2>Order summary</h2>
        <p class="cart-summary__note">Enter your details on the next step and send the order on WhatsApp.</p>
        <a class="btn btn--primary btn--block" href="checkout.html">Checkout via WhatsApp</a>
        <a class="btn btn--ghost btn--block" href="shop.html">Continue shopping</a>
      </aside>
    </div>
  `;

  root.querySelectorAll("[data-qty-dec]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = btn.getAttribute("data-qty-dec");
      const line = getCart().find((i) => i.id === id);
      if (line) setCartQty(id, line.qty - 1);
      renderCartPage();
    });
  });

  root.querySelectorAll("[data-qty-inc]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = btn.getAttribute("data-qty-inc");
      const line = getCart().find((i) => i.id === id);
      if (line) setCartQty(id, line.qty + 1);
      renderCartPage();
    });
  });

  root.querySelectorAll("[data-qty-input]").forEach((input) => {
    input.addEventListener("change", () => {
      const id = input.getAttribute("data-qty-input");
      const qty = parseInt(input.value, 10);
      setCartQty(id, Number.isFinite(qty) ? qty : 1);
      renderCartPage();
    });
  });

  root.querySelectorAll("[data-remove]").forEach((btn) => {
    btn.addEventListener("click", () => {
      removeFromCart(btn.getAttribute("data-remove"));
      renderCartPage();
    });
  });
}

function renderCheckoutSummary() {
  const root = document.getElementById("checkout-summary");
  if (!root) return;

  const lines = getCartLines();
  if (!lines.length) {
    window.location.href = "cart.html";
    return;
  }

  root.innerHTML = `
    <h2>Your order</h2>
    <ul class="checkout-lines">
      ${lines
        .map(
          (line) => `
        <li>
          <span>${line.product.name} × ${line.qty}</span>
        </li>
      `
        )
        .join("")}
    </ul>
  `;
}

const WHATSAPP_ORDER_NUMBER = "919168679621";

function buildWhatsAppOrderMessage(form, lines) {
  const firstName = form.firstName.value.trim();
  const lastName = form.lastName.value.trim();
  const email = form.email.value.trim();
  const phone = form.phone.value.trim();
  const address = form.address.value.trim();
  const city = form.city.value.trim();
  const pincode = form.pincode.value.trim();
  const notes = form.notes.value.trim();

  const itemLines = lines
    .map(
      (line) =>
        `- ${line.product.name} (${line.product.sku}) x ${line.qty}`
    )
    .join("\n");

  let message =
    `*New Bharatweld order*\n` +
    `Name: ${firstName} ${lastName}\n` +
    `Phone: ${phone}\n` +
    `Email: ${email}\n` +
    `Address: ${address}\n` +
    `City / PIN: ${city} / ${pincode}\n\n` +
    `Items:\n${itemLines}`;

  if (notes) {
    message += `\nNotes: ${notes}`;
  }

  return message;
}

function initCheckoutForm() {
  const form = document.getElementById("checkout-form");
  if (!form) return;

  renderCheckoutSummary();

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const status = document.getElementById("checkout-status");
    const lines = getCartLines();

    if (!lines.length) {
      status.textContent = "Your cart is empty.";
      status.className = "form-status is-error";
      return;
    }

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    const message = buildWhatsAppOrderMessage(form, lines);
    const url = `https://wa.me/${WHATSAPP_ORDER_NUMBER}?text=${encodeURIComponent(message)}`;

    window.open(url, "_blank", "noopener,noreferrer");

    clearCart();
    form.hidden = true;
    document.getElementById("checkout-success").hidden = false;
    status.textContent = "";
  });
}

function renderShopGrid() {
  const root = document.getElementById("shop-grid");
  if (!root) return;
  root.innerHTML = PRODUCTS.map((p) => renderProductCard(p)).join("");
  bindBuyNowButtons(root);

  const hash = window.location.hash.slice(1);
  if (hash) {
    const el = root.querySelector(`[data-product-id="${hash}"]`);
    if (el) el.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  if (typeof initReveals === "function") initReveals();
}

function renderFeaturedProducts() {
  const root = document.getElementById("featured-products");
  if (!root) return;
  root.innerHTML = PRODUCTS.slice(0, 3)
    .map((p) => renderProductCard(p, { featured: true }))
    .join("");
  bindBuyNowButtons(root);

  if (typeof initReveals === "function") initReveals();
}
