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
        // Palette geek développeur
        primary: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          200: '#bae6fd',
          300: '#7dd3fc',
          400: '#38bdf8',
          500: '#0ea5e9',  // Bleu tech
          600: '#0284c7',
          700: '#0369a1',
          800: '#075985',
          900: '#0c4a6e',
        },
        secondary: {
          50: '#fdf4ff',
          100: '#fae8ff',
          200: '#f5d0fe',
          300: '#f0abfc',
          400: '#e879f9',
          500: '#d946ef',  // Violet néon
          600: '#c026d3',
          700: '#a21caf',
          800: '#86198f',
          900: '#701a75',
        },
        terminal: {
          green: '#10b981',  // Vert terminal
          yellow: '#f59e0b', // Jaune warning
          red: '#ef4444',    // Rouge erreur
          blue: '#3b82f6',   // Bleu info
          gray: '#6b7280',   // Gris commande
        },
        matrix: '#00ff41',   // Vert matrix
        github: '#24292e',   // Noir GitHub
        linkedin: '#0a66c2', // Bleu LinkedIn
      },
      fontFamily: {
        'mono': ['"JetBrains Mono"', '"Fira Code"', 'monospace'],
        'sans': ['Inter', 'system-ui', 'sans-serif'],
        'geek': ['"Share Tech Mono"', 'monospace'],
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.5s ease-out',
        'pulse-glow': 'pulseGlow 2s infinite',
        'matrix-fall': 'matrixFall 20s linear infinite',
        'typing': 'typing 3.5s steps(40, end)',
        'blink-caret': 'blinkCaret 0.75s step-end infinite',
        'terminal-blink': 'terminalBlink 1s infinite',
        'hacker-text': 'hackerText 3s steps(30) infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        pulseGlow: {
          '0%, 100%': {
            boxShadow: '0 0 5px theme("colors.primary.500"), 0 0 20px theme("colors.primary.500")'
          },
          '50%': {
            boxShadow: '0 0 20px theme("colors.primary.500"), 0 0 40px theme("colors.primary.500")'
          },
        },
        matrixFall: {
          '0%': { transform: 'translateY(-100%)' },
          '100%': { transform: 'translateY(100vh)' },
        },
        typing: {
          from: { width: '0' },
          to: { width: '100%' },
        },
        blinkCaret: {
          'from, to': { borderColor: 'transparent' },
          '50%': { borderColor: 'theme("colors.terminal.green")' },
        },
        terminalBlink: {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0' },
        },
        hackerText: {
          '0%': {
            textShadow: '0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #0f0, 0 0 35px #0f0, 0 0 40px #0f0, 0 0 50px #0f0, 0 0 75px #0f0'
          },
          '100%': {
            textShadow: '0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #0f0, 0 0 35px #0f0, 0 0 40px #0f0, 0 0 50px #0f0, 0 0 75px #0f0'
          },
        },
      },
      backgroundImage: {
        'code-pattern': "url('data:image/svg+xml,%3Csvg width=\"60\" height=\"60\" xmlns=\"http://www.w3.org/2000/svg\"%3E%3Cg fill=\"none\" fill-rule=\"evenodd\"%3E%3Cg fill=\"%230ea5e9\" fill-opacity=\"0.05\"%3E%3Cpath d=\"M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\"/%3E%3C/g%3E%3C/g%3E%3C/svg%3E')",
        'grid-pattern': "url('data:image/svg+xml,%3Csvg width=\"40\" height=\"40\" xmlns=\"http://www.w3.org/2000/svg\"%3E%3Cdefs%3E%3Cpattern id=\"smallGrid\" width=\"40\" height=\"40\" patternUnits=\"userSpaceOnUse\"%3E%3Cpath d=\"M 40 0 L 0 0 0 40\" fill=\"none\" stroke=\"%233b82f6\" stroke-width=\"0.5\" opacity=\"0.2\"/%3E%3C/pattern%3E%3C/defs%3E%3Crect width=\"100%25\" height=\"100%25\" fill=\"url(%23smallGrid)\"/%3E%3C/svg%3E')",
        'binary-pattern': "url('data:image/svg+xml,%3Csvg width=\"100\" height=\"100\" xmlns=\"http://www.w3.org/2000/svg\"%3E%3Ctext x=\"10\" y=\"20\" font-family=\"monospace\" font-size=\"12\" fill=\"%230ea5e9\" opacity=\"0.1\"%3E101010%3C/text%3E%3Ctext x=\"50\" y=\"40\" font-family=\"monospace\" font-size=\"12\" fill=\"%230ea5e9\" opacity=\"0.1\"%3E010101%3C/text%3E%3Ctext x=\"30\" y=\"70\" font-family=\"monospace\" font-size=\"12\" fill=\"%230ea5e9\" opacity=\"0.1\"%3E110011%3C/text%3E%3C/svg%3E')",
      },
    },
  },
  plugins: [],
}

