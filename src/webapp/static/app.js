/* ===== UniversesAtWar Unit Browser ===== */
"use strict";

// ------------------------------------------------------------------
// State
// ------------------------------------------------------------------
const state = {
  units: [],         // full units-meta.json array
  filtered: [],      // current filtered result
  cart: [],          // [{id, name, points}] with repeats
  glossary: {},      // rules-glossary.json keyed by rule name
  page: 0,
  pageSize: 60,
};

// Filter state
const filters = {
  name: "",
  types: new Set(["BattleMech", "Vehicle", "Aerospace"]),
  techs: new Set(["Inner Sphere", "Clan"]),
  era: "",
  tonnageMin: 0,
  tonnageMax: 600,
  pointsMin: 0,
  pointsMax: 603,
  showNoPoints: true,
};

// ------------------------------------------------------------------
// DOM refs
// ------------------------------------------------------------------
const $ = id => document.getElementById(id);

const els = {
  grid:          $("results-grid"),
  count:         $("result-count"),
  badge:         $("cart-badge"),
  cartItems:     $("cart-items"),
  cartTotal:     $("cart-total-pts"),
  loadMoreWrap:  $("load-more-wrap"),
  searchName:    $("search-name"),
  filterEra:     $("filter-era"),
  tonnageMin:    $("tonnage-min"),
  tonnageMax:    $("tonnage-max"),
  tonnageRead:   $("tonnage-readout"),
  pointsMin:     $("points-min"),
  pointsMax:     $("points-max"),
  pointsRead:    $("points-readout"),
  showNoPoints:  $("show-no-points"),
  tooltip:       $("rule-tooltip"),
  overlay:       $("overlay"),
  drawerFilters: $("drawer-filters"),
  drawerCart:    $("drawer-cart"),
};

// ------------------------------------------------------------------
// Init
// ------------------------------------------------------------------
(async function init() {
  await Promise.all([loadUnits(), loadGlossary()]);
  applyFilters();
  bindEvents();
})();

async function loadUnits() {
  els.grid.innerHTML = skeletonHTML(12);
  const res = await fetch("/data/units-meta.json");
  state.units = await res.json();
}

async function loadGlossary() {
  try {
    const res = await fetch("/data/rules-glossary.json");
    state.glossary = await res.json();
  } catch (_) {
    state.glossary = {};
  }
}

// ------------------------------------------------------------------
// Filtering
// ------------------------------------------------------------------
function parseTonnage(u) {
  const t = u.tonnage;
  if (t === null || t === undefined) return null;
  const v = parseFloat(String(t).split(/\s+/)[0]);
  return isNaN(v) ? null : v;
}

function applyFilters() {
  const nameQ = filters.name.toLowerCase();

  state.filtered = state.units.filter(u => {
    // Name
    if (nameQ && !(u.name || "").toLowerCase().includes(nameQ)) return false;
    // Type
    if (!filters.types.has(u.unit_type)) return false;
    // Tech
    if (!filters.techs.has(u.tech_base)) return false;
    // Era
    if (filters.era && u.era !== filters.era) return false;
    // Tonnage
    const t = parseTonnage(u);
    if (t !== null && (t < filters.tonnageMin || t > filters.tonnageMax)) return false;
    // Points
    if (u.points === null || u.points === undefined) {
      if (!filters.showNoPoints) return false;
    } else {
      if (u.points < filters.pointsMin || u.points > filters.pointsMax) return false;
    }
    return true;
  });

  state.page = 0;
  renderGrid(true);
  updateCount();
}

// ------------------------------------------------------------------
// Rendering
// ------------------------------------------------------------------
function renderGrid(reset) {
  if (reset) els.grid.innerHTML = "";

  const start = state.page * state.pageSize;
  const end   = start + state.pageSize;
  const slice = state.filtered.slice(start, end);

  const cartIds = new Set(state.cart.map(c => c.id));

  slice.forEach(u => {
    const tile = buildTile(u, cartIds.has(u.id));
    els.grid.appendChild(tile);
  });

  const hasMore = end < state.filtered.length;
  els.loadMoreWrap.hidden = !hasMore;
}

