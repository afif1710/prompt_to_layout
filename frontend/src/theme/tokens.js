// src/theme/tokens.js
// Central theme tokens used by all layouts

const THEME_TOKENS = {
  "minimal-light": {
    // Page background + base text
    page: "bg-slate-100/90 text-slate-900",

    // Surfaces
    surface: "bg-white border border-slate-200 shadow-sm",
    card: "bg-white/90 border border-slate-200 shadow-md",

    // Text
    text: {
      primary: "text-slate-900",
      secondary: "text-slate-800",
      muted: "text-slate-700",
      label: "text-slate-800",
      bullet: "text-slate-800",
    },

    // Buttons
    button: {
      primary: "bg-emerald-500 text-slate-950 hover:bg-emerald-600",
      secondary: "bg-slate-900 text-slate-50 hover:bg-slate-800",
      ghost:
        "border border-slate-300 text-slate-800 hover:bg-slate-100",
    },

    // Navigation (tabs, sidebars)
    nav: {
      active: "bg-emerald-100 text-slate-900",
      inactive: "text-slate-800 hover:bg-slate-100",
    },

    // Borders (if you need them separately)
    border: {
      subtle: "border-slate-200",
      strong: "border-slate-400",
    },
  },

  "soft-pastel": {
    // Page background + base text
    page: "bg-slate-50 text-slate-900",

    // Surfaces
    surface:
      "bg-white/80 border border-slate-200 shadow-sm backdrop-blur-xl",
    card:
      "bg-white/90 border border-slate-200 shadow-md backdrop-blur-xl",

    // Text
    text: {
      primary: "text-slate-900",
      secondary: "text-slate-800",
      // still need enough contrast on near‑white surfaces
      muted: "text-slate-600",
      label: "text-slate-700",
      bullet: "text-slate-800",
    },

    // Buttons
    button: {
      // soft indigo/emerald accent; dark text for legibility
      primary:
        "bg-indigo-400 text-slate-950 hover:bg-indigo-300",
      secondary:
        "bg-emerald-300 text-slate-900 hover:bg-emerald-200",
      ghost:
        "border border-slate-300 text-slate-800 hover:bg-slate-100/80",
    },

    // Navigation
    nav: {
      active: "bg-indigo-100 text-slate-900",
      inactive: "text-slate-700 hover:bg-slate-100/80",
    },

    border: {
      subtle: "border-slate-200",
      strong: "border-slate-400",
    },
  },

  "premium-dark": {
    page: "bg-slate-950 text-slate-50",
    surface: "bg-slate-950 border border-white/10 shadow-lg shadow-slate-950/60",
    card: "bg-white/5 border border-white/10 shadow-xl shadow-slate-950/60",

    text: {
      primary: "text-slate-50",
      secondary: "text-slate-100",
      muted: "text-slate-400",
      label: "text-slate-300",
      bullet: "text-slate-200",
    },

    button: {
      primary: "bg-emerald-500 text-slate-950 hover:bg-emerald-400",
      secondary: "bg-white/10 text-slate-50 hover:bg-white/15",
      ghost:
        "border border-white/20 text-slate-200 hover:bg-white/10",
    },

    nav: {
      active: "bg-emerald-500/15 text-slate-50",
      inactive: "text-slate-300 hover:bg-white/5",
    },

    border: {
      subtle: "border-white/10",
      strong: "border-white/30",
    },
  },

  "high-contrast": {
  // Very dark page; strong global contrast
  page: "bg-black text-white",

  // Surfaces stay dark so white text tokens always work
  surface:
    "bg-neutral-950 border border-white shadow-[0_0_0_1px_rgba(255,255,255,0.6)]",
  card:
    "bg-neutral-900 border border-white shadow-[0_0_0_1px_rgba(255,255,255,0.8)]",

  text: {
    // All text is light-on-dark; no white cards
    primary: "text-white",
    secondary: "text-neutral-100",
    muted: "text-neutral-300",
    label: "text-neutral-200",
    bullet: "text-neutral-100",
  },

  button: {
    // Primary: inverted for emphasis
    primary:
      "bg-white text-black hover:bg-neutral-100",
    // Secondary: strong outline
    secondary:
      "bg-neutral-950 text-white border border-white hover:bg-neutral-900",
    // Ghost: minimalist but visible
    ghost:
      "border border-white text-white hover:bg-white/10",
  },

  nav: {
    // Active tab is clearly boxed and inverted
    active: "bg-white text-black",
    // Inactive keeps high contrast but slightly dimmer
    inactive: "text-neutral-200 hover:bg-white/10",
  },

  border: {
    subtle: "border-white/70",
    strong: "border-white",
  },
},


  "frosted-glass": {
    page:
      "bg-slate-900/90 text-slate-50 bg-[radial-gradient(circle_at_top,_rgba(148,163,184,0.35),_transparent_60%)]",
    surface:
      "bg-white/10 border border-white/30 backdrop-blur-2xl shadow-2xl shadow-slate-950/60",
    card:
      "bg-white/12 border border-white/35 backdrop-blur-2xl shadow-xl shadow-slate-950/60",

    text: {
      primary: "text-slate-50",
      secondary: "text-slate-100",
      muted: "text-slate-400",
      label: "text-slate-300",
      bullet: "text-slate-100",
    },

    button: {
      primary: "bg-emerald-400 text-slate-950 hover:bg-emerald-300",
      secondary: "bg-white/15 text-slate-50 hover:bg-white/25",
      ghost:
        "border border-white/30 text-slate-50 hover:bg-white/10",
    },

    nav: {
      active: "bg-emerald-400/25 text-slate-50",
      inactive: "text-slate-200 hover:bg-white/5",
    },

    border: {
      subtle: "border-white/25",
      strong: "border-white/50",
    },
  },
};

export function getThemeTokens(name) {
  return THEME_TOKENS[name] ?? THEME_TOKENS["premium-dark"];
}
