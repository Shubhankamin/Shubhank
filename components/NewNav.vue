<template>
  <div style="position: fixed; z-index: 999999" class="w-100">
    <!-- =========================
         DESKTOP NAV (unchanged)
    ========================== -->
    <v-container class="bg d-none d-md-block py-0" style="border: none" fluid>
      <v-row class="align-center py-0">
        <v-col class="" cols="4">
          <div>
            <NuxtLink
              to="/#reveal"
              style="text-decoration: none; scroll-behavior: smooth"
            >
              <p class="links bebas-Bold-h3">SHUBHANK</p>
            </NuxtLink>
          </div>
        </v-col>
        <v-col cols="4" class="d-flex justify-center">
          <div class="logo-wrapper">
            <v-img src="/images/logo-2.png" class="logo" @click="downloadPDF" />

            <svg
              class="resume-arrow"
              width="120"
              height="80"
              viewBox="0 0 120 80"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M15 68
       C18 45,
         42 22,
         70 18
       S102 10,
         104 12"
                fill="none"
                stroke="white"
                stroke-width="2"
                stroke-linecap="round"
                stroke-dasharray="5 6"
              />

              <!-- Arrow Head -->
              <path
                d="M95 5
       L105 12
       L94 17"
                fill="none"
                stroke="white"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>

            <div class="resume-card">
              <div class="resume-text">
                Click the logo to
                <span>download<br />my resume</span>
              </div>

              <div class="resume-icon">
                <v-icon size="22"> mdi-file-download-outline </v-icon>
              </div>
            </div>
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

    <!-- =========================
         MOBILE NAV (new)
    ========================== -->
    <div class="mnav d-block d-md-none">
      <header class="mnav-bar">
        <NuxtLink to="/" class="mnav-brand bebas-Bold-h3" @click="closeMenu">
          SHUBHANK
        </NuxtLink>

        <!-- New hamburger: pill with rolling label + morphing icon -->
        <button
          class="mnav-toggle"
          :class="{ open: drawer }"
          :aria-expanded="drawer"
          aria-controls="mnav-sheet"
          :aria-label="drawer ? 'Close navigation' : 'Open navigation'"
          @click="toggleDrawer"
        >
          <!-- <span class="mnav-label">
            <span class="mnav-label-track">
              <span>Menu</span>
              <span>Close</span>
            </span>
          </span> -->
          <span class="mnav-icon" aria-hidden="true">
            <i></i>
            <i></i>
          </span>
        </button>
      </header>

      <nav
        id="mnav-sheet"
        class="mnav-sheet"
        :class="{ open: drawer }"
        :aria-hidden="!drawer"
      >
        <ul class="mnav-links">
          <li
            v-for="(item, i) in mobileItems"
            :key="item.to"
            :style="{ '--i': i }"
          >
            <NuxtLink :to="item.to" class="mnav-link" @click="closeMenu">
              <span class="mnav-link-text">{{ item.label }}</span>
              <span class="mnav-link-bar"></span>
            </NuxtLink>
          </li>
        </ul>

        <div class="mnav-foot" :style="{ '--i': mobileItems.length }">
          <button class="mnav-resume" @click="downloadPDF">
            <span>Download resume</span>
            <v-icon size="20">mdi-file-download-outline</v-icon>
          </button>
        </div>
      </nav>
    </div>
  </div>
</template>

<script setup>
const drawer = ref(false);

const mobileItems = [
  { label: "Home", to: "/" },
  { label: "Work", to: "/#work" },
  { label: "Stack", to: "/#skills" },
  { label: "About", to: "/#about" },
  { label: "Contact", to: "/#connect" },
];

const toggleDrawer = () => {
  drawer.value = !drawer.value;
};
const closeMenu = () => {
  drawer.value = false;
};

