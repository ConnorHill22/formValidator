/* eslint-disable prettier/prettier */
<template>
  <div id="login_container">
    <h1>Welcome to Analytics Corp.</h1>
    <div id="email_or_username_div" class="input_div">
      <label for="username">Email or Username</label>
      <div class="input_container">
        <input name="username" class="input" type="text" id="email_or_username_input" />
      </div>
    </div>
    <div id="password_div" class="input_div">
      <label for="password">Password</label>
      <div class="input_container">
        <input name="password" class="input" type="password" id="password_input" />
      </div>
    </div>
    <div id="forgot_div">
      <p id="forgot_p">Forgot username/password?</p>
    </div>
    <div id="error_message_div">
      <p>{{ errorMesaage }}</p>
    </div>
    <div id="buttons_div">
      <input class="button" type="button" value="Login" id="login_button" />
      <input class="button" type="button" value="Sign Up" id="signup_button" />
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      errorMessage: ""
    };
  }
};
</script>

<style lang="scss">
@import "../../../scss/_variables.scss";

h1 {
  color: var(--heading-color);
  font-weight: 200;
}

label {
  color: var(--font-color);
  display: block;
}

.input_div {
  margin: 10px 0 10px 0;
}

.input_container {
  position: relative;
  border: var(--border-color) solid 1px;
  border-radius: 15px;
  width: 350px;
  height: var(--input-container-height);
  min-height: var(--input-min-height);
  -webkit-transition: all 0.3s ease-in-out !important;
  -moz-transition: all 0.3s ease-in-out !important;
  -ms-transition: all 0.3s ease-in-out !important;
  -o-transition: all 0.3s ease-in-out !important;
  outline: none;
  padding: 3px 0px 3px 3px;
  margin: 5px 1px 3px 0px;
}

.input_container:hover {
  border: var(--primary-color) solid 1px;
}

.input_container:focus-within {
  box-shadow: 0 0 5px var(--primary-color) !important;
  padding: 3px 0px 3px 3px !important;
  margin: 5px 1px 3px 0px !important;
  border: 1px solid var(--primary-color) !important;
}
.input {
  position: absolute;
  top: 50%;
  width: 80%;
  margin-left: 15px;
  height: var(--input-height);
  min-height: var(--input-min-height);
  border: none;
  //background-color: red;//var(--bg-color) !important;
  font-size: 1.5rem;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  color: var(--font-color);
}

#forgot_p {
  color: var(--primary-color);
}

#error_message_div {
  color: var(--error-color);
}

#buttons_div {
  display: inline-flex;
}

#forgot_p:hover,
.button:hover {
  cursor: pointer;
}

#buttons_div {
  margin-top: 20px;
}

.button {
  margin-right: 20px;
  border-radius: 15px;
  width: 125px;
  height: 40px;
  min-height: var(--input-min-height);
  font-size: 1rem;
  min-height: 20px;
}

#login_button {
  background-color: var(--primary-color);
  border: var(--primary-color) solid 1px;
  color: var(--bg-color);
}

#signup_button {
  background-color: var(--bg-color);
  border: var(--primary-color) solid 1px;
  color: var(--primary-color);
}
</style>
