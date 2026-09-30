<template>
  <div class="fullscreen-container" v-if="loading">
    <div class="loader">
      <div class="box box-1">
        <div class="side-left"></div>
        <div class="side-right"></div>
        <div class="side-top"></div>
      </div>

      <div class="box box-2">
        <div class="side-left"></div>
        <div class="side-right"></div>
        <div class="side-top"></div>
      </div>

      <div class="box box-3">
        <div class="side-left"></div>
        <div class="side-right"></div>
        <div class="side-top"></div>
      </div>

      <div class="box box-4">
        <div class="side-left"></div>
        <div class="side-right"></div>
        <div class="side-top"></div>
      </div>
    </div>
  </div>

  <div class="main" v-else>
    <!-- Mouse follower -->
    <div class="mouse-follower">
      <div class="energy-ring"></div>

      <span class="particle particle-1"></span>
      <span class="particle particle-2"></span>
      <span class="particle particle-3"></span>
    </div>

    <Nav />

    <v-container fluid class="about-container px-5 px-md-15">
      <!-- =========================================
           INTRO
      ========================================== -->

      <section class="about-intro">
        <div class="section-label" data-aos="fade-up" data-aos-duration="1000">
          <span>01</span>
          <span>PROFILE</span>
        </div>

        <div class="intro-grid">
          <div
            class="intro-heading"
            data-aos="fade-up"
            data-aos-duration="1200"
          >
            <h1 class="heading bebas-Bold-h1">
              ABOUT
              <br />
              <span>ME</span>
            </h1>
          </div>

          <div
            class="intro-content"
            data-aos="fade-up"
            data-aos-duration="1200"
            data-aos-delay="150"
          >
            <p class="intro-statement manrope-regular-h4">
              Front-End Developer and MCA student at MIT Manipal, focused on
              building modern digital experiences that balance
              <span>design</span>, <span>performance</span> and
              <span>usability</span>.
            </p>

            <div class="intro-actions">
              <button
                class="resume-button manrope-Bold-h5"
                @click="downloadResume"
              >
                <span>Download Resume</span>

                <span class="resume-arrow">
                  <v-icon size="18"> mdi-arrow-top-right </v-icon>
                </span>
              </button>

              <div class="social-links">
                <a
                  href="https://www.linkedin.com/in/shubhank-amin-a7b231225/"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="social-link"
                >
                  <v-icon size="19">mdi-linkedin</v-icon>
                  <span>LinkedIn</span>
                </a>

                <a
                  href="https://github.com/Shubhankamin?tab=repositories"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="social-link"
                >
                  <v-icon size="19">mdi-github</v-icon>
                  <span>GitHub</span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- =========================================
           IMAGE + PROFILE
      ========================================== -->

      <section class="profile-section">
        <div class="profile-image" data-aos="fade-up" data-aos-duration="1200">
          <v-img
            src="/images/me/me_8.jpeg"
            lazy-src="/images/me/me_8_lazy.jpeg"
            width="100%"
            height="auto"
            contain
          />

          <div class="image-label">
            <span>SHUBHANK AMIN</span>
            <span>FULL STACK DEVELOPER</span>
          </div>
        </div>

        <div
          class="profile-copy"
          data-aos="fade-up"
          data-aos-duration="1200"
          data-aos-delay="150"
        >
          <div class="section-label small">
            <span>02</span>
            <span>MY STORY</span>
          </div>

          <p class="story-lead manrope-Bold-h4">
            I build interfaces where technology and visual design work together.
          </p>

          <p class="story-text manrope-regular-h5">
            I am a Full Stack Developer currently pursuing a Master of Computer
            Applications at MIT Manipal, with professional experience across
            startup, freelance, and internship environments.
          </p>

          <p class="story-text manrope-regular-h5">
            My work revolves around building scalable web applications, admin
            dashboards, e-commerce platforms, and responsive interfaces. I enjoy
            taking an idea from its early visual concept through development and
            into a polished, production-ready experience.
          </p>

          <p class="story-text manrope-regular-h5">
            I am particularly interested in modern frontend architecture,
            interaction design, performance optimization, and creating
            interfaces that feel simple without becoming ordinary.
          </p>
        </div>
      </section>

      <!-- =========================================
     EXPERTISE / HOW I WORK
