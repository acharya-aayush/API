const express = require('express');
const validator = require('./middleware/validator');
const errorHandler = require('./middleware/errorHandler');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.post('/orders', validator, (req, res) => {
  res.status(201).json({ order: req.body, status: 'created' });
});
app.use(errorHandler);
app.get('/', (req, res) => res.json({ service: 'Error handling API' }));

app.listen(port, () => console.log(`Express error handling API on http://localhost:${port}`));
