<template>
  <section
    ref="section"
    class="name-reveal"
    @pointermove="handlePointerMove"
    @pointerleave="handlePointerLeave"
  >
    <!-- Background atmosphere -->
    <div class="atmosphere"></div>

    <!-- Fine grid -->
    <div class="grid"></div>

    <!-- Top information -->
    <div class="hero-meta mt-16 pt-16">
      <!-- <span>PORTFOLIO / 2026</span> -->

      <!-- <span class="meta-line"></span> -->

      <span>FRONT-END · FULL-STACK · CREATIVE</span>
    </div>

    <!-- Main content -->
    <div class="name-stage">
      <!-- Small eyebrow -->
      <div class="eyebrow w-100 px-10 pt-12">
        <span class="eyebrow-dot mt-1"></span>

        <span>HELLO, I'M</span>
      </div>

      <!-- Name -->
      <div ref="nameEl" class="name" aria-label="Shubhank Amin">
        <span
          v-for="(letter, index) in letters"
          :key="index"
          :ref="(el) => setLetterRef(el, index)"
          class="letter-slot"
          :class="{
            'is-space': letter === ' ',
            active: activeLetter === index,
          }"
          :tabindex="letter === ' ' ? -1 : 0"
          @focus="focusLetter(index)"
          @blur="clearFocus"
          @click="handleTap(index)"
        >
          <span class="letter" :style="getLetterStyle(index)">
            {{ letter === " " ? "\u00A0" : letter }}
          </span>
        </span>
      </div>

      <!-- Description -->
      <!-- <div class="hero-description">
        <span class="line"></span>

        <p>
          Building digital experiences that feel
          <strong>alive</strong>.
        </p>

        <span class="line"></span>
      </div> -->

      <!-- Interaction hint -->
      <div class="interaction">
        <div class="interaction-icon">
          <span></span>
        </div>

        <div>
          <span class="interaction-title"> MOVE THROUGH THE NAME </span>

          <span class="interaction-subtitle"> REVEAL EACH LETTER </span>
        </div>
      </div>
    </div>

    <!-- Bottom -->
    <div class="bottom-meta">
      <!-- <span>01 / 06</span> -->

      <div class="scroll-indicator">
        <span></span>
      </div>

      <span>SCROLL TO EXPLORE</span>
    </div>

    <!-- Horizontal scan -->
    <div class="scan-line"></div>
  </section>
</template>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref } from "vue";

const name = "SHUBHANK AMIN";

const letters = [...name];

const section = ref(null);

const letterRefs = [];

const cursorX = ref(-1000);
const cursorY = ref(-1000);

const activeLetter = ref(-1);

let rafId = null;
let targetX = -1000;
let targetY = -1000;

const setLetterRef = (el, index) => {
  if (el) {
    letterRefs[index] = el;
  }
};

/* =========================================================
   MOUSE MOVEMENT
========================================================= */

const handlePointerMove = (event) => {
  targetX = event.clientX;
  targetY = event.clientY;

  if (!rafId) {
    rafId = requestAnimationFrame(updateCursor);
  }
};

const updateCursor = () => {
  cursorX.value += (targetX - cursorX.value) * 0.18;

  cursorY.value += (targetY - cursorY.value) * 0.18;

  rafId = null;

  if (
    Math.abs(targetX - cursorX.value) > 0.5 ||
    Math.abs(targetY - cursorY.value) > 0.5
  ) {
    rafId = requestAnimationFrame(updateCursor);
  }
};

const handlePointerLeave = () => {
  targetX = -1000;
  targetY = -1000;
  activeLetter.value = -1;
};

/* =========================================================
   LETTER PROXIMITY
========================================================= */

const getLetterOpenness = (index) => {
  const el = letterRefs[index];

  if (!el) {
    return 0.055;
  }

  const rect = el.getBoundingClientRect();

  const centerX = rect.left + rect.width / 2;

  const distance = Math.abs(cursorX.value - centerX);

  /*
    Main interaction radius.
    Smaller = sharper effect.
  */
  const radius = 110;

  let openness = 1 - distance / radius;

  openness = Math.max(0, Math.min(1, openness));

  /*
    Minimum width so the letters
    never completely disappear.
  */
  return 0.055 + openness * 0.945;
};

