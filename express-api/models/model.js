const mongoose = require('mongoose');

const model = {
    statics: {
        connect: function () {
            return mongoose.connect(process.env.CONN_URL, {useNewUrlParser: true});
        },
        close: function () {
            mongoose.connection.close();
        }
    }
};

module.exports = model;