// src/api/routes.js

const express = require('express');
const router = express.Router();

// Define API routes here (example)
router.get('/servers', (req, res) => {
  res.json({ message: 'List of servers' });
});

module.exports = router;
