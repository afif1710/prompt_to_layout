// src/theme/tokens.js
// Central theme tokens used by all layouts

const THEME_TOKENS = {
  "minimal-light": {
    // Page background + base text
    page: "bg-slate-100 text-slate-900",

    // Surfaces
    surface: "bg-white border border-slate-200 shadow-sm",
    card: "bg-white border border-slate-200 shadow-md",

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
