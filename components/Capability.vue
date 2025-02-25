<template>
  <div class="main text-white pt-5">
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="6">
          <h1 class="heading bebas-Bold-h1">MY CAPABILITIES</h1>
        </v-col>
        <v-col cols="12" md="6">
          <p class="manrope-regular-h5">
            I am always looking to add more skills.Morbi egestas neque eu
            blandit fermentum. Nulla ac lobortis ligula. Pellentesque ac ex at
            purus faucibus tristique ut et dolor.
          </p>
          <div class="d-flex ga-4 flex-wrap pt-5">
            <div
              v-for="(skill, index) in skills"
              :key="index"
              class="d-flex skills px-2 py-1 ga-2 align-center"
            >
              <p class="manrope-Bold-h5">{{ skill.name }}</p>
              <v-icon>{{ skill.icon }}</v-icon>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script setup>
const skills = [
  { name: "HTML 5", icon: "mdi-language-html5" },
  { name: "CSS 3", icon: "mdi-language-css3" },
  { name: "JavaScript", icon: "mdi-language-javascript" },
  { name: "Vue 3", icon: "mdi-vuejs" },
  { name: "Nuxt 3", icon: "mdi-nuxt" },
  { name: "React ", icon: "mdi-react" },
  { name: "Tailwind CSS ", icon: "mdi-tailwind" },

  { name: "Vuetify", icon: "mdi-vuetify" },
  { name: "Python", icon: "mdi-language-python" },
];
</script>
<style scoped>
.heading {
  text-transform: uppercase;
}

.skills {
  background-color: rgb(53, 52, 52);
  border-radius: 20px;
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
