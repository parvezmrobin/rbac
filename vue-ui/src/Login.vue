<template>

    <div class="container-fluid" id="vm" v-cloak xmlns:v-on="http://www.w3.org/1999/xhtml">
        <div class="row">
            <div class="col-lg-10 col-xl-8 offset-lg-1 offset-xl-2">
                <h1 class="text-center">Log in</h1>
                <hr class="primary">
            </div>
        </div>

        <div class="card shadow col-lg-10 col-xl-8 offset-lg-1 offset-xl-2">
            <div class="card-body">
                <form novalidate v-on:submit.prevent="login">
                    <div class="form-group row">
                        <label for="username" class="col-md-4 col-form-label">Username</label>
                        <div class="col-md-8">
                            <input type="text" name="username" id="username" class="form-control"
                                   v-model="username" required>
                            <div class="invalid-feedback">Username is required</div>
                        </div>
                    </div>

                    <div class="form-group row">
                        <label for="password" class="col-md-4 col-form-label">Password</label>
                        <div class="col-md-8">
                            <input type="password" name="password" id="password" class="form-control"
                                   v-model="password" required>
                            <div class="invalid-feedback">Password is required</div>
                        </div>
                    </div>

                    <div class="form-check row">
                        <div class="offset-md-4 col-md-8">
                            <div class="mx-md-2 my-3">
                                <input class="form-check-input" type="checkbox" value="" id="remember-me"
                                       v-model="rememberMe">
                                <label class="form-check-label" for="remember-me">
                                    Remember Me
                                </label>
                            </div>
                        </div>
                    </div>

                    <div class="alert alert-danger" v-show="error" role="alert">
                        <span>Username and password doesn't match!</span>
                    </div>

                    <div class="form-group row">
                        <div class="col-md-8 offset-md-4">
                            <input class="btn btn-outline-primary" type="submit" value="Register">
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>

</template>

<script>
    import axios from "axios";
    import $ from 'jquery';

    import {openUrl} from "./assets/site.js";

    const origin = 'http://localhost:5000';
    axios.defaults.baseURL = origin;


    export default {
        name: "Login",
        data() {
            return {
                username: '',
                password: '',
                rememberMe: false,
                error: false,
                user: null,
            }
        },
        methods: {
            login: function () {
                $('form').addClass('was-validated');

                if (!(this.username && this.password)) {
                    return;
                }

                const url = '/api/v1/login';
                const params = {
                    username: this.username,
                    password: this.password,
                };

                axios.post(url, params)
                    .then(r => {
                        const token = r.data.access_token;
                        if (typeof Storage === 'undefined') { // If storage ain't supported, use cookies
                            const d = new Date();
                            // Set expire date to 10 weeks from now
                            d.setTime(d.getTime() + (70 * 24 * 60 * 60 * 1000));
                            const expires = "expires=" + d.toUTCString();
                            document.cookie = "token=" + token + ";" + expires + ";path=/";
                        } else {
                            if (this.rememberMe) {
                                localStorage.setItem("token", token)
                            } else {
                                sessionStorage.setItem("token", token)
                            }
                        }

                        openUrl('/')
                    })
                    .catch(err => {
                        if (err.response.status === 401) {
                            this.error = true;
                        } else {
                            console.error(err);
                        }
                    })
            }
        }
    }
</script>

<style scoped>

</style>