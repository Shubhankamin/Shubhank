<template>
  <div>
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

      <p class="intro-text">Every line of code tells a story. This is mine.</p>
      <div class="loading-bar">
        <span></span>
      </div>
    </div>

    <div v-else>
      <NuxtLayout>
        <v-app>
          <NuxtPage />
        </v-app>
      </NuxtLayout>
    </div>
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
</script>

<style scoped>
/* Fullscreen container to center the loader */
.fullscreen-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: black; /* Optional: background color */
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
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 18px;
  z-index: 9999;
}

/* Background Glow */

.bg-blur {
  position: absolute;
  border-radius: 50%;
  filter: blur(120px);
  animation: float 8s ease-in-out infinite;
}

.blur-1 {
  width: 300px;
  height: 300px;
  background: rgba(211, 233, 122, 0.15);
  top: 10%;
  left: 15%;
}

.blur-2 {
  width: 250px;
  height: 250px;
  background: rgba(100, 255, 218, 0.12);
  bottom: 10%;
  right: 15%;
}

.intro-title {
  color: #d3e97a;
  letter-spacing: 6px;
  font-size: 0.85rem;
  font-weight: 600;
  opacity: 0;
  animation: fadeUp 0.8s forwards;
}

.intro-name {
  font-size: clamp(3rem, 8vw, 6rem);
  font-weight: 800;
  line-height: 1;
  text-align: center;
  background: linear-gradient(90deg, #ffffff, #d3e97a, #ffffff);
  background-size: 200%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation:
    fadeUp 0.8s 0.3s forwards,
    shine 4s linear infinite;
  opacity: 0;
}

.intro-text {
  max-width: 600px;
  text-align: center;
  color: #9ca3af;
  font-size: 1.1rem;
  line-height: 1.7;
  padding: 0 20px;
  opacity: 0;
  animation: fadeUp 0.8s 0.6s forwards;
}

.loading-bar {
  width: 280px;
  height: 5px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 20px;
  overflow: hidden;
  margin-top: 20px;
}

.loading-bar span {
  display: block;
  height: 100%;
  width: 0;
  background: linear-gradient(90deg, #d3e97a, #ffffff, #d3e97a);
  box-shadow: 0 0 20px #d3e97a;
  animation: loading 2.5s ease forwards;
}

.loading-text {
  color: #6b7280;
  font-size: 0.9rem;
  letter-spacing: 2px;
}

@keyframes loading {
  to {
    width: 100%;
  }
}

@keyframes shine {
  from {
    background-position: 0%;
  }
  to {
    background-position: 200%;
  }
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes float {
  50% {
    transform: translateY(-30px);
  }
}
</style>
