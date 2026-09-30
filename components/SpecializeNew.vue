<template>
  <section class="specialized-section">
    <!-- ================= BACKGROUND ================= -->

    <div class="ambient ambient-one"></div>
    <div class="ambient ambient-two"></div>

    <div class="section-grid"></div>

    <v-container fluid class="specialized-container px-md-15">
      <!-- ================= HEADER ================= -->

      <div class="section-header" data-aos="fade-up" data-aos-duration="900">
        <div class="eyebrow">
          <span class="eyebrow-line"></span>
          <span>WHAT I DO</span>
        </div>

        <div class="header-main">
          <h1 class="heading bebas-Bold-h1">SPECIALIZED</h1>

          <p class="section-subtitle">
            I build digital products that combine
            <br class="d-none d-md-block" />
            thoughtful design with reliable technology.
          </p>
        </div>

        <div class="heading-divider"></div>
      </div>

      <!-- ================= SERVICE CARDS ================= -->

      <v-row class="cards-row">
        <v-col
          v-for="(card, index) in cardData"
          :key="card.title"
          cols="12"
          sm="6"
          md="4"
          class="card-column"
          data-aos="fade-up"
          :data-aos-delay="index * 140 + 200"
          data-aos-duration="900"
        >
          <div
            class="service-card"
            :class="{ flipped: flippedCard === index }"
            :style="cardStyles[index]"
            @click="toggleCard(index)"
            @mousemove="handleMouseMove($event, index)"
            @mouseleave="handleMouseLeave(index)"
          >
            <div class="card-inner">
              <!-- =================================================
                   FRONT
              ================================================== -->

              <div class="card-face card-front">
                <!-- Cursor spotlight -->
                <div class="cursor-light"></div>

                <!-- Image -->
                <div class="image-area">
                  <img
                    :src="card.image"
                    :alt="card.title"
                    class="service-image"
                  />

                  <div class="image-fade"></div>

                  <!-- Minimal image label -->
                  <div class="image-label">0{{ index + 1 }}</div>
                </div>

                <!-- Content -->

                <div class="front-content">
                  <div class="front-top">
                    <span class="category">
                      {{ card.category }}
                    </span>

                    <span class="year"> 2026 </span>
                  </div>

                  <h2 class="front-title">
                    {{ card.shortTitle }}
                  </h2>

                  <div class="front-footer">
                    <span class="front-description">
                      {{ card.shortDescription }}
                    </span>

                    <div class="flip-action">
                      <span> VIEW </span>

                      <span class="action-arrow"> ↗ </span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- =================================================
                   BACK
              ================================================== -->

              <div class="card-face card-back">
                <div class="back-top">
                  <span class="back-number"> 0{{ index + 1 }} </span>

                  <button
                    class="close-button"
                    aria-label="Close"
                    @click.stop="toggleCard(index)"
                  >
                    ×
                  </button>
                </div>

                <div class="back-content">
                  <span class="back-category">
                    {{ card.category }}
                  </span>

                  <h2 class="back-title">
                    {{ card.title }}
                  </h2>

                  <div class="back-line"></div>

                  <p class="back-description">
                    {{ card.description }}
                  </p>

                  <!-- ================= DETAILS ================= -->

                  <div class="details">
                    <div class="detail-row">
                      <span class="detail-label"> STACK </span>

                      <div class="technology-list">
                        <span
                          v-for="technology in card.technologies"
                          :key="technology"
                        >
                          {{ technology }}
                        </span>
                      </div>
                    </div>

                    <div class="detail-row">
                      <span class="detail-label"> FOCUS </span>

                      <span class="detail-value">
                        {{ card.focus }}
                      </span>
                    </div>

                    <div class="detail-row">
                      <span class="detail-label"> APPROACH </span>

                      <span class="detail-value">
                        {{ card.approach }}
                      </span>
                    </div>
                  </div>
                </div>

                <!-- Back footer -->

                <div class="back-footer">
                  <span class="back-note"> DIGITAL DEVELOPMENT </span>

                  <!-- <button class="project-button" @click.stop="handleView(card)">
                    VIEW PROJECT
                    <span>↗</span>
                  </button> -->
                </div>
              </div>
            </div>
          </div>
        </v-col>
      </v-row>

      <!-- ================= BOTTOM ================= -->

      <div class="section-footer" data-aos="fade-up" data-aos-delay="600">
        <div class="footer-line"></div>

        <span> CLICK A SERVICE TO DISCOVER MORE </span>

        <div class="footer-count">03 / 03</div>
      </div>
    </v-container>
  </section>
