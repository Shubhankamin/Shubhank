<template>
  <div class="fullscreen-container" v-if="loading">
    <div class="loader">
      <div class="box box-1">
        <div class="side-left"></div>
        <div class="side-right"></div>
        <div class="side-top"></div>
      </div>
      <div class="box box-2">
        <div class="side-left"></div>
        <div class="side-right"></div>
        <div class="side-top"></div>
      </div>
      <div class="box box-3">
        <div class="side-left"></div>
        <div class="side-right"></div>
        <div class="side-top"></div>
      </div>
      <div class="box box-4">
        <div class="side-left"></div>
        <div class="side-right"></div>
        <div class="side-top"></div>
      </div>
    </div>
  </div>
  <div class="main" v-else>
    <Nav />
    <v-container fluid class="px-md-15 pt-16 pt-md-16 mt-md-5">
      <v-row class="pt-md-10 pt-5">
        <v-col cols="12" md="6" class="">
          <h1 class="heading bebas-Bold-h1 text-white">ABOUT ME</h1>
        </v-col>
        <v-col cols="12" md="6" class="pt-md-5 pb-10">
          <p class="content manrope-regular-h4 text-white">
            I am a Front-End Developer based in Udupi, passionate about crafting
            seamless and engaging web experiences.
          </p>
          <p class="pt-2 text-justify manrope-regular-h5 text-white">
            Currently working at **Exelon Circuits Private Limited** as a
            Front-End Developer, I also take on exciting freelance projects,
            helping businesses and individuals bring their digital ideas to
            life. With a strong foundation in modern web technologies, I have
            worked with **Nuxt.js, Vue.js, React.js, Next.js, FlutterFlow, React
            Native, Supabase, Figma, Canva, and core web technologies like HTML,
            CSS, and JavaScript**. I am deeply interested in UI/UX design and
            always strive to create user-friendly, accessible, and
            high-performance applications. Outside of coding, I enjoy exploring
            new tech trends, refining my design skills, and taking on creative
            challenges.
          </p>
          <div class="align-center pt-10 ga-4 d-none d-md-flex">
            <button
              class="contact-button py-1 px-6 manrope-Bold-h5"
              @click="downloadResume"
            >
              Download Resume <span class="dot"></span>
            </button>
            <div class="icons">
              <a
                href="https://www.linkedin.com/in/shubhank-amin-a7b231225/"
                style="text-decoration: none"
                target="_blank"
              >
                <v-icon class="icon linkedin">mdi-linkedin</v-icon>
              </a>
              <a
                href="https://github.com/Shubhankamin?tab=repositories"
                style="text-decoration: none"
                target="_blank"
              >
                <v-icon class="icon linkedin">mdi-github</v-icon>
              </a>
            </div>
          </div>
          <div
            class="d-flex align-center pt-10 ga-4 d-md-none justify-center mb-5"
          >
            <button
              class="contact-button py-1 px-6 manrope-Bold-h5"
              @click="downloadResume"
            >
              Download Resume <span class="dot"></span>
            </button>
            <div class="icons d-flex ga-3">
              <div class="px-1 icon py-1">
                <v-icon class="icon-github"> mdi-linkedin </v-icon>
              </div>
              <div class="px-1 icon py-1">
                <v-icon class="icon-github"> mdi-github </v-icon>
              </div>
            </div>
          </div>
        </v-col>
      </v-row>
      <!-- <v-row class="mb-md-10">
        <v-col class="px-md-16 px-4">
          <v-img src="/images/person-2.png"></v-img>
        </v-col>
      </v-row> -->
      <Capability />
      <Experience class="text-white" />
      <Connect />
    </v-container>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";

const loading = ref(true); // Initial state for loading

// Simulate loading completion
onMounted(() => {
  setTimeout(() => {
    loading.value = false;
  }, 3000); // Simulates a 3-second loading delay
});

// Function to download resume
const downloadResume = () => {
  const link = document.createElement("a");
  link.href = "/files/resume.pdf"; // Replace with your actual PDF file path
  link.download = "Shubhank's Resume.pdf"; // Set the filename for the download
  link.click();
};
</script>

<style scoped>
.heading {
  text-transform: uppercase;
}
.content {
  font-weight: 600;
}
.contact-button {
  background-color: #d3f576; /* light green */
  border: none;
  border-radius: 30px;
  padding: 10px 20px;
  font-weight: bold;
  cursor: pointer;
  position: relative;
  display: flex;
  align-items: center;
  color: black;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.main {
  background-image: url("images/meteor.svg");
  background-size: cover;
}

.contact-button:hover {
  background-color: #0077b5; /* LinkedIn blue */
  color: #d3f576; /* light green */
}

.contact-button:hover .dot {
  background-color: #d3f576; /* Blue for dot when hovered */
}

.contact-button .dot {
  width: 8px;
  height: 8px;
  background-color: black; /* Default dot color */
  border-radius: 50%;
  margin-left: 8px;
  transition: background-color 0.3s ease;
}

.button-and-icons {
  display: flex;
  align-items: center;
}

.icons {
  display: flex;
  gap: 10px;
  margin-left: 20px;
}

.icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #333; /* dark background */
  display: flex;
  align-items: center;
  justify-content: center;
  color: #d3f576; /* light green */
  font-size: 20px;
  text-decoration: none;
  cursor: pointer;
}

.icon.linkedin:hover {
  background-color: #0077b5; /* LinkedIn blue */
}

.icon.github:hover {
  background-color: #333; /* GitHub dark */
}

.fullscreen-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: black; /* Optional: background color */
}
</style>
