<template>
  <section class="capability-section text-white">
    <v-container fluid>
      <!-- HEADER -->
      <div class="section-label" data-aos="fade-up" data-aos-duration="1000">
        <span>04</span>
        <span>CAPABILITIES</span>
      </div>

      <div
        class="capability-header"
        data-aos="fade-up"
        data-aos-duration="1200"
      >
        <h1 class="heading bebas-Bold-h1">
          WHAT I
          <span>BUILD WITH</span>
        </h1>

        <p class="capability-intro manrope-regular-h5">
          A combination of technologies, tools, and problem-solving skills I use
          to turn ideas into functional digital experiences.
        </p>
      </div>

      <!-- CAPABILITY MAP -->
      <div class="capability-map" data-aos="fade-up" data-aos-duration="1400">
        <!-- CONNECTIONS -->
        <div class="connection connection-one"></div>
        <div class="connection connection-two"></div>
        <div class="connection connection-three"></div>
        <div class="connection connection-four"></div>

        <!-- CENTER -->
        <div class="capability-core">
          <div class="core-ring"></div>

          <div class="core-content">
            <span class="core-small">I CREATE</span>

            <span class="core-main"> DIGITAL </span>

            <span class="core-main"> EXPERIENCES </span>

            <span class="core-small">
              <i></i>
              WITH CODE
            </span>
          </div>
        </div>

        <!-- FRONTEND -->
        <div class="capability-node node-frontend">
          <div class="node-number">01</div>

          <div class="node-title">FRONTEND</div>

          <div class="node-items">
            <span>Vue 3</span>
            <span>Nuxt 3</span>
            <span>React</span>
            <span>Next.js</span>
          </div>
        </div>

        <!-- BACKEND -->
        <div class="capability-node node-backend">
          <div class="node-number">02</div>

          <div class="node-title">BACKEND</div>

          <div class="node-items">
            <span>Firebase</span>
            <span>Supabase</span>
            <span>REST APIs</span>
          </div>
        </div>

        <!-- MOBILE -->
        <div class="capability-node node-mobile">
          <div class="node-number">03</div>

          <div class="node-title">MOBILE</div>

          <div class="node-items">
            <span>React Native</span>
            <span>FlutterFlow</span>
          </div>
        </div>

        <!-- TOOLS -->
        <div class="capability-node node-tools">
          <div class="node-number">04</div>

          <div class="node-title">TOOLS & CODE</div>

          <div class="node-items">
            <span>TypeScript</span>
            <span>JavaScript</span>
            <span>Git</span>
            <span>Figma</span>
            <span>C++</span>
            <span>Python</span>
          </div>
        </div>

        <!-- DECORATIVE POINTS -->
        <span class="map-point point-one"></span>
        <span class="map-point point-two"></span>
        <span class="map-point point-three"></span>
      </div>

      <!-- BOTTOM STATEMENT -->
      <div
        class="capability-footer"
        data-aos="fade-up"
        data-aos-duration="1000"
      >
        <span class="footer-line"></span>

        <p class="manrope-regular-h5">
          Technology changes.
          <span>Curiosity doesn't.</span>
        </p>

        <span class="footer-line"></span>
      </div>
    </v-container>
  </section>
</template>

<script setup></script>

<style scoped>
/* =========================================
   SECTION
========================================= */

.capability-section {
  position: relative;

  padding: 0px 0;
  padding-bottom: 50px;

  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}

/* =========================================
   LABEL
========================================= */

.section-label {
  display: flex;
  align-items: center;
  gap: 14px;

  margin-bottom: 50px;

  color: rgba(255, 255, 255, 0.4);

  font-family: "Manrope", sans-serif;

  font-size: 11px;
  font-weight: 700;

  letter-spacing: 0.15em;
}

.section-label span:first-child {
  color: #d3f576;
}

/* =========================================
   HEADER
========================================= */

.capability-header {
  display: grid;

  grid-template-columns: 1fr 0.8fr;

  gap: 8vw;

  align-items: end;

  margin-bottom: 100px;
}

.heading {
  margin: 0;

  color: #ffffff;

  font-size: clamp(75px, 10vw, 145px);

  line-height: 0.78;

  text-transform: uppercase;
}

