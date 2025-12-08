// src/specExamples/pricingSpec.js
export const pricingSpec = {
  layout: "pricing",
  theme: "premium-dark",
  sections: [
    {
      type: "pricing-grid",
      title: "Pricing that scales with you",
      subtitle:
        "Transparent pricing for modern SaaS teams. Change this text to see different copy.",
      tiers: [
        { id: "starter", name: "Starter", price: 19, interval: "month", popular: false },
        { id: "pro", name: "Pro", price: 49, interval: "month", popular: true },
        { id: "enterprise", name: "Enterprise", price: null, interval: "month", popular: false }
      ]
    }
  ]
};
