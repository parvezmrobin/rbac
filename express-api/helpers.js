const helpers = {
    errorHandler: (err, req, res) => {
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
    }
};

module.exports = helpers;