========================================== -->
      <section
        class="expertise-section"
        data-aos="fade-up"
        data-aos-duration="1200"
      >
        <div class="section-label">
          <span>03</span>
          <span>HOW I WORK</span>
        </div>

        <div class="expertise-intro">
          <h2 class="expertise-title bebas-Bold-h1">
            I DON'T JUST
            <span>BUILD.</span>
          </h2>

          <p class="expertise-description manrope-regular-h5">
            I focus on the thinking behind the interface — from understanding
            the problem to shaping the experience and turning it into something
            reliable, responsive and usable.
          </p>
        </div>

        <div class="expertise-process">
          <article class="process-item">
            <div class="process-index">01</div>

            <div class="process-main">
              <div class="process-top">
                <span class="process-kicker">THINK</span>
                <span class="process-line"></span>
              </div>

              <h3>UNDERSTAND THE PROBLEM</h3>

              <p>
                Before writing code, I break down the requirement, understand
                the users and figure out what the interface actually needs to
                do.
              </p>
            </div>

            <div class="process-mark">01</div>
          </article>

          <article class="process-item">
            <div class="process-index">02</div>

            <div class="process-main">
              <div class="process-top">
                <span class="process-kicker">DESIGN</span>
                <span class="process-line"></span>
              </div>

              <h3>SHAPE THE EXPERIENCE</h3>

              <p>
                I care about hierarchy, spacing, responsiveness and interaction
                — making complex functionality feel simple to use.
              </p>
            </div>

            <div class="process-mark">02</div>
          </article>

          <article class="process-item">
            <div class="process-index">03</div>

            <div class="process-main">
              <div class="process-top">
                <span class="process-kicker">BUILD</span>
                <span class="process-line"></span>
              </div>

              <h3>TURN IDEAS INTO SYSTEMS</h3>

              <p>
                I build reusable components and connect the frontend with APIs,
                databases and backend services to create complete applications.
              </p>
            </div>

            <div class="process-mark">03</div>
          </article>

          <article class="process-item">
            <div class="process-index">04</div>

            <div class="process-main">
              <div class="process-top">
                <span class="process-kicker">REFINE</span>
                <span class="process-line"></span>
              </div>

              <h3>MAKE IT FEEL RIGHT</h3>

              <p>
                Performance, responsiveness and the small details matter. I
                refine the final experience until it feels intentional.
              </p>
            </div>

            <div class="process-mark">04</div>
          </article>
        </div>

        <div class="expertise-footer">
          <span>MY APPROACH</span>

          <p class="manrope-Bold-h5">
            <span>Simple.</span>
            Thoughtful. Built to last.
          </p>
        </div>
      </section>

      <!-- =========================================
           EXISTING COMPONENTS
      ========================================== -->

      <section class="existing-section">
        <CapNew />

        <ExpNew class="text-white" />

        <Connect />
      </section>
    </v-container>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useScrollAurora } from "~/composables/useScrollAurora";
import { useMouseFollower } from "~/composables/useMouseFollower";

useScrollAurora();
useMouseFollower();

const loading = ref(true);

onMounted(() => {
  setTimeout(() => {
    loading.value = false;
  }, 1500);
});

const downloadResume = () => {
  const link = document.createElement("a");

  link.href = "/files/ShubhankAmin_251090700127.pdf";
  link.download = "Shubhank's Resume.pdf";

  link.click();
};
</script>

<style scoped>
/* =========================================
   BASE
========================================= */

.main {
  position: relative;
  width: 100%;
  min-height: 100vh;

  overflow: hidden;
  isolation: isolate;

  background: #030712;
}

.main::before {
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
}

.about-container {
  padding-top: 110px;
  padding-bottom: 100px;
}

/* =========================================
   SECTION LABEL
========================================= */

.section-label {
  display: flex;
  align-items: center;
  gap: 14px;

  margin-bottom: 45px;

  color: rgba(255, 255, 255, 0.45);

  font-family: "Manrope", sans-serif;
  font-size: 11px;
  font-weight: 700;

  letter-spacing: 0.14em;
}

