module.exports = (req, res, next) => {
  const token = req.headers['x-api-key'];
  if (!token || !token.startsWith('fake-token-')) {
    return res.status(401).json({ error: 'Invalid or missing API key' });
  }
  req.user = token.replace('fake-token-', '');
  next();
};
