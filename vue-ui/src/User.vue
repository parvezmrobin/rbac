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
                        <th>Username</th>
                        <th>Email</th>
                        <th>Edit</th>
                        <th>Delete</th>
                    </tr>
                    </thead>
                    <!--TODO: Implement User edit and delete-->
                    <tr v-for="user in users" v-bind:key="user.id" v-bind:id="user.id">
                        <td title="Click to see roles" @click="loadRoles(user.id, $event)">{{ user.first_name }}</td>
                        <td title="Click to see roles" @click="loadRoles(user.id, $event)">{{ user.last_name }}</td>
                        <td title="Click to see roles" @click="loadRoles(user.id, $event)">{{ user.username }}</td>
                        <td><a :href="'mailto:'+ user.email">{{ user.email }}</a></td>
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
                id: -1,
                placeholder: {},
                operation: '',
                roles: [],
                roleShown: false,
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
            loadRoles: function (user_id, e) {
                if (this.id === user_id) {
                    if (this.roleShown) {
                        this.hideRole();
                        return;
                    }

                    this.renderRole(e);
                    return;
                }

                this.id = user_id;
                const url = 'user/' + user_id + '/role';
                request.get(url).then(r => {
                    this.roles = r.data;
                    this.renderRole(e);
                });
            },
            renderRole: function (e) {
                // generate innerText
                let role_text = this.roles.reduce(
                    (txt, role) => (txt === '') ? role.role : txt + ', ' + role.role,
                    '' // initial value
                );
                let row;
                if (role_text === '') {
                    row =
                        '<tr title="Press Esc to close." data-placement="right" class="bg-warning text-white" id="roles">' +
                        '    <td colspan="6" class="rounded-bottom">No Role Associated</td>' +
                        '</tr>';
                } else {
                    row =
                        `<tr title="Press Esc to close." data-placement="right" class="bg-info text-white" id="roles">
                                <td colspan="6" class="rounded-bottom">${role_text}</td>
                            </tr>`;
                }
                // Remove previously shown roles
                $('[title]').tooltip('hide');
                $('.bg-info').removeClass('bg-info text-white');
                $('#roles').remove();

                // Render
                const $this = $(e.target).parent().children();
                $this.attr('id', 'selected').addClass('bg-info text-white');
                $('#' + this.id).after(row);
                $('tr[title]').tooltip({boundary: 'window'});

                this.roleShown = true;
            },
            hideRole: function () {
                $('.bg-info').removeClass('bg-info text-white');
                $('[title]').tooltip('hide');
                $('#roles').remove();
                this.roleShown = false;
            }
        },
        mounted() {
            request.get('/user/')
                .then(response => {
                    this.users = response.data;
                    this.$nextTick(() => {  // init tooltip when this.users is rendered
                        $('td[title]').tooltip({boundary: 'window'});
                    })
                });

            $(document).keyup(function (e) {
                if (e.key === 'Escape' && this.roleShown) {
                    this.hideRole();
                }
            });
        }
    };
</script>

<style scoped>
    .bg-info a {
        color: var(--warning);
    }

    tr td[title] {
        cursor: pointer;
    }
</style>