</template>

<script setup>
import { ref } from "vue";

/* =========================================================
   STATE
========================================================= */

const flippedCard = ref(null);

const cardStyles = ref([{}, {}, {}]);

/* =========================================================
   CARD DATA
========================================================= */

const cardData = [
  {
    image: "/images/admin.png",

    shortTitle: "ADMIN PANEL",

    category: "01 / DEVELOPMENT",

    shortDescription:
      "Powerful interfaces for managing data, users and operations.",

    title: "ADMIN PANEL DEVELOPMENT",

    description:
      "Custom admin panels designed around real business workflows, giving you clear control over data, users, analytics and everyday operations.",

    technologies: ["VUE", "NUXT", "NODE", "SUPABASE"],

    focus: "DATA & BUSINESS SYSTEMS",

    approach: "SCALABLE • SECURE • FAST",

    link: "/projects/admin-panel",
  },

  {
    image: "/images/mad.png",

    shortTitle: "MOBILE APP",

    category: "02 / DEVELOPMENT",

    shortDescription: "Smooth, intuitive applications built for everyday use.",

    title: "MOBILE APP DEVELOPMENT",

    description:
      "Mobile applications focused on performance, intuitive interaction and consistent experiences across different devices and platforms.",

    technologies: ["FLUTTER", "ANDROID", "IOS", "FIREBASE"],

    focus: "MOBILE EXPERIENCES",

    approach: "FAST • INTUITIVE • SCALABLE",

    link: "/projects/mobile-app",
  },

  {
    image: "/images/webdev.png",

    shortTitle: "WEBSITE",

    category: "03 / DEVELOPMENT",

    shortDescription: "Modern websites built to look sharp and perform better.",

    title: "WEBSITE DEVELOPMENT",

    description:
      "Responsive websites combining strong visual design, clean development and performance across desktop, tablet and mobile devices.",

    technologies: ["VUE", "NUXT", "JAVASCRIPT", "SEO"],

    focus: "WEB EXPERIENCES",

    approach: "RESPONSIVE • MODERN • FAST",

    link: "/projects/website",
  },
];

/* =========================================================
   FLIP CARD
========================================================= */

function toggleCard(index) {
  if (flippedCard.value === index) {
    flippedCard.value = null;
  } else {
    flippedCard.value = index;
  }
}

/* =========================================================
   MOUSE TILT
========================================================= */

function handleMouseMove(event, index) {
  /*
    Don't apply the tilt when the card is flipped.
    This keeps the back side clean and stable.
  */

  if (flippedCard.value === index) {
    return;
  }

  const card = event.currentTarget;

  const rect = card.getBoundingClientRect();

  const x = event.clientX - rect.left;

  const y = event.clientY - rect.top;

  const centerX = rect.width / 2;

  const centerY = rect.height / 2;

  const rotateY = ((x - centerX) / centerX) * 5;

  const rotateX = ((centerY - y) / centerY) * 5;

  const mouseX = (x / rect.width) * 100;

  const mouseY = (y / rect.height) * 100;

  cardStyles.value[index] = {
    "--rotate-x": `${rotateX}deg`,

    "--rotate-y": `${rotateY}deg`,

    "--mouse-x": `${mouseX}%`,

    "--mouse-y": `${mouseY}%`,
  };
}

/* =========================================================
   RESET
========================================================= */

function handleMouseLeave(index) {
  cardStyles.value[index] = {
    "--rotate-x": "0deg",

    "--rotate-y": "0deg",

    "--mouse-x": "50%",

    "--mouse-y": "50%",
  };
}

