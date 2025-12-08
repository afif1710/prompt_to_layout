/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"]
      },
      colors: {
        brand: {
          violet: "#7C3AED",
          blue: "#2563EB",
          mint: "#22C55E",
          orange: "#F97316"
        }
      },
      boxShadow: {
        "glass-soft": "0 24px 60px rgba(15,23,42,0.7)"
      },
      borderRadius: {
        "3xl": "1.5rem"
      }
    }
  },
  plugins: []
};
