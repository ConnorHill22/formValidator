<template>
  <div id="singup_div">
    <h1>Sign Up</h1>
    <div id="general_div">
      <div id="name_div">
        <input type="text" id="fname_input" placeholder="First Name" />
        <input type="text" id="lname_input" placeholder="Last Name" />
      </div>
      <div id="email_div">
        <div id="email" class="inputContainer">
          <input type="text" id="email_input" class="input" placeholder="Email" />
        </div>
      </div>
      <div id="password_div">
        <div id="password" class="inputContainer">
          <input type="password" id="password_input" class="input" placeholder="Password" />
        </div>
      </div>
      <div id="confirm_password_div">
        <div id="confirm_password" class="inputContainer">
          <input
            type="password"
            id="confirm_password_input"
            class="input"
            placeholder="Confirm Email"
          />
        </div>
      </div>
      <div id="show_password_div">
        <input type="checkbox" id="show_password_input" />
        <p>Show Password</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Signup"
};
</script>

<style lang="scss"></style>