function buildTile(u, inCart) {
  const techClass = u.tech_base === "Clan" ? "tag-tech-clan" : "tag-tech-is";
  const pts = u.points != null ? `<strong>${u.points}</strong> pts` : "— pts";
  const addedClass = inCart ? " added" : "";
  const addedLabel = inCart ? "✓ In Collection" : "+ Add to Collection";
  const inCartClass = inCart ? " in-cart" : "";
  const tonnageStr = u.tonnage != null
    ? Math.round(parseFloat(String(u.tonnage).split(/\s+/)[0])) + "t"
    : "—t";

  const div = document.createElement("div");
  div.className = `unit-tile${inCartClass}`;
  div.dataset.id = u.id;
  div.innerHTML = `
    <div class="tile-name" title="${esc(u.name)}">${esc(u.name)}</div>
    <div class="tile-meta">
      <span class="tag tag-type">${esc(u.unit_type)}</span>
      <span class="tag ${techClass}">${esc(u.tech_base)}</span>
      <span class="tag tag-era">${esc(u.era || "Other")}</span>
    </div>
    <div class="tile-stats">
      <div class="tile-stat">
        <span class="tile-stat-val">${esc(String(u.movement || "—"))}</span>
        <span class="tile-stat-lbl">Move</span>
      </div>
      <div class="tile-stat">
        <span class="tile-stat-val">${esc(u.armor_save || "—")}</span>
        <span class="tile-stat-lbl">Save</span>
      </div>
      <div class="tile-stat">
        <span class="tile-stat-val">${u.wounds ?? "—"}</span>
        <span class="tile-stat-lbl">W</span>
      </div>
      ${u.heat_threshold != null ? `<div class="tile-stat">
        <span class="tile-stat-val">${u.heat_threshold}</span>
        <span class="tile-stat-lbl">HT</span>
      </div>` : ""}
      <div class="tile-stat">
        <span class="tile-stat-val">${tonnageStr}</span>
        <span class="tile-stat-lbl">Tons</span>
      </div>
    </div>
    <div class="tile-points">${pts}</div>
    <div class="tile-footer">
      <button class="btn-add${addedClass}" data-id="${esc(u.id)}">${addedLabel}</button>
    </div>
  `;
  return div;
}

function updateCount() {
  els.count.textContent = `${state.filtered.length.toLocaleString()} units`;
}

function skeletonHTML(n) {
  return Array.from({length: n}, () =>
    `<div class="unit-tile skeleton" style="height:168px"></div>`
  ).join("");
}

// ------------------------------------------------------------------
// Cart
// ------------------------------------------------------------------
function cartAdd(unit) {
  state.cart.push({id: unit.id, name: unit.name, points: unit.points});
  refreshCart();
  refreshTileState(unit.id, true);
}

function cartRemoveAll(id) {
  state.cart = state.cart.filter(c => c.id !== id);
  refreshCart();
  refreshTileState(id, false);
}

function refreshCart() {
  // Badge
  const count = state.cart.length;
  els.badge.textContent = count;
  els.badge.hidden = count === 0;

  // Items
  if (count === 0) {
    els.cartItems.innerHTML = `<p class="cart-empty">No units added yet.</p>`;
    els.cartTotal.textContent = "0 pts";
    return;
  }

  // Group by id for display
  const groups = {};
  state.cart.forEach(c => {
    if (!groups[c.id]) groups[c.id] = {name: c.name, points: c.points, qty: 0};
    groups[c.id].qty++;
  });

  els.cartItems.innerHTML = Object.entries(groups).map(([id, g]) => `
    <div class="cart-item">
      <div class="cart-item-info">
        <div class="cart-item-name">${esc(g.name)}</div>
        <div class="cart-item-meta">${g.points != null ? g.points + " pts ea" : "— pts"}</div>
      </div>
      <span class="cart-qty">${g.qty > 1 ? "×" + g.qty : ""}</span>
      <button class="cart-remove" data-remove="${esc(id)}" aria-label="Remove ${esc(g.name)}">&times;</button>
    </div>
  `).join("");

  const total = state.cart.reduce((s, c) => s + (c.points || 0), 0);
  els.cartTotal.textContent = total.toLocaleString() + " pts";
}

