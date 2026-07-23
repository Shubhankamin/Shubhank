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
    <div class="mouse-follower">
      <div class="energy-ring"></div>
      <span class="particle particle-1"></span>
      <span class="particle particle-2"></span>
      <span class="particle particle-3"></span>
    </div>
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
            JavaScript, TypeScript, React Native, and Next.js. My technical
            expertise includes REST API integration, Firebase, Supabase,
            database-driven applications, frontend architecture, performance
            optimization, and modern UI/UX development. Passionate about
            creating intuitive and accessible digital experiences, I
            continuously explore emerging technologies and best practices to
            deliver efficient, maintainable, and user-focused web solutions.
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
            src="/images/me/me_8.jpeg"
            lazy-src="/images/me/me_8_lazy.jpeg"
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
import { useScrollAurora } from "~/composables/useScrollAurora";
import { useMouseFollower } from "~/composables/useMouseFollower";
useScrollAurora();
useMouseFollower();

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

.mouse-follower {
  position: fixed;
  top: 0;
  left: 0;

  width: 110px;
  height: 110px;

  pointer-events: none;
  z-index: 9999999999;

  transform: translate(
    calc(var(--follower-x, 50vw) - 50%),
    calc(var(--follower-y, 50vh) - 50%)
  );

  will-change: transform;
}

/* Main organic orbit */

.energy-ring {
  position: absolute;
  inset: 18px;

  border: 1px solid rgba(211, 245, 118, 0.45);

  border-radius: 55% 45% 62% 38% / 42% 58% 42% 58%;

  box-shadow:
    0 0 12px rgba(211, 245, 118, 0.18),
    inset 0 0 12px rgba(211, 245, 118, 0.06);

  animation:
    morphRing 5s ease-in-out infinite alternate,
    rotateRing 10s linear infinite;
}

/* Secondary orbit */

.energy-ring::before {
  content: "";

  position: absolute;
  inset: -14px;

  border-radius: 50%;

  border-top: 1px solid rgba(96, 165, 250, 0.5);
  border-right: 1px solid transparent;
  border-bottom: 1px solid rgba(211, 245, 118, 0.2);
  border-left: 1px solid transparent;

  animation: reverseRotate 6s linear infinite;
}

/* Core */

.energy-ring::after {
  content: "";

  position: absolute;

  width: 5px;
  height: 5px;

  top: 50%;
  left: 50%;

  transform: translate(-50%, -50%);

  border-radius: 50%;

  background: #d3f576;

  box-shadow:
    0 0 6px #d3f576,
    0 0 15px rgba(211, 245, 118, 0.8),
    0 0 30px rgba(211, 245, 118, 0.35);

  animation: corePulse 2s ease-in-out infinite;
}

/* Particles */

.particle {
  position: absolute;

  width: 3px;
  height: 3px;

  border-radius: 50%;

  background: #d3f576;

  box-shadow: 0 0 8px #d3f576;
}

.particle-1 {
  top: 7px;
  left: 52%;

  animation: particleFloat1 4s ease-in-out infinite;
}

.particle-2 {
  right: 5px;
  bottom: 22px;

  width: 2px;
  height: 2px;

  background: #60a5fa;

  box-shadow: 0 0 8px #60a5fa;

  animation: particleFloat2 5s ease-in-out infinite;
}

.particle-3 {
  display: none;
}

@keyframes morphRing {
  0% {
    border-radius: 55% 45% 62% 38% / 42% 58% 42% 58%;
    transform: scale(0.95);
  }

  50% {
    border-radius: 42% 58% 40% 60% / 60% 40% 55% 45%;
    transform: scale(1.05);
  }

  100% {
    border-radius: 63% 37% 52% 48% / 38% 62% 45% 55%;
    transform: scale(0.98);
  }
}

@keyframes rotateRing {
  to {
    rotate: 360deg;
  }
}

@keyframes reverseRotate {
  to {
    rotate: -360deg;
  }
}

@keyframes corePulse {
  0%,
  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0.7;
  }

  50% {
    transform: translate(-50%, -50%) scale(1.8);
    opacity: 1;
  }
}

@keyframes particleFloat1 {
  0%,
  100% {
    transform: translate(0, 0);
  }

  50% {
    transform: translate(8px, -5px);
  }
}

@keyframes particleFloat2 {
  0%,
  100% {
    transform: translate(0, 0);
  }

  50% {
    transform: translate(6px, 8px);
  }
}
</style>
