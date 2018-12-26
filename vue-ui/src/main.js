import Vue from 'vue'
import Dashboard from './Dashboard.vue'
import Permission from "./Permission.vue";
import {mixin} from "./assets/site.js";


Vue.config.productionTip = false;

let Component;

switch (window.location.pathname) {
    case "/":
        Component = Dashboard;
        break;
    case "/permission":
        Component = Permission;
        break;
    default:
        break;
}

new Vue({
    mixins: [mixin],
    render: h => h(Component),
}).$mount('#app');
