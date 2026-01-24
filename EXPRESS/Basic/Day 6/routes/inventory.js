const express = require('express');
const router = express.Router();
const inventory = require('../data/inventory');

router.get('/', (req, res) => {
  const { category } = req.query;
  const items = category ? inventory.filter((item) => item.category.toLowerCase() === category.toLowerCase()) : inventory;
  res.json(items);
});
router.get('/:itemId', (req, res) => {
  const item = inventory.find((entry) => entry.id === Number(req.params.itemId));
  if (!item) return res.status(404).json({ error: 'Item not found' });
  res.json(item);
});
module.exports = router;
