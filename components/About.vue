<template>
  <div>
    <v-container fluid class="main text-white">
      <div data-aos="fade-up" data-aos-duration="3000">
        <v-divider
          :thickness="3"
          class="border-opacity-50 mt-5"
          color="white"
        ></v-divider>
        <v-row class="px-md-12 pt-10">
          <v-col cols="12" md="6">
            <h1 class="heading bebas-Bold-h1">ABOUT ME</h1>
          </v-col>
          <v-col cols="12" md="6" class="pt-5 px-2">
            <p class="content manrope-Bold-h4">
              I am a Front-End Developer based in Udupi, passionate about
              crafting seamless and engaging web experiences.
            </p>
            <p class="pt-2 manrope-regular-h5">
              I have previously worked in a startup environment, where I honed
              my skills in modern web technologies and gained hands-on
              experience in building scalable and high-performance applications.
              My expertise includes
              <strong
                >Nuxt.js, Vue.js, React.js, Next.js, FlutterFlow, React Native,
                Supabase, Figma, Canva, and core web technologies like HTML,
                CSS, and JavaScript</strong
              >. I am passionate about UI/UX design and always strive to create
              intuitive, user-friendly, and accessible web experiences. Beyond
              coding, I enjoy exploring new tech trends, refining my design
              skills, and taking on creative challenges.
            </p>

            <NuxtLink to="/about" class="link pointer">
              <p class="link mt-md-10 my-5 manrope-regular-h5">More About Me</p>
            </NuxtLink>
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
/* .heading {
  text-transform: uppercase;
}

.link {
  color: #d3f576;
}

.main {
  background-image: url("/images/meteor.png");
  background-size: cover;
  height: 100%;
  width: 100%;
} */




.heading {
  text-transform: uppercase;
  line-height: 0.95;
}

/* ABOUT SECTION */

.main {
  position: relative;

  background: rgba(255, 255, 255, 0.02);

  backdrop-filter: blur(10px);

  border-top: 1px solid rgba(255,255,255,0.06);

  border-bottom: 1px solid rgba(255,255,255,0.06);

  overflow: hidden;
}

/* Glow effect */

.main::before {
  content: "";

  position: absolute;

  width: 500px;
  height: 500px;

  background: radial-gradient(
    circle,
    rgba(132, 204, 22, 0.08),
    transparent 70%
  );

  top: -150px;
  right: -100px;

  filter: blur(80px);

  z-index: 0;
}

/* Optional secondary glow */

.main::after {
  content: "";

  position: absolute;

  width: 400px;
  height: 400px;

  background: radial-gradient(
    circle,
    rgba(59,130,246,0.08),
    transparent 70%
  );

  bottom: -150px;
  left: -100px;

  filter: blur(90px);

  z-index: 0;
}

/* Keep content above effects */

.main > * {
  position: relative;
  z-index: 1;
}

/* Link Styling */

.link {
  color: #d3f576;
  text-decoration: none;
  position: relative;
  width: fit-content;
  transition: 0.3s ease;
}

.link::after {
  content: "";

  position: absolute;
  left: 0;
  bottom: -4px;

  width: 0%;
  height: 2px;

  background: #d3f576;

  transition: width 0.3s ease;
}

.link:hover::after {
  width: 100%;
}

.link:hover {
  opacity: 0.8;
}

/* Better text readability */

.content {
  max-width: 700px;
  line-height: 1.4;
}

</style>