.section-label span:first-child {
  color: #d3f576;
}

.section-label.small {
  margin-bottom: 30px;
}

/* =========================================
   INTRO
========================================= */

.about-intro {
  padding: 50px 0 130px;

  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}

.intro-grid {
  display: grid;

  grid-template-columns: 1fr 1fr;

  gap: 8vw;

  align-items: end;
}

.heading {
  margin: 0;

  color: #ffffff;

  font-size: clamp(80px, 12vw, 190px);

  line-height: 0.78;

  text-transform: uppercase;
}

.heading span {
  color: #d3f576;
}

.intro-content {
  max-width: 680px;
}

.intro-statement {
  margin: 0;

  color: rgba(255, 255, 255, 0.85);

  line-height: 1.45;
}

.intro-statement span {
  color: #d3f576;
}

/* =========================================
   ACTIONS
========================================= */

.intro-actions {
  display: flex;
  align-items: center;

  gap: 30px;

  margin-top: 45px;
}

.resume-button {
  display: inline-flex;
  align-items: center;
  gap: 15px;

  padding: 11px 8px 11px 22px;

  border: 1px solid #d3f576;
  border-radius: 50px;

  background: #d3f576;
  color: #030712;

  cursor: pointer;

  transition:
    transform 0.3s ease,
    background 0.3s ease;
}

.resume-arrow {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 34px;
  height: 34px;

  border-radius: 50%;

  background: #030712;
  color: #d3f576;

  transition: transform 0.3s ease;
}

.resume-button:hover {
  transform: translateY(-3px);
}

.resume-button:hover .resume-arrow {
  transform: translate(3px, -3px);
}

.social-links {
  display: flex;
  align-items: center;
  gap: 22px;
}

.social-link {
  display: flex;
  align-items: center;
  gap: 7px;

  color: rgba(255, 255, 255, 0.6);

  font-family: "Manrope", sans-serif;
  font-size: 13px;

  text-decoration: none;

  transition: color 0.3s ease;
}

.social-link:hover {
  color: #d3f576;
}

/* =========================================
   PROFILE
========================================= */

/* =========================================
   PROFILE
========================================= */

.profile-section {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 8vw;
  padding: 130px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}

.profile-image {
  position: relative;
  width: 100%;
  overflow: hidden;
  background: #111;
}

.profile-image :deep(.v-img) {
  width: 100%;
  height: auto !important;
}

.profile-image :deep(.v-img__img) {
  position: relative !important;
  width: 100%;
  height: auto !important;
  object-fit: contain !important;
}

.profile-image:hover :deep(.v-img__img) {
  transform: scale(1.015);
  transition: transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
}

.image-label {
  position: absolute;
  left: 20px;
  right: 20px;
  bottom: 20px;

  display: flex;
  justify-content: space-between;

  padding: 12px 15px;

  border: 1px solid rgba(255, 255, 255, 0.2);

  background: rgba(0, 0, 0, 0.55);

  backdrop-filter: blur(10px);

  color: #ffffff;

  font-family: "Manrope", sans-serif;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.1em;
}

.image-label span:last-child {
  color: #d3f576;
}

.profile-copy {
  align-self: center;
}

.story-lead {
  max-width: 550px;
  color: #ffffff;
  line-height: 1.5;
}

.story-text {
  max-width: 600px;
  margin-top: 25px;
  color: rgba(255, 255, 255, 0.55);
  line-height: 1.8;
}

/* =========================================
   TABLET
========================================= */

@media (max-width: 960px) {
  .profile-section {
    grid-template-columns: 1fr;
    gap: 60px;
    padding: 100px 0;
  }

  .profile-image {
    width: 100%;
  }

  .profile-copy {
    width: 100%;
  }
}

/* =========================================
   MOBILE
========================================= */

