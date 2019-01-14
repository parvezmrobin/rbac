import Vue from 'vue';
import Register from './Register.vue';
import Login from './Login.vue';
import Dashboard from './Dashboard.vue';
import User from './User.vue';
import Role from './Role.vue';
import Permission from "./Permission.vue";

import Layout from './Layout.vue';


Vue.config.productionTip = false;

let Component;

switch (window.location.pathname) {
    case "/":
        Component = Dashboard;
        break;
    case "/user":
        Component = User;
        break;
    case "/role":
        Component = Role;
        break;
    case "/permission":
        Component = Permission;
        break;
    case "/auth/login":
        Component = Login;
        break;
    case "/auth/register":
        Component = Register;
        break;
    default:
        break;
}

new Vue({
    render: h => h(Layout, [h(Component)]),
}).$mount('#app');