/* =========================================================
   LETTER STYLE
========================================================= */

const getLetterStyle = (index) => {
  const openness = getLetterOpenness(index);

  /*
    Slight vertical movement makes
    the typography feel alive.
  */
  const distance = Math.abs(
    cursorX.value - (letterRefs[index]?.getBoundingClientRect().left || 0),
  );

  const lift = Math.max(0, 1 - distance / 150) * 7;

  return {
    transform: `
      scaleX(${openness})
      translateY(${-lift}px)
    `,
    opacity: 0.55 + openness * 0.45,
  };
};

/* =========================================================
   KEYBOARD / TAP
========================================================= */

const focusLetter = (index) => {
  activeLetter.value = index;
};

const clearFocus = () => {
  activeLetter.value = -1;
};

const handleTap = (index) => {
  activeLetter.value = activeLetter.value === index ? -1 : index;
};

/* =========================================================
   MOUNT
========================================================= */

onMounted(async () => {
  await nextTick();

  /*
    Small initial entrance.
    Cursor starts outside the component.
  */
  cursorX.value = -1000;
  cursorY.value = -1000;
});

onBeforeUnmount(() => {
  if (rafId) {
    cancelAnimationFrame(rafId);
  }
});
</script>

<style scoped>
/* =========================================================
   SECTION
========================================================= */

.name-reveal {
  position: relative;

  width: 100%;
  min-height: calc(100vh - 90px);

  display: flex;
  align-items: center;
  justify-content: center;

  overflow: hidden;

  background: #030712;

  color: white;

  user-select: none;
}

/* =========================================================
   ATMOSPHERE
========================================================= */

.atmosphere {
  position: absolute;
  inset: -20%;

  background:
    radial-gradient(
      circle at 25% 45%,
      rgba(59, 130, 246, 0.11),
      transparent 28%
    ),
    radial-gradient(
      circle at 75% 55%,
      rgba(132, 204, 22, 0.09),
      transparent 25%
    ),
    radial-gradient(
      circle at 50% 20%,
      rgba(147, 51, 234, 0.06),
      transparent 30%
    );

  filter: blur(80px);

  animation: atmosphereMove 16s ease-in-out infinite alternate;

  pointer-events: none;
}

@keyframes atmosphereMove {
  from {
    transform: scale(1) translate3d(-2%, 0, 0);
  }

  to {
    transform: scale(1.1) translate3d(2%, -2%, 0);
  }
}

/* =========================================================
   GRID
========================================================= */

.grid {
  position: absolute;
  inset: 0;

  background-image:
    linear-gradient(rgba(255, 255, 255, 0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.025) 1px, transparent 1px);

  background-size: 80px 80px;

  mask-image: linear-gradient(
    to bottom,
    transparent,
    black 20%,
    black 80%,
    transparent
  );

  pointer-events: none;

  opacity: 0.4;
}

/* =========================================================
   TOP META
========================================================= */

.hero-meta {
  position: absolute;

  top: 30px;
  left: 40px;
  right: 40px;

  display: flex;
  align-items: center;
  gap: 18px;

  color: rgba(255, 255, 255, 0.4);

  font-family: monospace;
  font-size: 10px;

  letter-spacing: 0.18em;

  z-index: 5;
}

.meta-line {
  width: 45px;
  height: 1px;

  background: rgba(255, 255, 255, 0.25);
}

/* =========================================================
   MAIN STAGE
========================================================= */

.name-stage {
  position: relative;

  width: 100%;

  display: flex;
  flex-direction: column;

  align-items: center;

  z-index: 3;

  animation: stageReveal 1.4s cubic-bezier(0.16, 1, 0.3, 1) both;
}

@keyframes stageReveal {
  from {
    opacity: 0;

    transform: translateY(35px) scale(0.97);
  }

  to {
    opacity: 1;

    transform: translateY(0) scale(1);
  }
}

/* =========================================================
   EYEBROW
========================================================= */

.eyebrow {
  display: flex;
 

  gap: 10px;

  margin-bottom: 35px;

  color: rgba(255, 255, 255, 0.5);

  font-family: monospace;

  font-size: 11px;

  letter-spacing: 0.3em;

  animation: fadeIn 1s 0.4s both;
}

