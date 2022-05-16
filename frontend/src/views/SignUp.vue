<template>
  <div class="col-12 col-md-9 col-lg-9 col-xl-7 opacity-90">
    <div class="card" style="border-radius: 15px;">
      <div class="card-body p-5">
        <h2 class="text-uppercase text-center mb-5">Регистрация</h2>

        <form id="signup_form" @submit.prevent="onSubmit">
          <!-- Email Field -->
          <div class="form-outline mb-4">
            <label class="form-label" for="email">Email</label>
            <input
                type="text"
                id="email"
                name="email"
                class="form-control form-control-lg"
                :class="{invalid: v$.email.$error}"
                v-model="email"
            />

            <!-- Email Errors -->
            <small
                class="helper-text text-danger"
                v-if="v$.email.$error && v$.email.required.$invalid"
            >
              Поле не должно быть пустым
            </small>

            <small
                class="helper-text text-danger"
                v-else-if="v$.email.$error && v$.email.email.$invalid"
            >
              Введите корректный Email
            </small>
          </div>

          <!-- Password Field -->
          <div class="form-outline mb-4">
            <label class="form-label" for="password">Пароль</label>

            <input
                type="password"
                id="password"
                name="password"
                class="form-control form-control-lg"
                :class="{invalid: v$.password.$error}"
                v-model="password"
            />

            <!-- Password Errors -->
            <small
                class="helper-text text-danger"
                v-if="v$.password.$error && v$.password.required.$invalid"
            >
              Поле не должно быть пустым
            </small>

            <small
                class="helper-text text-danger"
                v-else-if="v$.password.$error && v$.password.minLength.$invalid"
            >
              Пароль должен быть длинее 6 символов
            </small>
          </div>

          <!-- Confirm Password Field -->
          <div class="form-outline mb-4">
            <label class="form-label" for="confirm">Подтвердите пароль</label>

            <input
                type="password"
                id="confirm"
                class="form-control form-control-lg"
                v-model="confirm"
                :class="{invalid: v$.confirm.$error}"
            />

            <!-- Confirm Password Errors -->
            <small
                class="helper-text text-danger"
                v-if="v$.confirm.$error && v$.confirm.required.$invalid"
            >
              Поле не должно быть пустым
            </small>

            <small
                class="helper-text text-danger"
                v-else-if="v$.confirm.$error && v$.confirm.sameAs.$invalid"
            >
              Пароли должны совпадать
            </small>
          </div>

          <!-- Submit Button -->
          <div class="d-flex justify-content-center">
            <button
                type="submit"
                class="btn btn-success btn-block btn-lg gradient-custom-4 text-body"
            >
              Зарегистрироваться
            </button>
          </div>

          <!-- Server Errors -->
          <div class="d-flex justify-content-center">
            <small
                class="helper-text text-danger"
                id="error_container"
                v-if="v$.email.$dirty"
            >
            </small>
          </div>

          <!-- SignIn Link -->
          <p class="text-center text-muted mt-5 mb-0">Уже есть аккаунт?
            <router-link to="/signin/" class="fw-bold text-body">
              <u>Войти!</u>
            </router-link>
          </p>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
  import { useVuelidate } from '@vuelidate/core';
  import { required, email, sameAs, minLength } from '@vuelidate/validators';
  import { convertFormToJSON } from '@/utils';
  import axios from 'axios';
  import $ from 'jquery';

  export default {
    name: 'signUp',

    data: () => ({
      v$: useVuelidate(),
      error409: false,
      email: '',
      password: '',
      confirm: '',
    }),

    validations () {
      return {
        email: { required, email },
        password: { required, minLength: minLength(6) },
        confirm: { required, sameAs: sameAs(this.password) },
      }
    },

    validationConfig: {
      $lazy: true,
    },

    methods: {
      onSubmit() {
        this.v$.$validate()  // Запускаем валидацию @vuelidate

        if (!this.v$.$error) {
          // При отсутствии ошибок отправляем данные для регистрации
          axios
            .post('/auth/signup/', convertFormToJSON('#signup_form'))
            .then(response => {
              if (response.status === 201) {
                this.$router.push('/'); // Переход на главную страницу, если пользователь создан
              }
            })
            .catch(function (error) {
              if (error.response.status === 409) {
                $('#error_container').text(error.response.data.detail);  // Вывод ошибки, что пользователь существует
              }
            });
        }
      }
    }
  }
</script>
