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
                    res.body.should.be.an('array');
                    res.body.length.should.be.equals(0);
                    done();
                });
        });
    });

    describe('POST Role', function () {
        it('should create a role', function (done) {
            chai.request(app)
                .post('/api/v1/roles')
                .send({role: 'admin'})
                .end((err, res) => {
                    res.status.should.be.equals(201);
                    res.body.should.be.an('object');
                    res.body._id.should.be.a('string');
                    res.body.role.should.be.a('string');
                    res.body.users.should.be.an('array');
                    res.body.users.should.have.length(0);

                    chai.request(app)
                        .get('/api/v1/roles')
                        .end((err, res) => {
                            res.should.have.status(200);
                            res.body.should.be.an('array');
                            res.body.length.should.be.equals(1);
                            res.body[0].should.be.include({role: 'admin'});
                            res.body[0].should.not.include({role: 'writer'});
                            res.body[0].should.not.have.property('users');
                            done();
                        });
                });
        });
    });
});