/* =========================================================
   PROJECT
========================================================= */

function handleView(card) {
  window.location.href = card.link;
}
</script>

<style scoped>
/* =========================================================
   VARIABLES
========================================================= */

.specialized-section {
  --lime: #d3f576;

  --white: #ffffff;

  --muted: rgba(255, 255, 255, 0.52);

  --faint: rgba(255, 255, 255, 0.18);

  position: relative;

  width: 100%;

  overflow: hidden;

  padding-top: 65px;

  padding-bottom: 85px;

  background: transparent;
}

/* =========================================================
   BACKGROUND
========================================================= */

.ambient {
  position: absolute;

  border-radius: 50%;

  pointer-events: none;

  filter: blur(120px);

  opacity: 0.08;
}

.ambient-one {
  width: 380px;

  height: 380px;

  top: 15%;

  left: -250px;

  background: #7c3aed;
}

.ambient-two {
  width: 350px;

  height: 350px;

  bottom: 5%;

  right: -250px;

  background: #2563eb;
}

.section-grid {
  position: absolute;

  inset: 0;

  pointer-events: none;

  opacity: 0.025;

  background-image:
    linear-gradient(rgba(255, 255, 255, 0.4) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.4) 1px, transparent 1px);

  background-size: 80px 80px;
}

/* =========================================================
   CONTAINER
========================================================= */

.specialized-container {
  position: relative;

  z-index: 2;
}

/* =========================================================
   HEADER
========================================================= */

.section-header {
  margin-bottom: 55px;
}

.eyebrow {
  display: flex;

  align-items: center;

  gap: 12px;

  margin-bottom: 16px;

  color: var(--lime);

  font-size: 11px;

  font-weight: 600;

  letter-spacing: 2.5px;
}

.eyebrow-line {
  width: 45px;

  height: 1px;

  background: var(--lime);
}

.header-main {
  display: flex;

  align-items: flex-end;

  justify-content: space-between;

  gap: 40px;
}

.heading {
  margin: 0;

  color: var(--white);

  font-size: clamp(60px, 8vw, 108px);

  line-height: 0.82;

  letter-spacing: 1px;
}

.section-subtitle {
  margin: 0 0 5px;

  max-width: 350px;

  color: var(--muted);

  font-size: 14px;

  line-height: 1.7;
}

.heading-divider {
  width: 100%;

  height: 1px;

  margin-top: 28px;

  background: linear-gradient(
    90deg,
    var(--lime),
    rgba(211, 245, 118, 0.18),
    transparent
  );
}

/* =========================================================
   CARDS
========================================================= */

.cards-row {
  row-gap: 30px;
}

.card-column {
  display: flex;

  justify-content: center;
}

/* =========================================================
   CARD
========================================================= */

.service-card {
  --rotate-x: 0deg;

  --rotate-y: 0deg;

  --mouse-x: 50%;

  --mouse-y: 50%;

  width: 100%;

  max-width: 400px;

  height: 535px;

  perspective: 1600px;

  cursor: pointer;

  transform: perspective(1400px) rotateX(var(--rotate-x))
    rotateY(var(--rotate-y));

  transition: transform 0.25s ease;
}

.service-card:hover {
  z-index: 5;
}

/* =========================================================
   INNER
========================================================= */

.card-inner {
  position: relative;

  width: 100%;

  height: 100%;

  transform-style: preserve-3d;

  transition: transform 0.85s cubic-bezier(0.2, 0.75, 0.25, 1);
}

.service-card.flipped .card-inner {
  transform: rotateY(180deg);
}

.service-card.flipped {
  transform: perspective(1400px) rotateX(0deg) rotateY(0deg);
}

/* =========================================================
   CARD FACE
========================================================= */

.card-face {
  position: absolute;

  inset: 0;

  width: 100%;

  height: 100%;

  overflow: hidden;

  border-radius: 24px;

  backface-visibility: hidden;

  -webkit-backface-visibility: hidden;

  border: 1px solid rgba(255, 255, 255, 0.13);

  background: #0a0b14;

  box-shadow: 0 25px 70px rgba(0, 0, 0, 0.38);

  transition:
    border-color 0.4s ease,
    box-shadow 0.4s ease;
}