@media (max-width: 600px) {
  .profile-section {
    display: block;
    width: 100%;
    padding: 80px 0;
  }

  /*
   * Full 12-column image.
   * No aspect-ratio.
   * No fixed height.
   */

  .profile-image {
    width: 100%;
    height: auto;
    aspect-ratio: auto;
    overflow: hidden;
  }

  .profile-image :deep(.v-img) {
    width: 100%;
    height: auto !important;
    min-height: 0 !important;
  }

  .profile-image :deep(.v-img__img) {
    position: relative !important;
    width: 100%;
    height: auto !important;
    min-height: 0 !important;
    object-fit: contain !important;
  }

  .image-label {
    left: 12px;
    right: 12px;
    bottom: 12px;

    padding: 10px 12px;

    font-size: 8px;
    letter-spacing: 0.08em;
  }

  .profile-copy {
    width: 100%;
    margin-top: 60px;
  }

  .story-lead {
    font-size: 18px;
    line-height: 1.5;
  }

  .story-text {
    font-size: 14px;
    line-height: 1.75;
  }
}
/* =========================================
   EXPERTISE / HOW I WORK
========================================= */

.expertise-section {
  position: relative;
  padding: 150px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}

.expertise-intro {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 8vw;
  align-items: end;
  margin-bottom: 100px;
}

.expertise-title {
  margin: 0;
  color: #ffffff;
  font-size: clamp(70px, 10vw, 150px);
  line-height: 0.78;
  text-transform: uppercase;
}

.expertise-title span {
  display: block;
  color: #d3f576;
}

.expertise-description {
  max-width: 520px;
  margin: 0;
  color: rgba(255, 255, 255, 0.5);
  line-height: 1.8;
}

/* PROCESS */

.expertise-process {
  border-top: 1px solid rgba(255, 255, 255, 0.16);
}

.process-item {
  position: relative;
  display: grid;
  grid-template-columns: 80px 1fr 120px;
  gap: 30px;
  min-height: 190px;
  padding: 38px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  overflow: hidden;
}

.process-index {
  padding-top: 4px;
  color: #d3f576;
  font-family: "Manrope", sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
}

.process-main {
  max-width: 720px;
}

.process-top {
  display: flex;
  align-items: center;
  gap: 18px;
  margin-bottom: 18px;
}

.process-kicker {
  color: rgba(255, 255, 255, 0.38);
  font-family: "Manrope", sans-serif;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.18em;
}

.process-line {
  width: 45px;
  height: 1px;
  background: rgba(211, 245, 118, 0.4);
}

.process-main h3 {
  margin: 0;
  color: #ffffff;
  font-family: "Bebas Neue", sans-serif;
  font-size: clamp(32px, 4vw, 58px);
  font-weight: 700;
  line-height: 0.95;
  letter-spacing: 0.01em;
}

.process-main p {
  max-width: 600px;
  margin: 18px 0 0;
  color: rgba(255, 255, 255, 0.42);
  font-family: "Manrope", sans-serif;
  font-size: 13px;
  line-height: 1.8;
}

.process-mark {
  align-self: center;
  justify-self: end;
  color: rgba(211, 245, 118, 0.08);
  font-family: "Bebas Neue", sans-serif;
  font-size: 110px;
  line-height: 1;
  transition:
    color 0.4s ease,
    transform 0.4s ease;
}

.process-item:hover .process-mark {
  color: rgba(211, 245, 118, 0.2);
  transform: translateX(-10px);
}

.process-item:hover .process-line {
  width: 70px;
  background: #d3f576;
}

.process-line {
  transition:
    width 0.4s ease,
    background 0.4s ease;
}

/* FOOTER */

.expertise-footer {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 30px;
  margin-top: 70px;
  padding-top: 25px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}

.expertise-footer > span {
  color: rgba(255, 255, 255, 0.3);
  font-family: "Manrope", sans-serif;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
}

.expertise-footer p {
  margin: 0;
  color: rgba(255, 255, 255, 0.65);
}

.expertise-footer p span {
  color: #d3f576;
}

/* =========================================
   EXPERTISE RESPONSIVE
========================================= */

@media (max-width: 960px) {
  .expertise-section {
    padding: 100px 0;
  }

  .expertise-intro {
    grid-template-columns: 1fr;
    gap: 40px;
    margin-bottom: 70px;
  }

  .process-item {
    grid-template-columns: 55px 1fr 80px;
    gap: 20px;
    min-height: 170px;
  }

  .process-mark {
    font-size: 75px;
  }

  .expertise-footer {
    grid-template-columns: 1fr;
    gap: 15px;
  }
}

