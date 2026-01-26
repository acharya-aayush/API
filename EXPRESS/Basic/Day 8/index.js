const express = require('express');
const path = require('path');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, 'public')));
app.get('/status', (req, res) => res.json({ service: 'Static site API', uptime: process.uptime() }));

app.listen(port, () => console.log(`Express static server on http://localhost:${port}`));
