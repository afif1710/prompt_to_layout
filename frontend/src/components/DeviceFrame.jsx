import React from "react";

export function DeviceFrame({ children }) {
  return (
    <div className="relative mx-auto w-full max-w-3xl rounded-[2rem] border border-white/15 bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 p-4 shadow-[0_40px_120px_rgba(15,23,42,0.9)]">
      <div className="mb-3 flex items-center justify-center gap-2">
        <div className="flex gap-1.5">
          <span className="h-2 w-2 rounded-full bg-red-500/80" />
          <span className="h-2 w-2 rounded-full bg-yellow-400/80" />
          <span className="h-2 w-2 rounded-full bg-emerald-400/80" />
        </div>
        <div className="h-1 w-24 rounded-full bg-slate-700/80" />
      </div>
      <div className="overflow-hidden rounded-[1.4rem] border border-white/10 bg-slate-950">
        {children}
      </div>
      <div className="pointer-events-none absolute inset-0 rounded-[2rem] border border-white/5" />
    </div>
  );
}
