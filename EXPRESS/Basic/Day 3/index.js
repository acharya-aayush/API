const express = require('express');
const logger = require('./middleware/logger');
const app = express();
const port = process.env.PORT || 3000;

app.use(logger);
app.get('/health', (req, res) => res.json({ status: 'ok', uptime: process.uptime() }));
app.get('/', (req, res) => res.json({ message: 'Express middleware health API' }));

app.listen(port, () => console.log(`Express health app on http://localhost:${port}`));
