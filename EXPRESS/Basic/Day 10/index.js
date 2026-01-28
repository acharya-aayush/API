const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use((req, res, next) => {
  res.setHeader('X-Service-Name', 'Express Headers API');
  res.setHeader('X-API-Version', 'v1');
  next();
});

app.get('/v1/info', (req, res) => res.json({ message: 'API version 1', docs: '/v1/info' }));
app.get('/', (req, res) => res.json({ service: 'Headers and versioning API' }));

app.listen(port, () => console.log(`Express versioned API on http://localhost:${port}`));
