<template>
    <!--login page section-->
   <div class="login-section">
    <b-container >
      <img src="../../../assets/sub_logo.png" alt="Logo" class="logo" />
      <h2 class="title">BANKQUEEN</h2>
      <p class="welcome">Log in to get started</p>
      <form class="login">
        <input
          type="text"
          placeholder="user"
          class="login__input login__input--user"
        />
        <!-- In practice, use type="password" -->
        <input
          type="text"
          placeholder="PIN"
          maxlength="4"
          class="login__input login__input--pin"
        />
        <button class="login__btn">&rarr;</button>
      </form>
    </b-container>
   </div>
   
      
</template>

<script>
export default{
    name: 'Bank',
    components: {},
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik+Wet+Paint&display=swap');

.login-section{
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
  padding: 15px;
  background: rgb(84,11,14);
  background: linear-gradient(90deg, rgba(84,11,14,1) 0%, rgba(120,0,0,1) 35%, rgba(158,42,43,1) 100%);
}
.title{
  font-family: "Rubik Wet Paint", system-ui;
  font-weight: 400;
  color: #f8f9fa;
}
.welcome {
  font-size: 32px;
  font-family: "Oswald", sans-serif;
  text-transform: uppercase;
  font-weight: 500;
  color: #f8f9fa;
}

.logo {
  height: 5.25rem;
}

.login {
  display: flex;
}

.login__input{
  text-align: center;
  border: 1px solid #e7e7e7;
  transition: all 0.3s;
  margin-left: 5px;
}

.login__input::placeholder {
  color: #bbb;
}

.login__btn{
  cursor: pointer;
  transition: all 0.3s;
  border: none;
  margin-left: 5px;
  border-radius: 5px;
  background-color: none;
}

.login__btn:hover,
.login__btn:focus
{
  outline: none;
  color: #777;
} 

</style>