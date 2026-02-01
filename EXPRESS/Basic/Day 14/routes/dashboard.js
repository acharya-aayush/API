const express = require('express');
const router = express.Router();
const metrics = require('../services/dashboardService');

router.get('/metrics', (req, res) => res.json(metrics.getMetrics()));
router.get('/health', (req, res) => res.json({ healthy: true, since: new Date().toISOString() }));

module.exports = router;
