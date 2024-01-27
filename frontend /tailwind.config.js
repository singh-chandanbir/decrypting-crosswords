/** @type {import('tailwindcss').Config} */



module.exports = {
  content: [

    "./templates/*.html",
    "./node_modules/flowbite/**/*.js"

  ],
  theme: {
    extend: {
      colors: {
        'blue': '#5A9EE1',
  
      },
      fontFamily: {
        'Gliker': ["gliker-bold", "sans-serif"],

      },
    plugins: [
        require("flowbite/plugin")
      ],
    }

  }}