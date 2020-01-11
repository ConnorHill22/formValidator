<template>
  <div id="singup_div">
    <h1>Welcome to Analytics Corp.</h1>
    <div id="general_div">
      <!-- <div id="name_div">
        <div class="input_container" id="name">
          <input type="text" id="fname_input" class="input" placeholder="First Name" />
        </div>
        <div class="input_container" id="name">
          <input type="text" id="lname_input" class="input" placeholder="Last Name" />
        </div>
      </div>-->
      <div id="email_div">
        <div id="email" class="input_container">
          <input type="text" id="email_input" class="input" placeholder="Email" />
        </div>
      </div>
      <div id="password_div">
        <div id="password" class="input_container">
          <input type="password" id="password_input" class="input" placeholder="Password" />
        </div>
      </div>
      <div id="confirm_password_div">
        <div id="confirm_password" class="input_container">
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
    <div id="signup_navigation">
      <div @click.prevent="decreaseIndex">
        <GreenArrow class="navigationGreenArrow" id="leftGreenArrowNav" />
      </div>
      <Circles :solid_green="pageIndex" />
      <div @click.prevent="increaseIndex">
        <GreenArrow class="navigationGreenArrow" id="rightGreenArrowNav" />
      </div>
    </div>
  </div>
</template>

<script>
import Circles from "@/components/auth/_helpers/Circles.vue";
import GreenArrow from "@/components/svgs/GreenArrow.vue";
export default {
  name: "SignupForm",
  components: {
    Circles,
    GreenArrow
  },
  data() {
    return {
      pageIndex: 1
    };
  },
  methods: {
    increaseIndex: function() {
      return (this.pageIndex = this.pageIndex + 1);
    },
    decreaseIndex: function() {
      return this.pageIndex--;
    }
  }
};
</script>

<style scoped lang="scss">
#general_div {
  margin: 0px 0 0px 0;
}

#name_div {
  display: grid;
  grid-template-rows: auto;
  grid-template-columns: 47.5% 47.5%;
  column-gap: 5%;
}

.input_container {
  margin-top: 0.5rem;
}

#show_password_div {
  color: var(--fadded-font-color);
  display: grid;
  grid-template-columns: 25px auto;
  grid-template-rows: auto;
}

#show_password_input {
  align-self: center;
}

#signup_navigation {
  position: relative;
  height: 50px;
  display: grid;
  align-items: center;
}

.navigationGreenArrow:hover {
  cursor: pointer;
}

.navigationGreenArrow {
  height: 2rem;
  width: 2rem;
}

#leftGreenArrowNav {
  position: absolute;
  transform: rotate(180deg);
  left: 0;
  top: 0;
}

#leftGreenArrowNav:hover {
  transform: rotate(180deg) scale(1.3) !important;
  transition: all ease 500ms;
}

#rightGreenArrowNav {
  position: absolute;
  right: 0;
  top: 0;
  animation: pulse 2s infinite;
  animation-timing-function: linear;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.5);
  }
  100% {
    transform: scale(1);
  }
}
</style>
