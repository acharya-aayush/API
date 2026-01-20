const express = require('express');
const productRoutes = require('./routes/products');
const app = express();
const port = process.env.PORT || 3000;

app.use('/products', productRoutes);

app.get('/', (req, res) => {
  res.json({ message: 'Product catalog API', version: '1.0' });
});

app.listen(port, () => console.log(`Express product API listening on http://localhost:${port}`));
