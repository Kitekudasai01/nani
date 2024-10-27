<template>
  <b-card class="main-section">
   <!--login page section-->
    <div class="login-section">
      <b-container >
        <img src="../../../assets/sub_logo.png" alt="Logo" class="logo" />
        <h2 class="title">BANKQUEEN</h2>
        <p class="welcome">Log in to get started</p>
        <form class="login" >
          <input
            type="text"
            placeholder="user"
            class="login__input login__input--user"
            v-model="usernameData"
          />
          <!-- In practice, use type="password" -->
          <input
            type="password"
            placeholder="PIN"
            maxlength="4"
            class="login__input login__input--pin"
            v-model="passwordData"
          />
          <button class="login__btn" @click="loginFunction">&rarr;</button>
        </form>
      </b-container>
   </div>
   <!--main bankist section-->
   <div  class="app" v-if="mainAccount">
     <div class="balance">
        <div>
          <p class="welcome"></p>
          <p class="balance__label">Current balance</p>
          <p class="balance__date">
            As of <span class="date">05/03/2037</span>
          </p>
        </div>
        <p class="balance__value">0000€</p>
      </div>
       <!-- MOVEMENTS -->
       <div class="movements">
        <div class="movements__row">
          <div class="movements__type movements__type--deposit">2 deposit</div>
          <div class="movements__date">3 days ago</div>
          <div class="movements__value">4 000€</div>
        </div>
        <div class="movements__row">
          <div class="movements__type movements__type--withdrawal">
            1 withdrawal
          </div>
          <div class="movements__date">24/01/2037</div>
          <div class="movements__value">-378€</div>
        </div>
      </div>

      <!-- SUMMARY -->
      <div class="summary">
        <p class="summary__label">In</p>
        <p class="summary__value summary__value--in">0000€</p>
        <p class="summary__label">Out</p>
        <p class="summary__value summary__value--out">0000€</p>
        <p class="summary__label">Interest</p>
        <p class="summary__value summary__value--interest">0000€</p>
        <button class="btn--sort">&downarrow; SORT</button>
      </div>

      <!-- OPERATION: TRANSFERS -->
      <div class="operation operation--transfer">
        <h2>Transfer money</h2>
        <form class="form form--transfer">
          <input type="text" class="form__input form__input--to" />
          <input type="number" class="form__input form__input--amount" />
          <button class="form__btn form__btn--transfer">&rarr;</button>
          <label class="form__label">Transfer to</label>
          <label class="form__label">Amount</label>
        </form>
      </div>

      <!-- OPERATION: LOAN -->
      <div class="operation operation--loan">
        <h2>Request loan</h2>
        <form class="form form--loan">
          <input type="number" class="form__input form__input--loan-amount" />
          <button class="form__btn form__btn--loan">&rarr;</button>
          <label class="form__label form__label--loan">Amount</label>
        </form>
      </div>

      <!-- OPERATION: CLOSE -->
      <div class="operation operation--close">
        <h2>Close account</h2>
        <form class="form form--close">
          <input type="text" class="form__input form__input--user" />
          <input
            type="password"
            maxlength="6"
            class="form__input form__input--pin"
          />
          <button class="form__btn form__btn--close">&rarr;</button>
          <label class="form__label">Confirm user</label>
          <label class="form__label">Confirm PIN</label>
        </form>
      </div>

      <!-- LOGOUT TIMER -->
      <p class="logout-timer">
        You will be logged out in <span class="timer">05:00</span>
      </p>
   </div>
  </b-card>  
</template>

