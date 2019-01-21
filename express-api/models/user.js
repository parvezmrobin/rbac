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

function fetchAll(query, params) {
    const connection = getConnection();
    return new Promise(function (resolve, reject) {
        const responseObj = {};
        connection.all(query, params, function cb(err, rows) {
            if (err) {
                responseObj.error = err;
                reject(responseObj);
            } else {
                responseObj.statement = this;
                responseObj.rows = rows;
                resolve(responseObj);
            }
            connection.close();
        });
    });
}

const UserModel = {
    index: async function () {
        const query = "SELECT id, username, email, first_name, last_name, info FROM user";
        const params = [];
        const result = await fetchAll(query, params);
        for (let row of result.rows) {
            row.info = JSON.parse(row.info);
        }
        return result.rows;
    }
};

module.exports = UserModel;