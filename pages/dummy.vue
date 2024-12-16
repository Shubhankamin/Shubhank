<template>
  <div>
    <h1>dsf</h1>
    <vue-tel-input v-model="phone" mode="international"></vue-tel-input>
  </div>
</template>

<script setup>
import VueTelInput from "vue-tel-input";
import "vue-tel-input/vue-tel-input.css";
const phone = ref(null);
</script>
