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
            <div class="box px-md-10 py-md-5 pa-5">
              <v-img :src="item.src" class="rounded-lg"> </v-img>
            </div>
          </v-col>
          <v-col cols="12" md="6" class="pl-md-10">
            <div class="pt-md-5 pt-5 pr-md-10 px-2">
              <p class="title w-md-75 manrope-Bold-h3 font-weight-bold">
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
                <a
                  v-if="item.liveDemo"
                  :href="item.liveDemo"
                  target="_blank"
                  class="d-flex ga-md-2 pointer text-decoration-none"
                >
                  <p class="icon manrope-Bold-h5">Live Demo</p>
                  <v-icon class="icon manrope-Bold-h5"
                    >mdi-arrow-top-right</v-icon
                  >
                </a>
                <a
                  v-if="item.github"
                  :href="item.github"
                  target="_blank"
                  class="d-flex ga-md-2 ga-1 pointer text-decoration-none"
                >
                  <p class="icon manrope-Bold-h5">See On Github</p>
                  <v-icon class="icon manrope-Bold-h5">mdi-github</v-icon>
                </a>
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
  background-image: url("/images/meteor.png");
  background-size: cover;
  height: 100%;
  width: 100%;
}
</style>

<script setup>
const projects = [
  {
    src: "/images/project-1.png",
    title: "Phoenix Academy Website",
    description:
      "Designed and developed a full-fledged web application for Phoenix Academy, encompassing both the client and admin sides. Built with Nuxt 3 and Vue 3 for a seamless front-end experience, while leveraging Supabase as the backend for robust data management. Implemented Resend for efficient email communication, ensuring a smooth user experience. This project was independently handled, covering both front-end and backend development to deliver a scalable and high-performance solution.",
    year: "2025",
    role: "Full-Stack Developer",
    liveDemo: "https://pheonixacademy.in/",
    github: "https://github.com/Shubhankamin/Pheonix",
  },
  {
    src: "/images/project-2.png",
    title: "Interactive Birthday Experience",
    description:
      "Developed a visually captivating and immersive birthday project, designed to deliver a seamless and engaging user experience. Built using Nuxt 3, Vue 3, and Vuetify, the project incorporates smooth animations and thoughtfully crafted UI/UX elements to create a memorable and interactive celebration. Focused on front-end development to ensure fluid transitions, responsiveness, and an overall delightful experience.",
    year: "2025",
    role: "Front-End Developer",
    liveDemo: "https://mymadamji.netlify.app/",
    github: "https://github.com/Shubhankamin/Madam-Ji",
  },

  {
    src: "/images/project-3.jpg",
    title: "AgriMart E-commerce Website",
    description:
      "Agri Mart — Role-Based eCommerce Website Developed a fully functional eCommerce platform connecting Farmers and Customers using pure HTML, CSS, and JavaScript. Implemented role-based access, a complete shopping flow, and data persistence using Local Storage, Cookies, IndexedDB, and data.js, all without a backend. Ensured WCAG 2.1 AA accessibility compliance, emphasizing performance, usability, and clean client-side architecture.",
    year: "2025",
    role: "Front-End Developer",
    liveDemo: "https://agrimaart.netlify.app",
    github: "https://github.com/Shubhankamin/Agri_Mart",
  },

  {
    src: "/images/project-4.jpg",
    title: "Lost & Found Management Portal",
    description:
      "Lost or Found — College Lost & Found Management Portal Developed a web-based portal for students to report and claim lost items within the campus. Built with Vue 3, Nuxt 3, and Vuetify, featuring a dedicated admin panel for the security department to manage users and item listings. Integrated Firebase for backend services including authentication, real-time database, and storage. Currently in the development and deployment proposal phase for college-wide implementation.",
    year: "2025",
    role: "Full Stack Developer",
    liveDemo: "https://lostorfound.netlify.app",
    github: "https://github.com/Shubhankamin/Find",
  },
  {
    src: "/images/project-5.jpg",
    title: "Lost & Found Management Admin Portal",
    description:
      "Lost or Found — College Lost & Found Management Portal Developed a web-based portal for students to report and claim lost items within the campus. Built with Vue 3, Nuxt 3, and Vuetify, featuring a dedicated admin panel for the security department to manage users and item listings. Integrated Firebase for backend services including authentication, real-time database, and storage. Currently in the development and deployment proposal phase for college-wide implementation.",
    year: "2025",
    role: "Full Stack Developer",
    // liveDemo: "https://lostorfound.netlify.app",
    github: "https://github.com/Shubhankamin/Find-Admin",
  },
];
</script>