const downloadPDF = () => {
  const link = document.createElement("a");
  link.href = "/files/ShubhankAmin_251090700127.pdf"; // Replace with your actual PDF file path
  link.download = "Shubhank's Resume.pdf"; // Set the filename for the download
  link.click();
  closeMenu();
};

// Lock page scroll while the mobile menu is open
watch(drawer, (val) => {
  if (import.meta.client) {
    document.documentElement.style.overflow = val ? "hidden" : "";
  }
});

// Close on Escape
const onKey = (e) => e.key === "Escape" && closeMenu();
onMounted(() => window.addEventListener("keydown", onKey));
onBeforeUnmount(() => {
  window.removeEventListener("keydown", onKey);
  document.documentElement.style.overflow = "";
});
</script>

<style scoped>
/* =====================================================
   DESKTOP STYLES (unchanged)
===================================================== */

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

.links {
  position: relative;
  color: rgba(255, 255, 255, 0.78);
  text-decoration: none;
  transition:
    color 0.35s ease,
    opacity 0.35s ease;
}

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

.links:hover {
  color: white;
}

.links:hover::after {
  width: 100%;
}

.bg:hover {
  border-color: rgba(211, 245, 118, 0.14);
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.45);
}

.bebas-Bold-h3,
.manrope-regular-h5 {
  margin: 0;
}

@media (max-width: 960px) {
  .logo {
    width: 80px;
  }
}

.logo-wrapper {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.resume-card {
  position: absolute;
  top: 130px;
  left: 50%;
  transform: translateX(-50%);
  width: 280px;
  padding: 14px 18px;
  border-radius: 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(12, 18, 28, 0.92);
  backdrop-filter: blur(18px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.45);
  animation: floating 3s ease-in-out infinite;
  z-index: 5;
}

.resume-text {
  color: white;
  font-size: 0.95rem;
  line-height: 1.4;
}

.resume-text span {
  color: #d3f576;
  font-weight: 700;
}

.resume-icon {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: #d3f576;
  color: #111;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
}

.resume-arrow {
  position: absolute;
  top: 60px;
  left: 0%;
  transform: translateX(-60%);
  overflow: visible;
  pointer-events: none;
}

.resume-arrow path:first-child {
  animation: dashMove 2.5s linear infinite;
}

@keyframes dashMove {
  from {
    stroke-dashoffset: 40;
  }
  to {
    stroke-dashoffset: 0;
  }
}

.logo {
  cursor: pointer;
  transition: 0.35s;
  animation: pulseLogo 3s infinite;
}

.logo:hover {
  transform: scale(1.08);
  filter: drop-shadow(0 0 18px rgba(211, 245, 118, 0.45));
}

@keyframes floating {
  0%,
  100% {
    transform: translateX(-50%) translateY(0);
  }
  50% {
    transform: translateX(-50%) translateY(-6px);
  }
}

@keyframes pulseLogo {
  0%,
  100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}

.logo-wrapper:hover::after {
  animation: logoPulse 1.5s infinite;
}

@keyframes logoPulse {
  0% {
    transform: translate(-50%, -50%) scale(0.95);
    opacity: 0.9;
  }
  100% {
    transform: translate(-50%, -50%) scale(1.35);
    opacity: 0;
  }
}

.logo-wrapper {
  position: relative;
  display: inline-flex;
  justify-content: center;
  align-items: center;
}

.logo-wrapper::before {
  content: "";
  position: absolute;
  width: 68px;
  height: 68px;
  border-radius: 50%;
  border: 2px solid #d3f576;
  opacity: 0;
  transform: scale(0.9);
  transition: 0.35s ease;
  pointer-events: none;
}

.logo-wrapper:hover::before {
  animation: pulseRing 1.4s ease infinite;
}

@keyframes pulseRing {
  0% {
    transform: scale(0.95);
    opacity: 0.9;
  }
  100% {
    transform: scale(1.35);
    opacity: 0;
  }
}

/* =====================================================
   MOBILE STYLES (new)
===================================================== */

.mnav {
  --lime: #d3f576;
  --ink: #05080f;
  --white: #ffffff;
  --muted: rgba(255, 255, 255, 0.42);
  --line: rgba(255, 255, 255, 0.1);
  --ease: cubic-bezier(0.22, 1, 0.36, 1);
}

/* =========================================================
   TOP BAR
========================================================= */

.mnav-bar {
  position: relative;
  z-index: 10;

  display: flex;
  align-items: center;
  justify-content: space-between;

  margin: 10px 12px;
  padding: 7px 7px 7px 18px;

  border: 1px solid rgba(255, 255, 255, 0.09);
  border-radius: 999px;

  background: linear-gradient(
    120deg,
    rgba(255, 255, 255, 0.055),
    rgba(255, 255, 255, 0.015)
  );

  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);

  box-shadow:
    0 12px 40px rgba(0, 0, 0, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.04);

  transition:
    border-color 0.4s ease,
    background 0.4s ease;
}

