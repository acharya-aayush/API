const express = require('express');
const dashboardRoutes = require('./routes/dashboard');
const app = express();
const port = process.env.PORT || 3000;

app.use('/dashboard', dashboardRoutes);
app.get('/', (req, res) => res.json({ service: 'Admin dashboard API' }));

app.listen(port, () => console.log(`Express dashboard API on http://localhost:${port}`));
