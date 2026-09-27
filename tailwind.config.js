module.exports = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}", "./pages/**/*.{ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        geist: ['Geist', 'ui-sans-serif', 'system-ui'],
      },
      colors: {
        bg: '#071026',
        surface: '#0b1420',
        slate: '#16212b',
        accent: '#00BFA6',
        gold: '#C9A66B',
        positive: '#13B58A',
        warning: '#F59E0B',
        risk: '#E05252'
      },
      backgroundImage: {
        'radial-glow': 'radial-gradient(600px 400px at 10% 10%, rgba(0,191,166,0.12), transparent 20%), radial-gradient(500px 300px at 90% 80%, rgba(201,166,107,0.06), transparent 18%)'
      }
    }
  },
  plugins: []
}
