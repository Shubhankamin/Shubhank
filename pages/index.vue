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
    <div class="mouse-follower">
      <div class="energy-ring"></div>
      <span class="particle particle-1"></span>
      <span class="particle particle-2"></span>
      <span class="particle particle-3"></span>
    </div>
    <Nav />
    <div class="d-none d-md-block" id="reveal">
      <Reveal />
    </div>

    <section id="hero" class="reveal-section">
      <Hero class="mt-10 mt-md-0" />
    </section>

    <section id="work" class="reveal-section">
      <Projects />
    </section>

    <section id="specialize" class="reveal-section">
      <Specialize />
    </section>

    <section id="skills" class="reveal-section">
      <Skills />
    </section>

    <section id="about" class="reveal-section">
      <About />
    </section>

    <section id="connect" class="reveal-section">
      <Connect />
    </section>

    <ResumeAI />
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
import { useScrollAurora } from "~/composables/useScrollAurora";
import { useMouseFollower } from "~/composables/useMouseFollower";
import Reveal from "~/components/Reveal.vue";
import ResumeAI from "~/components/ResumeAI.vue";
useScrollAurora();
useMouseFollower();

const loading = ref(true);

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

:root {
  --aurora-x: 15%;
  --aurora-y: 20%;
  --aurora-color-1: 59, 130, 246;
  --aurora-color-2: 132, 204, 22;
}

.main::before {
  content: "";
  position: fixed;
  inset: 0;

  background:
    radial-gradient(
      circle at var(--aurora-x) var(--aurora-y),
      rgba(var(--aurora-color-1), 0.18),
      transparent 35%
    ),
    radial-gradient(
      circle at calc(100% - var(--aurora-x)) calc(100% - var(--aurora-y)),
      rgba(var(--aurora-color-2), 0.14),
      transparent 30%
    );

  filter: blur(90px);

  transition: background 1.2s cubic-bezier(0.22, 1, 0.36, 1);

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
  animation: fadeUp 0.8s forwards;
}

.intro-name {
  color: white;
  font-size: clamp(2rem, 6vw, 4rem);
  font-weight: 700;
  opacity: 0;
  animation: fadeUp 0.8s 0.3s forwards;
}

.intro-text {
  color: #9ca3af;
  opacity: 0;
  animation: fadeUp 0.8s 0.6s forwards;
}

.loading-bar {
  width: 250px;
  height: 4px;
  background: rgba(255, 255, 255, 0.1);
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

/* .mouse-follower {
  position: fixed;
  top: 0;
  left: 0;
  width: 400px;
  height: 400px;
  pointer-events: none;
  z-index: -2;

  transform: translate(
    calc(var(--follower-x, 50vw) - 50%),
    calc(var(--follower-y, 50vh) - 50%)
  );

  background: radial-gradient(
    circle,
    rgba(211, 245, 118, 0.35),
    transparent 70%
  );

  filter: blur(40px);
}

.main::before {
  z-index: -3;
}
.mouse-follower {
  z-index: -2;
} 
.main::after {
  z-index: -1;
}  */

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

@media (max-width: 1024px) {
  .mouse-follower {
    display: none;
  }
}
</style>
