const express = require('express');
const router = express.Router();
const userModel =  require('../models/user');

/* GET users listing. */
router.get('/', async function(req, res) {
  const result = await userModel.index();
  console.log(result.rows);
  res.json(result);
});

module.exports = router;