@media (max-width: 600px) {
  .expertise-section {
    padding: 80px 0;
  }

  .expertise-title {
    font-size: 70px;
  }

  .expertise-description {
    font-size: 14px;
    line-height: 1.75;
  }

  .expertise-intro {
    margin-bottom: 55px;
  }

  .process-item {
    grid-template-columns: 35px 1fr;
    gap: 15px;
    min-height: auto;
    padding: 30px 0;
  }

  .process-index {
    font-size: 9px;
  }

  .process-main h3 {
    font-size: 38px;
  }

  .process-main p {
    margin-top: 15px;
    font-size: 12px;
    line-height: 1.75;
  }

  .process-mark {
    display: none;
  }

  .process-top {
    margin-bottom: 15px;
  }

  .expertise-footer {
    margin-top: 50px;
  }

  .expertise-footer p {
    font-size: 15px;
  }
}
/* =========================================
   EXISTING COMPONENTS
========================================= */

.existing-section {
  /* padding-top: 100px; */
}

/* =========================================
   LOADER
========================================= */

.fullscreen-container {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 100vw;
  height: 100vh;

  background: #000;
}

.loader {
  scale: 3;

  width: 40px;
  height: 50px;
}

.box {
  position: relative;

  left: 10px;

  opacity: 0;
}

.side-left,
.side-right,
.side-top {
  position: absolute;
}

.side-left {
  top: 14px;
  left: 10px;

  width: 19px;
  height: 5px;

  background: #d3e97a;

  transform: skew(0deg, -25deg);
}

.side-right {
  top: 14px;
  left: -9px;

  width: 19px;
  height: 5px;

  background: #d3e97a;

  transform: skew(0deg, 25deg);
}

.side-top {
  width: 20px;
  height: 20px;

  background: #d3e97a;

  rotate: 45deg;

  transform: skew(-20deg, -20deg);
}

.box-1 {
  animation: from-left 4s infinite;
}

.box-2 {
  animation: from-right 4s infinite;
  animation-delay: 1s;
}

.box-3 {
  animation: from-left 4s infinite;
  animation-delay: 2s;
}

.box-4 {
  animation: from-right 4s infinite;
  animation-delay: 3s;
}

@keyframes from-left {
  0% {
    opacity: 0;
    translate: -20px -6px;
  }

  20% {
    opacity: 1;
    translate: 0 0;
  }

  40% {
    translate: 0 4px;
  }

  60% {
    translate: 0 8px;
  }

  80% {
    translate: 0 12px;
  }

  100% {
    opacity: 0;
    translate: 0 30px;
  }
}

@keyframes from-right {
  0% {
    opacity: 0;
    translate: 20px -6px;
  }

  20% {
    opacity: 1;
    translate: 0 0;
  }

  40% {
    translate: 0 4px;
  }

  60% {
    translate: 0 8px;
  }

  80% {
    translate: 0 12px;
  }

  100% {
    opacity: 0;
    translate: 0 30px;
  }
}

/* =========================================
   MOUSE FOLLOWER
========================================= */

.mouse-follower {
  position: fixed;

  top: 0;
  left: 0;

  width: 110px;
  height: 110px;

  pointer-events: none;

  z-index: 9999999999;

  transform: translate(
    calc(var(--follower-x, 50vw) - 50%),
    calc(var(--follower-y, 50vh) - 50%)
  );

  will-change: transform;
}

.energy-ring {
  position: absolute;

  inset: 18px;

  border: 1px solid rgba(211, 245, 118, 0.45);

  border-radius: 55% 45% 62% 38% / 42% 58% 42% 58%;

  box-shadow:
    0 0 12px rgba(211, 245, 118, 0.18),
    inset 0 0 12px rgba(211, 245, 118, 0.06);

  animation:
    morphRing 5s ease-in-out infinite alternate,
    rotateRing 10s linear infinite;
}

