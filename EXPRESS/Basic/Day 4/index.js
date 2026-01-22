const express = require('express');
const messageRoutes = require('./routes/messages');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use('/messages', messageRoutes);
app.get('/', (req, res) => res.json({ service: 'Message board API' }));

app.listen(port, () => console.log(`Express message board on http://localhost:${port}`));