.mnav-bar:has(.mnav-toggle.open) {
  border-color: rgba(211, 245, 118, 0.2);
}

/* =========================================================
   BRAND
========================================================= */

.mnav-brand {
  position: relative;

  color: var(--white);
  text-decoration: none;
  margin: 0;

  transition:
    color 0.3s ease,
    letter-spacing 0.3s ease;
}

.mnav-brand::after {
  /* content: "PORTFOLIO"; */

  position: absolute;
  left: 0;
  bottom: -7px;

  font-family: "Manrope", sans-serif;
  font-size: 5px;
  font-weight: 700;
  letter-spacing: 0.22em;

  color: rgba(255, 255, 255, 0.3);

  transition: color 0.3s ease;
}

.mnav-brand:hover {
  color: var(--lime);
  letter-spacing: 0.04em;
}

.mnav-brand:hover::after {
  color: rgba(211, 245, 118, 0.6);
}

/* =========================================================
   MENU BUTTON
========================================================= */

.mnav-toggle {
  position: relative;

  display: flex;
  align-items: center;
  gap: 9px;

  height: 42px;
  padding: 0 7px 0 15px;

  border: 1px solid rgba(211, 245, 118, 0.22);
  border-radius: 999px;

  background: rgba(211, 245, 118, 0.08);
  color: var(--lime);

  font-family: "Manrope", sans-serif;
  font-size: 8px;
  font-weight: 800;
  letter-spacing: 0.12em;

  cursor: pointer;

  overflow: hidden;

  transition:
    background 0.35s ease,
    border-color 0.35s ease,
    transform 0.3s var(--ease);
}

.mnav-toggle:hover {
  background: rgba(211, 245, 118, 0.13);
  border-color: rgba(211, 245, 118, 0.45);
}

.mnav-toggle:active {
  transform: scale(0.95);
}

.mnav-toggle:focus-visible {
  outline: 2px solid var(--lime);
  outline-offset: 3px;
}

/* =========================================================
   MENU LABEL
========================================================= */

.mnav-label {
  height: 16px;
  overflow: hidden;
  line-height: 16px;
}

.mnav-label-track {
  display: flex;
  flex-direction: column;

  transition: transform 0.55s var(--ease);
}

.mnav-toggle.open .mnav-label-track {
  transform: translateY(-16px);
}

/* =========================================================
   MENU ICON
========================================================= */

.mnav-icon {
  position: relative;

  width: 29px;
  height: 29px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 50%;

  background: var(--lime);

  transition:
    transform 0.55s var(--ease),
    background 0.35s ease;
}

.mnav-icon::before {
  content: "";

  position: absolute;
  inset: 4px;

  border: 1px solid rgba(5, 8, 15, 0.18);
  border-radius: 50%;

  transition: transform 0.55s var(--ease);
}

.mnav-icon i {
  position: absolute;
  left: 50%;
  top: 50%;

  width: 11px;
  height: 1.5px;

  border-radius: 99px;

  background: var(--ink);

  transition:
    transform 0.5s var(--ease),
    width 0.5s var(--ease);
}

