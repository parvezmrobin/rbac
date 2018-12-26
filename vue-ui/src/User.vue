<template>
    <Template>
        <div class="container-fluid">
            <div class="row">
                <div class="col">
                    <h1 class="text-center">Users</h1>
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
                        <tr v-for="user in users">
                            <td>{{ user.first_name }}</td>
                            <td>{{ user.last_name }}</td>
                            <td><a :href="'mailto:'+ user.email">{{ user.email }}</a></td>
                            <td>{{ user.username }}</td>
                            <td><a href="#">Edit</a></td>
                            <td><a href="#">Delete</a></td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
    </Template>
</template>

<script>
    import Template from "./Template.vue";


    const request = window.request;
    const nav = 'nav-user';

    export default {
        name: "User",
        components: {Template},
        data() {
            return {
                users: []
            }
        },
        mounted() {
            request.get('/user/')
                .then(response => {
                    this.users = response.data;
                })
        }
    }
</script>

<style scoped>

</style>