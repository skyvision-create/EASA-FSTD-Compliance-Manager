import { useState, useEffect } from 'react'

function App() {
  const [health, setHealth] = useState<string>('checking...')
  const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000'

  useEffect(() => {
    fetch(`${apiUrl}/health`)
      .then(res => res.json())
      .then(data => setHealth(data.status))
      .catch(err => setHealth('error: ' + err.message))
  }, [apiUrl])

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>EASA FSTD Compliance Manager</h1>
      <div style={{ marginTop: '2rem' }}>
        <h2>API Health: {health}</h2>
        <p>API URL: {apiUrl}</p>
      </div>
      <div style={{ marginTop: '2rem', padding: '1rem', backgroundColor: '#f0f0f0' }}>
        <h3>Getting Started</h3>
        <ol>
          <li>Configure VITE_API_URL environment variable</li>
          <li>Build: npm run build</li>
          <li>Deploy to Railway or your hosting provider</li>
        </ol>
      </div>
    </div>
  )
}

export default App