.eyebrow-dot {
  width: 6px;
  height: 6px;

  border-radius: 50%;

  background: #d3f576;

  box-shadow: 0 0 10px rgba(211, 245, 118, 0.7);

  animation: pulseDot 2s ease-in-out infinite;
}

@keyframes pulseDot {
  50% {
    transform: scale(1.7);

    opacity: 0.5;
  }
}

/* =========================================================
   NAME
========================================================= */

.name {
  width: 100%;

  display: flex;

  align-items: center;
  justify-content: center;

  padding: 0 2vw;

  white-space: nowrap;
}

/* =========================================================
   LETTER SLOT
========================================================= */

.letter-slot {
  position: relative;

  width: clamp(48px, 7vw, 125px);

  height: clamp(150px, 20vw, 330px);

  display: flex;

  align-items: center;
  justify-content: center;

  flex-shrink: 0;

  cursor: crosshair;

  outline: none;

  z-index: 1;

  transition: z-index 0.2s ease;
}

.letter-slot:hover,
.letter-slot:focus {
  z-index: 10;
}

/* SPACE */

.letter-slot.is-space {
  width: clamp(22px, 3vw, 55px);

  cursor: default;
}

/* =========================================================
   LETTER
========================================================= */

.letter {
  display: block;

  flex-shrink: 0;

  font-family: "Roboto Condensed", "Arial Narrow", Arial, sans-serif;

  font-size: clamp(8rem, 17vw, 16rem);

  font-weight: 200;

  line-height: 0.72;

  letter-spacing: -0.055em;

  color: rgba(255, 255, 255, 0.6);

  transform-origin: center center;

  transition:
    transform 0.35s cubic-bezier(0.16, 1, 0.3, 1),
    opacity 0.35s ease,
    color 0.35s ease,
    text-shadow 0.35s ease;

  will-change: transform;

  pointer-events: none;
}

/* =========================================================
   HOVERED LETTER
========================================================= */

.letter-slot:hover .letter,
.letter-slot:focus .letter {
  background: linear-gradient(
    180deg,
    #d3f576 0%,
    #d3f576 45%,
    #60a5fa 55%,
    #3b82f6 100%
  );

  -webkit-background-clip: text;
  background-clip: text;

  color: transparent;
  -webkit-text-fill-color: transparent;

  filter: brightness(1.25);

  text-shadow:
    0 0 3px rgba(211, 245, 118, 0.9),
    0 0 12px rgba(211, 245, 118, 0.55),
    0 0 28px rgba(96, 165, 250, 0.45),
    0 0 50px rgba(59, 130, 246, 0.2);
}
.letter-slot::after {
  content: "";

  position: absolute;

  width: 1px;
  height: 0;

  top: 50%;
  left: 50%;

  background: linear-gradient(
    to bottom,
    transparent,
    #d3f576 25%,
    #d3f576 45%,
    #60a5fa 55%,
    #3b82f6 75%,
    transparent
  );

  box-shadow:
    0 0 8px rgba(211, 245, 118, 0.8),
    0 0 18px rgba(96, 165, 250, 0.6);

  opacity: 0;

  transform: translate(-50%, -50%);

  transition:
    height 0.45s ease,
    opacity 0.3s ease;

  pointer-events: none;
}

.letter-slot:hover::after,
.letter-slot:focus::after {
  height: 75%;
  opacity: 0.9;
}
.letter-slot:hover::after,
.letter-slot:focus::after {
  height: 75%;
  opacity: 0.9;
}

.letter-slot:hover::after,
.letter-slot:focus::after {
  height: 75%;

  opacity: 0.8;
}
/* =========================================================
   DESCRIPTION
========================================================= */

.hero-description {
  display: flex;

  align-items: center;

  gap: 20px;

  margin-top: 35px;

  color: rgba(255, 255, 255, 0.4);

  font-size: 13px;

  letter-spacing: 0.04em;

  animation: fadeIn 1s 0.8s both;
}

.hero-description p {
  margin: 0;
}

.hero-description strong {
  color: #d3f576;

  font-weight: 500;
}

.line {
  width: 35px;

  height: 1px;

  background: rgba(255, 255, 255, 0.2);
}

