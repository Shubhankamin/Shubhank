<template>
  <div class="pt-md-10 main">
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="6">
          <h1 class="heading bebas-Bold-h1 text-white">My Experience</h1>
        </v-col>
        <v-col cols="12" md="6">
          <div
            v-for="(experience, index) in experiences"
            :key="index"
            class="pt-md-10 mb-5"
          >
            <div class="d-flex justify-space-between">
              <p class="manrope-Bold-h4 font-weight-bold">
                {{ experience.title }}
              </p>
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
    title: "Front-End Developer",
    dates: "Jan 2024 — Present",
    description:
      "• Developed and maintained e-commerce websites, real estate platforms, portfolios, and admin panels using HTML, CSS, JavaScript, Nuxt.js, and Vue.js.\n" +
      "• Implemented seamless API integrations and utilized Postman for efficient testing and debugging.\n" +
      "• Designed and delivered fully responsive, cross-browser-compatible web applications to ensure optimal user experience.\n" +
      "• Collaborated with teams to meet project requirements, deadlines, and high-quality standards.",
  },
  {
    title: "Freelance Developer",
    dates: "Nov 2024 — Present",
    description:
      "• Built and deployed custom websites, admin panels, and database-driven applications for various clients.\n" +
      "• Integrated APIs efficiently to enhance web functionalities and improve performance.\n" +
      "• Worked on both front-end and back-end tasks, ensuring a seamless user experience and robust system architecture.\n" +
      "• Managed multiple projects independently, meeting client expectations and deadlines with high-quality deliverables.",
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
  background-image: url("/images/meteor.png");
  background-size: cover;
  height: 100%;
  width: 100%;
}
</style>
