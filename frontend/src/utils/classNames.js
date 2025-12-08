/**
 * Utility for conditionally joining class names
 */
export function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}