.heading span {
  display: block;

  color: #d3f576;
}

.capability-intro {
  max-width: 570px;

  margin: 0;

  color: rgba(255, 255, 255, 0.55);

  line-height: 1.8;
}

/* =========================================
   MAP
========================================= */

.capability-map {
  position: relative;

  width: 100%;

  min-height: 720px;

  overflow: hidden;

  border-top: 1px solid rgba(255, 255, 255, 0.12);
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);

  background: radial-gradient(
    circle at 50% 50%,
    rgba(211, 245, 118, 0.055),
    transparent 28%
  );
}

/* =========================================
   CORE
========================================= */

.capability-core {
  position: absolute;

  top: 50%;
  left: 50%;

  width: 260px;
  height: 260px;

  transform: translate(-50%, -50%);

  display: flex;
  align-items: center;
  justify-content: center;

  border: 1px solid rgba(211, 245, 118, 0.25);

  border-radius: 50%;

  background: radial-gradient(
    circle,
    rgba(211, 245, 118, 0.08),
    rgba(3, 7, 18, 0.9) 65%
  );

  box-shadow:
    0 0 80px rgba(211, 245, 118, 0.06),
    inset 0 0 50px rgba(211, 245, 118, 0.04);
}

.core-ring {
  position: absolute;

  inset: -18px;

  border: 1px dashed rgba(211, 245, 118, 0.18);

  border-radius: 50%;

  animation: rotate 25s linear infinite;
}

.core-ring::before,
.core-ring::after {
  content: "";

  position: absolute;

  width: 5px;
  height: 5px;

  border-radius: 50%;

  background: #d3f576;

  box-shadow: 0 0 12px #d3f576;
}

.core-ring::before {
  top: 12%;
  right: 7%;
}

.core-ring::after {
  bottom: 10%;
  left: 5%;
}

@keyframes rotate {
  to {
    transform: rotate(360deg);
  }
}

.core-content {
  display: flex;

  flex-direction: column;

  align-items: center;

  text-align: center;

  z-index: 2;
}

.core-small {
  color: rgba(255, 255, 255, 0.4);

  font-family: "Manrope", sans-serif;

  font-size: 9px;
  font-weight: 700;

  letter-spacing: 0.2em;
}

.core-small i {
  display: inline-block;

  width: 5px;
  height: 5px;

  margin-right: 6px;

  border-radius: 50%;

  background: #d3f576;
}

.core-main {
  color: #ffffff;

  font-family: "Bebas Neue", sans-serif;

  font-size: 34px;

  line-height: 0.85;

  letter-spacing: 0.02em;
}

/* =========================================
   NODES
========================================= */

.capability-node {
  position: absolute;

  width: 250px;

  z-index: 3;
}

.node-number {
  margin-bottom: 7px;

  color: #d3f576;

  font-family: "Manrope", sans-serif;

  font-size: 10px;
  font-weight: 700;

  letter-spacing: 0.1em;
}

.node-title {
  color: #ffffff;

  font-family: "Bebas Neue", sans-serif;

  font-size: 34px;

  line-height: 0.9;

  letter-spacing: 0.02em;

  transition: color 0.3s ease;
}

.capability-node:hover .node-title {
  color: #d3f576;
}

.node-items {
  display: flex;

  flex-wrap: wrap;

  gap: 7px 14px;

  margin-top: 15px;
}

.node-items span {
  position: relative;

  color: rgba(255, 255, 255, 0.48);

  font-family: "Manrope", sans-serif;

  font-size: 12px;

  transition: color 0.3s ease;
}

.node-items span:not(:last-child)::after {
  content: "·";

  position: absolute;

  right: -9px;

  color: rgba(211, 245, 118, 0.45);
}

.capability-node:hover .node-items span {
  color: rgba(255, 255, 255, 0.8);
}

/* =========================================
   NODE POSITIONS
========================================= */

.node-frontend {
  top: 100px;
  left: 7%;
}

.node-backend {
  top: 100px;
  right: 7%;
}

.node-mobile {
  bottom: 100px;
  left: 7%;
}

.node-tools {
  bottom: 100px;
  right: 7%;
}

/* =========================================
   CONNECTIONS
========================================= */

