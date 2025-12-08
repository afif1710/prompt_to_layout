import React from "react";
import { AnimatePresence, motion } from "framer-motion";

export function Toast({ message, type = "success" }) {
  return (
    <AnimatePresence>
      {message && (
        <motion.div
          className="pointer-events-none fixed inset-x-0 top-4 z-50 flex justify-center px-4"
          initial={{ opacity: 0, y: -12 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -12 }}
        >
          <div
            className={`pointer-events-auto inline-flex items-center gap-3 rounded-2xl border px-4 py-2 text-sm shadow-lg shadow-black/40 backdrop-blur-md ${
              type === "error"
                ? "border-red-500/40 bg-red-500/10 text-red-100"
                : "border-emerald-500/40 bg-emerald-500/10 text-emerald-100"
            }`}
          >
            <span className="h-2 w-2 rounded-full bg-current shadow-[0_0_0_4px_rgba(34,197,94,0.35)]" />
            <span>{message}</span>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
