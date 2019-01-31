const express = require('express');
const router = express.Router();
const Role = require('../models/role');

router.get('/', function (request, response) {
    Role.connect().then(() => {
        Role.find({}).then(result => {
            Role.close();
            response.json(result);
        });
    })
});

router.post('/', function (request, response) {
   const role = request.params.role;
});

module.exports = router;