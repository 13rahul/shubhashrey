const PRODUCT_CATEGORIES = [
  {
    id: "mild-steel",
    title: "Welding Electrodes",
    subtitle: "Mild steel & structural grades",
    description: "General fabrication, gates, grills, structural steel, and heavy engineering.",
  },
  {
    id: "stainless",
    title: "Stainless Steel Electrodes",
    subtitle: "Corrosion-resistant grades",
    description: "Food, chemical, pharmaceutical, and architectural stainless fabrication.",
  },
  {
    id: "cutting",
    title: "Cutting & Gouging Electrodes",
    subtitle: "Metal removal — not joining",
    description: "Cutting, piercing, gouging, and defect removal without oxy-fuel equipment.",
  },
  {
    id: "hardfacing",
    title: "Hardfacing Electrodes",
    subtitle: "Wear-resistant overlays",
    description: "Crushers, mining equipment, rails, and heavy wear surfaces.",
  },
];

const PRODUCTS = [
  {
    id: "e-6013",
    sku: "BW-E6013",
    name: "E6013 Welding Electrodes",
    shortName: "E6013",
    category: "Mild Steel Welding Electrodes",
    categoryGroup: "mild-steel",
    tagline: "General-purpose rutile electrode for mild steel fabrication",
    description:
      "Bharatweld E6013 is a rutile-coated general-purpose electrode for mild steel. Smooth arc, easy slag removal, and a clean bead — ideal for gates, grills, sheet metal, and everyday workshop welding across India.",
    price: 1900,
    unit: "",
    image: "assets/products/e-6013.png?v=3",
    current: "AC / DC",
    aws: "E6013",
    coating: "Rutile",
    positions: "All positions (especially flat & horizontal)",
    polarity: "AC or DC either polarity",
    diameters: "2.5 mm, 3.15 mm, 4 mm",
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
    name: "E7018 Welding Electrodes",
    shortName: "E7018",
    category: "Low Hydrogen Structural Electrodes",
    categoryGroup: "mild-steel",
    tagline: "Low-hydrogen electrode for structural and high-strength steel",
    description:
      "Bharatweld E7018 (E7018/E7018-1) is a low-hydrogen electrode for high-strength, crack-resistant welds on structural steel, heavy fabrication, bridges, and pressure-boundary work where ductility matters.",
    price: 3000,
    unit: "",
    image: "assets/products/e-7018.png?v=3",
    current: "AC / DC+",
    aws: "E7018 / E7018-1",
    coating: "Low hydrogen",
    positions: "All positions",
    polarity: "AC or DC+ (DCEP)",
    diameters: "2.5 mm, 3.15 mm, 4 mm",
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
    name: "E308L Stainless Steel Electrodes",
    shortName: "E308L",
    category: "Stainless Steel Welding Electrodes",
    categoryGroup: "stainless",
    tagline: "Stainless electrode for 304/308 grades and corrosion-resistant work",
    description:
      "Bharatweld E308L-16 is designed for 18/8 stainless steels including AISI 304L and 308L. Stable arc, clean bead appearance, and reliable performance for food, chemical, and architectural stainless applications.",
    price: 5000,
    unit: "",
    image: "assets/products/e-308l.png?v=3",
    current: "AC / DC",
    aws: "E308L-16",
    coating: "Extra low carbon stainless",
    positions: "All positions",
    polarity: "AC or DC+",
    diameters: "2.5 mm, 3.15 mm",
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
    name: "Industrial Cutting Electrodes",
    shortName: "Captain Cut",
    category: "Cutting & Gouging Electrodes",
    categoryGroup: "cutting",
    tagline: "Captain-Cut electrodes for metal cutting and gouging",
    description:
      "Bharatweld Captain-Cut cutting electrodes are for metal severing, piercing, gouging, and weld removal on mild steel, cast iron, and non-ferrous metals — a practical tool for maintenance crews and fabrication shops.",
    price: 2500,
    unit: "",
    image: "assets/products/cutting.png?v=3",
    current: "AC / DC",
    aws: "Cutting / gouging type",
    coating: "Special cutting flux",
    positions: "Flat, vertical (cutting applications)",
    polarity: "AC or DC",
    diameters: "4 mm, 5 mm",
    industries: ["Maintenance", "Demolition", "Foundries", "General fabrication"],
    applications: [
      "Metal cutting and severing",
      "Piercing holes",
      "Gouging cracks before re-weld",
      "Removing old welds and rusty bolts",
    ],
  },
  {
    id: "manganese",
    sku: "BW-MN",
    name: "Manganese Hardfacing Electrodes",
    shortName: "Manganese",
    category: "Hardfacing & Wear Resistant Electrodes",
    categoryGroup: "hardfacing",
    tagline: "High-manganese overlay for impact and abrasion resistance",
    description:
      "Bharatweld manganese hardfacing electrodes deposit wear-resistant overlays on crushers, excavator parts, railway components, and mining equipment subject to heavy impact and abrasion in Indian industrial conditions.",
    price: 20000,
    unit: "",
    image: "assets/products/manganese.png?v=3",
    current: "AC / DC",
    aws: "High manganese hardfacing",
    coating: "Hardfacing flux",
    positions: "Flat, horizontal (overlay passes)",
    polarity: "AC or DC+",
    diameters: "3.15 mm, 4 mm",
    industries: ["Mining", "Quarrying", "Railways", "Heavy industry"],
    applications: [
      "Crusher and mill parts",
      "Rail and track overlays",
      "Wear-resistant hardfacing",
      "Mining equipment repair",
    ],
  },
];

