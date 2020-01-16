<template>
  <div id="singup_div">
    <h1 id="title">Sign Up</h1>
    <div id="general_div">
      <div class="form_Group" id="name_div">
        <div id="first_name_container">
          <label for="first_name">First Name*</label>
          <div class="form-group input_container" :class="{'error':$v.first_name.$error}">
            <input
              name="first_name"
              type="text"
              id="fname_input"
              class="input"
              v-model="$v.first_name.$model"
            />
          </div>
        </div>
        <div id="last_name_container">
          <label for="last_name">Last Name*</label>
          <div class="input_container" :class="{'error':$v.last_name.$error}">
            <input
              name="last_name"
              type="text"
              id="lname_input"
              class="input"
              v-model="$v.last_name.$model"
            />
          </div>
        </div>
      </div>
      <div class="form_Group" id="email_div">
        <label for="email">Email*</label>
        <div id="email" class="input_container" :class="{'error':$v.email.$error}">
          <input
            name="email"
            type="email"
            id="email_input"
            class="input"
            v-model="$v.email.$model"
            @focus="email_input_selected=true"
            @blur="email_input_selected=false"
          />
        </div>
        <div id="email_error_container" class="error_container" v-if="email_input_selected">
          <div class="error_box_container">
            <div class="error_row">
              <p>Real email address</p>
              <div>
                <span v-if="!realEmail">
                  <img class="feedbackIcon" src="../../../public/wrong.svg" />
                </span>
                <span v-if="realEmail">
                  <img class="feedbackIcon" src="../../../public/right.svg" />
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="password_div" class="form_Group">
        <label for="password">Password*</label>
        <div id="password" class="input_container" :class="{'error':$v.password.$invalid}" >
          <input
            name="password"
            :type="password_Input_Type"
            id="password_input"
            class="input"
            v-model="password"
            @focus="password_input_selected=true"
            @blur="password_input_selected=false"
          />
        </div>
        <div id="password_validation_div" v-if="password_input_selected">
          <div class= "error_box_container">
            <div class="error_row">
              <p>Minimum 8 characters</p>
              <div>
                <span v-if="!min8Characters">
                  <img class="feedbackIcon" src="../../../public/wrong.svg" />
                </span>
                <span v-if="min8Characters">
                  <img class="feedbackIcon" src="../../../public/right.svg" />
                </span>
              </div>
            </div>
            <div class="error_row">
              <p>Capital letter required</p>
              <div>
                <span v-if="!$v.password.capital_Letter">
                  <img class="feedbackIcon" src="../../../public/wrong.svg" />
                </span>
                <span v-if="$v.password.capital_Letter">
                  <img class="feedbackIcon" src="../../../public/right.svg" />
                </span>
              </div>
            </div>
            <div class="error_row">
              <p>Lower case letter required</p>
              <div>
                <span v-if="!$v.password.lower_Letter">
                  <img class="feedbackIcon" src="../../../public/wrong.svg" />
                </span>
                <span v-if="$v.password.lower_Letter">
                  <img class="feedbackIcon" src="../../../public/right.svg" />
                </span>
              </div>
            </div>
            <div class="error_row">
              <p>Number required</p>
              <div>
                <span v-if="!$v.password.conatain_number">
                  <img class="feedbackIcon" src="../../../public/wrong.svg" />
                </span>
                <span v-if="$v.password.conatain_number">
                  <img class="feedbackIcon" src="../../../public/right.svg" />
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="form_Group" id="confirm_password_div" >
        <label for="c_password">Confirm Password*</label>
        <div id="confirm_password" class="input_container" :class="{'error':$v.confirm_password.$invalid}">
          <input
            name="c_password"
            :type="password_Input_Type"
            id="confirm_password_input"
            v-model="confirm_password"
            class="input"
            @focus="confirm_input_selected=true"
            @blur="confirm_input_selected=false"
          />
        </div>
        <div id="password_validation_div" v-if="confirm_input_selected ">
          <div class= "error_box_container">
            <div class="error_row">
              <p>Match Password</p>
              <div>
                <span v-if="!matchPassword">
                  <img class="feedbackIcon" src="../../../public/wrong.svg" />
                </span>
                <span v-if="matchPassword">
                  <img class="feedbackIcon" src="../../../public/right.svg" />
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="show_password_div">
        <input
          id="show_password_input"
          type="checkbox"
          v-model="password_Input_Type"
          true-value="text"
          false-value="password"
        />
        <p>Show Password</p>
      </div>
    </div>
    <div id="buttons">
      <input class="button" type="button" value="Sign Up" id="login_button" />
      <router-link to="/" id="haveAccount_p">
        <p>Have an account? Click to sign in</p>
      </router-link>
    </div>
  </div>
