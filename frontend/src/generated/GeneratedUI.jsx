import React from "react";
import { motion } from "framer-motion";

export default function GeneratedUI() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-slate-50 p-8">
      <div className="mx-auto max-w-5xl rounded-3xl border border-white/10 bg-white/5 shadow-xl shadow-slate-950/60 backdrop-blur-xl">
        <div className="border-b border-white/10 px-8 py-6 flex items-center justify-between">
          <div>
            <p className="text-xs uppercase tracking-[0.2em] text-slate-400">AI Generated</p>
            <h1 className="mt-1 text-xl font-semibold">Premium Dashboard</h1>
          </div>
          <div className="flex gap-2">
            <div className="h-2 w-2 rounded-full bg-emerald-400" />
            <span className="text-xs text-slate-400">Live</span>
          </div>
        </div>
        <div className="grid gap-6 px-8 py-6 md:grid-cols-[260px,1fr]">
          <aside className="rounded-2xl border border-white/10 bg-gradient-to-b from-white/5 to-white/0 p-4">
            <p className="text-xs font-medium uppercase text-slate-400">Navigation</p>
            <ul className="mt-4 space-y-1 text-sm">
              <li className="flex items-center justify-between rounded-xl bg-white/10 px-3 py-2">
                <span>Overview</span>
              </li>
              <li className="rounded-xl px-3 py-2 text-slate-300 hover:bg-white/5">Analytics</li>
              <li className="rounded-xl px-3 py-2 text-slate-300 hover:bg-white/5">Settings</li>
            </ul>
          </aside>
          <main className="space-y-6">
            <section className="grid gap-4 md:grid-cols-3">
              {["Users","Revenue","Rate"].map((label, idx) => (
                <motion.div
                  key={label}
                  className="rounded-2xl border border-white/10 bg-white/5 p-4"
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.05 * idx }}
                >
                  <p className="text-xs text-slate-400">{label}</p>
                  <p className="mt-2 text-2xl font-semibold">
                    {idx === 0 ? "1.2k" : idx === 1 ? "$42k" : "4.7%"}
                  </p>
                </motion.div>
              ))}
            </section>
          </main>
        </div>
      </div>
    </div>
  );
}
