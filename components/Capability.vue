<template>
  <div class="main text-white pt-5">
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="6">
          <h1 class="heading bebas-Bold-h1">MY CAPABILITIES</h1>
        </v-col>
        <v-col cols="12" md="6">
          <p class="manrope-regular-h5">
            I develop high-performance web interfaces using modern frameworks
            like Nuxt 3, Vue 3, and React. My capabilities include building
            responsive UI, integrating APIs, creating admin dashboards,
            optimizing performance, and delivering clean, maintainable code. I
            enjoy solving practical problems with efficient front-end
            architecture and continuously expanding my skill set to stay aligned
            with industry standards.
          </p>

          <div class="d-flex ga-4 flex-wrap pt-5">
            <div
              v-for="(skill, index) in skills"
              :key="index"
              class="d-flex skills px-2 py-1 ga-2 align-center"
            >
              <p class="manrope-Bold-h5">{{ skill.name }}</p>
              <v-icon>{{ skill.icon }}</v-icon>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script setup>
const skills = [
  { name: "Nuxt 3", icon: "mdi-nuxt" },
  { name: "Vue 3", icon: "mdi-vuejs" },
  { name: "JavaScript", icon: "mdi-language-javascript" },
  { name: "TypeScript", icon: "mdi-language-typescript" },
  { name: "React", icon: "mdi-react" },
  { name: "Next.js", icon: "mdi-react" },
  { name: "Vuetify", icon: "mdi-vuetify" },
  { name: "Tailwind CSS", icon: "mdi-tailwind" },
  { name: "Firebase", icon: "mdi-firebase" },
  { name: "Supabase", icon: "mdi-database" },
  { name: "REST APIs", icon: "mdi-api" },
  { name: "Figma", icon: "mdi-figma" },
  { name: "React Native", icon: "mdi-cellphone" },
  { name: "Git", icon: "mdi-git" },
  { name: "C++", icon: "mdi-language-cpp" },
  { name: "Python", icon: "mdi-language-python" },
];
</script>
<style scoped>
.heading {
  text-transform: uppercase;
}

.skills {
  background-color: rgb(53, 52, 52);
  border-radius: 20px;
}

.content {
  font-size: 22px;
  font-weight: 600;
}
.link {
  color: #d3f576;
}
/* 
.main {
  background-image: url("/images/meteor.png");
  background-size: cover;
  height: 100%;
  width: 100%;
} */


/* .main {
  position: relative;

  padding: 120px 0;

  overflow: hidden;
}


.main::before {
  content: "";

  position: absolute;

  width: 500px;
  height: 500px;

  background:
    radial-gradient(
      circle,
      rgba(132,204,22,0.08),
      transparent 70%
    );

  top: -200px;
  right: -150px;

  filter: blur(90px);

  pointer-events: none;
} */

.main {
  position: relative;
  width: 100%;
  overflow: hidden;
  background: transparent;
}

/* HEADING */

.heading {
  text-transform: uppercase;

  /* color: #d3f576; */

  line-height: 0.95;

  max-width: 500px;
}

/* TEXT */

.manrope-regular-h5 {
  color: rgba(255,255,255,0.72);

  line-height: 1.9;

  max-width: 720px;
}

/* SKILLS WRAPPER */

.skills {
  position: relative;

  padding: 12px 18px;

  border-radius: 999px;

  background:
    rgba(255,255,255,0.04);

  border:
    1px solid rgba(255,255,255,0.08);

  backdrop-filter:
    blur(12px);

  overflow: hidden;

  transition:
    transform 0.35s ease,
    border-color 0.35s ease,
    background 0.35s ease,
    box-shadow 0.35s ease;
}

.skills::before {
  content: "";

  position: absolute;

  width: 100px;
  height: 100px;

  top: -50px;
  right: -50px;

  background:
    radial-gradient(
      circle,
      rgba(211,245,118,0.12),
      transparent 70%
    );

  opacity: 0;

  transition: opacity 0.35s ease;
}

.skills:hover {
  transform:
    translateY(-4px);

  border-color:
    rgba(211,245,118,0.18);

  box-shadow:
    0 10px 30px rgba(0,0,0,0.25);
}

.skills:hover::before {
  opacity: 1;
}

.skills p {
  margin: 0;

  color: white;

  font-size: 14px;

  font-weight: 600;
}

.skills .v-icon {
  color: #d3f576;

  font-size: 18px;

  transition: transform 0.35s ease;
}

.skills:hover .v-icon {
  transform: scale(1.15);
}

/* CONTENT */

.content {
  font-size: 22px;

  font-weight: 600;
}

/* LINK */

.link {
  color: #d3f576;
}

</style>
