<template>
  <div class="pt-md-10 main">
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="6">
          <p class="heading bebas-Bold-h1">My Experience</p>
        </v-col>
        <v-col cols="12" md="6">
          <div
            v-for="(experience, index) in experiences"
            :key="index"
            class="pt-md-10 mb-5"
          >
            <div class="d-flex justify-space-between">
              <p class="manrope-Bold-h4">{{ experience.title }}</p>
              <p class="manrope-regular-h5">{{ experience.dates }}</p>
            </div>
            <p class="text-justify pt-5 manrope-regular-h5">
              {{ experience.description }}
            </p>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script setup>
const experiences = [
  {
    title: "Freelance Developer",
    dates: "Nov 2023 — Present",
    description:
      "Ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
  },
  {
    title: "Freelance Developer",
    dates: "Nov 2023 — Present",
    description:
      "Ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
  },
];
</script>
<style scoped>
.heading {
  text-transform: uppercase;
}
.content {
  font-size: 22px;
  font-weight: 600;
}
.link {
  color: #d3f576;
}

.main {
  background-image: url("images/meteor.svg");
  background-size: cover;
}
</style>
