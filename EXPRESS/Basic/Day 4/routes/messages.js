const express = require('express');
const router = express.Router();
const messages = [];

router.post('/', (req, res) => {
  const { text, author } = req.body;
  if (!text || !author) {
    return res.status(400).json({ error: 'text and author are required' });
  }
  const message = { id: messages.length + 1, text, author, createdAt: new Date().toISOString() };
  messages.push(message);
  res.status(201).json(message);
});

router.get('/', (req, res) => res.json(messages));

module.exports = router;
