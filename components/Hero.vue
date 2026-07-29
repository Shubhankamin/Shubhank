<template>
  <div>
    <v-container fluid class="main pt-md-16">
      <v-row
        class="mt-md-14 mt-8 mb-10"
        data-aos="fade-up"
        data-aos-duration="2000"
      >
        <v-col cols="12" md="8" sm="6" class="pt-md-16 pt-md-7">
          <div class="px-md-16">
            <div class="pt-md-14 d-flex flex-column justify-center">
              <h1 class="heading text-white bebas-Bold-h1">hi, i am</h1>
              <h1 class="heading bebas-Bold-h1" style="line-height: 1.3">
                shubhank amin.
              </h1>
            </div>
            
            <div class="d-flex pl-8 pt-2">
              <p class="text-white manrope-regular-h5">
                I’m a Front-End Developer currently pursuing a Master of
                Computer Applications (MCA) at MIT Manipal, with experience
                delivering production-ready web applications across startup,
                freelance, and internship environments. My expertise lies in
                Nuxt 3, Vue 3, JavaScript, and modern frontend architecture,
                complemented by hands-on experience with React Native, Next.js,
                Firebase, Supabase, REST APIs, and responsive UI engineering. I
                enjoy transforming complex requirements into intuitive,
                high-performance digital experiences and continuously exploring
                emerging technologies to build better products.
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
        <v-col cols="12" md="4" sm="6" class="pt-10 pt-sm-0 pt-md-0 pr-md-16">
          <div>
            <!-- <v-img
              src="/images/me-new.PNG"
              class="profile d-none d-md-block"
              lazy-src="/images/me-resized-new-1.png"
              height="600"
              style="border-radius: 20px"
            >
            </v-img> -->
            <v-img
              src="/images/me/me_10.jpeg"
              class="profile d-none d-md-block"
              lazy-src="/images/me/me_4_lazy.jpeg"
              cover
              height="800"
              style="border-radius: 20px; "
            >
            </v-img>
            <v-img
              src="/images/me/me_11.jpeg"
              class="profile d-block d-md-none"
              lazy-src="/images/me/me_4_lazy.jpeg"
              style="border-radius: 20px"
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

/* .main {
  background-image: url("/images/meteor.png");
  background-size: cover;
  height: 100%;
  width: 100%;
} */

.heading {
  text-transform: uppercase;
  color: #d3f576;
  line-height: 0.9;
}

/* HERO SECTION */

.main {
  position: relative;

  width: 100%;

  overflow: hidden;

  background: #030712;

  isolation: isolate;
}

/* Aurora Background */

/* .main::before {
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
} */

.main {
  position: relative;
  width: 100%;
  overflow: hidden;
  background: transparent;
}



/* CONTACT SECTION */

.contact-section {
  display: flex;
  align-items: center;
  gap: 18px;
  flex-wrap: wrap;
}

/* BUTTON */

.contact-button {
  background: rgba(211, 245, 118, 0.95);

  border: 1px solid rgba(255, 255, 255, 0.08);

  border-radius: 999px;

  padding: 14px 28px;

  font-weight: 700;

  cursor: pointer;

  position: relative;

  display: flex;
  align-items: center;
  gap: 10px;

  color: black;

  transition: all 0.35s ease;

  backdrop-filter: blur(12px);

  box-shadow: 0 10px 30px rgba(211, 245, 118, 0.12);
}

.contact-button:hover {
  transform: translateY(-4px);

  background: #d3f576;

  box-shadow: 0 15px 40px rgba(211, 245, 118, 0.2);
}

/* DOT */

.contact-button .dot {
  width: 8px;
  height: 8px;

  background-color: black;

  border-radius: 50%;
}

/* ICONS */

.icons {
  display: flex;
  gap: 14px;
}

/* ICON STYLE */

.icon {
  width: 48px;
  height: 48px;

  border-radius: 50%;

  background: rgba(255, 255, 255, 0.05);

  border: 1px solid rgba(255, 255, 255, 0.08);

  backdrop-filter: blur(10px);

  display: flex;
  align-items: center;
  justify-content: center;

  color: #d3f576;

  font-size: 22px;

  transition: all 0.35s ease;

  cursor: pointer;
}

.icon:hover {
  transform: translateY(-5px);

  background: rgba(211, 245, 118, 0.12);

  box-shadow: 0 10px 30px rgba(211, 245, 118, 0.12);
}

/* PROFILE IMAGE */

.profile {
  position: relative;

  border-radius: 50px;

  overflow: hidden;
}

/* IMAGE GLOW */

.profile::before {
  content: "";

  position: absolute;

  inset: -40px;

  background: radial-gradient(
    circle,
    rgba(132, 204, 22, 0.18),
    transparent 70%
  );

  filter: blur(60px);

  z-index: -1;
}

/* TEXT */

.manrope-regular-h5 {
  color: rgba(255, 255, 255, 0.72);

  line-height: 1.8;

  max-width: 700px;
}

/* DIVIDER */

.v-divider {
  opacity: 0.2;
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
  transition:
    background-color 0.3s ease,
    color 0.3s ease;
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
