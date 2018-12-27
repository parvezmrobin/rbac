<template>
    <div class="container-fluid pt-3">
        <div class="row">
            <div class="col">
                <h1 class="text-center">
                    Users
                    <button type="button" class="btn btn-primary float-sm-right" @click="showCreate">
                        Create Permission
                    </button>
                </h1>
            </div>
        </div>
        <div class="row">
            <div class="col table-responsive">
                <table class="table table-hover">
                    <thead>
                    <tr>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Username</th>
                        <th>Edit</th>
                        <th>Delete</th>
                    </tr>
                    </thead>
                    <!--TODO: Implement User edit and delete-->
                    <tr v-for="user in users" v-bind:key="user.id" v-bind:id="user.id">
                        <td @click="loadRoles(user.id)">{{ user.first_name }}</td>
                        <td @click="loadRoles(user.id)">{{ user.last_name }}</td>
                        <td @click="loadRoles(user.id)"><a :href="'mailto:'+ user.email">{{ user.email }}</a></td>
                        <td @click="loadRoles(user.id)">{{ user.username }}</td>
                        <td><a href="#">Edit</a></td>
                        <td><a href="#">Delete</a></td>
                    </tr>
                </table>
            </div>
        </div>

        <!-- Modal -->
        <!--Create / Edit Modal-->
        <div class="modal fade" id="modal-create" tabindex="-1" role="dialog"
             aria-labelledby="modal-create-label" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">
                            <span v-text="operation.capitalize()"></span> User
                        </h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form class="needs-validation" novalidate id="form-create">
                            <div v-for="key in Object.keys(placeholder)" v-bind:key="key" class="form-group row">
                                <label for="name" class="col-md-4 col-form-label" v-text="key.capitalize()"></label>
                                <div class="col-md-8">
                                    <input type="text" id="name" class="form-control"
                                           v-model="placeholder[key]" required>
                                    <div class="invalid-feedback"></div>
                                </div>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Discard</button>
                        <button type="button" class="btn btn-primary" v-on:click="doOperation"
                                v-text="operation.capitalize()"></button>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    import $ from "jquery";


    const request = window.request;

    export default {
        name: "User",
        data() {
            return {
                users: [],
                placeholder: {},
                operation: '',
                roles: []
            }
        },
        methods: {
            showCreate: function () {
                this.operation = 'create';
                this.placeholder = {
                    first_name: '',
                    last_name: '',
                    email: '',
                    username: '',
                    password: '',
                };

                $('#modal-create').modal('show');
            },
            doOperation: function () {
                if (this.operation === 'create') {
                    this.create();
                } else if (this.operation === 'edit') {
                    this.edit();
                }
            },
            create: function () {

            },
            edit: function () {

            },
            delete: function () {

            },
            loadRoles: function (user_id) {
                const url = 'user/' + user_id + '/role';
                request.get(url).then(r => {
                    this.roles = r.data;

                    let role_text = this.roles.reduce(
                        (txt, role) => (txt === '') ? role.role : txt + ', ' + role.role,
                        '' // initial value
                    );
                    let row;
                    if (role_text === '') {
                        row =
                            '<tr title="Press Esc to close." class="bg-warning text-white" id="roles">' +
                            '    <td colspan="6" class="rounded-bottom">No Role Associated</td>' +
                            '</tr>';
                    } else {
                        row =
                            `<tr title="Press Esc to close." class="bg-info text-white" id="roles">
                                <td colspan="6" class="rounded-bottom">${role_text}</td>
                            </tr>`;
                    }

                    $('#roles').remove();
                    $('#' + user_id).after(row);
                });
            }
        },
        mounted() {
            request.get('/user/')
                .then(response => {
                    this.users = response.data;
                })
        }
    }

    $(document).keyup(function (e) {
        if (e.key === 'Escape') {
            $('#roles').remove();
        }
    })
</script>

<style scoped>
    tr td:not(:last-child):not(:nth-last-child(2)) {
        cursor: pointer;
    }
</style>