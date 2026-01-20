const express = require('express');
const router = express.Router();
const products = require('../data/products');

router.get('/', (req, res) => {
  const { category, search } = req.query;
  let results = products;
  if (category) {
    results = results.filter((item) => item.category.toLowerCase() === category.toLowerCase());
  }
  if (search) {
    const term = search.toLowerCase();
    results = results.filter((item) => item.name.toLowerCase().includes(term) || item.description.toLowerCase().includes(term));
  }
  res.json(results);
});

router.get('/:productId', (req, res) => {
  const product = products.find((item) => item.id === Number(req.params.productId));
  if (!product) return res.status(404).json({ error: 'Product not found' });
  res.json(product);
});

module.exports = router;