function refreshTileState(id, inCart) {
  document.querySelectorAll(`.btn-add[data-id="${CSS.escape(id)}"]`).forEach(btn => {
    btn.classList.toggle("added", inCart);
    btn.textContent = inCart ? "✓ In Collection" : "+ Add to Collection";
    btn.closest(".unit-tile").classList.toggle("in-cart", inCart);
  });
}

// ------------------------------------------------------------------
// Print
// ------------------------------------------------------------------
async function printCollection() {
  if (state.cart.length === 0) { alert("Add units to your collection first."); return; }
  const ids = state.cart.map(c => c.id);
  const res = await fetch("/api/render-cards", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({unit_ids: ids}),
  });
  if (!res.ok) { alert("Render failed: " + (await res.text())); return; }
  const html = await res.text();
  const win = window.open("", "_blank");
  win.document.write(html);
  win.document.close();
}

// ------------------------------------------------------------------
// Drawers
// ------------------------------------------------------------------
function openDrawer(drawer) {
  drawer.classList.add("open");
  drawer.setAttribute("aria-hidden", "false");
  els.overlay.hidden = false;
}
function closeDrawer(drawer) {
  drawer.classList.remove("open");
  drawer.setAttribute("aria-hidden", "true");
  if (!els.drawerFilters.classList.contains("open") &&
      !els.drawerCart.classList.contains("open")) {
    els.overlay.hidden = true;
  }
}

// ------------------------------------------------------------------
// Rule tooltip
// ------------------------------------------------------------------
let tooltipTimer = null;

function showTooltip(name, anchorEl) {
  const entry = state.glossary[name];
  if (!entry) return;

  clearTimeout(tooltipTimer);
  const tt = els.tooltip;
  tt.hidden = false;

  if (entry.source === "li_rulebook") {
    tt.innerHTML = `<div class="rule-tooltip-name">${esc(name)}</div>
      <div class="rule-tooltip-li">📖 Refer to the Legions Imperialis rulebook.</div>`;
  } else {
    tt.innerHTML = `<div class="rule-tooltip-name">${esc(name)}</div>
      <div>${esc(entry.description || "")}</div>`;
  }

  const rect = anchorEl.getBoundingClientRect();
  const ttW = 280, ttH = 100;
  let left = rect.left;
  let top = rect.bottom + 6;
  if (left + ttW > window.innerWidth - 8) left = window.innerWidth - ttW - 8;
  if (top + ttH > window.innerHeight - 8) top = rect.top - ttH - 6;
  tt.style.left = left + "px";
  tt.style.top = top + "px";
}

function hideTooltip() {
  tooltipTimer = setTimeout(() => { els.tooltip.hidden = true; }, 120);
}

