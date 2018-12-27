<template>
    <div class="container-fluid" id="vm">
        <div class="row">
            <div class="col-lg-10 col-xl-8 offset-lg-1 offset-xl-2">
                <h1 class="text-center">Register</h1>
                <hr class="info">
            </div>
        </div>
        <div class="row">
            <div class="card shadow col-lg-10 col-xl-8 offset-lg-1 offset-xl-2">
                <div class="card-body">
                    <form novalidate v-on:submit.prevent="register">
                        <div class="form-group row">
                            <label for="first_name" class="col-md-4 col-form-label">First Name</label>
                            <div class="col-md-8">
                                <input type="text" name="first_name" id="first_name" class="form-control"
                                       v-model="firstName" required>
                                <div class="invalid-feedback"></div>
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="last_name" class="col-md-4 col-form-label">Last Name</label>
                            <div class="col-md-8">
                                <input type="text" name="last_name" id="last_name" class="form-control"
                                       v-model="lastName" required>
                                <div class="invalid-feedback"></div>
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="email" class="col-md-4 col-form-label">Email</label>
                            <div class="col-md-8">
                                <input type="email" name="email" id="email" class="form-control"
                                       v-model="email" required>
                                <div class="invalid-feedback"></div>
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="username" class="col-md-4 col-form-label">Username</label>
                            <div class="col-md-8">
                                <input type="text" name="username" id="username" class="form-control"
                                       v-model="username" required>
                                <div class="invalid-feedback"></div>
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="password" class="col-md-4 col-form-label">Password</label>
                            <div class="col-md-8">
                                <input type="password" name="password" id="password" class="form-control"
                                       v-model="password" required>
                                <div class="invalid-feedback"></div>
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="confirm_password" class="col-md-4 col-form-label">Confirm Password</label>
                            <div class="col-md-8">
                                <input type="password" name="confirm_password" id="confirm_password"
                                       class="form-control" v-model="confirmPassword" required>
                                <div class="invalid-feedback"></div>
                            </div>
                        </div>

                        <div class="form-group row">
                            <div class="col-md-8 offset-md-4">
                                <input class="btn btn-outline-success" type="submit" value="Register">
                            </div>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import axios from "axios";
    import $ from 'jquery';
    import {openUrl} from "./assets/site";

    export default {
        name: "Register",
        data() {
            return {
                firstName: '',
                lastName: '',
                email: '',
                username: '',
                password: '',
                confirmPassword: '',
                user: null,
            }
        },
        methods: {
            register: function () {
                const url = '/api/v1/auth/register';
                const params = {
                    first_name: this.firstName,
                    last_name: this.lastName,
                    email: this.email,
                    username: this.username,
                    password: this.password,
                    confirm_password: this.confirmPassword
                };

                axios.post(url, params)
                    .then(r => {
                        if (r.status === 201) {
                            openUrl('login')
                        } else {
                            console.err(r)
                        }
                    })
                    .catch(err => {
                        const errors = err.response.data;
                        for (let field in params) {
                            if (errors.hasOwnProperty(field)) {
                                $(`#${field}`).addClass('is-invalid');
                                $(`#${field}+div`).text(errors[field]);
                            } else {
                                $(`#${field}`).addClass('is-valid').removeClass('is-invalid');
                            }
                        }
                    })
            }
        }

    }
</script>

<style scoped>

</style>