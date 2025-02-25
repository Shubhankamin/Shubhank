<template>
  <div>
    <v-container fluid class="main pt-md-16">
      <v-row class="mt-md-14 mt-3" data-aos="fade-up" data-aos-duration="3000">
        <v-col cols="12" md="6" class="pt-md-16 pt-md-7">
          <div class="px-md-16">
            <div class="pt-md-14 d-flex flex-column justify-center">
              <h1 class="heading text-white bebas-Bold-h1">hi, i am</h1>
              <h1 class="heading bebas-Bold-h1">shubhank amin.</h1>
            </div>
            <div class="d-flex justify-center pr-5 pt-2">
              <p class="text-white manrope-regular-h5">
                I am a passionate Front-End Developer with a Bachelor's in
                Computer Applications (BCA) and experience in building dynamic,
                high-performance web applications. I specialize in Nuxt 3, Vue
                3, HTML, CSS, JavaScript, and Supabase, with a strong eye for
                design using Figma.
              </p>
            </div>
            <div class="contact-section pt-10">
              <NuxtLink to="/#connect" style="text-decoration: none">
                <button class="contact-button">
                  CONTACT ME <span class="dot manrope-regular-h5"></span>
                </button>
              </NuxtLink>

              <div class="icons">
                <a
                  href="https://www.linkedin.com/in/shubhank-amin-a7b231225/"
                  style="text-decoration: none"
                  target="_blank"
                >
                  <v-icon class="icon linkedin">mdi-linkedin</v-icon>
                </a>
                <a
                  href="https://github.com/Shubhankamin?tab=repositories"
                  style="text-decoration: none"
                  target="_blank"
                >
                  <v-icon class="icon linkedin">mdi-github</v-icon>
                </a>
              </div>
            </div>
          </div>
        </v-col>
        <v-col cols="12" md="6" class="pt-10 pt-md-0">
          <div>
            <v-img
              src="/images/me.jpg"
              class="profile d-none d-md-block"
              height="550"
            >
            </v-img>
            <v-img
              src="/images/me.jpg"
              class="profile d-block d-md-none"
              height="550"
            >
            </v-img>
          </div>
        </v-col>
      </v-row>
      <v-divider
        :thickness="3"
        class="border-opacity-50 mt-5"
        color="white"
      ></v-divider>
    </v-container>
  </div>
</template>
<style scoped>
.heading {
  text-transform: uppercase;
  color: #d3f576;
}

.contact-section {
  display: flex;
  align-items: center;
}

.main {
  background-image: url("images/meteor.png");
  background-size: cover;
}

.contact-button {
  background-color: #d3f576; /* light green */
  border: none;
  border-radius: 30px;
  padding: 10px 20px;
  font-weight: bold;
  cursor: pointer;
  position: relative;
  display: flex;
  align-items: center;
  color: black;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.contact-button:hover {
  background-color: #0077b5; /* LinkedIn blue */
  color: #d3f576; /* light green */
}

.contact-button:hover .dot {
  background-color: #d3f576; /* Blue for dot when hovered */
}

.contact-button .dot {
  width: 8px;
  height: 8px;
  background-color: black; /* Default dot color */
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
  background-color: #333; /* dark background */
  display: flex;
  align-items: center;
  justify-content: center;
  color: #d3f576; /* light green */
  font-size: 20px;
  text-decoration: none;
  cursor: pointer;
}

.icon.linkedin:hover {
  background-color: #0077b5; /* LinkedIn blue */
}

.icon.github:hover {
  background-color: #333; /* GitHub dark */
}
</style>
