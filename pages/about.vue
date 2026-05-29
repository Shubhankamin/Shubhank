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
            Front-End Developer and MCA student at MIT Manipal, specializing in
            modern web development, responsive user interfaces, and
            high-performance web applications.
          </p>

          <p class="pt-2 text-justify manrope-regular-h5 text-white">
            I am a Front-End Developer currently pursuing a Master of Computer
            Applications (MCA) at MIT Manipal, with professional experience
            across startup, freelance, and internship environments. I specialize
            in building scalable web applications, admin dashboards, e-commerce
            platforms, and responsive user interfaces using Nuxt 3, Vue 3,
            JavaScript, TypeScript, React Native, and Next.js. My technical expertise
            includes REST API integration, Firebase, Supabase, database-driven
            applications, frontend architecture, performance optimization, and
            modern UI/UX development. Passionate about creating intuitive and
            accessible digital experiences, I continuously explore emerging
            technologies and best practices to deliver efficient, maintainable,
            and user-focused web solutions.
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
                style="text-decoration: none"
              >
                <v-icon class="icon linkedin">mdi-linkedin</v-icon>
              </a>
              <a
                href="https://github.com/Shubhankamin?tab=repositories"
                target="_blank"
                style="text-decoration: none"
              >
                <v-icon class="icon github">mdi-github</v-icon>
              </a>
            </div>
          </div>
          <div class="align-center pt-10 ga-4 d-block d-md-none">
            <button
              class="contact-button py-1 px-6 manrope-Bold-h5"
              @click="downloadResume"
            >
              Download Resume <span class="dot"></span>
            </button>
            <div class="icons pt-5">
              <a
                href="https://www.linkedin.com/in/shubhank-amin-a7b231225/"
                target="_blank"
                style="text-decoration: none"
              >
                <v-icon class="icon linkedin">mdi-linkedin</v-icon>
              </a>
              <a
                href="https://github.com/Shubhankamin?tab=repositories"
                target="_blank"
                style="text-decoration: none"
              >
                <v-icon class="icon github">mdi-github</v-icon>
              </a>
            </div>
          </div>
        </v-col>
      </v-row>
      <v-row class="justify-center mb-5">
        <v-col cols="12" md="10">
          <!-- <v-img
            src="/images/me-new-3.PNG"
            lazy-src="/images/me-resized-2.png"
            style="border-radius: 20px"
          ></v-img> -->

            <v-img
              src="/images/me/me_2.jpeg"
            lazy-src="/images/me-resized-2.png"
            style="border-radius: 20px"
          ></v-img>
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
  setTimeout(() => {
    loading.value = false;
  }, 1500);
});

// Function to download resume
const downloadResume = () => {
  const link = document.createElement("a");
  link.href = "/files/ShubhankAmin_251090700127.pdf"; // Replace with your actual PDF file path
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
  transition:
    background-color 0.3s ease,
    color 0.3s ease;
}

/* .main {
  background-image: url("/images/meteor.png");
  background-size: cover;
  background-position: center;
  height: 100%;
  width: 100%;
} */

.main {
  position: relative;

  width: 100%;

  overflow: hidden;

  isolation: isolate;

  background: #030712;
}

.main::before {
  content: "";

  position: absolute;

  inset: 0;

  background:
    radial-gradient(
      circle at 15% 20%,
      rgba(59, 130, 246, 0.16),
      transparent 30%
    ),
    radial-gradient(
      circle at 85% 10%,
      rgba(132, 204, 22, 0.12),
      transparent 25%
    ),
    radial-gradient(
      circle at 50% 80%,
      rgba(147, 51, 234, 0.12),
      transparent 30%
    );

  filter: blur(90px);

  animation: auroraMove 14s ease infinite alternate;

  z-index: -2;
}

.main::after {
  content: "";

  position: absolute;

  inset: 0;

  background-image: radial-gradient(
    rgba(255, 255, 255, 0.03) 1px,
    transparent 1px
  );

  background-size: 4px 4px;

  opacity: 0.12;

  z-index: -1;
}

@keyframes auroraMove {
  from {
    transform: scale(1) rotate(0deg);
  }

  to {
    transform: scale(1.1) rotate(6deg);
  }
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