.mnav-icon i:first-child {
  transform: translate(-50%, -3px);
}

.mnav-icon i:last-child {
  transform: translate(-50%, 3px);
}

.mnav-toggle:hover .mnav-icon {
  transform: rotate(12deg);
}

.mnav-toggle:hover .mnav-icon::before {
  transform: rotate(-30deg);
}

/* OPEN */

.mnav-toggle.open .mnav-icon {
  transform: rotate(90deg);
}

.mnav-toggle.open .mnav-icon::before {
  transform: rotate(-90deg);
}

.mnav-toggle.open .mnav-icon i:first-child {
  width: 12px;
  transform: translate(-50%, -1px) rotate(45deg);
}

.mnav-toggle.open .mnav-icon i:last-child {
  width: 12px;
  transform: translate(-50%, -1px) rotate(-45deg);
}

/* =========================================================
   FULL SCREEN MENU
========================================================= */

.mnav-sheet {
  position: fixed;
  inset: 0;
  z-index: 5;

  display: flex;
  flex-direction: column;
  justify-content: space-between;

  padding: 105px 22px max(25px, env(safe-area-inset-bottom));

  background:
    radial-gradient(
      circle at 90% 8%,
      rgba(211, 245, 118, 0.07),
      transparent 28%
    ),
    radial-gradient(
      circle at 10% 90%,
      rgba(255, 255, 255, 0.035),
      transparent 25%
    ),
    var(--ink);

  clip-path: circle(0 at calc(100% - 48px) 40px);

  visibility: hidden;

  transition:
    clip-path 0.8s var(--ease),
    visibility 0s linear 0.8s;
}

.mnav-sheet::before {
  content: "NAVIGATION";

  position: absolute;
  top: 92px;
  left: 22px;

  font-family: "Manrope", sans-serif;
  font-size: 7px;
  font-weight: 800;
  letter-spacing: 0.25em;

  color: rgba(255, 255, 255, 0.25);
}

.mnav-sheet::after {
  content: "01 — 05";

  position: absolute;
  top: 92px;
  right: 22px;

  font-family: "Manrope", sans-serif;
  font-size: 7px;
  font-weight: 800;
  letter-spacing: 0.15em;

  color: rgba(211, 245, 118, 0.55);
}

.mnav-sheet.open {
  clip-path: circle(150% at calc(100% - 48px) 40px);

  visibility: visible;

  transition:
    clip-path 0.9s var(--ease),
    visibility 0s;
}

/* =========================================================
   NAV LINKS
========================================================= */

.mnav-links {
  list-style: none;
  margin: 0;
  padding: 0;
}

.mnav-links li {
  position: relative;

  opacity: 0;
  transform: translateY(35px);

  transition:
    opacity 0.25s ease,
    transform 0.6s var(--ease);
}

.mnav-sheet.open .mnav-links li,
.mnav-sheet.open .mnav-foot {
  opacity: 1;
  transform: translateY(0);

  transition:
    opacity 0.5s ease calc(0.2s + var(--i) * 0.07s),
    transform 0.65s var(--ease) calc(0.2s + var(--i) * 0.07s);
}

/* =========================================================
   LINK
========================================================= */

.mnav-link {
  position: relative;

  display: flex;
  align-items: center;

  min-height: 68px;
  padding: 7px 0;

  color: rgba(255, 255, 255, 0.9);
  text-decoration: none;

  border-bottom: 1px solid var(--line);

  overflow: hidden;
}

.mnav-link::before {
  content: "0" counter(menu-item);

  position: absolute;
  right: 2px;
  top: 50%;

  transform: translateY(-50%);

  font-family: "Manrope", sans-serif;
  font-size: 7px;
  font-weight: 700;
  letter-spacing: 0.12em;

  color: rgba(255, 255, 255, 0.2);

  transition:
    color 0.35s ease,
    transform 0.45s var(--ease);
}

