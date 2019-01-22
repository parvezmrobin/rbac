const express = require('express');
const router = express.Router();
const UserModel = require('../models/user');

/* GET users listing. */
router.get('/', function (req, res, next) {
    UserModel.index()
        .then(rows => {
            res.json(rows);
        })
        .catch(next);
});

router.get('/:id', function (req, res, next) {
    UserModel.find(req.params.id)
        .then(row => {
            res.json(row);
        })
        .catch(next);
});

module.exports = router;
