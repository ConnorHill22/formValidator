<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>-->
    <router-view />
  </div>
</template>

<style lang="scss">
:root {
  --primary-color: #11a234;
  --secondary-color: #ffffff;
  --font-color: #3c3c3c;
  --bg-color: #ffffff;
  --heading-color: #707070;
  --error-color: #ed2f2f;
  --border-color: #707070;

  --auth-height: 60vh;
  --input-container-height: 5vh;
  --input-height: 4vh;
  --input-min-height: 20px;
}

[data-theme="dark"] {
  --primary-color: #9a97f3;
  --secondary-color: #818cab;
  --font-color: #e1e1ff;
  --bg-color: #161625;
  --heading-color: #818cab;
}

input[type="text"],
input[type="password"] {
  outline-style: none !important;
  box-shadow: none !important;
  border-color: transparent !important;
}

input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
input:-webkit-autofill:active {
  -webkit-box-shadow: 0 0 0 30px var(--bg-color) inset !important;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
