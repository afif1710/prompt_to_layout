import React, { useRef } from "react";
import { ThemeToggle } from "./ThemeToggle";
import { useHotkeys } from "../hooks/useHotkeys";

export function InputPanel({
  description,
  setDescription,
  onGenerate,
  theme,
  setTheme,
  complexity,
  setComplexity,
  setSketchFile,
  loading
}) {
  const fileRef = useRef(null);
  useHotkeys(() => {
    if (!loading) onGenerate();
  });

  return (
    <div className="flex h-full flex-col gap-4 rounded-3xl border border-white/10 bg-white/[0.04] p-4 shadow-glass-soft backdrop-blur-2xl">
      <div>
        <p className="text-[11px] font-medium uppercase tracking-[0.2em] text-slate-400">
          Describe your interface
        </p>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Ex: Create a modern analytics dashboard with sidebar, stat cards, and a chart section."
          className="mt-3 h-32 w-full resize-none rounded-2xl border border-white/10 bg-slate-950/60 px-3 py-2 text-sm text-slate-100 placeholder:text-slate-500 focus:border-brand-violet/60 focus:outline-none"
        />
      </div>

      <div>
        <p className="text-[11px] font-medium uppercase tracking-[0.2em] text-slate-400">
          Sketch upload (optional)
        </p>
        <button
          type="button"
          onClick={() => fileRef.current?.click()}
          className="mt-3 flex w-full flex-col items-center justify-center gap-2 rounded-2xl border border-dashed border-brand-blue/60 bg-slate-950/40 px-4 py-6 text-xs text-slate-300 shadow-inner shadow-black/60 hover:border-brand-violet/80 hover:bg-slate-950/80"
        >
          <span className="rounded-full bg-brand-blue/15 px-3 py-1 text-[10px] uppercase tracking-[0.2em] text-brand-blue">
            Drag & drop or click
          </span>
          <span>Upload a low-fidelity wireframe or hand-drawn sketch.</span>
        </button>
        <input
          ref={fileRef}
          type="file"
          accept="image/*"
          className="hidden"
          onChange={(e) => {
            const file = e.target.files?.[0];
            if (file) setSketchFile(file);
          }}
        />
      </div>

      <ThemeToggle value={theme} onChange={setTheme} />

      <div className="space-y-2">
        <div className="flex items-center justify-between text-xs text-slate-400">
          <span>Component complexity</span>
          <span className="text-slate-200">{complexity}</span>
        </div>
        <input
          type="range"
          min={1}
          max={5}
          value={complexity}
          onChange={(e) => setComplexity(Number(e.target.value))}
          className="w-full accent-brand-violet"
        />
      </div>

      <button
        type="button"
        onClick={onGenerate}
        disabled={loading}
        className={`mt-auto flex items-center justify-center gap-2 rounded-2xl bg-gradient-to-r from-brand-violet via-brand-blue to-brand-mint px-4 py-3 text-sm font-medium text-slate-50 shadow-[0_22px_60px_rgba(37,99,235,0.7)] transition-transform ${
          loading ? "opacity-60 cursor-not-allowed" : "hover:scale-[1.01]"
        }`}
      >
        <span>{loading ? "Generating..." : "Generate UI (Ctrl+Enter)"}</span>
        <span className="h-1.5 w-1.5 rounded-full bg-slate-50" />
      </button>
    </div>
  );
}
