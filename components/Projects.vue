<template>
  <div>
    <v-container fluid class="main text-white pt-md-10">
      <div data-aos="fade-up" data-aos-duration="3000">
        <v-row>
          <v-col cols="12" md="6" class="px-md-16 px-5">
            <h1 class="heading bebas-Bold-h1">Featured Projects</h1>
            <p class="mt-3 mt-md-0 manrope-regular-h5">
              Here are some of the selected projects that showcase my passion
              for front-end development.
            </p>
          </v-col>
        </v-row>
        <v-row class="px-md-10 pt-10" v-for="(item, i) in projects" :key="i">
          <v-col cols="12" md="6">
            <div class="box px-md-10 py-md-16 pa-5">
              <v-img :src="item.src"> </v-img>
            </div>
          </v-col>
          <v-col cols="12" md="6" class="pl-md-10">
            <div class="pt-md-5 pt-5 pr-md-10 px-2">
              <p class="title w-md-75 manrope-Bold-h3">
                {{ item.title }}
              </p>
              <p class="pt-5 manrope-regular-h5">
                {{ item.description }}
              </p>
              <p class="pt-8 manrope-regular-h4">Project Info</p>
              <v-divider
                :thickness="2"
                class="border-opacity-25 mt-5"
              ></v-divider>
              <div class="d-flex justify-space-between pt-3">
                <p class="manrope-regular-h5">Year</p>
                <p class="manrope-regular-h5">{{ item.year }}</p>
              </div>
              <v-divider
                :thickness="2"
                class="border-opacity-25 mt-5"
              ></v-divider>
              <div class="d-flex justify-space-between pt-3">
                <p class="manrope-regular-h5">Role</p>
                <p class="manrope-regular-h5">{{ item.role }}</p>
              </div>
              <div class="pt-10 d-flex ga-10 links ga-1">
                <div class="d-flex ga-md-2 pointer">
                  <p class="icon manrope-Bold-h5">Live Demo</p>
                  <v-icon class="icon manrope-Bold-h5"
                    >mdi-arrow-top-right</v-icon
                  >
                </div>
                <div class="d-flex ga-md-2 ga-1 pointer">
                  <p class="icon manrope-Bold-h5">See On Github</p>
                  <v-icon class="icon manrope-Bold-h5">mdi-github</v-icon>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>
        <v-divider
          :thickness="3"
          class="border-opacity-50 mt-5"
          color="white"
        ></v-divider>
      </div>
    </v-container>
  </div>
</template>
<style scoped>
.heading {
  text-transform: uppercase;
}

.box {
  background-color: #1a1a1a;
  border-radius: 10px;
}

.icon {
  color: #d3f576;
}
.main {
  background-image: url("images/meteor.svg");
  background-size: cover;
}
</style>

<script setup>
const projects = [
  {
    src: "/images/work1.png",
    title: "Promotional landing page for our favorite show",
    description:
      " Teamed up with a designer to breathe life into a promotional webpage for our beloved show, Adventure Time. Delivered a fully responsive design with dynamic content capabilities, seamlessly integrating a newsletter feature to keep fans updated with the latest adventures.",
    year: "2023",
    role: "Front End Developer",
  },
  {
    src: "/images/work1.png",

    title: "Promotional landing page for our favorite show",
    description:
      " Teamed up with a designer to breathe life into a promotional webpage for our beloved show, Adventure Time. Delivered a fully responsive design with dynamic content capabilities, seamlessly integrating a newsletter feature to keep fans updated with the latest adventures.",
    year: "2023",
    role: "Front End Developer",
  },
  {
    src: "/images/work1.png",

    title: "Promotional landing page for our favorite show",
    description:
      " Teamed up with a designer to breathe life into a promotional webpage for our beloved show, Adventure Time. Delivered a fully responsive design with dynamic content capabilities, seamlessly integrating a newsletter feature to keep fans updated with the latest adventures.",
    year: "2023",
    role: "Front End Developer",
  },
];
</script>
