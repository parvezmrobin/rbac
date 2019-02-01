const express = require('express');
const router = express.Router();
const Role = require('../models/role');

router.get('/', function (request, response) {
    Role.connect().then(() => {
        Role.find({}, {users: 0}).then(result => {
            Role.close();
            response.json(result);
        });
    })
});

router.get('/:role', function (request, response, next) {
    Role.connect().then(() => {
        Role.findOne({role: request.params.role}, {users: 0}).then(result => {
            Role.close();
            if (result) {
                response.json(result);
            } else {
                next();
            }
        })
    })
});

router.post('/', function (request, response) {
    Role.connect().then(() => {
        const role = {role: request.body.role, users: []};
        Role.create(role).then((res) => {
            Role.close();
            response.status(201).json(res);
        })
    })
});


module.exports = router;