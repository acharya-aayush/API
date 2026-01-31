const express = require('express');
const router = express.Router();
const items = require('../data/searchItems');

router.post('/', (req, res) => {
  const { query, tags } = req.body;
  let results = items;
  if (query) {
    const term = query.toLowerCase();
    results = results.filter((item) => item.title.toLowerCase().includes(term) || item.description.toLowerCase().includes(term));
  }
  if (tags && Array.isArray(tags) && tags.length) {
    results = results.filter((item) => tags.every((tag) => item.tags.includes(tag)));
  }
  res.json(results);
});

module.exports = router;
