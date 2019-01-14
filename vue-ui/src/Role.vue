<template>
    <div class="container-fluid pt-3">
        <div class="row">
            <div class="col">
                <h1 class="text-center">Roles</h1>
            </div>
        </div>
        <div class="row bg-lite rounded-top" :class="{'rounded-bottom': !selectedRole}">
            <div class="col-lg-2 col-md-4 my-2 text-center text-md-left">
                <button type="button" class="btn btn-primary" @click="showCreateRole">
                    <span data-feather="plus-square"></span>
                    Create Role
                </button>
            </div>
            <div class="col-lg-4 col-md-8 my-2">
                <div class="input-group">
                    <div class="input-group-prepend">
                        <label for="role" class="input-group-text">Role</label>
                    </div>
                    <select class="form-control" v-model="selectedRole" @change="roleChanged" name="role" id="role">
                        <option v-bind:key="r.role" v-for="r in roles" :value="r.role"
                                v-text="r.role.capitalize()"></option>
                    </select>
                </div>
            </div>
            <div class="col-lg-6 d-inline-flex justify-content-lg-end justify-content-center my-2">
                <div class="btn-group">
                    <button type="button" class="btn btn-outline-info" @click="showEditRole">
                        <span data-feather="edit"></span>
                        Edit
                    </button>
                    <button type="button" class="btn btn-outline-danger" @click="showDeleteRole">
                        <span data-feather="delete"></span>
                        Delete
                    </button>
                    <button type="button" class="btn btn-outline-success" @click="showAddUser">
                        <span data-feather="user-plus"></span>
                        Add User
                    </button>
                    <button type="button" class="btn btn-outline-success" @click="showAddPermission">
                        <span data-feather="file-plus"></span>
                        Add Permission
                    </button>
                </div>
            </div>

        </div>
        <div class="row bg-lite rounded-bottom" v-show="selectedRole">
            <div class="col">
                <ul class="nav nav-pills py-3">
                    <li class="nav-item">
                        <a class="nav-link active" data-toggle="pill" href="#pills-permission">
                            Permissions
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" data-toggle="pill" href="#pills-user">
                            Users
                        </a>
                    </li>

                    <li class="navbar-text pl-2" v-if="role">
                        <em>of role <span v-text="selectedRole.capitalize()"></span></em>
                    </li>
                </ul>
            </div>
        </div>
        <div class="row mt-2" v-show="selectedRole">
            <div class="col table-responsive">

                <div class="tab-content">
                    <div class="tab-pane fade show active" id="pills-permission">
                        <table class="table">
                            <thead>
                            <tr>
                                <th>Permission</th>
                                <th>Entity</th>
                                <th>Operation</th>
                                <th></th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-bind:key="permission.id" v-for="(permission, i) in permissions">
                                <td v-text="permission.name.capitalize()"></td>
                                <td v-text="permission.entity.capitalize()"></td>
                                <td v-text="permission.operation.capitalize()"></td>
                                <td>
                                    <button class="btn btn-outline-warning"
                                            @click="showDetouchPermission(permission, i)">Remove
                                    </button>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="tab-pane fade" id="pills-user">
                        <table class="table">
                            <thead>
                            <tr>
                                <th>First Name</th>
                                <th>Last Name</th>
                                <th>Username</th>
                                <th>Email</th>
                                <th></th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-bind:key="user.id" v-for="(user, i) in users">
                                <td v-text="user.first_name"></td>
                                <td v-text="user.last_name"></td>
                                <td v-text="user.username"></td>
                                <td>
                                    <a :href="'mailto:' + user.email" v-text="user.email"></a>
                                </td>
                                <td>
                                    <button class="btn btn-outline-warning" @click="showDetouchUser(user, i)">Remove
                                    </button>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal -->
        <!-- Create Edit Role -->
        <div class="modal fade" id="modal-create-edit" tabindex="-1" role="dialog"
             aria-labelledby="modal-create-edit-label" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header text-white"
                         :class="{'bg-info': role.operation === 'edit', 'bg-primary': role.operation === 'create'}">
                        <h5 class="modal-title">
                            <span v-text="role.operation.capitalize()"></span> Role
                        </h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form class="needs-validation" novalidate id="form-create">
                            <div v-bind:key="key" v-for="(val, key) in role.value" class="form-group row">
                                <label :for="key" class="col-md-4 col-form-label" v-text="key.capitalize()"></label>
                                <div class="col-md-8">
                                    <!--suppress HtmlFormInputWithoutLabel -->
                                    <input type="text" :id="key" class="form-control"
                                           v-model="role.value[key]" required>
                                    <div class="invalid-feedback"></div>
                                </div>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Discard</button>
                        <button type="button" class="btn btn-primary" @click="doOperation"
                                v-text="role.operation.capitalize()"></button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add User -->
        <div class="modal" tabindex="-1" role="dialog" id="modal-add-user">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header text-white bg-success">
                        <h5 class="modal-title">Add Users to role <span v-text="selectedRole.capitalize()"></span></h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form class="needs-validation" novalidate>
                            <!--TODO: validate add users to role-->
                            <div class="form-group row">
                                <label class="col-md-4 col-form-label">Select Users</label>
                                <div class="col-md-8">
                                    <v-select v-model="selectedUsers" multiple label="username" :close-on-select="false"
                                              :options="usersToAdd" placeholder="No User Selected">
                                        <template slot="option" slot-scope="option">
                                        <span v-text="`${option.first_name} ${option.last_name} (${option.username})`">
                                        </span>
                                        </template>
                                    </v-select>
                                </div>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary" data-dismiss="modal">Cancel</button>
                        <button type="button" class="btn btn-outline-success"
                                @click="addSelectedUsersToRole()">Add
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add Permission -->
        <div class="modal" tabindex="-1" role="dialog" id="modal-add-permission">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header text-white bg-success">
                        <h5 class="modal-title">
                            Add Permissions to role <span v-text="selectedRole.capitalize()"></span>
                        </h5>

                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form class="needs-validation" novalidate>
                            {# TODO: validate add permissions to role #}
                            <div class="form-group row">
                                <label class="col-md-4 col-form-label">Select Permission</label>
                                <div class="col-md-8">
                                    <v-select v-model="selectedPermissions" multiple label="name"
                                              :close-on-select="false"
                                              :options="permissionsToAdd" placeholder="No Permission Selected">
                                        <template slot="option" slot-scope="option">
                                        <span v-text="option.name">
                                        </span>
                                        </template>
                                    </v-select>
                                </div>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary" data-dismiss="modal">Cancel</button>
                        <button type="button" class="btn btn-outline-success"
                                @click="addSelectedPermissionsToRole()">Add
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Remove Anything -->
        <div class="modal" tabindex="-1" role="dialog" id="modal-delete">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header bg-danger text-white">
                        <h5 class="modal-title">Delete <span v-text="remove.entity.capitalize()"></span></h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <p>
                            Are your sure to delete
                            <span v-text="remove.entity"></span>
                            '<span v-text="remove.name"></span>'?
                        </p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary" data-dismiss="modal">Nope</button>
                        <button type="button" class="btn btn-outline-danger" @click="doRemove()">Yep</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Vue from "vue";
    import VueSelect from "vue-select";
    import $ from 'jquery';

    Vue.component('v-select', VueSelect);
    const request = window.request;

    export default {
        name: "Role",
        data() {
            return {
                roles: [],          // all roles
                selectedRole: '',   // selected role in the dropdown
                role: {             // placeholder for showing value in create-edit role modal
                    operation: '',
                    value: {}
                },
                permissions: [],    // permissions that this.selectedRole has
                permission: undefined,  // don't know
                users: [],          // users that has role this.selectedRole
                user: undefined,    // don't know
                showUser: false,    // whether to show user of permission list
                remove: {           // placeholder for showing value in delete role/user/permission modal
                    entity: '',
                    name: '',
                    value: {}
                },
                allUsers: [],       // list of all users in system
                allPermissions: [], // list of all permissions in the system
                selectedUsers: [],  // selected users to add role this.selectedRole
                selectedPermissions: [],  // selected permissions to add role this.selectedRole

                removeWithoutConfirmation: false, // TODO: implement bulk remove
            }
        },
        computed: {
            /**
             * Filters out users that already have role this.selectedRole.
             * This is achieved by removing users from this.allUsers those belongs to this.users.
             * @return {array}
             */
            usersToAdd: function () {
                return this.allUsers.filter(user => {
                    for (let i = 0; i < this.users.length; i++) {
                        const roleUser = this.users[i];
                        if (roleUser.id === user.id) {
                            return false;
                        }
                    }
                    return true;
                })
            },
            /**
             * Filters out permissions that already this.selectedRole has.
             * This is achieved by removing permissions from this.allPermissions
             * those belongs to this.permissions.
             * @return {array}
             */
            permissionsToAdd: function () {
                return this.allPermissions.filter(permission => {
                    for (let i = 0; i < this.permissions.length; i++) {
                        const rolePermission = this.permissions[i];
                        if (rolePermission.id === permission.id) {
                            return false;
                        }
                    }
                    return true;
                })
            },
        },
        methods: {
            /**
             * Handle role changed in the dropdown event.
             * Load users who have this.selectedRole
             */
            roleChanged: function () {
                request.get('role/' + this.selectedRole + '/permission').then(r => {
                    this.permissions = r.data;
                });

                request.get('role/' + this.selectedRole + '/user').then(r => {
                    this.users = r.data;
                });
            },
            /**
             * Show modal for creating role
             */
            showCreateRole: function () {
                $('#modal-create-edit form.needs-validation').removeClass('was-validated');

                this.role = {
                    operation: 'create',
                    value: {
                        'role': '',
                    }
                };

                $('#modal-create-edit').modal('show');
            },
            /**
             * Show modal for editing role
             */
            showEditRole: function () {
                $('#modal-create-edit form.needs-validation').removeClass('was-validated');

                this.role = {
                    operation: 'edit',
                    value: {
                        'role': this.selectedRole,
                    }
                };

                $('#modal-create-edit').modal('show');
            },
            doOperation: function () {
                /**
                 * Do create or edit role based on this.role placeholder's value
                 */
                if (this.role.operation === 'create') {
                    this.createRole()
                } else if (this.role.operation === 'edit') {
                    this.editRole()
                } else {
                    console.error("Unknown operation:", this.role.operation)
                }
            },
            /**
             * Create a new role
             */
            createRole: function () {
                const url = 'role/create';
                const params = this.role.value;

                request.post(url, params).then(() => {
                    this.roles.splice(this.roles.length, 0, {
                        role: params.role,
                    });
                    this.selectedRole = this.roles[this.roles.length - 1].role;
                    this.permissions = [];
                    this.users = [];
                    $('#modal-create-edit').modal('hide');
                });
            },
            getIndexOfSelectedRole: function () {
                const search = (reduced, val, i) => {
                    return val.role === this.selectedRole ? reduced + i : reduced;
                };
                return this.roles.reduce(search, 0);
            },
            editRole: function () {
                const url = 'role/' + this.selectedRole;
                const params = this.role.value;

                request.post(url, params).then(() => {
                    const index = this.getIndexOfSelectedRole();
                    this.roles.splice(index, 1, {
                        role: params.role,
                    });
                    this.selectedRole = this.roles[index].role;
                    $('#modal-create-edit').modal('hide');
                });
            },
            doRemove: function () {
                if (this.remove.entity === 'role') {
                    this.removeRole();
                } else if (this.remove.entity === 'user') {
                    this.detouchUser();
                } else if (this.remove.entity === 'permission') {
                    this.detouchPermission();
                } else {
                    console.error("Trying to remove unknow entity " + this.remove.entity);
                }
            },
            showAddUser: function () {
                this.selectedUsers = [];
                $('#modal-add-user').modal('show');
            },
            /**
             * Add selected users to role this.selectedRole
             */
            addSelectedUsersToRole: function () {
                const url = '/role/' + this.selectedRole + '/user';
                for (let i = 0; i < this.selectedUsers.length; i++) {
                    const selectedUser = this.selectedUsers[i];
                    const param = {user_id: selectedUser.id};
                    request.post(url, param).then(() => {
                        // find the user with same id as selectedUser.id
                        const userToAdd = this.allUsers.filter(user => user.id === selectedUser.id)[0];
                        // add it to end of this.users
                        this.users.splice(this.users.length, 0, userToAdd)
                    })
                }

                $('#modal-add-user').modal('hide');
            },
            showAddPermission: function () {
                this.selectedPermissions = [];
                $('#modal-add-permission').modal('show');
            },
            /**
             * Add selected permissions to role this.selectedRole
             */
            addSelectedPermissionsToRole: function () {
                const url = '/role/' + this.selectedRole + '/permission';
                for (let i = 0; i < this.selectedPermissions.length; i++) {
                    const selectedPermission = this.selectedPermissions[i];
                    const param = {permission_id: selectedPermission.id};
                    request.post(url, param).then(() => {
                        // find the permission with same id as selectedPermission.id
                        const permissionToAdd = this.allPermissions
                            .filter(user => user.id === selectedPermission.id)[0];
                        // add it to end of this.permissions
                        this.permissions.splice(this.users.length, 0, permissionToAdd)
                    })
                }

                $('#modal-add-permission').modal('hide');
            },
            showDeleteRole: function () {
                this.remove = {
                    entity: 'role',
                    name: this.selectedRole,
                    value: {
                        role: this.selectedRole
                    }
                };

                $('#modal-delete').modal('show');
            },
            /**
             * Removes a role
             */
            removeRole: function () {
                const url = 'role/' + this.selectedRole;
                request.delete(url).then(() => {
                    let index = this.getIndexOfSelectedRole();
                    this.roles.splice(index, 1);

                    // Update this.selectedRole if there is any role
                    if (this.roles.length > 0) {
                        // if index is same as this.roles.length, this index no longer exists
                        if (index === this.roles.length) {
                            index--;
                        }
                        this.selectedRole = this.roles[index].role;
                        this.roleChanged();
                    }

                    $('#modal-delete').modal('hide');
                });
            },
            showDetouchUser: function (user, i) {
                this.remove = {
                    entity: 'user',
                    name: user.first_name + ' ' + user.last_name,
                    value: user,
                    index: i,
                };
                if (this.removeWithoutConfirmation) {
                    this.detouchUser();
                } else {
                    $('#modal-delete').modal('show');
                }
            },
            /**
             * Detouch a user from this.selectedRole
             */
            detouchUser: function () {
                const url = '/role/' + this.selectedRole + '/user';
                const param = {user_id: this.remove.value.id};
                request.delete(url, {data: param}).then(() => {
                    this.users.splice(this.remove.index, 1);
                });

                $('#modal-delete').modal('hide');
            },
            showDetouchPermission: function (permission, i) {
                this.remove = {
                    entity: 'permission',
                    name: permission.name,
                    value: permission,
                    index: i,
                };
                if (this.removeWithoutConfirmation) {
                    this.detouchPermission();
                } else {
                    $('#modal-delete').modal('show');
                }
            },
            /**
             * Detouch a permission from this.selectedRole
             */
            detouchPermission: function () {
                const url = '/role/' + this.selectedRole + '/permission';
                const param = {permission_id: this.remove.value.id};
                request.delete(url, {data: param}).then(() => {
                    this.permissions.splice(this.remove.index, 1);
                });

                $('#modal-delete').modal('hide');
            },
        },
        /**
         * Loads all the roles at the beginning.
         * After loading roles, loads all users and permissions.
         */
        mounted() {
            request.get('/role/')
                .then(response => {
                    this.roles = response.data;

                    // Load users and permissions after loading roles
                    // so that they don't slow down loading roles
                    request.get('/user/').then(r => {
                        this.allUsers = r.data;
                    });

                    request.get('/permission/').then(r => {
                        this.allPermissions = r.data;
                    });
                })
        }

    }
</script>

<style scoped>
    .nav-pills .nav-link {
        transition: color, background-color 1s;
    }

    .bg-lite {
        background-color: navajowhite;
    }
</style>