module.exports = (req, res, next) => {
  const { productId, quantity } = req.body;
  if (!productId || typeof quantity !== 'number') {
    const err = new Error('productId and numeric quantity are required');
    err.status = 400;
    return next(err);
  }
  next();
};