.service-card:hover .card-face {
  border-color: rgba(211, 245, 118, 0.42);

  box-shadow:
    0 30px 80px rgba(0, 0, 0, 0.48),
    0 0 35px rgba(211, 245, 118, 0.06);
}

/* =========================================================
   FRONT
========================================================= */

.card-front {
  display: flex;

  flex-direction: column;
}

/* =========================================================
   CURSOR LIGHT
========================================================= */

.cursor-light {
  position: absolute;

  inset: 0;

  z-index: 6;

  pointer-events: none;

  background: radial-gradient(
    280px circle at var(--mouse-x) var(--mouse-y),
    rgba(211, 245, 118, 0.08),
    transparent 45%
  );
}

/* =========================================================
   IMAGE AREA
========================================================= */

.image-area {
  position: relative;

  width: 100%;

  height: 61%;

  overflow: hidden;

  background: #eeeeeb;
}

/*
  IMPORTANT:
  contain instead of cover.

  This means the generated image will
  NEVER be cropped.
*/

.service-image {
  width: 100%;

  height: 100%;

  display: block;

  object-fit: contain;

  object-position: center;

  transform: scale(1.01);

  transition: transform 0.8s cubic-bezier(0.2, 0.7, 0.2, 1);
}

/* Gentle zoom */

.service-card:hover .service-image {
  transform: scale(1.045);
}

/* =========================================================
   IMAGE FADE
========================================================= */

