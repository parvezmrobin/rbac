const sqlite3 = require('sqlite3');
const path = require('path');
const join = path.join;

function errorHandler(err) {
    if (err) {
        return console.error(err.message);
    }
}

function getConnection() {
    const path = join(__dirname, '..', 'rbac.sqlite');
    return new sqlite3.Database(path, errorHandler);
}

function fetchOne(query, params) {
    const fetchAll = false;
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

function execute(query, params) {
    return new Promise(function (resolve, reject) {
        const connection = getConnection();
        const callback = function cb(err) {
            connection.close();
            if (err) {
                reject(err);
            } else {
                resolve(this);
            }
        };
        connection.run(query, params, callback);
    });
}

class UserModel {


    static index(withPassword=false) {
        const query = `SELECT id,username,${withPassword? 'password,': ''}email,first_name,last_name,info FROM user`;
        const params = [];
        return fetch(query, params);
    }

    static find(id, withPassword=false) {
        const query = `SELECT id,username,${withPassword? 'password,': ''}email,first_name,last_name,info` +
            ' FROM user WHERE id=?';
        const params = [id];
        return fetchOne(query, params);
    }

    static update(user) {
        const keys = Object.keys(user).map(key => key + '=?').join(',');
        const query = `UPDATE user SET ${keys} WHERE id=?`;
        const params = Object.values(user);
        params.push(user.id);
        console.log(query, params);
        return execute(query, params)
    }

    static where(parameters) {
        let query = "SELECT id, username, email, first_name, last_name, info FROM user";
        const keys = Object.keys(parameters);
        if (keys.length) {
            query += (" WHERE " + keys[0] + "=?");
        }
        for (let i = 1; i < keys.length; i++) {
            query += " & " + keys[i] + "=?";
        }
        const params = Object.values(parameters);

        return fetch(query, params);
    }

    static whereUsername(username) {
        return UserModel.where({username: username})
    }
}

module.exports = UserModel;