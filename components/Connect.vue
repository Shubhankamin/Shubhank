<template>
  <div>
    <v-container fluid class="main text-white pt-10">
      <v-row
        class="px-md-10 pt-md-10"
        data-aos="fade-up"
        data-aos-duration="3000"
      >
        <v-col cols="12" md="6">
          <p class="heading text-white bebas-Bold-h1">Let’s connect</p>
          <p class="manrope-regular-h5">Say hello at aminshubhank@gmail.com</p>
          <ul class="example-2 pt-10">
            <li class="icon-content">
              <a
                href="https://www.linkedin.com/in/shubhank-amin-a7b231225/"
                aria-label="LinkedIn"
                target="_blank"
                data-social="LinkedIn"
              >
                <div class="filled"></div>
                <v-icon>mdi-linkedin</v-icon>
              </a>
              <div class="tooltip">LinkedIn</div>
            </li>
            <li class="icon-content">
              <a
                href="https://github.com/Shubhankamin?tab=repositories"
                aria-label="github"
                data-social="github"
                target="_blank"
              >
                <div class="filled"></div>
                <v-icon>mdi-github</v-icon>
              </a>
              <div class="tooltip">GitHub</div>
            </li>
            <li class="icon-content">
              <a
                :href="whatsappLink"
                target="_blank"
                rel="noopener noreferrer"
                class="neon pointer"
                aria-label="whatsapp"
                data-social="whatsapp"
              >
                <div class="filled"></div>
                <v-icon>mdi-whatsapp</v-icon>
              </a>
              <div class="tooltip">WhatsApp</div>
            </li>
            <li class="icon-content">
              <a
                href="https://www.instagram.com/"
                aria-label="Instagram"
                target="_blank"
                data-social="instagram"
              >
                <div class="filled"></div>
                <v-icon>mdi-instagram</v-icon>
              </a>
              <div class="tooltip">Instagram</div>
            </li>
          </ul>
        </v-col>

        <!-- DESKTOP FORM -->
        <v-col cols="12" md="6" class="pr-md-10 d-none d-md-block">
          <form @submit.prevent="submitForm">
            <div>
              <p class="pb-5">Name</p>
              <input
                v-model="form.name"
                class="input w-75 py-1"
                type="text"
                placeholder="Enter your Name"
              />
            </div>
            <div>
              <p class="py-5">Email</p>
              <input
                v-model="form.email"
                class="input w-75 py-1"
                type="email"
                placeholder="Enter Email"
              />
            </div>
            <div>
              <p class="py-5">Subject</p>
              <input
                v-model="form.subject"
                class="input w-75 py-1"
                type="text"
                placeholder="Enter Subject"
              />
            </div>
            <div>
              <p class="py-5">Message</p>
              <textarea
                v-model="form.message"
                class="input w-75"
                placeholder="Message"
              />
            </div>
            <button
              type="submit"
              class="submit py-2 px-4 my-10 manrope-Bold-h5 d-flex align-center justify-center ga-2"
              :class="{ sending: loading }"
              :disabled="loading"
            >
              <span class="submit-label">{{
                loading ? "Sending" : "Submit"
              }}</span>
              <v-icon class="submit-rocket" size="20">mdi-rocket-launch</v-icon>
            </button>
          </form>
        </v-col>

        <!-- MOBILE FORM -->
        <v-col cols="12" md="6" class="px-5 d-block d-md-none">
          <form @submit.prevent="submitForm">
            <div>
              <p class="pb-5">Name</p>
              <input
                v-model="form.name"
                class="input py-1"
                type="text"
                placeholder="Enter your Name"
              />
            </div>
            <div>
              <p class="py-5">Email</p>
              <input
                v-model="form.email"
                class="input py-1"
                type="email"
                placeholder="Enter Email"
              />
            </div>
            <div>
              <p class="py-5">Subject</p>
              <input
                v-model="form.subject"
                class="input py-1"
                type="text"
                placeholder="Enter Subject"
              />
            </div>
            <div>
              <p class="py-5">Message</p>
              <textarea
                v-model="form.message"
                class="input"
                placeholder="Message"
              />
            </div>
            <div class="d-flex justify-center align-center">
              <button
                type="submit"
                class="submit py-2 px-4 my-10 manrope-Bold-h5 d-flex align-center justify-center ga-2"
                :class="{ sending: loading }"
                :disabled="loading"
              >
                <span class="submit-label">{{
                  loading ? "Sending" : "Submit"
                }}</span>
                <v-icon class="submit-rocket" size="20"
                  >mdi-rocket-launch</v-icon
                >
              </button>
            </div>
          </form>
        </v-col>
      </v-row>

      <v-snackbar
        v-model="snackbar"
        :color="snackbarColor"
        timeout="3000"
        location="top right"
        rounded="lg"
      >
        {{ snackbarMessage }}
      </v-snackbar>
    </v-container>

    <!-- FULL-LAYOUT ROCKET OVERLAY -->
    <Teleport to="body">
      <Transition name="launch-fade">
        <div
          v-if="loading"
          class="launch-overlay"
          role="status"
          aria-live="polite"
        >
          <div class="launch-stars" aria-hidden="true">
            <span v-for="(s, i) in stars" :key="i" :style="s"></span>
          </div>

          <div class="launch-rocket" aria-hidden="true">
            <v-icon class="launch-rocket-icon" size="88"
              >mdi-rocket-launch</v-icon
            >
            <div class="launch-flame"></div>
            <div class="launch-trail"></div>
          </div>

          <p class="launch-text manrope-regular-h5">
            Sending your message<span class="dots"><i></i><i></i><i></i></span>
          </p>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref } from "vue";