/* =========================================================
   INTERACTION
========================================================= */

.interaction {
  display: flex;

  align-items: center;

  gap: 12px;

  margin-top: 55px;

  opacity: 0.65;

  animation: fadeIn 1s 1.1s both;
}

.interaction-icon {
  width: 28px;
  height: 28px;

  border: 1px solid rgba(211, 245, 118, 0.35);

  border-radius: 50%;

  display: flex;

  align-items: center;
  justify-content: center;
}

.interaction-icon span {
  width: 5px;
  height: 5px;

  border-radius: 50%;

  background: #d3f576;

  box-shadow: 0 0 8px rgba(211, 245, 118, 0.8);
}

.interaction-title,
.interaction-subtitle {
  display: block;

  font-family: monospace;

  font-size: 9px;

  letter-spacing: 0.18em;
}

.interaction-title {
  color: rgba(255, 255, 255, 0.7);
}

.interaction-subtitle {
  margin-top: 4px;

  color: rgba(255, 255, 255, 0.3);
}

/* =========================================================
   BOTTOM META
========================================================= */

.bottom-meta {
  position: absolute;

  bottom: 28px;

  left: 40px;
  right: 40px;

  display: flex;

  justify-content: space-between;

  align-items: center;

  color: rgba(255, 255, 255, 0.3);

  font-family: monospace;

  font-size: 9px;

  letter-spacing: 0.18em;

  z-index: 5;
}

/* =========================================================
   SCROLL INDICATOR
========================================================= */

.scroll-indicator {
  position: absolute;

  left: 50%;

  transform: translateX(-50%);

  width: 1px;

  height: 35px;

  background: rgba(255, 255, 255, 0.12);

  overflow: hidden;
}

.scroll-indicator span {
  display: block;

  width: 100%;
  height: 45%;

  background: #d3f576;

  animation: scrollLine 1.8s ease-in-out infinite;
}

@keyframes scrollLine {
  0% {
    transform: translateY(-100%);
  }

  50% {
    transform: translateY(120%);
  }

  100% {
    transform: translateY(220%);
  }
}

/* =========================================================
   SCAN LINE
========================================================= */

.scan-line {
  position: absolute;

  left: 0;

  width: 100%;
  height: 1px;

  top: 50%;

  background: linear-gradient(
    90deg,
    transparent,
    rgba(211, 245, 118, 0.15),
    transparent
  );

  opacity: 0.5;

  pointer-events: none;

  animation: scanMove 8s ease-in-out infinite;
}

@keyframes scanMove {
  0%,
  100% {
    transform: translateY(-120px);
  }

  50% {
    transform: translateY(120px);
  }
}

/* =========================================================
   GENERAL
========================================================= */

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* =========================================================
   TABLET
========================================================= */

@media (max-width: 900px) {
  .hero-meta {
    left: 20px;
    right: 20px;
  }

  .letter-slot {
    width: 6vw;
  }

  .letter {
    font-size: clamp(6rem, 16vw, 10rem);
  }

  .hero-description {
    margin-top: 25px;
  }
}

/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 600px) {
  .name-reveal {
    min-height: 75vh;
  }

  .hero-meta {
    top: 20px;

    font-size: 7px;

    gap: 8px;

    letter-spacing: 0.12em;
  }

  .hero-meta span:last-child {
    display: none;
  }

  .letter-slot {
    width: 22px;

    height: 130px;
  }

  .letter-slot.is-space {
    width: 10px;
  }

  .letter {
    font-size: 5rem;

    transform: scaleX(0.08);
  }

  .hero-description {
    font-size: 10px;

    text-align: center;

    padding: 0 25px;
  }

  .hero-description .line {
    width: 15px;
  }

  .interaction {
    margin-top: 35px;
  }

  .bottom-meta {
    left: 20px;
    right: 20px;

    bottom: 20px;
  }

  .scan-line {
    display: none;
  }
}

/* =========================================================
   REDUCED MOTION
========================================================= */

@media (prefers-reduced-motion: reduce) {
  .atmosphere,
  .name-stage,
  .eyebrow,
  .hero-description,
  .interaction,
  .scroll-indicator span,
  .scan-line {
    animation: none;
  }

  .letter {
    transition: none;
  }
}
</style>