// ------------------------------------------------------------------
// Event bindings
// ------------------------------------------------------------------
function bindEvents() {
  // Filter drawer
  $("btn-filters").addEventListener("click", () => openDrawer(els.drawerFilters));
  $("btn-close-filters").addEventListener("click", () => closeDrawer(els.drawerFilters));

  // Cart drawer
  $("btn-cart").addEventListener("click", () => openDrawer(els.drawerCart));
  $("btn-close-cart").addEventListener("click", () => closeDrawer(els.drawerCart));

  // Overlay closes all drawers
  els.overlay.addEventListener("click", () => {
    closeDrawer(els.drawerFilters);
    closeDrawer(els.drawerCart);
  });

  // Escape closes drawers
  document.addEventListener("keydown", e => {
    if (e.key === "Escape") {
      closeDrawer(els.drawerFilters);
      closeDrawer(els.drawerCart);
    }
  });

  // Print buttons
  $("btn-print").addEventListener("click", printCollection);
  $("btn-print-cart").addEventListener("click", printCollection);

  // Load more
  $("btn-load-more").addEventListener("click", () => {
    state.page++;
    renderGrid(false);
  });

  // --- Filters ---
  let nameDebounce;
  els.searchName.addEventListener("input", () => {
    clearTimeout(nameDebounce);
    nameDebounce = setTimeout(() => {
      filters.name = els.searchName.value;
      applyFilters();
    }, 200);
  });

  document.querySelectorAll("input[name=type]").forEach(cb => {
    cb.addEventListener("change", () => {
      filters.types = new Set(
        [...document.querySelectorAll("input[name=type]:checked")].map(c => c.value)
      );
      applyFilters();
    });
  });

  document.querySelectorAll("input[name=tech]").forEach(cb => {
    cb.addEventListener("change", () => {
      filters.techs = new Set(
        [...document.querySelectorAll("input[name=tech]:checked")].map(c => c.value)
      );
      applyFilters();
    });
  });

  els.filterEra.addEventListener("change", () => {
    filters.era = els.filterEra.value;
    applyFilters();
  });

  function bindRangeSliders(minEl, maxEl, readEl, filterMinKey, filterMaxKey) {
    function update() {
      let lo = parseInt(minEl.value), hi = parseInt(maxEl.value);
      if (lo > hi) { const tmp = lo; lo = hi; hi = tmp; }
      readEl.textContent = `${lo} – ${hi}`;
      filters[filterMinKey] = lo;
      filters[filterMaxKey] = hi;
      applyFilters();
    }
    minEl.addEventListener("input", update);
    maxEl.addEventListener("input", update);
  }
  bindRangeSliders(els.tonnageMin, els.tonnageMax, els.tonnageRead, "tonnageMin", "tonnageMax");
  bindRangeSliders(els.pointsMin, els.pointsMax, els.pointsRead, "pointsMin", "pointsMax");

  els.showNoPoints.addEventListener("change", () => {
    filters.showNoPoints = els.showNoPoints.checked;
    applyFilters();
  });

  $("btn-reset-filters").addEventListener("click", resetFilters);

  // --- Grid delegation (add to cart + tooltips) ---
  els.grid.addEventListener("click", e => {
    const btn = e.target.closest(".btn-add");
    if (!btn) return;
    const id = btn.dataset.id;
    const unit = state.units.find(u => u.id === id);
    if (!unit) return;
    if (btn.classList.contains("added")) {
      // One-at-a-time add: allow adding more by not toggling off here
      // (remove is done from cart drawer)
      cartAdd(unit);
    } else {
      cartAdd(unit);
    }
  });

  // --- Cart delegation (remove) ---
  els.cartItems.addEventListener("click", e => {
    const btn = e.target.closest("[data-remove]");
    if (!btn) return;
    cartRemoveAll(btn.dataset.remove);
  });

  // --- Tooltip delegation ---
  document.addEventListener("mouseover", e => {
    const el = e.target.closest("[data-rule]");
    if (el) showTooltip(el.dataset.rule, el);
  });
  document.addEventListener("mouseout", e => {
    if (e.target.closest("[data-rule]")) hideTooltip();
  });
}

// ------------------------------------------------------------------
// Reset
// ------------------------------------------------------------------
function resetFilters() {
  filters.name = "";
  filters.types = new Set(["BattleMech", "Vehicle", "Aerospace"]);
  filters.techs = new Set(["Inner Sphere", "Clan"]);
  filters.era = "";
  filters.tonnageMin = 0; filters.tonnageMax = 600;
  filters.pointsMin = 0; filters.pointsMax = 603;
  filters.showNoPoints = true;

  els.searchName.value = "";
  document.querySelectorAll("input[name=type]").forEach(c => c.checked = true);
  document.querySelectorAll("input[name=tech]").forEach(c => c.checked = true);
  els.filterEra.value = "";
  els.tonnageMin.value = 0; els.tonnageMax.value = 600;
  els.pointsMin.value = 0; els.pointsMax.value = 603;
  els.tonnageRead.textContent = "0 – 600";
  els.pointsRead.textContent = "0 – 603";
  els.showNoPoints.checked = true;
  applyFilters();
}

// ------------------------------------------------------------------
// Helpers
// ------------------------------------------------------------------
function esc(s) {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}
