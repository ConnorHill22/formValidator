<template>
  <div id="singup_div">
    <h1 id= "title">Sign Up</h1>
    <div id="general_div">
      <div class="form_Group" id="name_div">
        <div id="first_name_container">
          <div class="form-group input_container" :class="{'error':$v.first_name.$error}"  id="name" >
            <input 
              type="text" 
              id="fname_input" 
              class="input" 
              placeholder="First Name" 
              v-model="$v.first_name.$model"
            />
          </div>
          <div class = "error required_error" v-if="$v.first_name.$error">
            First Name is required
          </div>
        </div>
        <div id="last_name_container">
          <div class="input_container" :class="{'error':$v.last_name.$error}" id="name">
            <input 
              type="text" 
              id="lname_input" 
              class="input" 
              placeholder="Last Name" 
              v-model="$v.last_name.$model"
            />
          </div>
          <div class = "error required_error" v-if="$v.last_name.$error">
            Last Name is required
          </div>
        </div>
      </div>
      <div class="form_Group" id="email_div">
        <div id="email" class="input_container" :class="{'error':$v.email.$error}">
          <input 
            type="email" 
            id="email_input" 
            class="input" 
            placeholder="Email" 
            v-model="$v.email.$model"
            @focus="email_input_selected=true"
            @blur="email_input_selected=false"
          />
        </div>
        <div id="email_error" v-if="email_input_selected">
          <div id="input_email_error">
            <div class="error_row">
              <p>Email required</p>
              <span v-if="!$v.email.required"><img class="feedbackIcon" src="../../../public/wrong.svg"></span>
              <span v-if="$v.email.required"><img class="feedbackIcon" src="../../../public/right.svg"></span>
            </div>
            <div class="error_row">
              <p>Email required</p>
              <span v-if="!$v.email.email"><img class="feedbackIcon" src="../../../public/wrong.svg"></span>
              <span v-if="$v.email.email"><img class="feedbackIcon" src="../../../public/right.svg"></span>
            </div>
          </div>
        </div>
      </div>
      <!-- <div id="password_div" class="form_Group">
        <div id="password" class="input_container">
          <input 
            :type="password_Input_Type" 
            id="password_input" 
            class="input" 
            placeholder="Password" 
            v-model="password"
          />
        </div>
        <div class = "error required_error" v-if="!$v.password.required">
          Password is required
        </div>
        <div class = "error required_error" v-if="!$v.password.minLength">
          Minimum 8 characters
        </div>
        <div class = "error required_error" v-if="!$v.password.capital_Letter">
          Capital letter is required
        </div>
        <div class = "error required_error" v-if="!$v.password.lower_Letter">
          Lower case letter is required
        </div>
        <div class = "error required_error" v-if="!$v.password.conatain_number">
          Number is required
        </div>
      </div> -->
      <div class="form_Group" id="confirm_password_div">
        <div id="confirm_password" class="input_container">
          <input
            :type="password_Input_Type"
            id="confirm_password_input"
            class="input"
            placeholder="Confirm Email"
          />
        </div>
      </div>
      <div id="show_password_div">
        <input id="show_password_input" type="checkbox" v-model="password_Input_Type" true-value="text" false-value="password" />
        <p>Show Password</p>
      </div>
    </div>
    <div id="buttons_div">
      <input class="button" type="button" value="Sign Up" id="login_button" />
      <router-link to="/" id="haveAccount_p">
        <p >Have an account? Click to signin</p>
      </router-link>
    </div>
  </div>
</template>

<script>
import { required, minLength, email, sameAs} from 'vuelidate/lib/validators'

export default {
  name: "SignupForm",

  data() {
    return {
      first_name:'',
      last_name: "",
      email: "",
      email_input_selected:false,
      password: "",
      password_input_selected:false,
      confirm_password: "",
      confirm_input_selected:false,
      password_Input_Type: "password"
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
      required,
      email
    },
    password: {
      required,
      minLength: minLength(8),
      capital_Letter:(password) => {return (/[A-Z]/.test(password))},
      lower_Letter:(password) => {return (/[a-z]/.test(password))},
      conatain_number:(password) => {return (/[0-9]/.test(password))}
    },
    confirm_password: {
      required,
      sameASPassword: sameAs("password")
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

.form_Group {
  position: absolute;
  height: 100px;
}

.input_container {
  margin-top: 1.5rem;
}

.error {
  color: red;
  border-color: red;
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

#haveAccount_p {
  color: var(--primary-color);
  text-decoration: none !important;
}

.feedbackIcon {
  width: 20px;
  height: 20px;
}

.email_error{
  position: absolute;
}


</style>
