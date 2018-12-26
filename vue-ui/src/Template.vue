<template>
    <div class="container-fluid" id="vm" v-cloak>
        <nav class="navbar navbar-expand-sm navbar-dark bg-dark fixed-top">
            <a class="navbar-brand ml-sm-4 pl-sm-1" href="/">RBAC</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar-rbac"
                    aria-controls="navbar-rbac" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbar-rbac">
                <form class="form-inline w-100">
                    <input class="form-control search w-100 mx-sm-3" type="text" placeholder="Search"
                           aria-label="Search">
                </form>

                <ul class="navbar-nav ml-auto">
                    <template v-if="user">
                        <li class="nav-item text-nowrap pr-2">
                            <span class="navbar-text">Hi <span v-text="user.username"></span>!</span>
                        </li>
                        <li class="nav-item text-nowrap">
                            <a class="nav-link" v-on:click="logout" href="#">Logout</a>
                        </li>
                    </template>
                    <template v-else>
                        <li class="nav-item text-nowrap">
                            <a class="nav-link" href="/auth/login">Login</a>
                        </li>
                        <li class="nav-item text-nowrap">
                            <a class="nav-link" href="#">Register</a>
                        </li>
                    </template>
                </ul>
            </div>
        </nav>

        <div class="container-fluid mt-5 pt-2">
            <div class="row">
                <nav class="col-md-3 col-lg-2 mt-5" id="sidebar">
                    <ul class="nav flex-column">
                        <li class="nav-item">
                            <a class="nav-link" id="nav-dash" href="/">
                                <span data-feather="home"></span>
                                Dashboard
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" id="nav-user" href="/user">
                                <span data-feather="user"></span>
                                Users
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" id="nav-role" href="/role">
                                <span data-feather="briefcase"></span>
                                Roles
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" id="nav-permission" href="/permission">
                                <span data-feather="globe"></span>
                                Permissions
                            </a>
                        </li>
                    </ul>
                </nav>

                <main role="main" class="col-md-9 col-lg-10 px-5">
                    <slot></slot>
                </main>
            </div>
        </div>
    </div>
</template>

<script>
    import boostrap from 'bootstrap';
    import {mixin} from "./assets/site.js";


    export default {
        name: "vm",
        mixins: [mixin]
    }
</script>

<style scoped>
    @import "assets/css/bootstrap.css";
    @import "assets/css/site.css";
</style>