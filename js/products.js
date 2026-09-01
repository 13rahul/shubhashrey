const PRODUCTS = [
  {
    id: "e-6013",
    sku: "BW-E6013",
    name: "E-6013",
    category: "General Purpose",
    description:
      "General-purpose rutile electrode for mild steel. Smooth arc, easy slag removal — ideal for fabrication, gates, grills, and repair work.",
    price: 1900,
    unit: "",
    image: "assets/products/e-6013.svg",
    current: "AC / DC",
    industries: ["General fabrication", "Furniture", "Construction", "Repair shops"],
    applications: [
      "Sheet metal welding",
      "Gate and grill fabrication",
      "Light-duty steel structures",
      "Maintenance and repair",
    ],
  },
  {
    id: "e-7018",
    sku: "BW-E7018",
    name: "E-7018",
    category: "Low Hydrogen",
    description:
      "Low-hydrogen electrode (E7018/E7018-1) for high-strength, crack-resistant welds on structural steel and heavy fabrication.",
    price: 3000,
    unit: "",
    image: "assets/products/e-7018.svg",
    current: "AC / DC+",
    industries: ["Heavy construction", "Mining", "Oil and gas", "Shipbuilding"],
    applications: [
      "High-tensile steel",
      "Structural frames and bridges",
      "Heavy machinery parts",
      "Pressure vessels",
    ],
  },
  {
    id: "e-308l",
    sku: "BW-E308L",
    name: "E-308L",
    category: "Stainless Steel",
    description:
      "Stainless steel electrode (E308L-16) for 18/8 grades. Stable arc and clean bead for food, chemical, and architectural stainless work.",
    price: 5000,
    unit: "",
    image: "assets/products/e-308l.svg",
    current: "AC / DC",
    industries: ["Food processing", "Chemical", "Pharmaceutical", "Architectural stainless"],
    applications: [
      "AISI 304L and 308L stainless",
      "Food and chemical equipment",
      "Corrosion-resistant fabrication",
      "General stainless steel work",
    ],
  },
  {
    id: "cutting",
    sku: "BW-CAPTAIN-CUT",
    name: "Cutting Electrodes",
    category: "Cutting & Gouging",
    description:
      "Captain-Cut cutting electrodes for metal cutting, piercing, and gouging — mild steel, cast iron, and non-ferrous metals without oxygen.",
    price: 2500,
    unit: "",
    image: "assets/products/cutting.svg",
    current: "AC / DC",
    industries: ["Maintenance", "Demolition", "Foundries", "General fabrication"],
    applications: [
      "Metal cutting and severing",
      "Piercing holes",
      "Gouging out cracks before re-weld",
      "Removing old welds and rusty bolts",
    ],
  },
  {
    id: "manganese",
    sku: "BW-MN",
    name: "Manganese Electrodes",
    category: "Hardfacing",
    description:
      "High-manganese hardfacing electrodes for wear-resistant overlays on crushers, rails, mining equipment, and heavy wear surfaces.",
    price: 20000,
    unit: "",
    image: "assets/products/manganese.svg",
    current: "AC / DC",
    industries: ["Mining", "Quarrying", "Railways", "Heavy industry"],
    applications: [
      "Crusher and mill parts",
      "Rail and track overlays",
      "Wear-resistant hardfacing",
      "Mining equipment repair",
    ],
  },
];

const INDUSTRIES = [
  {
    id: "fabrication",
    title: "General fabrication",
    grades: "E-6013",
    summary:
      "Sheet metal, gates, grills, furniture, and light steel structures — easy arc, smooth finish, easy slag removal.",
    image: "assets/products/e-6013.svg",
  },
  {
    id: "structural",
    title: "Structural & heavy engineering",
    grades: "E-7018",
    summary:
      "High-tensile steel, bridges, heavy frames, mining equipment, and pressure vessels with low-hydrogen strength.",
    image: "assets/products/e-7018.svg",
  },
  {
    id: "stainless",
    title: "Stainless steel work",
    grades: "E-308L",
    summary:
      "Food, chemical, and pharmaceutical equipment plus architectural stainless fabrication with corrosion resistance.",
    image: "assets/products/e-308l.svg",
  },
  {
    id: "cutting",
    title: "Cutting & maintenance",
    grades: "Captain-Cut",
    summary:
      "Cut, pierce, and gouge metal for maintenance, demolition, and repair without oxy-fuel equipment.",
    image: "assets/products/cutting.svg",
  },
  {
    id: "hardfacing",
    title: "Hardfacing & wear protection",
    grades: "Manganese Electrodes",
    summary:
      "Wear-resistant overlays for crushers, rails, and mining equipment in heavy industrial environments.",
    image: "assets/products/manganese.svg",
  },
];

function getProductById(id) {
  return PRODUCTS.find((p) => p.id === id);
}

function formatINR(amount) {
  return new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    maximumFractionDigits: 0,
  }).format(amount);
}