<script>
export default{
  name: 'Bank',
  data(){
    return{}
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Rubik+Wet+Paint&display=swap');


.login-section{
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
  padding: 15px;
  width: 100%;
  /* margin-top: 15%;
  margin-left: 10%; */
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
 width: 100%;
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

.app {
  position: relative;
  max-width: 100rem;
  margin: 4rem auto;
  display: grid;
  grid-template-columns: 4fr 3fr;
  grid-template-rows: auto repeat(3, 15rem) auto;
  gap: 2rem;
  
  /* NOTE This creates the fade in/out anumation */
   /* opacity: 0;
  transition: all 1s;  */
}

.balance {
  grid-column: 1 / span 2;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 2rem;
  font-family: "Oswald", sans-serif;
  text-transform: uppercase;
}

.balance__label {
  font-size: 2.2rem;
  font-weight: 500;
  margin-bottom: -0.2rem;
}

.balance__date {
  font-size: 1.4rem;
  color: #888;
}

.balance__value {
  font-size: 4.5rem;
  font-weight: 400;
}

.movements {
  grid-row: 2 / span 3;
  background-color: #fff;
  border-radius: 1rem;
  overflow: scroll;
}

.movements__row {
  padding: 2.25rem 4rem;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #eee;
}

.movements__type {
  font-size: 1.1rem;
  text-transform: uppercase;
  font-weight: 500;
  color: #fff;
  padding: 0.1rem 1rem;
  border-radius: 10rem;
  margin-right: 2rem;
}

.movements__date {
  font-size: 1.1rem;
  text-transform: uppercase;
  font-weight: 500;
  color: #666;
}

.movements__type--deposit {
  background-image: linear-gradient(to top left, #39b385, #9be15d);
}

.movements__type--withdrawal {
  background-image: linear-gradient(to top left, #e52a5a, #ff585f);
}

.movements__value {
  font-size: 1.7rem;
  margin-left: auto;
}
.summary {
  grid-row: 5 / 6;
  display: flex;
  align-items: baseline;
  padding: 0 0.3rem;
  margin-top: 1rem;
}

.summary__label {
  font-size: 1.2rem;
  font-weight: 500;
  text-transform: uppercase;
  margin-right: 0.8rem;
}

.summary__value {
  font-size: 2.2rem;
  margin-right: 2.5rem;
}

.summary__value--in,
.summary__value--interest {
  color: #66c873;
}

.summary__value--out {
  color: #f5465d;
}

.btn--sort {
  margin-left: auto;
  border: none;
  background: none;
  font-size: 1.3rem;
  font-weight: 500;
  cursor: pointer;
}

/* OPERATIONS */
.operation {
  border-radius: 1rem;
  padding: 3rem 4rem;
  color: #333;
}

.operation--transfer {
  background: rgb(102,155,188);
  background: radial-gradient(circle, rgba(102,155,188,1) 0%, rgba(0,48,73,1) 100%);
  box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
}

.operation--loan {
  background: rgb(144,169,85);
  background: radial-gradient(circle, rgba(144,169,85,1) 0%, rgba(49,87,44,1) 100%);
  box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
}

.operation--close {
  background: rgb(164,22,26);
  background: radial-gradient(circle, rgba(164,22,26,1) 0%, rgba(229,56,59,1) 100%);
  box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
}

h2 {
  margin-bottom: 1.5rem;
  text-transform: uppercase;
  font-family: "Oswald", sans-serif;
  font-weight: 800;
  color: #f8f9fa;
}

.form {
  display: grid;
  grid-template-columns: 2.5fr 2.5fr 1fr;
  grid-template-rows: auto auto;
  gap: 0.4rem 1rem;
}

/* Exceptions for interst */
.form.form--loan {
  grid-template-columns: 2.5fr 1fr 2.5fr;
}
.form__label--loan {
  grid-row: 2;
}

.form__label{
  text-transform: uppercase;
  font-family: "Oswald", sans-serif;
  font-weight: 800;
  color: #f8f9fa;
}

.form__input{
  text-align: center;
 width: 100%;
  border: 1px solid #e7e7e7;
  transition: all 0.3s;
  margin-left: 5px;
  transition: all 0.3s;
}


.form__btn{
  cursor: pointer;
  transition: all 0.3s;
  border: none;
  margin-left: 5px;
  border-radius: 5px;
  background-color: none;
}
.form__btn:hover,
.form__btn:focus
{
  outline: none;
  color: #777;
} 


.logout-timer {
  padding: 0 0.3rem;
  margin-top: 1.9rem;
  text-align: right;
  font-size: 1.25rem;
}

.timer {
  font-weight: 600;
}

</style>