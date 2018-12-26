<template>
    <Template>
        <div class="container-fluid pt-3">
        <div class="row">
            <div class="col">
                <h1 class="text-center">
                    Permission
                    <button type="button" class="btn btn-primary float-sm-right" v-on:click="showCreate">
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
                        <th>Name</th>
                        <th>Entity</th>
                        <th>Operation</th>
                        <th>Edit</th>
                        <th>Delete</th>
                    </tr>
                    </thead>
                    <tr v-for="(permission, i) in permissions">
                        <td>{{ permission.name.capitalize() }}</td>
                        <td>{{ permission.entity.capitalize() }}</td>
                        <td>{{ permission.operation.capitalize() }}</td>
                        <td><a href="#" class="btn btn-outline-info" v-on:click="showEdit(i)">Edit</a></td>
                        <td><a href="#" class="btn btn-outline-danger" v-on:click="showRemove(i)">Delete</a></td>
                    </tr>
                </table>
            </div>
        </div>


        <!-- Modal -->
        <div class="modal fade" id="modal-create" tabindex="-1" role="dialog" aria-labelledby="modal-delete-label"
             aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">
                            <span v-text="operation"></span> Permission
                        </h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form class="needs-validation" novalidate id="form-create">
                            <div class="form-group row">
                                <label for="name" class="col-md-4 col-form-label">Name</label>
                                <div class="col-md-8">
                                    <input type="text" id="name" class="form-control"
                                           v-model="permission.name" required>
                                    <div class="invalid-feedback"></div>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="entity" class="col-md-4 col-form-label">Entity</label>
                                <div class="col-md-8">
                                    <input type="text" id="entity" class="form-control"
                                           v-model="permission.entity" required>
                                    <div class="invalid-feedback"></div>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="operation" class="col-md-4 col-form-label">Operation</label>
                                <div class="col-md-8">
                                    <input type="text" id="operation" class="form-control"
                                           v-model="permission.operation" required>
                                    <div class="invalid-feedback"></div>
                                </div>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Discard</button>
                        <button type="button" class="btn btn-primary" v-on:click="doOperation"
                                v-text="operation"></button>
                    </div>
                </div>
            </div>
        </div>

        <div class="modal" tabindex="-1" role="dialog" id="modal-delete">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Delete Permission</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <p>Are your sure to delete permission '<span v-text="permission.name"></span>'?</p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary" data-dismiss="modal">Nope</button>
                        <button type="button" class="btn btn-outline-danger" v-on:click="remove()">Delete</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </Template>
</template>

<script>
    const nav = 'nav-permission';
    const request = window.request;

    import Template from './Template';

    export default {
        name: "Permission",
        components: {Template},
        data() {
            return {
                permissions: [],
                permission: {
                    name: '',
                    entity: '',
                    operation: ''
                },
                i: -1,
                operation: 'Create',
            }
        },
        methods: {
            doOperation: function () {
                if (this.operation === 'Create') {
                    this.createPermission()
                } else {
                    this.editPermission()
                }
            },
            resetPermission: function () {
                this.permission = {
                    name: '',
                    entity: '',
                    operation: ''
                }
            },
            showCreate: function () {
                this.resetPermission();
                this.operation = 'Create';
                $('#modal-create').modal()
            },
            createPermission: function () {
                const url = "permission/create";
                const params = this.permission;

                request.post(url, params)
                    .then(() => {
                        this.permissions.push({
                            name: params.name,
                            entity: params.entity,
                            operation: params.operation
                        });

                        $('input').removeClass(['is-valid', 'is-invalid']);
                        $('#modal-create').modal('hide');
                    })
                    .catch(err => {
                        this.handleError(err.response);
                    })

            },
            showEdit: function (i) {
                this.permission = Object.assign({}, this.permissions[i]);
                this.operation = 'Edit';
                this.i = i;
                $('#modal-create').modal();
            },
            editPermission: function () {
                const url = "permission/" + this.permission.id;
                const params = this.permission;

                request.put(url, params)
                    .then(() => {
                        this.permissions.splice(this.i, 1, this.permission);

                        $('input').removeClass(['is-valid', 'is-invalid']);
                        $('#modal-create').modal('hide');
                    })
                    .catch(err => {
                        this.handleError(err.response);
                    })
            },
            showRemove: function (i) {
                this.permission = Object.assign({}, this.permissions[i]);
                this.i = i;
                $('#modal-delete').modal('show');
            },
            remove: function () {
                const url = "permission/" + this.permission.id;

                request.delete(url)
                    .then(() => {
                        this.permissions.splice(this.i, 1);

                        $('#modal-delete').modal('hide');
                    })
                    .catch(err => {
                        console.err(err);
                    })
            },
            handleError: function (response) {
                const errors = response.data;
                for (let key in this.permission) {
                    if (this.permission.hasOwnProperty(key)) {
                        if (errors.hasOwnProperty(key)) {
                            $(`#${key}`).removeClass('is-valid').addClass('is-invalid');
                            $(`#${key}+div`).text(errors[key])
                        } else {
                            $(`#${key}`).removeClass('is-invalid').addClass('is-valid');
                        }
                    }
                }
            }
        },
        mounted() {
            request.get('permission')
                .then(response => {
                    this.permissions = response.data;
                })
        }
    }
</script>

<style scoped>

</style>