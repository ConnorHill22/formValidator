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
          <LoginForm />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HomePicture from "@/components/svgs/HomePicture";
import LoginForm from "@/components/auth/Login_Form";

export default {
  name: "Login",
  components: {
    HomePicture,
    LoginForm
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
  max-width: 450px;
  width: 90%;
  padding-left: 5vw;
  float: left;
}
</style>