const COMPANY_VALUES = [
  {
    title: "Quality",
    text: "Consistent electrode performance, batch after batch — from raw materials to dispatch under ISO 9001:2015 processes.",
  },
  {
    title: "Innovation",
    text: "Continuous improvement in manufacturing methods, packaging, and product development for Indian workshop conditions.",
  },
  {
    title: "Customer Satisfaction",
    text: "Responsive service, clear communication, and electrodes welders can depend on across fabrication and industrial applications.",
  },
  {
    title: "Employee Involvement",
    text: "Skilled teams trained in safe production practices who take pride in every Bharatweld box that leaves Baramati.",
  },
  {
    title: "Responsibility to Society",
    text: "Supporting Indian industry and manufacturing locally under Make in India — Proudly Indian For Indians.",
  },
  {
    title: "Dealers & Vendors as Partners",
    text: "Long-term relationships with distributors and dealers built on reliable supply, fair dealing, and shared growth.",
  },
];

const INDUSTRIES = [
  {
    id: "fabrication",
    title: "General fabrication",
    grades: "E6013 Welding Electrodes",
    summary:
      "Sheet metal, gates, grills, furniture, and light steel structures — easy arc, smooth finish, easy slag removal.",
    image: "assets/products/e-6013.png?v=3",
  },
  {
    id: "structural",
    title: "Structural & heavy engineering",
    grades: "E7018 Welding Electrodes",
    summary:
      "High-tensile steel, bridges, heavy frames, mining equipment, and pressure vessels with low-hydrogen strength.",
    image: "assets/products/e-7018.png?v=3",
  },
  {
    id: "stainless",
    title: "Stainless steel work",
    grades: "E308L Stainless Steel Electrodes",
    summary:
      "Food, chemical, and pharmaceutical equipment plus architectural stainless fabrication with corrosion resistance.",
    image: "assets/products/e-308l.png?v=3",
  },
  {
    id: "cutting",
    title: "Cutting & maintenance",
    grades: "Industrial Cutting Electrodes",
    summary:
      "Cut, pierce, and gouge metal for maintenance, demolition, and repair without oxy-fuel equipment.",
    image: "assets/products/cutting.png?v=3",
  },
  {
    id: "hardfacing",
    title: "Hardfacing & wear protection",
    grades: "Manganese Hardfacing Electrodes",
    summary:
      "Wear-resistant overlays for crushers, rails, and mining equipment in heavy industrial environments.",
    image: "assets/products/manganese.png?v=3",
  },
];

function getProductById(id) {
  return PRODUCTS.find((p) => p.id === id);
}

function getProductsByCategory(categoryId) {
  return PRODUCTS.filter((p) => p.categoryGroup === categoryId);
}

function formatINR(amount) {
  return new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    maximumFractionDigits: 0,
  }).format(amount);
}
