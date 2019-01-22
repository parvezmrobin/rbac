const express = require('express');
const router = express.Router();
const userModel = require('../models/user');
const helpers = require("../helpers");

/* GET users listing. */
router.get('/', function (req, res) {
    userModel.index()
        .then(rows => {
            res.json(rows);
        })
        .catch(err => {
            helpers.errorHandler(err, req, res);
        });
});

module.exports = router;
