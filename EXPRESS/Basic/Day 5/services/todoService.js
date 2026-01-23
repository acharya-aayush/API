const todos = [
  { id: 1, title: 'Draft API plan', completed: false },
];
let nextId = 2;

exports.getAll = () => todos;
exports.create = (payload) => {
  const todo = { id: nextId++, title: payload.title || 'Untitled task', completed: false };
  todos.push(todo);
  return todo;
};
exports.update = (id, payload) => {
  const todo = todos.find((item) => item.id === id);
  if (!todo) return null;
  if (payload.title !== undefined) todo.title = payload.title;
  if (payload.completed !== undefined) todo.completed = payload.completed;
  return todo;
};
exports.remove = (id) => {
  const index = todos.findIndex((item) => item.id === id);
  if (index === -1) return false;
  todos.splice(index, 1);
  return true;
};