.connection {
  position: absolute;

  height: 1px;

  background: linear-gradient(
    90deg,
    transparent,
    rgba(211, 245, 118, 0.3),
    transparent
  );

  transform-origin: left center;
}

.connection-one {
  width: 31%;

  top: 32%;

  left: 23%;

  transform: rotate(25deg);
}

.connection-two {
  width: 31%;

  top: 32%;

  right: 23%;

  transform: rotate(-25deg);
}

.connection-three {
  width: 31%;

  bottom: 32%;

  left: 23%;

  transform: rotate(-25deg);
}

.connection-four {
  width: 31%;

  bottom: 32%;

  right: 23%;

  transform: rotate(25deg);
}

/* =========================================
   MAP POINTS
========================================= */

.map-point {
  position: absolute;

  width: 5px;
  height: 5px;

  border-radius: 50%;

  background: #d3f576;

  box-shadow: 0 0 10px rgba(211, 245, 118, 0.7);

  animation: pointPulse 2.5s ease-in-out infinite;
}

.point-one {
  top: 25%;
  left: 29%;
}

.point-two {
  top: 25%;
  right: 29%;

  animation-delay: 0.8s;
}

.point-three {
  bottom: 24%;
  left: 50%;

  animation-delay: 1.4s;
}

@keyframes pointPulse {
  0%,
  100% {
    opacity: 0.3;
    transform: scale(0.8);
  }

  50% {
    opacity: 1;
    transform: scale(1.5);
  }
}

/* =========================================
   FOOTER
========================================= */

.capability-footer {
  display: flex;

  align-items: center;

  gap: 25px;

  margin-top: 70px;
}

.capability-footer p {
  flex-shrink: 0;

  margin: 0;

  color: rgba(255, 255, 255, 0.4);

  font-family: "Manrope", sans-serif;

  font-size: 12px;

  text-transform: uppercase;

  letter-spacing: 0.08em;
}

.capability-footer p span {
  color: #d3f576;
}

.footer-line {
  width: 100%;
  height: 1px;

  background: rgba(255, 255, 255, 0.12);
}

/* =========================================
   TABLET
========================================= */

@media (max-width: 960px) {
  .capability-section {
    padding: 100px 0;
  }

  .capability-header {
    grid-template-columns: 1fr;

    gap: 30px;

    margin-bottom: 70px;
  }

  .capability-map {
    min-height: 850px;
  }

  .capability-core {
    width: 220px;
    height: 220px;
  }

  .capability-node {
    width: 210px;
  }

  .node-frontend {
    top: 80px;
    left: 5%;
  }

  .node-backend {
    top: 80px;
    right: 5%;
  }

  .node-mobile {
    bottom: 80px;
    left: 5%;
  }

  .node-tools {
    bottom: 80px;
    right: 5%;
  }

  .connection-one,
  .connection-two,
  .connection-three,
  .connection-four {
    width: 25%;
  }
}

/* =========================================
   MOBILE
========================================= */

@media (max-width: 600px) {
  .capability-section {
    padding: 80px 0;
  }

  .section-label {
    margin-bottom: 35px;
  }

  .heading {
    font-size: 70px;
  }

  .capability-intro {
    font-size: 14px;
    line-height: 1.7;
  }

  .capability-header {
    margin-bottom: 55px;
  }

  .capability-map {
    min-height: auto;

    display: flex;

    flex-direction: column;

    gap: 0;

    padding: 40px 0;

    overflow: visible;

    background: none;
  }

  .capability-core {
    position: relative;

    top: auto;
    left: auto;

    transform: none;

    width: 190px;
    height: 190px;

    margin: 0 auto 60px;
  }

  .core-main {
    font-size: 28px;
  }

  .capability-node {
    position: relative;

    top: auto;
    right: auto;
    bottom: auto;
    left: auto;

    width: 100%;

    padding: 25px 0;

    border-top: 1px solid rgba(255, 255, 255, 0.12);
  }

  .capability-node:last-of-type {
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  }

  .node-title {
    font-size: 30px;
  }

  .connection,
  .map-point {
    display: none;
  }

  .capability-footer {
    margin-top: 50px;
  }

  .capability-footer p {
    font-size: 9px;
    text-align: center;
  }
}
</style>
