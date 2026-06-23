<template>
  <!-- <div class="fullscreen-container" v-if="loading">
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
  </div> -->

  <div v-if="loading" class="intro-loader">
    <h1 class="intro-title">Welcome to My Portfolio</h1>

    <h2 class="intro-name">Shubhank Amin</h2>

    <p class="intro-text">Front-End Developer • Vue • Nuxt • React Native</p>

    <div class="loading-bar">
      <span></span>
    </div>
  </div>

  <div v-else class="main">
    <Nav />
    <Hero class="mt-10 mt-md-0" />
    <Projects id="work" />
    <Specialize id="spcialize" />
    <!-- <Education /> -->
    <!-- <Project-1 /> -->
    <Skills id="skills" />
    <About id="about" />
    <Connect id="connect" />
  </div>
</template>

<script setup>
useHead({
  title: "Shubank | Front-end Developer (Nuxt 3, Vue 3)",
  meta: [
    {
      name: "description",
      content:
        "Front-end developer skilled in Nuxt 3, Vue 3, Vuetify, and UI development. 1 year of experience building websites, PWAs, e-commerce, and custom dashboards.",
    },
    {
      name: "keywords",
      content:
        "Shubank, front-end developer, Nuxt developer, Vue developer, portfolio, Udupi developer, India developer",
    },
    { property: "og:title", content: "Shubank | Front-end Developer" },
    {
      property: "og:description",
      content:
        "Portfolio of Shubank, a front-end developer specializing in Nuxt 3, Vue 3, and modern UI development.",
    },
    {
      property: "og:image",
      content: "https://shubhankportfolio.netlify.app/logo.png",
    },
    { property: "og:url", content: "https://shubhankportfolio.netlify.app" },
  ],
});

import { onMounted, ref } from "vue";

const loading = ref(true); // Initial state for loading

onMounted(() => {
  const img = new Image();
  img.src = "/images/meteor.png";

  img.onload = () => {
    loading.value = false;
  };

  // Fallback: If image takes too long, hide loader after 5s
  setTimeout(() => {
    loading.value = false;
  }, 5000);
});
</script>

<style scoped>
.fullscreen-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: black;
}

/* .main {
  background-image: url("/images/meteor.png");
  background-size: cover;
  background-position: center;
  height: 100%;
  width: 100%;
} */

.fullscreen-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background: #030712;
}

/* MAIN BACKGROUND */

.main {
  position: relative;
  min-height: 100vh;
  width: 100%;
  overflow: hidden;
  background: #030712;
  isolation: isolate;
}

/* Aurora Glow Layer */

.main::before {
  content: "";
  position: fixed;
  inset: 0;

  background:
    radial-gradient(
      circle at 15% 20%,
      rgba(59, 130, 246, 0.18),
      transparent 30%
    ),
    radial-gradient(
      circle at 85% 15%,
      rgba(132, 204, 22, 0.14),
      transparent 25%
    ),
    radial-gradient(
      circle at 50% 80%,
      rgba(147, 51, 234, 0.14),
      transparent 30%
    );

  filter: blur(90px);

  animation: auroraMove 14s ease infinite alternate;

  z-index: -2;
}

/* Noise Texture */

.main::after {
  content: "";
  position: fixed;
  inset: 0;

  background-image: radial-gradient(
    rgba(255, 255, 255, 0.03) 1px,
    transparent 1px
  );

  background-size: 4px 4px;

  opacity: 0.15;

  z-index: -1;
}

/* Aurora Animation */

@keyframes auroraMove {
  0% {
    transform: scale(1) rotate(0deg);
  }

  100% {
    transform: scale(1.15) rotate(8deg);
  }
}

/* LOADER */

.loader {
  scale: 3;
  height: 50px;
  width: 40px;
}

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

@keyframes from-left {
  0% {
    z-index: 20;
    opacity: 0;
    translate: -20px -6px;
  }

  20% {
    z-index: 10;
    opacity: 1;
    translate: 0px 0px;
  }

  40% {
    z-index: 9;
    translate: 0px 4px;
  }

  60% {
    z-index: 8;
    translate: 0px 8px;
  }

  80% {
    z-index: 7;
    opacity: 1;
    translate: 0px 12px;
  }

  100% {
    z-index: 5;
    translate: 0px 30px;
    opacity: 0;
  }
}

@keyframes from-right {
  0% {
    z-index: 20;
    opacity: 0;
    translate: 20px -6px;
  }

  20% {
    z-index: 10;
    opacity: 1;
    translate: 0px 0px;
  }

  40% {
    z-index: 9;
    translate: 0px 4px;
  }

  60% {
    z-index: 8;
    translate: 0px 8px;
  }

  80% {
    z-index: 7;
    opacity: 1;
    translate: 0px 12px;
  }

  100% {
    z-index: 5;
    translate: 0px 30px;
    opacity: 0;
  }
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
    z-index: 20;
    opacity: 0;
    translate: -20px -6px;
  }

  20% {
    z-index: 10;
    opacity: 1;
    translate: 0px 0px;
  }

  40% {
    z-index: 9;
    translate: 0px 4px;
  }

  60% {
    z-index: 8;
    translate: 0px 8px;
  }

  80% {
    z-index: 7;
    opacity: 1;
    translate: 0px 12px;
  }

  100% {
    z-index: 5;
    translate: 0px 30px;
    opacity: 0;
  }
}

@keyframes from-right {
  0% {
    z-index: 20;
    opacity: 0;
    translate: 20px -6px;
  }

  20% {
    z-index: 10;
    opacity: 1;
    translate: 0px 0px;
  }

  40% {
    z-index: 9;
    translate: 0px 4px;
  }

  60% {
    z-index: 8;
    translate: 0px 8px;
  }

  80% {
    z-index: 7;
    opacity: 1;
    translate: 0px 12px;
  }

  100% {
    z-index: 5;
    translate: 0px 30px;
    opacity: 0;
  }
}






.intro-loader {
  position: fixed;
  inset: 0;
  background: #030712;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 16px;
  z-index: 9999;
}

.intro-title {
  color: #d3e97a;
  font-size: 1rem;
  letter-spacing: 4px;
  text-transform: uppercase;
  opacity: 0;
  animation: fadeUp .8s forwards;
}

.intro-name {
  color: white;
  font-size: clamp(2rem, 6vw, 4rem);
  font-weight: 700;
  opacity: 0;
  animation: fadeUp .8s .3s forwards;
}

.intro-text {
  color: #9ca3af;
  opacity: 0;
  animation: fadeUp .8s .6s forwards;
}

.loading-bar {
  width: 250px;
  height: 4px;
  background: rgba(255,255,255,.1);
  border-radius: 20px;
  overflow: hidden;
  margin-top: 20px;
}

.loading-bar span {
  display: block;
  height: 100%;
  width: 0%;
  background: #d3e97a;
  animation: loading 2s ease forwards;
}

@keyframes loading {
  to {
    width: 100%;
  }
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
