const express = require('express');
const router = express.Router();
const UserModel = require('../models/user');

/* GET users listing. */
router.get('/', function (req, res, next) {
    UserModel.index()
        .then(users => {
            res.json(users);
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

router.post('/:id', function (req, res, next) {
    UserModel.find(req.params.id).then(user => {
        user.update(req.body).then(result => {
            res.status(200).json({status: 'updated'});
        });
    }).catch(next);
});

module.exports = router;
