<template>
  <div id="container">
    <div id="home">
      <div id="left">
        <div id="left_container">
          <HomePicture />
        </div>
      </div>
      <div id="right">
        <div id="right_container">
          <Login />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HomePicture from "@/components/svgs/HomePicture";
import Login from "@/components/auth/Login";

export default {
  name: "Login",
  components: {
    HomePicture,
    Login
  }
};
</script>

<style lang="scss">
@import "../../scss/_variables.scss";

#container {
  height: 100vh;
  display: grid;
}

#home {
  display: grid;
  align-self: center;
  grid-template-columns: 50% 50%;
  grid-template-rows: auto;
  height: var(--auth-height);
  width: 100vw;
  background-color: var(--bg-color);
}

#left {
  max-height: var(--auth-height);
}

#left_container {
  padding-right: 5vw;
  float: right;
}

#right {
  max-height: var(--auth-height);
}

#right_container {
  padding-left: 5vw;
  float: left;
}

#buttons_div {
  display: inline-flex;
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