/* Numbering */

.mnav-links {
  counter-reset: menu-item;
}

.mnav-links li {
  counter-increment: menu-item;
}

/* =========================================================
   LINK TEXT
========================================================= */

.mnav-link-text {
  position: relative;
  z-index: 2;

  display: inline-block;

  font-family: "Bebas Neue", sans-serif;
  font-size: clamp(3.2rem, 16vw, 5rem);
  line-height: 0.9;
  letter-spacing: 0.01em;

  transition:
    transform 0.5s var(--ease),
    color 0.35s ease;
}

/* Accent bar */

.mnav-link-bar {
  position: absolute;
  left: 0;
  bottom: -1px;

  width: 100%;
  height: 2px;

  background: var(--lime);

  transform: scaleX(0);
  transform-origin: left;

  transition: transform 0.55s var(--ease);
}

/* Hover */

.mnav-link:hover .mnav-link-text {
  color: var(--lime);
  transform: translateX(12px);
}

.mnav-link:hover .mnav-link-bar {
  transform: scaleX(1);
}

.mnav-link:hover::before {
  color: var(--lime);
  transform: translate(-5px, -50%);
}

/* =========================================================
   RESUME
========================================================= */

.mnav-foot {
  opacity: 0;
  transform: translateY(24px);
}

.mnav-resume {
  position: relative;

  display: flex;
  align-items: center;
  justify-content: space-between;

  width: 100%;

  padding: 15px 17px;

  border: 1px solid rgba(211, 245, 118, 0.3);
  border-radius: 6px;

  background: rgba(211, 245, 118, 0.035);

  color: var(--lime);

  font-family: "Manrope", sans-serif;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.13em;
  text-transform: uppercase;

  cursor: pointer;

  overflow: hidden;

  transition:
    background 0.4s ease,
    color 0.4s ease,
    border-color 0.4s ease;
}

.mnav-resume::before {
  content: "";

  position: absolute;
  inset: 0;

  background: var(--lime);

  transform: translateX(-101%);

  transition: transform 0.55s var(--ease);
}

.mnav-resume span,
.mnav-resume .v-icon {
  position: relative;
  z-index: 2;
}

.mnav-resume:hover {
  color: var(--ink);
  border-color: var(--lime);
}

.mnav-resume:hover::before {
  transform: translateX(0);
}

/* =========================================================
   RESPONSIVE
========================================================= */

@media (max-width: 600px) {
  .mnav-bar {
    margin: 8px 10px;
    padding-left: 16px;
  }

  .mnav-brand {
    font-size: 25px;
  }

  .mnav-brand::after {
    font-size: 4.5px;
  }

  .mnav-toggle {
    height: 40px;
    gap: 8px;
    padding-left: 13px;
  }

  .mnav-sheet {
    padding-left: 20px;
    padding-right: 20px;
  }

  .mnav-link {
    min-height: 64px;
  }

  .mnav-link-text {
    /* font-size: clamp(3rem, 17vw, 4.5rem); */
    font-size:20px !important;
  }
}

@media (max-width: 380px) {
  .mnav-brand {
    font-size: 23px;
  }

  .mnav-toggle {
    height: 38px;
    padding-left: 12px;
  }

  .mnav-icon {
    width: 27px;
    height: 27px;
  }

  .mnav-sheet {
    padding-top: 100px;
  }

  .mnav-link {
    min-height: 59px;
  }

  .mnav-link-text {
    font-size: 2.9rem;
  }
}

/* =========================================================
   REDUCED MOTION
========================================================= */

@media (prefers-reduced-motion: reduce) {
  .mnav *,
  .mnav-sheet,
  .mnav-sheet.open {
    transition-duration: 0.01s !important;
    transition-delay: 0s !important;
    animation: none !important;
  }
}
</style>
