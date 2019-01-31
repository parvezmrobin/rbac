const mongoose = require('mongoose');
const model = require("./model");

const schema = new mongoose.Schema({
    role: String,
    users: Array,
});

schema.statics = model.statics;

const Role = mongoose.model('Role', schema);

module.exports = Role;