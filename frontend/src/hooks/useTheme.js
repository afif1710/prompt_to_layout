import { useState } from "react";

export function useTheme(initial = "premium-dark") {
  const [theme, setTheme] = useState(initial);
  return { theme, setTheme };
}
