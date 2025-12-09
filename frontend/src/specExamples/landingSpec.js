// src/specExamples/landingSpec.js
export const landingSpec = {
  layout: "landing",
  theme: "premium-dark",
  sections: [
    {
      type: "hero",
      eyebrow: "AI landing layout",
      title: "Turn a prompt into a landing page layout.",
      subtitle:
        "Describe your product once. Get a themed React/Tailwind layout you can refine and ship.",
      bullets: [
        "Token-based, theme-aware sections",
        "Structured JSON spec for your backend",
        "Layouts only, no full app scaffold yet",
      ],
      primaryCta: { label: "Generate layout" },
      secondaryCta: { label: "Edit JSON spec" },
    },
    {
      type: "features",
      title: "Explain the value in three cards",
      subtitle:
        "Each feature is a simple object in the JSON spec. Add, remove, or reorder freely.",
      items: [
        {
          id: "feature-1",
          name: "Design tokens first",
          description:
            "All colors and states come from a single theme token file.",
        },
        {
          id: "feature-2",
          name: "LLM-friendly schema",
          description:
            "Prompt your model to fill this spec instead of raw JSX.",
        },
        {
          id: "feature-3",
          name: "Multi-layout support",
          description:
            "Switch between dashboard, auth, pricing, settings, and landing.",
        },
      ],
    },
    {
      type: "social-proof",
      label: "Concept layout — swap these with your own brands",
      logos: [
        { id: "acme", name: "ACME" },
        { id: "pulse", name: "PULSE" },
        { id: "zenstack", name: "ZENSTACK" },
        { id: "northwind", name: "NORTHWIND" },
      ],
    },
    {
      type: "cta",
      title: "Ready to use this schema in your backend?",
      subtitle:
        "Send prompts to your model, map responses into this JSON spec, and preview the result live.",
      primaryCta: { label: "Try a prompt" },
      secondaryCta: { label: "View spec shape" },
    },
  ],
};
