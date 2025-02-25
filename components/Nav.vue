<template>
  <div style="position: fixed; z-index: 999999" class="w-100">
    <v-container class="bg d-none d-md-block py-0" style="border: none" fluid>
      <v-row class="align-center py-0">
        <v-col class="" cols="1">
          <div>
            <NuxtLink
              to="/"
              style="text-decoration: none; scroll-behavior: smooth"
            >
              <p class="links bebas-Bold-h3">SHUBHANK</p>
            </NuxtLink>
          </div>
        </v-col>
        <v-col cols="9" class="d-flex justify-center">
          <div>
            <v-img src="/images/logo-2.png" class="logo" @click="downloadPDF" />
          </div>
        </v-col>
        <v-col cols="2">
          <div class="d-flex ga-5 justify-space-between">
            <NuxtLink
              to="/#work"
              style="text-decoration: none; scroll-behavior: smooth"
              class="links"
            >
              <p class="manrope-regular-h5">WORK</p>
            </NuxtLink>
            <NuxtLink
              to="/#about"
              style="text-decoration: none; scroll-behavior: smooth"
              class="links"
            >
              <p class="manrope-regular-h5">ABOUT</p>
            </NuxtLink>
            <NuxtLink
              to="/#connect"
              style="text-decoration: none; scroll-behavior: smooth"
              class="links"
            >
              <p class="manrope-regular-h5">CONTACT</p>
            </NuxtLink>
          </div>
        </v-col>
      </v-row>
    </v-container>
    <v-container class="d-block d-md-none bg-black" fluid>
      <v-row>
        <v-col class="d-flex justify-space-between">
          <div>
            <NuxtLink
              to="/"
              style="
                text-decoration: none;
                color: white;
                scroll-behavior: smooth;
              "
            >
              <p class="bebas-Bold-h3">SHUBHANK</p>
            </NuxtLink>
          </div>
          <div class="d-block d-md-none">
            <div class="background" @click="openDrawer">
              <button class="menu__icon">
                <span></span>
                <span></span>
                <span></span>
              </button>
            </div>
          </div>
          <v-navigation-drawer v-model="drawer" class="bg-black" temporary>
            <v-row>
              <v-col class="">
                <div class="px-0 pt-5">
                  <v-img
                    src="/images/logo-2.png"
                    class="logo"
                    @click="downloadPDF"
                  />
                </div>
                <div class="px-4 pt-2 d-flex flex-column ga-5">
                  <NuxtLink
                    to="/"
                    style="
                      text-decoration: none;
                      color: white;
                      scroll-behavior: smooth;
                    "
                  >
                    <p class="manrope-regular-h4">HOME</p>
                  </NuxtLink>
                  <NuxtLink
                    to="/#work"
                    style="
                      text-decoration: none;
                      color: white;
                      scroll-behavior: smooth;
                    "
                  >
                    <p class="manrope-regular-h4">WORK</p>
                  </NuxtLink>
                  <NuxtLink
                    to="/#about"
                    style="
                      text-decoration: none;
                      color: white;
                      scroll-behavior: smooth;
                    "
                  >
                    <p class="manrope-regular-h4">ABOUT</p>
                  </NuxtLink>
                  <NuxtLink
                    to="/#connect"
                    style="
                      text-decoration: none;
                      color: white;
                      scroll-behavior: smooth;
                    "
                  >
                    <p class="manrope-regular-h4">CONTACT</p>
                  </NuxtLink>
                </div>
              </v-col>
            </v-row>
          </v-navigation-drawer>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script setup>
const drawer = ref(false);

const openDrawer = () => {
  drawer.value = true;
};

const downloadPDF = () => {
  const link = document.createElement("a");
  link.href = "/files/resume.pdf"; // Replace with your actual PDF file path
  link.download = "Shubhank's Resume.pdf"; // Set the filename for the download
  link.click();
};
</script>

<style scoped>
.links {
  color: white;
  transition: 0.4sec;
}

.logo {
  width: 100px;
  padding: 0;
  cursor: pointer;
}

.links:hover {
  color: #d3f576;
}

/* From Uiverse.io by ArturCodeCraft */
/* <reset-style> ============================ */
button {
  border: none;
  background: none;
  padding: 0;
  margin: 0;
  cursor: pointer;
  font-family: inherit;
}
/* ============================ */
/* <style for bg> ======== */
.background {
  border-radius: 16px;
  mix-blend-mode: luminosity;
  backdrop-filter: blur(15px);
  display: flex;
  justify-content: center;
  align-items: center;
}

.bg {
  background: rgb(1, 17, 20);
  background: linear-gradient(
    90deg,
    rgba(1, 17, 20, 1) 0%,
    rgba(2, 27, 42, 1) 48%,
    rgba(0, 0, 0, 1) 100%
  );
}

/* <style for menu__icon> ======== */
.menu__icon {
  width: 20px;
  height: 15px;
}

.menu__icon span {
  display: block;
  width: 100%;
  height: 0.125rem;
  border-radius: 2px;
  background-color: white;
  box-shadow: 0 0.5px 2px 0 hsla(0, 0%, 0%, 0.2);
  transition: background-color 0.4s;
  position: relative;
}

.menu__icon span + span {
  margin-top: 0.375rem;
}

.menu__icon span:nth-child(1) {
  animation: ease 0.8s menu-icon-top-2 forwards;
}

.menu__icon span:nth-child(2) {
  animation: ease 0.8s menu-icon-scaled-2 forwards;
}

.menu__icon span:nth-child(3) {
  animation: ease 0.8s menu-icon-bottom-2 forwards;
}

.menu__icon:hover span:nth-child(1) {
  animation: ease 0.8s menu-icon-top forwards;
}

.menu__icon:hover span:nth-child(2) {
  animation: ease 0.8s menu-icon-scaled forwards;
}

.menu__icon:hover span:nth-child(3) {
  animation: ease 0.8s menu-icon-bottom forwards;
  background-color: #d3f576;
}

@keyframes menu-icon-top {
  0% {
    top: 0;
    transform: rotate(0);
  }

  50% {
    top: 0.5rem;
    transform: rotate(0);
  }

  100% {
    top: 0.5rem;
    transform: rotate(45deg);
  }
}

@keyframes menu-icon-top-2 {
  0% {
    top: 0.5rem;
    transform: rotate(45deg);
  }

  50% {
    top: 0.5rem;
    transform: rotate(0);
  }

  100% {
    top: 0;
    transform: rotate(0);
  }
}

@keyframes menu-icon-bottom {
  0% {
    bottom: 0;
    transform: rotate(0);
  }

  50% {
    bottom: 0.5rem;
    transform: rotate(0);
  }

  100% {
    bottom: 0.5rem;
    transform: rotate(135deg);
  }
}

@keyframes menu-icon-bottom-2 {
  0% {
    bottom: 0.5rem;
    transform: rotate(135deg);
  }

  50% {
    bottom: 0.5rem;
    transform: rotate(0);
  }

  100% {
    bottom: 0;
    transform: rotate(0);
  }
}

@keyframes menu-icon-scaled {
  50% {
    transform: scale(0);
  }

  100% {
    transform: scale(0);
  }
}

@keyframes menu-icon-scaled-2 {
  0% {
    transform: scale(0);
  }

  50% {
    transform: scale(0);
  }

  100% {
    transform: scale(1);
  }
}
</style>
