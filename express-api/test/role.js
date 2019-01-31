process.env.NODE_ENV = 'test';

const Role = require('../models/role');
const app = require('../app');
const chaiHttp = require('chai-http');
const chai = require('chai');

chai.should();
chai.use(chaiHttp);

describe('Role', function () {
    beforeEach(done => {
        Role.connect().then(() => {
            Role.deleteMany({}).then(() => {
                Role.close().then(done);
            });
        });
    });

    describe('GET Role', function () {
        it('should list the roles', function (done) {
            chai.request(app)
                .get('/api/v1/roles')
                .end((err, res) => {
                    res.should.have.status(200);
                    res.body.should.be.a('array');
                    res.body.length.should.be.equals(0);
                    done();
                });
        });
    });
});