.energy-ring::before {
  content: "";

  position: absolute;

  inset: -14px;

  border-radius: 50%;

  border-top: 1px solid rgba(96, 165, 250, 0.5);
  border-right: 1px solid transparent;
  border-bottom: 1px solid rgba(211, 245, 118, 0.2);
  border-left: 1px solid transparent;

  animation: reverseRotate 6s linear infinite;
}

.energy-ring::after {
  content: "";

  position: absolute;

  width: 5px;
  height: 5px;

  top: 50%;
  left: 50%;

  transform: translate(-50%, -50%);

  border-radius: 50%;

  background: #d3f576;

  box-shadow:
    0 0 6px #d3f576,
    0 0 15px rgba(211, 245, 118, 0.8),
    0 0 30px rgba(211, 245, 118, 0.35);

  animation: corePulse 2s ease-in-out infinite;
}

.particle {
  position: absolute;

  width: 3px;
  height: 3px;

  border-radius: 50%;

  background: #d3f576;

  box-shadow: 0 0 8px #d3f576;
}

.particle-1 {
  top: 7px;
  left: 52%;

  animation: particleFloat1 4s ease-in-out infinite;
}

.particle-2 {
  right: 5px;
  bottom: 22px;

  width: 2px;
  height: 2px;

  background: #60a5fa;

  box-shadow: 0 0 8px #60a5fa;

  animation: particleFloat2 5s ease-in-out infinite;
}

.particle-3 {
  display: none;
}

@keyframes morphRing {
  0% {
    border-radius: 55% 45% 62% 38% / 42% 58% 42% 58%;
    transform: scale(0.95);
  }

  50% {
    border-radius: 42% 58% 40% 60% / 60% 40% 55% 45%;
    transform: scale(1.05);
  }

  100% {
    border-radius: 63% 37% 52% 48% / 38% 62% 45% 55%;
    transform: scale(0.98);
  }
}

@keyframes rotateRing {
  to {
    rotate: 360deg;
  }
}

@keyframes reverseRotate {
  to {
    rotate: -360deg;
  }
}

@keyframes corePulse {
  0%,
  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0.7;
  }

  50% {
    transform: translate(-50%, -50%) scale(1.8);
    opacity: 1;
  }
}

@keyframes particleFloat1 {
  0%,
  100% {
    transform: translate(0, 0);
  }

  50% {
    transform: translate(8px, -5px);
  }
}

@keyframes particleFloat2 {
  0%,
  100% {
    transform: translate(0, 0);
  }

  50% {
    transform: translate(6px, 8px);
  }
}

/* =========================================
   RESPONSIVE
========================================= */

@media (max-width: 960px) {
  .about-container {
    padding-top: 80px;
  }

  .intro-grid,
  .profile-section,
  .expertise-grid {
    grid-template-columns: 1fr;
    gap: 55px;
  }

  .profile-section {
    padding: 90px 0;
  }

  .expertise-section {
    padding: 90px 0;
  }

  .intro-heading {
    order: 1;
  }

  .intro-content {
    order: 2;
  }

  .profile-image {
    width: 100%;
  }

  .skill-row {
    grid-template-columns: 40px 1fr;
  }

  .skill-stack {
    grid-column: 2;
    text-align: left;
    padding-bottom: 20px;
  }
}

@media (max-width: 600px) {
  .about-container {
    padding-top: 65px;
    padding-bottom: 60px;
  }

  .about-intro {
    padding: 35px 0 80px;
  }

  .heading {
    font-size: 82px;
  }

  .intro-statement {
    font-size: 18px;
  }

  .intro-actions {
    align-items: flex-start;
    flex-direction: column;
    gap: 25px;
  }

  .profile-section {
    padding: 80px 0;
  }

  .profile-image {
    aspect-ratio: 1 / 1.15;
  }

  .image-label {
    flex-direction: column;
    gap: 5px;
  }

  .expertise-section {
    padding: 80px 0;
  }

  .expertise-heading h2 {
    font-size: 70px;
  }

  .skill-row {
    grid-template-columns: 35px 1fr;
    gap: 10px;
  }

  .skill-name {
    font-size: 14px;
  }

  .skill-stack {
    font-size: 11px;
  }

  .existing-section {
    /* padding-top: 70px; */
  }

  .mouse-follower {
    display: none;
  }
}
</style>
