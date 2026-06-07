/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        accent: {
          DEFAULT: '#6366f1',   /* Indigo-500 */
          hover:   '#4f46e5',   /* Indigo-600 */
          light:   '#818cf8',   /* Indigo-400 */
        },
        dark: {
          DEFAULT: '#18181b',   /* Zinc-900 */
          800:     '#27272a',
          900:     '#09090b',
        },
        section: {
          DEFAULT: '#312e81',   /* Indigo-900 – remplace l'orange */
        },
        light: {
          DEFAULT: '#fafafa',
          100:     '#ffffff',
        },
      },
      fontFamily: {
        'heading': ['"Open Sans"', 'Helvetica Neue', 'Arial', 'sans-serif'],
        'body':    ['Merriweather', 'Georgia', 'serif'],
        'sans':    ['"Open Sans"', 'Helvetica Neue', 'Arial', 'sans-serif'],
      },
      animation: {
        'fade-in':  'fadeIn 0.6s ease-out forwards',
        'slide-up': 'slideUp 0.5s ease-out forwards',
        'float':    'float 6s ease-in-out infinite',
      },
      keyframes: {
        fadeIn:  {
          '0%':   { opacity: '0', transform: 'translateY(16px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideUp: {
          '0%':   { opacity: '0', transform: 'translateY(24px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%':      { transform: 'translateY(-10px)' },
        },
      },
      borderRadius: {
        'pill': '300px',
      },
    },
  },
  plugins: [],
}