.image-fade {
  position: absolute;

  left: 0;

  right: 0;

  bottom: 0;

  height: 120px;

  background: linear-gradient(to bottom, transparent, #0a0b14);
}

/* =========================================================
   IMAGE NUMBER
========================================================= */

.image-label {
  position: absolute;

  top: 18px;

  left: 20px;

  z-index: 4;

  display: flex;

  align-items: center;

  justify-content: center;

  width: 38px;

  height: 38px;

  border: 1px solid rgba(10, 11, 20, 0.22);

  border-radius: 50%;

  background: rgba(255, 255, 255, 0.55);

  backdrop-filter: blur(8px);

  color: #11131b;

  font-size: 10px;

  font-weight: 700;
}

/* =========================================================
   FRONT CONTENT
========================================================= */

.front-content {
  position: relative;

  z-index: 8;

  display: flex;

  flex-direction: column;

  flex: 1;

  margin-top: -12px;

  padding: 0 25px 24px;
}

.front-top {
  display: flex;

  align-items: center;

  justify-content: space-between;

  margin-bottom: 10px;
}

.category {
  color: var(--lime);

  font-size: 9px;

  letter-spacing: 1.8px;

  font-weight: 600;
}

.year {
  color: rgba(255, 255, 255, 0.22);

  font-size: 8px;

  letter-spacing: 1px;
}

.front-title {
  margin: 0;

  color: white;

  font-size: 30px;

  line-height: 0.95;

  font-weight: 800;

  letter-spacing: -0.4px;
}

.front-footer {
  display: flex;

  align-items: flex-end;

  justify-content: space-between;

  gap: 15px;

  margin-top: auto;

  padding-top: 18px;

  border-top: 1px solid rgba(255, 255, 255, 0.09);
}

.front-description {
  max-width: 210px;

  color: rgba(255, 255, 255, 0.42);

  font-size: 12px;

  line-height: 1.5;
}

.flip-action {
  display: flex;

  align-items: center;

  gap: 8px;

  flex-shrink: 0;

  color: var(--lime);

  font-size: 8px;

  font-weight: 700;

  letter-spacing: 1.4px;
}

.action-arrow {
  display: flex;

  align-items: center;

  justify-content: center;

  width: 32px;

  height: 32px;

  border: 1px solid rgba(211, 245, 118, 0.4);

  border-radius: 50%;

  font-size: 15px;

  transition:
    transform 0.35s ease,
    background 0.35s ease;
}

.service-card:hover .action-arrow {
  transform: rotate(45deg);

  background: rgba(211, 245, 118, 0.08);
}

/* =========================================================
   BACK
========================================================= */

.card-back {
  transform: rotateY(180deg);

  display: flex;

  flex-direction: column;

  padding: 28px;

  background:
    radial-gradient(
      circle at 100% 0%,
      rgba(211, 245, 118, 0.08),
      transparent 35%
    ),
    linear-gradient(145deg, #11131e, #07080e);
}

/* =========================================================
   BACK TOP
========================================================= */

.back-top {
  display: flex;

  align-items: center;

  justify-content: space-between;
}

.back-number {
  color: rgba(211, 245, 118, 0.35);

  font-size: 11px;

  letter-spacing: 2px;
}

.close-button {
  width: 32px;

  height: 32px;

  display: flex;

  align-items: center;

  justify-content: center;

  border: 1px solid rgba(255, 255, 255, 0.14);

  border-radius: 50%;

  background: rgba(255, 255, 255, 0.025);

  color: rgba(255, 255, 255, 0.55);

  font-size: 19px;

  cursor: pointer;

  transition: all 0.3s ease;
}

.close-button:hover {
  border-color: var(--lime);

  color: var(--lime);

  transform: rotate(90deg);
}

/* =========================================================
   BACK CONTENT
========================================================= */

.back-content {
  margin-top: 45px;
}

.back-category {
  color: var(--lime);

  font-size: 9px;

  letter-spacing: 2px;
}

.back-title {
  max-width: 330px;

  margin: 10px 0 0;

  color: white;

  font-size: 30px;

  line-height: 1;

  font-weight: 800;
}

.back-line {
  width: 55px;

  height: 2px;

  margin-top: 22px;

  background: var(--lime);
}

.back-description {
  margin: 20px 0 0;

  color: rgba(255, 255, 255, 0.58);

  font-size: 13px;

  line-height: 1.7;
}

/* =========================================================
   DETAILS
========================================================= */

.details {
  margin-top: 30px;

  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.detail-row {
  display: grid;

  grid-template-columns:
    80px
    1fr;

  gap: 15px;

  padding: 13px 0;

  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
}

.detail-label {
  color: rgba(255, 255, 255, 0.25);

  font-size: 8px;

  letter-spacing: 1.5px;
}

.detail-value {
  color: rgba(255, 255, 255, 0.55);

  font-size: 9px;

  letter-spacing: 0.7px;
}

.technology-list {
  display: flex;

  flex-wrap: wrap;

  gap: 6px;
}

.technology-list span {
  color: rgba(255, 255, 255, 0.65);

  font-size: 9px;
}

.technology-list span:not(:last-child)::after {
  content: " / ";

  margin-left: 6px;

  color: rgba(211, 245, 118, 0.35);
}

/* =========================================================
   BACK FOOTER
========================================================= */

.back-footer {
  display: flex;

  align-items: center;

  justify-content: space-between;

  gap: 15px;

  margin-top: auto;

  padding-top: 18px;

  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.back-note {
  color: rgba(255, 255, 255, 0.22);

  font-size: 7px;

  letter-spacing: 1.3px;
}

.project-button {
  display: flex;

  align-items: center;

  gap: 8px;

  padding: 9px 13px;

  border: 1px solid rgba(211, 245, 118, 0.4);

  border-radius: 20px;

  background: transparent;

  color: var(--lime);

  font-size: 8px;

  font-weight: 700;

  letter-spacing: 1px;

  cursor: pointer;

  transition: all 0.3s ease;
}

.project-button span {
  font-size: 14px;
}

.project-button:hover {
  background: var(--lime);

  color: #07080e;

  gap: 12px;
}

/* =========================================================
   FOOTER
========================================================= */

.section-footer {
  display: flex;

  align-items: center;

  gap: 14px;

  margin-top: 32px;

  color: rgba(255, 255, 255, 0.25);

  font-size: 8px;

  letter-spacing: 1.5px;
}

.footer-line {
  width: 55px;

  height: 1px;

  background: rgba(211, 245, 118, 0.45);
}

.footer-count {
  margin-left: auto;

  color: rgba(255, 255, 255, 0.18);
}

/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 768px) {
  .specialized-section {
    padding-top: 35px;
    padding-bottom: 60px;
  }

  .section-header {
    margin-bottom: 38px;
  }

  .header-main {
    display: block;
  }

  .heading {
    font-size: clamp(55px, 16vw, 85px);
  }

  .section-subtitle {
    margin-top: 20px;
    font-size: 13px;
    line-height: 1.7;
  }

  .heading-divider {
    margin-top: 22px;
  }

  /* CARD */
  .service-card {
    width: 100%;
    max-width: 420px;
    height: 430px;
    transform: none !important;
  }

  .card-face {
    border-radius: 22px;
  }

  /* IMAGE */
  .image-area {
    height: 54%;
    flex-shrink: 0;
  }

  .service-image {
    object-fit: contain;
  }

  .image-label {
    top: 14px;
    left: 16px;
    width: 34px;
    height: 34px;
    font-size: 9px;
  }

  /* FRONT CONTENT */
  .front-content {
    flex: none;
    height: auto;
    margin-top: -10px;
    padding: 0 20px 18px;
  }

  .front-top {
    margin-bottom: 8px;
  }

  .category {
    font-size: 8px;
    letter-spacing: 1.5px;
  }

  .year {
    font-size: 7px;
  }

  .front-title {
    font-size: 26px;
    line-height: 0.95;
  }

  /* IMPORTANT:
     Do not push footer to bottom on mobile */
  .front-footer {
    margin-top: 24px;
    padding-top: 14px;
    gap: 12px;
  }

  .front-description {
    max-width: 200px;
    font-size: 12px;
    line-height: 1.5;
  }

  .flip-action {
    font-size: 7px;
    gap: 6px;
  }

  .action-arrow {
    width: 30px;
    height: 30px;
    font-size: 14px;
  }

  /* BACK */
  .card-back {
    padding: 22px;
  }

  .back-content {
    margin-top: 28px;
  }

  .back-category {
    font-size: 8px;
  }

  .back-title {
    font-size: 25px;
    line-height: 0.95;
  }

  .back-line {
    margin-top: 18px;
  }

  .back-description {
    margin-top: 16px;
    font-size: 11px;
    line-height: 1.6;
  }

  .details {
    margin-top: 22px;
  }

  .detail-row {
    grid-template-columns: 65px 1fr;
    gap: 10px;
    padding: 10px 0;
  }

  .detail-label {
    font-size: 7px;
  }

  .detail-value,
  .technology-list span {
    font-size: 8px;
  }

  .back-footer {
    padding-top: 14px;
  }

  .back-note {
    font-size: 6px;
  }
}

/* =========================================================
   SMALL MOBILE
========================================================= */

@media (max-width: 450px) {
  .specialized-section {
    padding-left: 5px;
    padding-right: 5px;
  }

  .service-card {
    height: 410px;
  }

  .image-area {
    height: 53%;
  }

  .front-content {
    margin-top: -8px;
    padding: 0 18px 16px;
  }

  .front-title {
    font-size: 24px;
  }

  .front-footer {
    margin-top: 20px;
    padding-top: 16px;
  }

  .front-description {
    max-width: 225px;
    font-size: 14px;
  }

  .flip-action span:first-child {
    display: none;
  }

  .action-arrow {
    width: 29px;
    height: 29px;
  }

  /* BACK */
  .card-back {
    padding: 20px;
  }

  .back-content {
    margin-top: 24px;
  }

  .back-title {
    font-size: 23px;
  }

  .back-description {
    font-size: 12px;
    line-height: 1.55;
  }

  .details {
    margin-top: 18px;
  }

  .detail-row {
    padding: 8px 0;
  }

  .section-footer {
    justify-content: center;
  }

  .footer-count {
    display: none;
  }
}
</style>
