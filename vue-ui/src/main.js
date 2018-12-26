import Vue from 'vue';
import Login from './Login.vue';
import Dashboard from './Dashboard.vue';
import Permission from "./Permission.vue";


Vue.config.productionTip = false;

let Component;

switch (window.location.pathname) {
    case "/":
        Component = Dashboard;
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
