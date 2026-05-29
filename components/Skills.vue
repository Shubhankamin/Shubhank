```vue id="gnf8sl"
<template>
  <div>
    <v-divider
      :thickness="3"
      class="border-opacity-50 mt-5"
      color="white"
    ></v-divider>
    <v-container fluid class="main text-white px-md-15 py-16">
      <!-- HEADER -->

      <div data-aos="fade-up" data-aos-duration="1000">
        <v-row>
          <v-col cols="12" md="6">
            <h1 class="heading bebas-Bold-h1">Tech Stack</h1>

            <p class="subtitle mt-4 manrope-regular-h5">
              Technologies and tools I use to build scalable, performant, and
              modern applications.
            </p>
          </v-col>
        </v-row>
      </div>

      <!-- SWIPER -->

      <div class="skills-wrapper pt-12">
        <Swiper
          :modules="[Autoplay]"
          :slides-per-view="2"
          :space-between="20"
          :loop="true"
          :speed="2500"
          :autoplay="{
            delay: 0,
            disableOnInteraction: false,
          }"
          :breakpoints="{
            640: {
              slidesPerView: 3,
            },
            960: {
              slidesPerView: 5,
            },
            1280: {
              slidesPerView: 6,
            },
          }"
        >
          <SwiperSlide v-for="(skill, index) in skills" :key="index">
            <div class="skill-card">
              <img :src="skill.logo" :alt="skill.name" class="skill-logo" />

              <p class="skill-name">
                {{ skill.name }}
              </p>
            </div>
          </SwiperSlide>
        </Swiper>
      </div>
    </v-container>
  </div>
</template>
<script setup>
import { Swiper, SwiperSlide } from "swiper/vue";

import { Autoplay } from "swiper/modules";

import "swiper/css";

const skills = [
  {
    name: "Nuxt 3",
    logo: "/images/logos/nuxt.svg",
  },

  {
    name: "Vue 3",
    logo: "/images/logos/vue.png",
  },

  {
    name: "Vuetify",
    logo: "/images/logos/vue-1.svg",
  },

  {
    name: "JavaScript",
    logo: "/images/logos/js.png",
  },

  {
    name: "TypeScript",
    logo: "/images/logos/ts.svg",
  },

  {
    name: "Firebase",
    logo: "/images/logos/fire.svg",
  },

  {
    name: "Supabase",
    logo: "/images/logos/supa.svg",
  },

  {
    name: "Figma",
    logo: "/images/logos/figma.png",
  },

  {
    name: "Canva",
    logo: "/images/logos/canva.png",
  },

  {
    name: "React Native",
    logo: "/images/logos/react.png",
  },

  {
    name: "FlutterFlow",
    logo: "/images/logos/flutter.png",
  },

{
  name: "C++",
  logo: "/images/logos/c++.png",
},

{
  name: "Java",
  logo: "/images/logos/java.png",
},
];
</script>
<style scoped>
.main {
  position: relative;

  overflow: hidden;
}

/* HEADER */

.heading {
  line-height: 0.95;
}

.subtitle {
  color: rgba(255, 255, 255, 0.72);

  line-height: 1.8;

  max-width: 650px;
}

/* SWIPER */

.skills-wrapper {
  position: relative;

  overflow: hidden;

  padding: 40px 0;
}

/* SKILL CARD */

.skill-card {
  position: relative;

  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: center;

  gap: 16px;

  padding: 30px 20px;

  transition:
    transform 0.35s ease,
    opacity 0.35s ease;
}

/* LOGO */

.skill-logo {
  width: 72px;
  height: 72px;

  object-fit: contain;

  position: relative;

  transition:
    transform 0.35s ease,
    filter 0.35s ease;

  filter: drop-shadow(0 10px 20px rgba(0, 0, 0, 0.25));
}

/* SUBTLE GLOW */

.skill-card::before {
  content: "";

  position: absolute;

  width: 120px;
  height: 120px;

  background: radial-gradient(
    circle,
    rgba(255, 255, 255, 0.08),
    transparent 70%
  );

  border-radius: 50%;

  opacity: 0;

  transition: opacity 0.35s ease;

  filter: blur(20px);
}

/* NAME */

.skill-name {
  color: rgba(255, 255, 255, 0.7);

  font-size: 14px;

  font-weight: 500;

  letter-spacing: 0.5px;

  transition:
    color 0.35s ease,
    transform 0.35s ease;
}

/* HOVER */

.skill-card:hover {
  transform: translateY(-6px);
}

.skill-card:hover::before {
  opacity: 1;
}

.skill-card:hover .skill-logo {
  transform: translateY(-4px) scale(1.08);

  filter: drop-shadow(0 20px 30px rgba(0, 0, 0, 0.35));
}

.skill-card:hover .skill-name {
  color: white;

  transform: translateY(-2px);
}
</style>
