const sqlite3 = require('sqlite3');
const path = require('path');
const join = path.join;

function errorHandler(err) {
    if (err) {
        return console.error(err.message);
    }
}

function getConnection() {
    const path = join(__dirname, '..', '..', 'rbac.sqlite');
    return new sqlite3.Database(path, errorHandler);
}

function fetchOne(query, params) {
    const fetchAll = true;
    return fetch(query, params, fetchAll);
}

function fetch(query, params, all = true) {
    return new Promise(function (resolve, reject) {
        const connection = getConnection();
        const callback = function cb(err, rows) {
            connection.close();
            if (err) {
                reject(err);
            } else {
                resolve(rows);
            }
        };
        if (all) {
            connection.all(query, params, callback);
        } else {
            connection.get(query, params, callback);
        }
    });
}

const UserModel = {
    index: function () {
        const query = "SELECT id, username, email, first_name, last_name, info FROM user";
        const params = [];
        return fetch(query, params).then(rows => {
            for (let row of rows) {
                row.info = JSON.parse(row.info);
            }

            return rows;
        })
    }
};

module.exports = UserModel;