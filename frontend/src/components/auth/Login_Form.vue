/* eslint-disable prettier/prettier */
<template>
  <div id="login_container">
    <h1>Welcome to Analytics Corp.</h1>
    <div id="form_div">
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
        <router-link to="/signup">
          <input class="button" type="button" value="Sign Up" id="signup_button" />
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      errorMessage: ""
    };
  }
};
</script>

<style lang="scss">
@import "../../../scss/_variables.scss";

label {
  color: var(--font-color);
  display: block;
}

#form_div {
  margin-top: 50px;
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
