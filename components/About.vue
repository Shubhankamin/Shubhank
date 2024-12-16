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
              I am a front-end developer based in Sydney. Has Mechanical
              Engineering background.
            </p>
            <p class="pt-2 manrope-regular-h5">
              I am a front-end developer based in Sydney looking for exciting
              opportunities. Has Mechanical Engineering background. Likes to
              focus on accessibility when developing. Passionate and curious
              about solving problems. Currently, I’m exploring Reactjs, Webflow
              and a bit of Designing. While I am not programming, I enjoy
              playing football, photography and playing Valorant. Learning more
              to improve skill.
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
  background-image: url("images/meteor.svg");
  background-size: cover;
}
</style>
