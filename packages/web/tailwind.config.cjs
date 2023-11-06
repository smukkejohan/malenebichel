const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      screens: {
        'hover-hover': {'raw': '(hover: hover)'}
      },
      fontFamily: {
        sans: [
          'Helvetica Neue', // TODO: headline is/was cantarell
          ...defaultTheme.fontFamily.sans,
        ],
        mono:[ 
          ...defaultTheme.fontFamily.mono,
        ],
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
