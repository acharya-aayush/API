const express = require('express');
const router = express.Router();
const verifyApiKey = require('../middleware/auth');

router.post('/login', (req, res) => {
  const { username } = req.body;
  if (!username) {
    return res.status(400).json({ error: 'username is required' });
  }
  res.json({ token: `fake-token-${username}`, user: username });
});

router.get('/profile', verifyApiKey, (req, res) => {
  res.json({ user: req.user, role: 'member', message: 'Protected profile data' });
});

module.exports = router;
