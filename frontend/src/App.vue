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
  --fadded-font-color: #a7a7a7;

  --auth-height: 60vh;
  --input-container-height: 30px;
  --input-height: 4vh;
  --input-min-height: 15px;
  --input-max-height: 50px;
}

h1 {
  color: var(--heading-color);
  font-weight: 100;
  font-size: 2rem;
  //font-size: 40px;
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
  box-shadow: 0 0 0 30px var(--bg-color) inset !important;
  -webkit-box-shadow: 0 0 0 30px var(--bg-color) inset !important;
}

.input_div {
  margin: 10px 0 10px 0;
}

.input_container {
  position: relative;
  border: var(--border-color) solid 1px;
  border-radius: 15px;
  width: 100%;
  height: var(--input-container-height);
  min-height: var(--input-min-height);
  max-height: var(--input-max-height);
  outline: none;
  padding: 3px 0px 3px 3px;
 
}

.input_container:hover {
  border: var(--primary-color) solid 1px;
}

.input_container:focus-within {
  box-shadow: 0 0 5px var(--primary-color) !important;
  border: 1px solid var(--primary-color) !important;
}
.input {
  position: absolute;
  top: 50%;
  width: 80%;
  margin-left: 15px;
  border: none;
  // font-size: 25px;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  color: var(--font-color);
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
