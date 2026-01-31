const express = require('express');
const searchRoutes = require('./routes/search');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use('/search', searchRoutes);
app.get('/', (req, res) => res.json({ service: 'Search and filter API' }));

app.listen(port, () => console.log(`Express search API on http://localhost:${port}`));
