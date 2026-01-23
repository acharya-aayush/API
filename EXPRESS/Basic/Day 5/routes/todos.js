const express = require('express');
const router = express.Router();
const todoService = require('../services/todoService');

router.get('/', (req, res) => res.json(todoService.getAll()));
router.post('/', (req, res) => res.status(201).json(todoService.create(req.body)));
router.put('/:todoId', (req, res) => {
  const updated = todoService.update(Number(req.params.todoId), req.body);
  if (!updated) return res.status(404).json({ error: 'Todo not found' });
  res.json(updated);
});
router.delete('/:todoId', (req, res) => {
  const deleted = todoService.remove(Number(req.params.todoId));
  if (!deleted) return res.status(404).json({ error: 'Todo not found' });
  res.json({ status: 'deleted' });
});

module.exports = router;
