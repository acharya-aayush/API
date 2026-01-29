const express = require('express');
const uploadRoutes = require('./routes/upload');
const app = express();
const port = process.env.PORT || 3000;

app.use('/upload', uploadRoutes);
app.get('/', (req, res) => res.json({ service: 'File upload API' }));

app.listen(port, () => console.log(`Express upload API on http://localhost:${port}`));
