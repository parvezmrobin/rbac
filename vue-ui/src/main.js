import Vue from 'vue';
import Login from './Login.vue';
import Dashboard from './Dashboard.vue';
import User from './User.vue';
import Role from './Role.vue';
import Permission from "./Permission.vue";


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
    default:
        break;
}

new Vue({
    render: h => h(Component),
}).$mount('#app');
