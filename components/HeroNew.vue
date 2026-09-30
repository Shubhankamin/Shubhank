<template>
  <div>
    <v-container fluid class="main pt-md-16">
      <v-row
        class="mt-md-14 mt-8 mb-10"
        data-aos="fade-up"
        data-aos-duration="2000"
      >
        <!-- LEFT : content (unchanged) -->
        <v-col cols="12" md="7" sm="6" class="pt-md-16 pt-md-7">
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
                  <v-icon class="icon github">mdi-github</v-icon>
                </a>
              </div>
            </div>
          </div>
        </v-col>

        <!-- RIGHT : hanging ID card -->
        <v-col cols="12" md="5" sm="6" class="pt-10 pt-sm-0 pt-md-0 pr-md-16">
          <div ref="stage" class="badge-stage">
            <div
              ref="swing"
              class="swing"
              :class="{ dragging }"
              @pointerdown="onDown"
              @pointermove="onMove"
              @pointerup="onUp"
              @pointercancel="onUp"
            >
              <!-- lanyard -->
              <div class="strap"></div>
              <div class="clip"><span></span></div>

              <!-- card -->
              <div class="id-card">
                <div class="slot"></div>

                <div class="card-top">
                  <div class="avatar">
                    <img
                      :src="profile.photo"
                      :alt="profile.name"
                      draggable="false"
                    />
                    <span class="avatar-dot"></span>
                  </div>
                </div>

                <div class="card-body">
                  <h3 class="card-name">{{ profile.name }}</h3>
                  <span class="role-pill">{{ profile.role }}</span>
                  <div class="rule"></div>

                  <div class="info-grid">
                    <div v-for="item in profile.info" :key="item.label">
                      <p class="info-label">{{ item.label }}</p>
                      <p class="info-value" :class="{ active: item.active }">
                        <span v-if="item.active" class="status-dot"></span
                        >{{ item.value }}
                      </p>
                    </div>
                  </div>

                  <div class="barcode-box">
                    <div class="barcode">
                      <span
                        v-for="(w, i) in bars"
                        :key="i"
                        :style="{
                          width: w + 'px',
                          height: (i % 3 === 0 ? 22 : 14) + 'px',
                        }"
                      ></span>
                    </div>
                    <div class="barcode-meta">
                      <span>{{ profile.dob }}</span>
                      <span>{{ profile.org }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <p class="hint manrope-regular-h5">Drag or click the card</p>
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

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";

/* ---- edit the card content here ---- */
const profile = {
  photo: "/images/me/me_new_1.jpeg",
  name: "Shubhank Amin",
  role: "Full Stack Developer",
  dob: "01-04-2002",
  org: "MIT MANIPAL",
  info: [
    { label: "SPECIALTY", value: "Nuxt 3 & Vue 3" },
    { label: "LOCATION", value: "Manipal, India" },
    { label: "EDUCATION", value: "MCA, MIT Manipal" },
    { label: "STATUS", value: "Active", active: true },
  ],
};

const bars = [
  2, 1, 3, 1, 2, 1, 1, 3, 2, 1, 2, 3, 1, 1, 2, 1, 3, 1, 2, 2, 1, 3, 1, 2, 1, 1,
  3, 2, 1, 2,
];

/* ---- swing physics (pendulum around the top of the lanyard) ---- */
const stage = ref(null);
const swing = ref(null);
const dragging = ref(false);

let angle = 0; // degrees
let velocity = 0;
let raf = 0;
let last = 0;
let moved = false;
let downPos = { x: 0, y: 0 };

const STIFFNESS = 38; // pull back to vertical
const DAMPING = 2.4; // air resistance
const MAX_ANGLE = 65;

function pivot() {
  const r = stage.value.getBoundingClientRect();
  return { x: r.left + r.width / 2, y: r.top };
}

function apply() {
  if (swing.value) {
    swing.value.style.transform = `translateX(-50%) rotate(${angle}deg)`;
  }
}

function tick(t) {
  const dt = Math.min((t - last) / 1000, 0.032) || 0.016;
  last = t;
  if (!dragging.value) {
    velocity += (-STIFFNESS * angle - DAMPING * velocity) * dt;
    angle += velocity * dt;
    if (Math.abs(angle) < 0.01 && Math.abs(velocity) < 0.05) {
      angle = 0;
      velocity = 0;
    }
  }
  apply();
  raf = requestAnimationFrame(tick);
}

function onDown(e) {
  dragging.value = true;
  moved = false;
  downPos = { x: e.clientX, y: e.clientY };
  e.currentTarget.setPointerCapture(e.pointerId);
}

function onMove(e) {
  if (!dragging.value) return;
  if (Math.hypot(e.clientX - downPos.x, e.clientY - downPos.y) > 4)
    moved = true;
  const p = pivot();
  const target = (Math.atan2(p.x - e.clientX, e.clientY - p.y) * 180) / Math.PI;
  const next = Math.max(-MAX_ANGLE, Math.min(MAX_ANGLE, target));
  velocity = (next - angle) * 18; // carries momentum into the release
  angle = next;
}

function onUp() {
  if (!dragging.value) return;
  dragging.value = false;
  if (!moved) velocity += angle >= 0 ? -160 : 160; // click = swing kick
}

onMounted(() => {
  // gentle intro swing
  angle = 28;
  last = performance.now();
  raf = requestAnimationFrame(tick);
});

onBeforeUnmount(() => cancelAnimationFrame(raf));
</script>

<style scoped>
.heading {
  text-transform: uppercase;
  color: #d3f576;
  line-height: 0.9;
}

.main {
  position: relative;
  width: 100%;
  overflow: hidden;
  background: transparent;
}

/* TEXT */
.manrope-regular-h5 {
  color: rgba(255, 255, 255, 0.72);
  line-height: 1.8;
  max-width: 700px;
}

.v-divider {
  opacity: 0.2;
}

/* CONTACT SECTION */
.contact-section {
  display: flex;
  align-items: center;
  gap: 18px;
  flex-wrap: wrap;
}

.contact-button {
  background-color: #d3f576;
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
  background-color: #0077b5;
  color: #d3f576;
}

.contact-button .dot {
  width: 8px;
  height: 8px;
  background-color: black;
  border-radius: 50%;
  margin-left: 8px;
  transition: background-color 0.3s ease;
}

.contact-button:hover .dot {
  background-color: #d3f576;
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
  background-color: #333;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #d3f576;
  font-size: 20px;
  cursor: pointer;
}

.icon.linkedin:hover {
  background-color: #0077b5;
}

.icon.github:hover {
  background-color: #333;
}

/* ---------- BADGE ---------- */
.badge-stage {
  position: relative;
  height: 640px;
  display: flex;
  justify-content: center;
  user-select: none;
}

.swing {
  position: absolute;
  top: 0;
  left: 50%;
  width: 300px;
  transform: translateX(-50%);
  transform-origin: 50% 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: grab;
  touch-action: none;
  will-change: transform;
}

.swing.dragging {
  cursor: grabbing;
}

/* lanyard */
.strap {
  width: 18px;
  height: 90px;
  background: repeating-linear-gradient(
    180deg,
    #d3f576 0 10px,
    #b8dc5c 10px 12px
  );
  border-radius: 0 0 4px 4px;
  box-shadow: 0 0 20px rgba(211, 245, 118, 0.25);
}

.clip {
  width: 26px;
  height: 34px;
  margin-top: -2px;
  border-radius: 6px;
  background: linear-gradient(180deg, #2a2f3a, #0b0f17);
  border: 1px solid rgba(255, 255, 255, 0.12);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 6px;
  position: relative;
  z-index: 2;
}

.clip span {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #d3f576;
}

/* card */
.id-card {
  width: 300px;
  margin-top: -10px;
  border-radius: 28px;
  overflow: hidden;
  background: #0b1220;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow:
    0 30px 60px rgba(0, 0, 0, 0.55),
    0 0 50px rgba(132, 204, 22, 0.14);
  position: relative;
}

.slot {
  position: absolute;
  top: 12px;
  left: 50%;
  transform: translateX(-50%);
  width: 46px;
  height: 8px;
  border-radius: 8px;
  background: #030712;
  border: 1px solid rgba(255, 255, 255, 0.12);
  z-index: 3;
}

.card-top {
  height: 150px;
  position: relative;
  display: flex;
  justify-content: center;
  background:
    linear-gradient(
      115deg,
      transparent 35%,
      rgba(255, 255, 255, 0.22) 50%,
      transparent 65%
    ),
    linear-gradient(135deg, #d3f576 0%, #5f9c1f 38%, #0f2a1d 100%);
}

.avatar {
  position: absolute;
  bottom: -48px;
  width: 150px;
  height: 154px;
  border-radius: 50%;
  padding: 4px;
  background: #0b1220;
  border: 2px solid #d3f576;
  box-shadow: 0 0 24px rgba(211, 245, 118, 0.35);
}

.avatar img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: top;
  pointer-events: none;
}

.avatar-dot {
  position: absolute;
  right: 6px;
  bottom: 8px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #22c55e;
  border: 3px solid #0b1220;
}

.card-body {
  padding: 62px 20px 18px;
  text-align: center;
}

.card-name {
  color: #fff;
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -0.02em;
}

.role-pill {
  display: inline-block;
  margin-top: 8px;
  padding: 4px 14px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
  color: #d3f576;
  background: rgba(211, 245, 118, 0.08);
  border: 1px solid rgba(211, 245, 118, 0.3);
}

.rule {
  height: 1px;
  margin: 16px 0;
  background: rgba(255, 255, 255, 0.18);
}

.info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px 12px;
  padding: 14px;
  text-align: left;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.info-label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.06em;
  color: rgba(255, 255, 255, 0.45);
  margin: 0 0 3px;
}

.info-value {
  font-size: 13px;
  font-weight: 700;
  color: #fff;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 6px;
}

.info-value.active {
  color: #22c55e;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #22c55e;
}

.barcode-box {
  margin-top: 14px;
  padding: 8px 10px 6px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.barcode {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: 2px;
  height: 24px;
}

.barcode span {
  display: block;
  background: #d3f576;
}

.barcode-meta {
  display: flex;
  justify-content: space-between;
  margin-top: 6px;
  font-size: 10px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.7);
}

/* .hint {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  margin: 0 auto;
  text-align: center;
  font-size: 12px;
  line-height: 1;
  color: rgba(255, 255, 255, 0.4);
} */

.hint {
  margin: 30px 0 0;
  text-align: center;
  font-size: 12px;
  line-height: 1;
  color: rgba(255, 255, 255, 0.4);
}

@media (max-width: 960px) {
  .badge-stage {
    height: 600px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .swing {
    transition: none;
  }
}
</style>
