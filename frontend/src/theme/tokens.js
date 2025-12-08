// src/theme/tokens.js
// Central theme tokens used by all layouts

const THEME_TOKENS = {
  "minimal-light": {
    // Page background + base text color
    bg: "bg-slate-100 text-slate-900",
    // Panels (big containers like cards, shells)
    panel: "bg-white border border-slate-200 shadow-sm",
    // Inner cards
    card: "bg-white border border-slate-200 shadow-md",
    // Text colors
    bodyText: "text-slate-900",
    mutedText: "text-slate-700",
    labelText: "text-slate-800",
    bulletText: "text-slate-800",
  },

  "premium-dark": {
    bg: "bg-slate-950 text-slate-50",
    panel: "bg-slate-950 border border-white/10 shadow-lg shadow-slate-950/60",
    card: "bg-white/5 border border-white/10 shadow-xl shadow-slate-950/60",
    bodyText: "text-slate-50",
    mutedText: "text-slate-400",
    labelText: "text-slate-300",
    bulletText: "text-slate-200",
  },

  "frosted-glass": {
    bg: "bg-slate-900/90 text-slate-50 bg-[radial-gradient(circle_at_top,_rgba(148,163,184,0.35),_transparent_60%)]",
    panel:
      "bg-white/10 border border-white/30 backdrop-blur-2xl shadow-2xl shadow-slate-950/60",
    card:
      "bg-white/12 border border-white/35 backdrop-blur-2xl shadow-xl shadow-slate-950/60",
    bodyText: "text-slate-50",
    mutedText: "text-slate-400",
    labelText: "text-slate-300",
    bulletText: "text-slate-100",
  },
};

export function getThemeTokens(name) {
  return THEME_TOKENS[name] ?? THEME_TOKENS["premium-dark"];
}
