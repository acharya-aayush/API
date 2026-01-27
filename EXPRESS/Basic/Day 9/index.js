const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const appName = process.env.APP_NAME || 'Express Config API';
const env = process.env.NODE_ENV || 'development';

app.get('/config', (req, res) => {
  res.json({ appName, env, port });
});
app.get('/', (req, res) => res.json({ message: 'Environment config API', appName }));

app.listen(port, () => console.log(`Express config API running on http://localhost:${port}`));
