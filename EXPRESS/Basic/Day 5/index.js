const express = require('express');
const todoRoutes = require('./routes/todos');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use('/todos', todoRoutes);
app.get('/', (req, res) => res.json({ service: 'Todo CRUD API' }));

app.listen(port, () => console.log(`Express todo API on http://localhost:${port}`));
