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
        <v-col cols="12" md="6">
          <h1 class="heading bebas-Bold-h1 text-white">ABOUT ME</h1>
        </v-col>
        <v-col cols="12" md="6" class="pt-md-5 pb-10">
          <p class="content manrope-regular-h4 text-white">
            I am a Front-End Developer based in Udupi, passionate about crafting
            seamless and engaging web experiences.
          </p>
          <p class="pt-2 text-justify manrope-regular-h5 text-white">
            Currently working at
            <strong>Exelon Circuits Private Limited</strong> as a Front-End
            Developer, I also take on exciting freelance projects, helping
            businesses and individuals bring their digital ideas to life. With a
            strong foundation in modern web technologies, I have worked with
            <strong
              >Nuxt.js, Vue.js, React.js, Next.js, FlutterFlow, React Native,
              Supabase, Figma, Canva, and core web technologies like HTML, CSS,
              and JavaScript</strong
            >. I am deeply interested in UI/UX design and always strive to
            create user-friendly, accessible, and high-performance applications.
            Outside of coding, I enjoy exploring new tech trends, refining my
            design skills, and taking on creative challenges.
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
                target="_blank"
              >
                <v-icon class="icon linkedin">mdi-linkedin</v-icon>
              </a>
              <a
                href="https://github.com/Shubhankamin?tab=repositories"
                target="_blank"
              >
                <v-icon class="icon github">mdi-github</v-icon>
              </a>
            </div>
          </div>
        </v-col>
      </v-row>
      <Capability />
      <Experience class="text-white" />
      <Connect />
    </v-container>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";

const loading = ref(true); // Initial state for loading

onMounted(() => {
  const img = new Image();
  img.src = "/images/meteor.png"; // Path to your background image

  img.onload = () => {
    loading.value = false;
  };

  // Fallback: If image takes too long, hide loader after 5s
  setTimeout(() => {
    loading.value = false;
  }, 5000);
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
  background-color: #d3f576;
  border: none;
  border-radius: 30px;
  padding: 10px 20px;
  font-weight: bold;
  cursor: pointer;
  display: flex;
  align-items: center;
  color: black;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.main {
  background-image: url("/images/meteor.png");
  background-size: cover;
  background-position: center;
  height: 100%;
  width: 100%;
}

.contact-button:hover {
  background-color: #0077b5;
  color: #d3f576;
}

.contact-button:hover .dot {
  background-color: #d3f576;
}

.contact-button .dot {
  width: 8px;
  height: 8px;
  background-color: black;
  border-radius: 50%;
  margin-left: 8px;
  transition: background-color 0.3s ease;
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
  background-color: #333;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #d3f576;
  font-size: 20px;
  cursor: pointer;
}

.icon.linkedin:hover {
  background-color: #0077b5;
}

.icon.github:hover {
  background-color: #333;
}

.fullscreen-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: black;
}

/* Loader scaling */
.loader {
  scale: 3;
  height: 50px;
  width: 40px;
}

/* Box animations */
.box {
  position: relative;
  opacity: 0;
  left: 10px;
}

.side-left,
.side-right,
.side-top {
  position: absolute;
}

.side-left {
  background-color: #d3e97a;
  width: 19px;
  height: 5px;
  transform: skew(0deg, -25deg);
  top: 14px;
  left: 10px;
}

.side-right {
  background-color: #d3e97a;
  width: 19px;
  height: 5px;
  transform: skew(0deg, 25deg);
  top: 14px;
  left: -9px;
}

.side-top {
  background-color: #d3e97a;
  width: 20px;
  height: 20px;
  rotate: 45deg;
  transform: skew(-20deg, -20deg);
}

.box-1 {
  animation: from-left 4s infinite;
}

.box-2 {
  animation: from-right 4s infinite;
  animation-delay: 1s;
}

.box-3 {
  animation: from-left 4s infinite;
  animation-delay: 2s;
}

.box-4 {
  animation: from-right 4s infinite;
  animation-delay: 3s;
}

/* Keyframes for box animation */
@keyframes from-left {
  0% {
    opacity: 0;
    translate: -20px -6px;
  }
  20% {
    opacity: 1;
    translate: 0px 0px;
  }
  40% {
    translate: 0px 4px;
  }
  60% {
    translate: 0px 8px;
  }
  80% {
    translate: 0px 12px;
  }
  100% {
    opacity: 0;
    translate: 0px 30px;
  }
}

@keyframes from-right {
  0% {
    opacity: 0;
    translate: 20px -6px;
  }
  20% {
    opacity: 1;
    translate: 0px 0px;
  }
  40% {
    translate: 0px 4px;
  }
  60% {
    translate: 0px 8px;
  }
  80% {
    translate: 0px 12px;
  }
  100% {
    opacity: 0;
    translate: 0px 30px;
  }
}
</style>
