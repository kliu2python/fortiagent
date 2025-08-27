import { useEffect, useState } from 'react';

export default function Home() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ prompt: 'Hello from Next.js' })
    })
      .then(res => res.json())
      .then(setData)
      .catch(console.error);
  }, []);

  return (
    <div>
      <h1>FortiAgent Frontend</h1>
      <pre>{data ? JSON.stringify(data, null, 2) : 'Loading...'}</pre>
    </div>
  );
}
