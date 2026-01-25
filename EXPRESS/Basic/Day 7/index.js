const express = require('express');
const authRoutes = require('./routes/auth');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use(authRoutes);
app.get('/', (req, res) => res.json({ service: 'Auth simulation API' }));

app.listen(port, () => console.log(`Express auth API on http://localhost:${port}`));