const whatsappLink = "https://wa.me/9731837215";

const form = ref({
  name: "",
  email: "",
  subject: "",
  message: "",
});

const loading = ref(false); // BUTTON + OVERLAY ANIMATION
const snackbar = ref(false); // SNACKBAR VISIBILITY
const snackbarMessage = ref(""); // SNACKBAR TEXT
const snackbarColor = ref("success"); // success or error

const scriptURL =
  "https://script.google.com/macros/s/AKfycbz9dTnJD-D_zmVeQa-_8dvgfnRG8bwbyLQfaa3lh-B746AXhVtF0SYurI7thqK0ymox/exec";

// Falling speed-lines behind the rocket (deterministic, so no SSR mismatch)
const stars = Array.from({ length: 18 }, (_, i) => ({
  left: `${(i * 53) % 100}%`,
  height: `${22 + (i % 4) * 16}px`,
  animationDuration: `${0.6 + (i % 5) * 0.18}s`,
  animationDelay: `${(i % 7) * 0.14}s`,
}));

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// The request is usually instant, so keep the animation up long enough
// for one full rocket launch to play.
const MIN_ANIMATION_MS = 2200;

const submitForm = async () => {
  try {
    loading.value = true;

    await Promise.all([
      fetch(scriptURL, {
        method: "POST",
        mode: "no-cors",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form.value),
      }),
      sleep(MIN_ANIMATION_MS),
    ]);

    snackbarMessage.value = "Message sent successfully!";
    snackbarColor.value = "success";
    snackbar.value = true;

    form.value = { name: "", email: "", subject: "", message: "" };
  } catch (error) {
    snackbarMessage.value = "Error sending message.";
    snackbarColor.value = "error";
    snackbar.value = true;
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.heading {
  text-transform: uppercase;
}
.neon {
  color: #d3f576;
}
.neon:hover {
  color: #0077b5;
}
/* From Uiverse.io by xueyuantan */
button {
  width: 9em;
  height: 3em;
  border-radius: 30em;
  font-size: 15px;
  font-family: inherit;
  border: 1px solid white;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.main {
  position: relative;
  overflow: hidden;
  isolation: isolate;
}

/* TOP GLOW */
.main::before {
  content: "";
  position: absolute;
  top: -200px;
  right: -150px;
  width: 600px;
  height: 600px;
  background: radial-gradient(
    circle,
    rgba(132, 204, 22, 0.08),
    transparent 70%
  );
  filter: blur(120px);
  z-index: -1;
}

/* BOTTOM GLOW */
.main::after {
  content: "";
  position: absolute;
  bottom: -250px;
  left: -150px;
  width: 600px;
  height: 600px;
  background: radial-gradient(
    circle,
    rgba(59, 130, 246, 0.08),
    transparent 70%
  );
  filter: blur(140px);
  z-index: -1;
}

button::before {
  content: "";
  width: 0;
  height: 3em;
  border-radius: 30em;
  position: absolute;
  top: 0;
  left: 0;
  background-image: linear-gradient(to right, #93da04 0%, #d3f576 100%);
  transition: 0.5s ease;
  display: block;
  z-index: -1;
}

button:hover::before {
  width: 9em;
}

.input {
  width: 100%;
  padding: 22px 20px;
  height: 54px;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: white;
  outline: none;
  transition: all 0.3s ease;
  backdrop-filter: blur(12px);
}

textarea.input {
  min-height: 140px;
  resize: vertical;
}

.input::placeholder {
  color: rgba(255, 255, 255, 0.4);
}

.input:focus {
  border-color: rgba(211, 245, 118, 0.25);
  box-shadow: 0 0 20px rgba(211, 245, 118, 0.08);
}

/* From Uiverse.io by Artahs */
ul {
  list-style: none;
}

.example-2 {
  display: flex;
}
.example-2 .icon-content {
  margin: 0 10px;
  position: relative;
}
.example-2 .icon-content .tooltip {
  position: absolute;
  top: -30px;
  left: 50%;
  transform: translateX(-50%);
  color: #fff;
  padding: 6px 10px;
  border-radius: 5px;
  opacity: 0;
  visibility: hidden;
  font-size: 14px;
  transition: all 0.3s ease;
}
.example-2 .icon-content:hover .tooltip {
  opacity: 1;
  visibility: visible;
  top: -50px;
}
.example-2 .icon-content a {
  position: relative;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  color: #4d4d4d;
  background-color: #fff;
  transition: all 0.3s ease-in-out;
}
.example-2 .icon-content a:hover {
  box-shadow: 3px 2px 45px 0px rgb(0 0 0 / 12%);
}
.example-2 .icon-content a svg {
  position: relative;
  z-index: 1;
  width: 30px;
  height: 30px;
}
.example-2 .icon-content a:hover {
  color: white;
}
.example-2 .icon-content a .filled {
  position: absolute;
  top: auto;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 0;
  background-color: #000;
  transition: all 0.3s ease-in-out;
}
.example-2 .icon-content a:hover .filled {
  height: 100%;
}

.example-2 .icon-content a[data-social="LinkedIn"] .filled,
.example-2 .icon-content a[data-social="LinkedIn"] ~ .tooltip {
  background-color: #1343f2;
}

.example-2 .icon-content a[data-social="whatsapp"] .filled,
.example-2 .icon-content a[data-social="whatsapp"] ~ .tooltip {
  background-color: #03f930;
}

.example-2 .icon-content a[data-social="github"] .filled,
.example-2 .icon-content a[data-social="github"] ~ .tooltip {
  background-color: #171d25;
}
.example-2 .icon-content a[data-social="instagram"] .filled,
.example-2 .icon-content a[data-social="instagram"] ~ .tooltip {
  background: linear-gradient(
    45deg,
    #405de6,
    #5b51db,
    #b33ab4,
    #c135b4,
    #e1306c,
    #fd1f1f
  );
}
.example-2 .icon-content a[data-social="youtube"] .filled,
.example-2 .icon-content a[data-social="youtube"] ~ .tooltip {
  background-color: #ff0000;
}

/* =====================================================
   SUBMIT BUTTON ROCKET
===================================================== */

.submit-rocket {
  transition: transform 0.35s ease;
}

.submit:hover:not(:disabled) .submit-rocket {
  transform: translate(3px, -3px);
}

.submit:disabled {
  cursor: progress;
}

/* rocket shakes, shoots out of the button, re-enters from the corner */
.submit.sending .submit-rocket {
  animation: btnLaunch 1s ease-in infinite;
}

@keyframes btnLaunch {
  0% {
    transform: translate(0, 0);
    opacity: 1;
  }
  15% {
    transform: translate(-1px, 1px);
  }
  30% {
    transform: translate(1px, -1px);
  }
  60% {
    transform: translate(30px, -30px);
    opacity: 0;
  }
  61% {
    transform: translate(-30px, 30px);
    opacity: 0;
  }
  100% {
    transform: translate(0, 0);
    opacity: 1;
  }
}

/* =====================================================
   FULL-LAYOUT LAUNCH OVERLAY
===================================================== */

.launch-overlay {
  position: fixed;
  inset: 0;
  z-index: 1000000; /* above the fixed navbar */
  overflow: hidden;
  background: rgba(5, 8, 15, 0.82);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
}

.launch-fade-enter-active,
.launch-fade-leave-active {
  transition: opacity 0.4s ease;
}

.launch-fade-enter-from,
.launch-fade-leave-to {
  opacity: 0;
}

/* speed lines */
.launch-stars span {
  position: absolute;
  top: -60px;
  width: 2px;
  border-radius: 2px;
  background: linear-gradient(
    to bottom,
    transparent,
    rgba(255, 255, 255, 0.55)
  );
  animation-name: starFall;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
}

@keyframes starFall {
  from {
    transform: translateY(0);
  }
  to {
    transform: translateY(calc(100vh + 120px));
  }
}

/* rocket */
.launch-rocket {
  position: absolute;
  left: 50%;
  bottom: 18vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  transform: translate(-50%, 0);
  animation: rocketLaunch 2.2s ease-in infinite;
}

/* the mdi rocket points up-right, turn it to point straight up */
.launch-rocket-icon {
  color: #d3f576;
  transform: rotate(-45deg);
  filter: drop-shadow(0 0 18px rgba(211, 245, 118, 0.55));
}

.launch-flame {
  width: 18px;
  height: 58px;
  margin-top: -4px;
  background: linear-gradient(
    to bottom,
    #fff,
    #d3f576 45%,
    rgba(211, 245, 118, 0)
  );
  clip-path: polygon(0 0, 100% 0, 50% 100%);
  transform-origin: top center;
  animation: flicker 0.12s ease-in-out infinite alternate;
}

.launch-trail {
  width: 3px;
  height: 45vh;
  margin-top: -2px;
  background: linear-gradient(to bottom, rgba(211, 245, 118, 0.7), transparent);
  filter: blur(1px);
}

@keyframes flicker {
  from {
    transform: scaleY(0.85);
  }
  to {
    transform: scaleY(1.15);
  }
}

/* shake on the pad, then lift off and leave the screen */
@keyframes rocketLaunch {
  0% {
    transform: translate(-50%, 0);
    opacity: 0;
  }
  8% {
    opacity: 1;
  }
  14% {
    transform: translate(calc(-50% - 2px), 0);
  }
  20% {
    transform: translate(calc(-50% + 2px), 0);
  }
  26% {
    transform: translate(calc(-50% - 2px), 0);
  }
  32% {
    transform: translate(-50%, 0);
  }
  100% {
    transform: translate(-50%, -140vh);
    opacity: 1;
  }
}

/* caption */
.launch-text {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 7vh;
  margin: 0;
  text-align: center;
  color: #fff;
}

.dots i {
  display: inline-block;
  width: 5px;
  height: 5px;
  margin-left: 4px;
  border-radius: 50%;
  background: #d3f576;
  animation: dotBlink 1.2s infinite;
}

.dots i:nth-child(2) {
  animation-delay: 0.2s;
}

.dots i:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes dotBlink {
  0%,
  80%,
  100% {
    opacity: 0.2;
  }
  40% {
    opacity: 1;
  }
}

/* reduced motion: keep a calm, static rocket */
@media (prefers-reduced-motion: reduce) {
  .launch-rocket {
    animation: none;
    opacity: 1;
  }
  .launch-stars,
  .launch-trail {
    display: none;
  }
  .launch-flame,
  .submit.sending .submit-rocket {
    animation: none;
  }
}
</style>
