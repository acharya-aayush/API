const express = require('express');
const inventoryRoutes = require('./routes/inventory');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use('/inventory', inventoryRoutes);
app.get('/', (req, res) => res.json({ service: 'Inventory API' }));

app.listen(port, () => console.log(`Express inventory API on http://localhost:${port}`));
