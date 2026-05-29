<template>
  <div style="position: fixed; z-index: 999999" class="w-100">
    <v-container class="bg d-none d-md-block py-0" style="border: none" fluid>
      <v-row class="align-center py-0">
        <v-col class="" cols="4">
          <div>
            <NuxtLink
              to="/"
              style="text-decoration: none; scroll-behavior: smooth"
            >
              <p class="links bebas-Bold-h3">SHUBHANK</p>
            </NuxtLink>
          </div>
        </v-col>
        <v-col cols="4" class="d-flex justify-center">
          <div>
            <v-img src="/images/logo-2.png" class="logo" @click="downloadPDF" />
          </div>
        </v-col>
        <v-col cols="4">
          <div class="d-flex ga-5 justify-space-between">
            <NuxtLink
              to="/#work"
              style="text-decoration: none; scroll-behavior: smooth"
              class="links"
            >
              <p class="manrope-regular-h5">WORK</p>
            </NuxtLink>

            <NuxtLink
              to="/#skills"
              style="text-decoration: none; scroll-behavior: smooth"
              class="links"
            >
              <p class="manrope-regular-h5">STACKS</p>
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
    <v-container class="d-block d-md-none" fluid>
      <v-row>
        <v-col
          class="d-flex justify-space-between bg-black mx-1 my-2 py-2"
          style="border-radius: 10px"
        >
          <div class="d-flex align-center">
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
          <div class="d-flex d-md-none align-center">
            <div class="background">
              <button
                class="menu__icon"
                :class="{ open: drawer }"
                @click="toggleDrawer"
              >
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
                    @click="goToHome"
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
                    to="/#skills"
                    style="
                      text-decoration: none;
                      color: white;
                      scroll-behavior: smooth;
                    "
                  >
                    <p class="manrope-regular-h4">STACK</p>
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
                  <p class="manrope-regular-h4" @click="downloadPDF">
                    DOWNLOAD RESUME
                  </p>
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
const router = useRouter();
const toggleDrawer = () => {
  drawer.value = !drawer.value;
};
const downloadPDF = () => {
  const link = document.createElement("a");
  link.href = "/files/ShubhankAmin_251090700127.pdf"; // Replace with your actual PDF file path
  link.download = "Shubhank's Resume.pdf"; // Set the filename for the download
  link.click();
};

const goToHome = () => {
  router.push("/");
};
</script>

<style scoped>
/* =========================
   NAVBAR WRAPPER
========================= */

.navbar-wrapper {
  position: fixed;

  top: 20px;

  left: 50%;

  transform: translateX(-50%);

  width: calc(100% - 40px);

  z-index: 1000;
}

/* =========================
   DESKTOP NAVBAR
========================= */

.bg {
  border-radius: 24px;

  background: rgba(255, 255, 255, 0.04);

  border: 1px solid rgba(255, 255, 255, 0.08);

  backdrop-filter: blur(18px);

  -webkit-backdrop-filter: blur(18px);

  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.35);

  padding: 12px 28px;

  transition:
    background 0.35s ease,
    border-color 0.35s ease,
    box-shadow 0.35s ease;
}

/* =========================
   LOGO
========================= */

.logo {
  width: 90px;

  cursor: pointer;

  transition:
    transform 0.35s ease,
    opacity 0.35s ease;
}

.logo:hover {
  transform: scale(1.05);

  opacity: 0.9;
}

/* =========================
   LINKS
========================= */

.links {
  position: relative;

  color: rgba(255, 255, 255, 0.78);

  text-decoration: none;

  transition:
    color 0.35s ease,
    opacity 0.35s ease;
}

/* UNDERLINE */

.links::after {
  content: "";

  position: absolute;

  left: 0;

  bottom: -6px;

  width: 0%;

  height: 2px;

  border-radius: 999px;

  background: #d3f576;

  transition: width 0.35s ease;
}

/* HOVER */

.links:hover {
  color: white;
}

.links:hover::after {
  width: 100%;
}

/* =========================
   MOBILE NAVBAR
========================= */

.mobile-nav {
  border-radius: 20px;

  background: rgba(3, 7, 18, 0.75);

  border: 1px solid rgba(255, 255, 255, 0.08);

  backdrop-filter: blur(18px);

  -webkit-backdrop-filter: blur(18px);

  padding: 14px 18px;

  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.35);
}
/* =========================
   MOBILE DRAWER
========================= */

:deep(.v-navigation-drawer) {
  background: rgba(255, 255, 255, 0.04) !important;

  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);

  border-right: 1px solid rgba(255, 255, 255, 0.08);

  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.35);
}

/* =========================
   MOBILE LINKS
========================= */

.mobile-link {
  color: rgba(255, 255, 255, 0.82);

  text-decoration: none;

  transition:
    color 0.3s ease,
    transform 0.3s ease;
}

.mobile-link:hover {
  color: #d3f576;

  transform: translateX(4px);
}

/* =========================
   MENU BUTTON RESET
========================= */

button {
  border: none;

  background: none;

  padding: 0;

  margin: 0;

  cursor: pointer;

  font-family: inherit;
}

/* =========================
   MENU ICON
========================= */

.menu__icon {
  width: 26px;

  height: 20px;

  display: flex;

  flex-direction: column;

  justify-content: space-between;

  position: relative;
}

/* LINES */

.menu__icon span {
  width: 100%;

  height: 2px;

  border-radius: 999px;

  background: white;

  transition:
    transform 0.35s ease,
    opacity 0.35s ease,
    background 0.35s ease;
}

/* OPEN STATE */

.menu__icon.open span:nth-child(1) {
  transform: translateY(9px) rotate(45deg);
}

.menu__icon.open span:nth-child(2) {
  opacity: 0;
}

.menu__icon.open span:nth-child(3) {
  transform: translateY(-9px) rotate(-45deg);
}

/* =========================
   NAVBAR SCROLL EFFECT
========================= */

.bg:hover,
.mobile-nav:hover {
  border-color: rgba(211, 245, 118, 0.14);

  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.45);
}

/* =========================
   TYPOGRAPHY FIXES
========================= */

.bebas-Bold-h3,
.manrope-regular-h5,
.manrope-regular-h4 {
  margin: 0;
}

/* =========================
   RESPONSIVE
========================= */

@media (max-width: 960px) {
  .mobile-nav {
    background: rgba(255, 255, 255, 0.03);

    border: 1px solid rgba(255, 255, 255, 0.08);

    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    border-radius: 24px;

    padding: 12px 16px;

    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.25);
  }

  .logo {
    width: 80px;
  }
}

.bg-mobile {
}
</style>
