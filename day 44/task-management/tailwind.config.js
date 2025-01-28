/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Template at project level
    "./**/templates/**/*.html", // Template inside apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
