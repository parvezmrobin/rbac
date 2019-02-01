process.env.NODE_ENV = 'test';

const Role = require('../models/role');
const app = require('../app');
const chaiHttp = require('chai-http');
const chai = require('chai');

chai.should();
chai.use(chaiHttp);

describe('Role', function () {
    before(done => {
        Role.connect().then(() => {
            Role.deleteMany({}).then(() => {
                Role.close().then(done);
            });
        });
    });

    describe('GET Role', function () {
        it('should get an empty list of roles', function (done) {
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

                    done();
                });
        });

        it('should check if a role is created', function (done) {
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

        it('should access newly created role', function (done) {
            chai.request(app)
                .get('/api/v1/roles/admin')
                .end((err, res) => {
                    res.should.have.status(200);
                    res.body.should.be.an('object');
                    res.body.should.have.all.keys(['_id', 'role', '__v']);
                    res.body.should.be.include({role: 'admin'});
                    res.body.should.not.include({role: 'writer'});
                    res.body.should.not.have.property('users');

                    done();
                });
        });

        it('should receive error while accessing a non existing role', function (done) {
            chai.request(app)
                .get('/api/v1/roles/writer')
                .end((err, res) => {
                    res.should.have.status(404);
                    res.body.message.should.be.equals('Not Found');
                    res.body.error.should.be.an('object').that.is.empty;

                    done();
                });
        });
    });

    describe('PUT Role', function () {
        it('should edit role `admin` to `administrator`', function (done) {
            chai.request(app)
                .put('/api/v1/roles/admin')
                .send({role: 'administrator'})
                .end(((err, res) => {
                    res.should.have.status(200);
                    res.body.should.be.empty;

                    done();
                }));

        });

        it('should not edit a non-existing role', function (done) {
            chai.request(app)
                .put('/api/v1/roles/writer')
                .send({role: 'administrator'})
                .end((err, res) => {
                    res.should.have.status(404);
                    res.body.message.should.be.equals('Not Found');
                    res.body.error.should.be.an('object').that.is.empty;

                    done();
                });
        });
    });

    describe('DELETE Role', function () {
        it('should not delete a non-existing role', function (done) {
            chai.request(app)
                .put('/api/v1/roles/writer')
                .end((err, res) => {
                    res.should.have.status(404);
                    res.body.message.should.be.equals('Not Found');
                    res.body.error.should.be.an('object').that.is.empty;

                    done();
                });
        });

        it('should delete role `administrator`', function (done) {
            chai.request(app)
                .put('/api/v1/roles/administrator')
                .end((err, res) => {
                    res.should.have.status(200);
                    res.body.should.be.an('object').that.is.empty;

                    done();
                });
        });

        it('should not delete an already-deleted role', function (done) {
            chai.request(app)
                .put('/api/v1/roles/administrator')
                .end((err, res) => {
                    res.should.have.status(404);
                    res.body.message.should.be.equals('Not Found');
                    res.body.error.should.be.an('object').that.is.empty;

                    done();
                });
        });
    })
});