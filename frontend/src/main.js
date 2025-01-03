import {createApp} from 'vue' 
import App from './App.vue' 
import {createBootstrap} from 'bootstrap-vue-next' 
import './style.css' 
import router from './router'
// Add the necessary CSS 
import 'bootstrap/dist/css/bootstrap.css' 
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css' 
 
const app = createApp(App) 
app.use(router)
app.use(createBootstrap())  
app.mount('#app')
