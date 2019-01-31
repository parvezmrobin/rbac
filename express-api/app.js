const createError = require('http-errors');
const express = require('express');
require('dotenv').config();
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');

const indexRouter = require('./routes/index');
const rolesRouter = require('./routes/roles');

const app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/api/v1/', indexRouter);
app.use('/api/v1/roles', rolesRouter);

// catch 404 and forward to error handler
app.use(function (req, res, next) {
    next(createError(404));
});

// error handler
// noinspection JSUnusedLocalSymbols
app.use(function (err, req, res, next) {
    // generate the error
    res.status(err.status || 500);
    const error = {};

    Object.getOwnPropertyNames(err).forEach(function (key) {
        error[key] = err[key];
    });

    error.stack = error.stack.split("\n").map(str => str.trim());

    // only providing error in development
    res.json({
        message: error.message,
        error: req.app.get('env') === 'development' ? error : {}
    });
});

module.exports = app;
