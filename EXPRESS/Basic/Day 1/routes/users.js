const express = require('express');
const router = express.Router();
const users = require('../data/users');

router.get('/', (req, res) => res.json(users));

router.get('/:userId', (req, res) => {
  const user = users.find((item) => item.id === Number(req.params.userId));
  if (!user) return res.status(404).json({ error: 'User not found' });
  res.json(user);
});

module.exports = router;
