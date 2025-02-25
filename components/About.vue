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
              Currently working at **Exelon Circuits Private Limited** as a
              Front-End Developer, I also take on exciting freelance projects,
              helping businesses and individuals bring their digital ideas to
              life. With a strong foundation in modern web technologies, I have
              worked with **Nuxt.js, Vue.js, React.js, Next.js, FlutterFlow,
              React Native, Supabase, Figma, Canva, and core web technologies
              like HTML, CSS, and JavaScript**. I am deeply interested in UI/UX
              design and always strive to create user-friendly, accessible, and
              high-performance applications. Outside of coding, I enjoy
              exploring new tech trends, refining my design skills, and taking
              on creative challenges.
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
.heading {
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
}
</style>
