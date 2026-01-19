const express = require('express');
const userRoutes = require('./routes/users');
const app = express();
const port = process.env.PORT || 3000;

app.use('/users', userRoutes);

app.get('/', (req, res) => {
  res.json({ service: 'User profile service', status: 'ready' });
});

app.listen(port, () => {
  console.log(`Express app running on http://localhost:${port}`);
});