</template>

<script>
import { required, minLength, email, sameAs } from "vuelidate/lib/validators";

export default {
  name: "SignupForm",

  data() {
    return {
      first_name: "",
      first_name_wrong: false,
      last_name: "",
      last_name_wrong: false,
      email: "",
      email_wrong: false,
      email_input_selected: false,
      password: "",
      password_wrong: false,
      password_input_selected: false,
      confirm_password: "",
      confirm_password_wrong: false,
      confirm_input_selected: false,
      password_Input_Type: "password",
    };
  },
  computed: {
    realEmail() {
      return (this.email== "" ? false : this.$v.email.email)
    },
    min8Characters() {
      return (this.password== "" ? false : this.$v.password.minLength)
    },
    matchPassword() {
      return (this.confirm_password== "" ? false : this.$v.confirm_password.sameASPassword)
    }
  },
  validations: {
    first_name: {
      required
    },
    last_name: {
      required
    },
    email: {
      email
    },
    password: {
      minLength: minLength(8),
      capital_Letter: password => {
        return /[A-Z]/.test(password);
      },
      lower_Letter: password => {
        return /[a-z]/.test(password);
      },
      conatain_number: password => {
        return /[0-9]/.test(password);
      }
    },
    confirm_password: {
      sameASPassword: sameAs("password")
    }
  }
};
</script>

<style scoped lang="scss">
#general_div {
  margin: 30px 0 30px 0;
}

#name_div {
  display: grid;
  grid-template-rows: auto;
  grid-template-columns: 47.5% 47.5%;
  column-gap: 5%;
}

.form_Group {
  height: 70px;
}

.error {
  color: red;
  border-color: red;
}

#show_password_div {
  height: auto;
  color: var(--fadded-font-color);
  display: grid;
  grid-template-columns: 25px auto;
  grid-template-rows: auto;

  p {
    display: block;
    margin-block-start: 0;
    margin-block-end: 0;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
  }

  input {
    margin: 0;
  }
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

#haveAccount_p {
  color: var(--primary-color);
  text-decoration: none !important;
}

.feedbackIcon {
  width: 20px;
  height: 20px;
}

.error_container{
  position: absolute;
  
}

.error_box_container {
  position: absolute;
  width: 18vw;
  margin-top: 10px;
  border-radius: 10px;
  background: #ffffff;
  z-index: 10;
  -webkit-box-shadow: -4px 10px 29px 0px rgba(110,110,110,1);
  -moz-box-shadow: -4px 10px 29px 0px rgba(110,110,110,1);
  box-shadow: -4px 10px 29px 0px rgba(110,110,110,1);
}

.error_box_container:before, .error_box_container:after {
  content: '';
  display: block;
  position: absolute;
  bottom: 100%;
  width: 0;
  height: 0;
}
.error_box_container:before {
  left: 19px;
  border: 11px solid transparent;
}
.error_box_container:after {
  left: 20px;
  border: 10px solid transparent;
  border-bottom-color: #fff;
}

.error_row {
  color: var(--border-color);
  size: 2rem;
  margin: 0px 10px 0 10px;
  display: grid;
  grid-template-columns: 90% 10%;
  grid-template-rows: auto auto;
  align-items: center;
}

</style>
