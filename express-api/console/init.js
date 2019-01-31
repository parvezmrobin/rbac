const Role = require('../models/role');
const join = require('path').join;
require('dotenv').config({path: join(__dirname, '..', '.env')});

// console.log(Role);
roles = [
    {role: 'admin'},
    {role: 'user'},
    {role: 'guest'},
];

Role.connect().then(() => {
    Role.deleteMany({}).then(res => {
        console.error("DELETED");
        console.log(res);

        let count = roles.length;
        for (const role of roles) {
            Role.create(role).then(res => {
                console.log("SAVED", res);

                if (--count === 0) {
                    Role.close();
                }
            });
        }

    });
});