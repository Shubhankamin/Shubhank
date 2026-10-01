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
          <form novalidate @submit.prevent="submitForm">
            <div>
              <p class="pb-5">Name</p>
              <input
                v-model="form.name"
                data-field="name"
                class="input w-75 py-1"
                :class="{
                  'input-error': isBad('name'),
                  shake: validationError && isBad('name'),
                }"
                type="text"
                placeholder="Enter your Name"
              />
            </div>
            <div>
              <p class="py-5">Email</p>
              <input
                v-model="form.email"
                data-field="email"
                class="input w-75 py-1"
                :class="{
                  'input-error': isBad('email'),
                  shake: validationError && isBad('email'),
                }"
                type="email"
                placeholder="Enter Email"
              />
            </div>
            <div>
              <p class="py-5">Subject</p>
              <input
                v-model="form.subject"
                data-field="subject"
                class="input w-75 py-1"
                :class="{
                  'input-error': isBad('subject'),
                  shake: validationError && isBad('subject'),
                }"
                type="text"
                placeholder="Enter Subject"
              />
            </div>
            <div>
              <p class="py-5">Message</p>
              <textarea
                v-model="form.message"
                data-field="message"
                class="input w-75"
                :class="{
                  'input-error': isBad('message'),
                  shake: validationError && isBad('message'),
                }"
                placeholder="Message"
              />
            </div>
            <button
              type="submit"
              class="submit py-2 px-4 my-10 manrope-Bold-h5 d-flex align-center justify-center ga-2"
              :class="{ sending: loading, abort: validationError }"
              :disabled="loading"
            >
              <span class="submit-label">{{ buttonLabel }}</span>
              <v-icon class="submit-rocket" size="20">mdi-rocket-launch</v-icon>
            </button>
          </form>
        </v-col>

        <!-- MOBILE FORM -->
        <v-col cols="12" md="6" class="px-5 d-block d-md-none">
          <form novalidate @submit.prevent="submitForm">
            <div>
              <p class="pb-5">Name</p>
              <input
                v-model="form.name"
                data-field="name"
                class="input py-1"
                :class="{
                  'input-error': isBad('name'),
                  shake: validationError && isBad('name'),
                }"
                type="text"
                placeholder="Enter your Name"
              />
            </div>
            <div>
              <p class="py-5">Email</p>
              <input
                v-model="form.email"
                data-field="email"
                class="input py-1"
                :class="{
                  'input-error': isBad('email'),
                  shake: validationError && isBad('email'),
                }"
                type="email"
                placeholder="Enter Email"
              />
            </div>
            <div>
              <p class="py-5">Subject</p>
              <input
                v-model="form.subject"
                data-field="subject"
                class="input py-1"
                :class="{
                  'input-error': isBad('subject'),
                  shake: validationError && isBad('subject'),
                }"
                type="text"
                placeholder="Enter Subject"
              />
            </div>
            <div>
              <p class="py-5">Message</p>
              <textarea
                v-model="form.message"
                data-field="message"
                class="input"
                :class="{
                  'input-error': isBad('message'),
                  shake: validationError && isBad('message'),
                }"
                placeholder="Message"
              />
            </div>
            <div class="d-flex justify-center align-center">
              <button
                type="submit"
                class="submit py-2 px-4 my-10 manrope-Bold-h5 d-flex align-center justify-center ga-2"
                :class="{ sending: loading, abort: validationError }"
                :disabled="loading"
              >
                <span class="submit-label">{{ buttonLabel }}</span>
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

    <!-- PRE-LAUNCH CHECKLIST (validation feedback) -->
    <Teleport to="body">
      <Transition name="hud">
        <div
          v-if="showChecks"
          class="hud"
          :class="{ ready: allReady }"
          role="alert"
          aria-live="assertive"
          @click="showChecks = false"
        >
          <div class="hud-stripe"></div>
          <div class="hud-body">
            <div class="hud-head">
              <div class="hud-rocket" aria-hidden="true">
                <v-icon class="hud-rocket-icon" size="34"
                  >mdi-rocket-launch</v-icon
                >
                <div v-if="allReady" class="hud-flame"></div>
                <div v-else class="hud-smoke"><i></i><i></i><i></i></div>
              </div>
              <div>
                <p class="hud-title">
                  {{ allReady ? "All systems go" : "Launch aborted" }}
                </p>
                <p class="hud-sub">
                  {{
                    allReady
                      ? "Ready for liftoff. Hit submit."
                      : `${failed.length} of ${checklist.length} systems not ready`
                  }}
                </p>
              </div>
            </div>

            <!-- mobile: compact chips instead of the full list -->
            <div v-if="!allReady" class="hud-chips">
              <span v-for="c in failed" :key="c.key">{{ c.label }}</span>
            </div>

            <ul class="hud-list">
              <li v-for="c in checklist" :key="c.key" :class="{ ok: c.ok }">
                <v-icon size="18">{{
                  c.ok ? "mdi-check-circle" : "mdi-close-circle"
                }}</v-icon>
                <span class="hud-label">{{ c.label }}</span>
                <span class="hud-hint">{{ c.ok ? "Ready" : c.hint }}</span>
              </li>
            </ul>

            <div class="hud-meter" aria-hidden="true">
              <span
                v-for="c in checklist"
                :key="c.key"
                :class="{ on: c.ok }"
              ></span>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>

    <!-- FULL-LAYOUT ROCKET OVERLAY (only after validation passes) -->
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
            <!-- glow behind rocket -->
            <div class="rocket-glow"></div>

            <!-- smoke before liftoff -->
            <div class="rocket-smoke">
              <i></i>
              <i></i>
              <i></i>
              <i></i>
              <i></i>
            </div>

            <!-- rocket -->
            <div class="rocket-body">
              <v-icon class="launch-rocket-icon" size="82">
                mdi-rocket-launch
              </v-icon>
            </div>

            <!-- engine -->
            <div class="rocket-engine">
              <div class="engine-core"></div>

              <div class="engine-flame flame-inner"></div>
              <div class="engine-flame flame-middle"></div>
              <div class="engine-flame flame-outer"></div>
            </div>

            <!-- exhaust -->
            <div class="rocket-exhaust">
              <span></span>
              <span></span>
              <span></span>
            </div>
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
import { ref, computed, watch, nextTick, onBeforeUnmount } from "vue";

const whatsappLink = "https://wa.me/9731837215";

const form = ref({
  name: "",
  email: "",
  subject: "",
  message: "",
});

const loading = ref(false); // BUTTON + OVERLAY ANIMATION
const validationError = ref(false); // short-lived: drives shake / misfire
const showChecks = ref(false); // pre-launch checklist visibility
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

const MIN_ANIMATION_MS = 2200;

const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const okMap = computed(() => {
  const f = form.value;
  return {
    name: !!f.name.trim(),
    email: emailRe.test(f.email.trim()),
    subject: !!f.subject.trim(),
    message: !!f.message.trim(),
  };
});

const checklist = computed(() => [
  { key: "name", label: "Name", ok: okMap.value.name, hint: "Missing" },
  {
    key: "email",
    label: "Email",
    ok: okMap.value.email,
    hint: form.value.email.trim() ? "Invalid address" : "Missing",
  },
  {
    key: "subject",
    label: "Subject",
    ok: okMap.value.subject,
    hint: "Missing",
  },
  {
    key: "message",
    label: "Message",
    ok: okMap.value.message,
    hint: "Missing",
  },
]);

const failed = computed(() => checklist.value.filter((c) => !c.ok));
const allReady = computed(() => failed.value.length === 0);

const isBad = (key) => showChecks.value && !okMap.value[key];

const buttonLabel = computed(() =>
  loading.value ? "Sending" : validationError.value ? "Hold on" : "Submit",
);

let hideTimer;
let shakeTimer;

const isMobile = () =>
  typeof window !== "undefined" &&
  window.matchMedia("(max-width: 959.98px)").matches;

// shorter on mobile so the card never lingers over the form
const ABORT_MS = () => (isMobile() ? 2800 : 5000);
const READY_MS = () => (isMobile() ? 900 : 2000);

const hideChecksIn = (ms) => {
  clearTimeout(hideTimer);
  hideTimer = setTimeout(() => (showChecks.value = false), ms);
};

// Checklist updates live: once everything turns green it closes itself.
watch(allReady, (ready) => {
  if (!showChecks.value) return;
  hideChecksIn(ready ? READY_MS() : ABORT_MS());
});

// Desktop: focus the first bad field.
// Mobile: only scroll it into view (focusing would pop the keyboard
// over the form and the card).
const focusField = (key) =>
  nextTick(() => {
    const el = [...document.querySelectorAll(`[data-field="${key}"]`)].find(
      (e) => e.offsetParent !== null,
    );
    if (!el) return;
    if (isMobile()) {
      el.scrollIntoView({ behavior: "smooth", block: "center" });
    } else {
      el.focus();
    }
  });

onBeforeUnmount(() => {
  clearTimeout(hideTimer);
  clearTimeout(shakeTimer);
});

/* ---------- SUBMIT ---------- */

const submitForm = async () => {
  // 1) Not ready: abort the launch, show the checklist, no rocket
  if (!allReady.value) {
    showChecks.value = true;
    hideChecksIn(ABORT_MS());

    validationError.value = true;
    clearTimeout(shakeTimer);
    shakeTimer = setTimeout(() => (validationError.value = false), 800);

    focusField(failed.value[0].key);
    return;
  }

  // 2) All systems go: launch
  showChecks.value = false;

  const payload = {
    name: form.value.name.trim(),
    email: form.value.email.trim(),
    subject: form.value.subject.trim(),
    message: form.value.message.trim(),
  };

  try {
    loading.value = true;

    await Promise.all([
      fetch(scriptURL, {
        method: "POST",
        mode: "no-cors",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
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

/* field flagged by the pre-launch check */
.input.input-error,
.input.input-error:focus {
  border-color: rgba(255, 93, 93, 0.75);
  box-shadow: 0 0 22px rgba(255, 93, 93, 0.16);
}

.input.shake {
  animation: fieldShake 0.5s cubic-bezier(0.36, 0.07, 0.19, 0.97);
}

@keyframes fieldShake {
  10%,
  90% {
    transform: translateX(-2px);
  }
  20%,
  80% {
    transform: translateX(4px);
  }
  30%,
  50%,
  70% {
    transform: translateX(-6px);
  }
  40%,
  60% {
    transform: translateX(6px);
  }
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

/* misfire: button shakes, rocket sputters, tilts and drops back */
.submit.abort {
  border-color: #ff5d5d;
  color: #ff8a8a;
  animation: fieldShake 0.5s cubic-bezier(0.36, 0.07, 0.19, 0.97);
}

.submit.abort .submit-rocket {
  animation: btnMisfire 0.8s ease-out;
}

@keyframes btnMisfire {
  0% {
    transform: translate(0, 0) rotate(0deg);
  }
  15% {
    transform: translate(3px, -3px);
  }
  25% {
    transform: translate(0, 0);
  }
  38% {
    transform: translate(4px, -5px);
  }
  55% {
    transform: translate(1px, 1px) rotate(0deg);
  }
  80% {
    transform: translate(-1px, 5px) rotate(35deg);
    opacity: 0.55;
  }
  100% {
    transform: translate(0, 0) rotate(0deg);
    opacity: 1;
  }
}

/* =====================================================
   PRE-LAUNCH CHECKLIST (HUD)
===================================================== */

.hud {
  position: fixed;
  left: 50%;
  bottom: max(24px, env(safe-area-inset-bottom));
  transform: translateX(-50%);
  z-index: 1000001;
  width: min(380px, calc(100vw - 24px));
  overflow: hidden;
  border-radius: 18px;
  background: rgba(12, 18, 28, 0.94);
  border: 1px solid rgba(255, 93, 93, 0.35);
  box-shadow:
    0 20px 50px rgba(0, 0, 0, 0.5),
    0 0 40px rgba(255, 93, 93, 0.1);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  color: #fff;
  cursor: pointer;
  transition:
    border-color 0.4s ease,
    box-shadow 0.4s ease;
}

.hud.ready {
  border-color: rgba(211, 245, 118, 0.45);
  box-shadow:
    0 20px 50px rgba(0, 0, 0, 0.5),
    0 0 40px rgba(211, 245, 118, 0.12);
}

/* moving hazard stripe */
.hud-stripe {
  height: 6px;
  background: repeating-linear-gradient(
    -45deg,
    #ff5d5d 0 10px,
    #1a1012 10px 20px
  );
  background-size: 28.28px 6px;
  animation: stripeMove 0.9s linear infinite;
}

.hud.ready .hud-stripe {
  background: repeating-linear-gradient(
    -45deg,
    #d3f576 0 10px,
    #10150a 10px 20px
  );
  background-size: 28.28px 6px;
}

@keyframes stripeMove {
  from {
    background-position-x: 0;
  }
  to {
    background-position-x: 28.28px;
  }
}

.hud-body {
  padding: 14px 18px 16px;
}

.hud-head {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 12px;
}

.hud-title {
  margin: 0;
  font-family: "Bebas Neue", sans-serif;
  font-size: 1.6rem;
  line-height: 1;
  letter-spacing: 0.06em;
  color: #ff6b6b;
}

.hud.ready .hud-title {
  color: #d3f576;
}

.hud-sub {
  margin: 2px 0 0;
  font-size: 0.82rem;
  color: rgba(255, 255, 255, 0.6);
}

/* little rocket in the header */
.hud-rocket {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 40px;
  flex-shrink: 0;
}

.hud-rocket-icon {
  color: #ff6b6b;
  transform: rotate(-45deg);
  animation: hudMisfire 2.2s ease-in-out infinite;
}

.hud.ready .hud-rocket-icon {
  color: #d3f576;
  animation: none;
  filter: drop-shadow(0 0 10px rgba(211, 245, 118, 0.6));
}

@keyframes hudMisfire {
  0%,
  100% {
    transform: rotate(-45deg) translate(0, 0);
  }
  10% {
    transform: rotate(-45deg) translate(0, -3px);
  }
  18% {
    transform: rotate(-45deg) translate(0, 0);
  }
  26% {
    transform: rotate(-45deg) translate(0, -4px);
  }
  55% {
    transform: rotate(-62deg) translate(0, 3px);
  }
  75% {
    transform: rotate(-52deg) translate(0, 1px);
  }
}

.hud-smoke {
  position: relative;
  width: 24px;
  height: 18px;
  margin-top: -2px;
}

.hud-smoke i {
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 8px;
  height: 8px;
  margin-left: -4px;
  border-radius: 50%;
  background: rgba(190, 200, 215, 0.55);
  animation: smokePuff 1.4s ease-out infinite;
}

.hud-smoke i:nth-child(2) {
  animation-delay: 0.45s;
}

.hud-smoke i:nth-child(3) {
  animation-delay: 0.9s;
}

@keyframes smokePuff {
  0% {
    transform: translate(0, 0) scale(0.5);
    opacity: 0.8;
  }
  100% {
    transform: translate(10px, 16px) scale(1.8);
    opacity: 0;
  }
}

.hud-flame {
  width: 8px;
  height: 14px;
  margin-top: -2px;
  background: linear-gradient(to bottom, #fff, #d3f576, rgba(211, 245, 118, 0));
  clip-path: polygon(0 0, 100% 0, 50% 100%);
  animation: flicker 0.12s ease-in-out infinite alternate;
  transform-origin: top center;
}

/* checklist rows */
.hud-list {
  margin: 0;
  padding: 0;
}

.hud-list li {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 7px 0;
  border-top: 1px dashed rgba(255, 255, 255, 0.1);
  font-size: 0.92rem;
}

.hud-list li .v-icon {
  color: #ff6b6b;
}

.hud-list li.ok .v-icon {
  color: #d3f576;
}

.hud-label {
  flex: 1;
}

.hud-hint {
  font-size: 0.78rem;
  letter-spacing: 0.04em;
  color: #ff8a8a;
}

.hud-list li.ok .hud-hint {
  color: rgba(211, 245, 118, 0.8);
}

/* readiness meter */
.hud-meter {
  display: flex;
  gap: 6px;
  margin-top: 12px;
}

.hud-meter span {
  flex: 1;
  height: 4px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.1);
  transition:
    background 0.4s ease,
    box-shadow 0.4s ease;
}

.hud-meter span.on {
  background: #d3f576;
  box-shadow: 0 0 10px rgba(211, 245, 118, 0.6);
}

/* slide-up entrance */
.hud-enter-active,
.hud-leave-active {
  transition:
    opacity 0.35s ease,
    transform 0.45s cubic-bezier(0.22, 1, 0.36, 1);
}

.hud-enter-from,
.hud-leave-to {
  opacity: 0;
  transform: translate(-50%, 30px) scale(0.96);
}

/* chips are mobile-only */
.hud-chips {
  display: none;
}

/* ---------- MOBILE: slim card at the top, never blocks the form ---------- */
@media (max-width: 959.98px) {
  .hud {
    /* sits just under the mobile navbar instead of covering the submit area */
    top: 78px;
    bottom: auto;
    width: calc(100vw - 24px);
    border-radius: 16px;
    pointer-events: none; /* taps go straight through to the form */
  }

  .hud-stripe {
    height: 4px;
  }

  .hud-body {
    padding: 10px 14px 12px;
  }

  .hud-head {
    gap: 10px;
    margin-bottom: 0;
  }

  .hud-title {
    font-size: 1.25rem;
  }

  .hud-sub {
    font-size: 0.76rem;
  }

  .hud-rocket {
    width: 30px;
  }

  .hud-rocket-icon {
    font-size: 26px !important;
  }

  .hud-smoke {
    height: 12px;
  }

  /* full list + meter are replaced by chips */
  .hud-list,
  .hud-meter {
    display: none;
  }

  .hud-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 8px;
  }

  .hud-chips span {
    padding: 3px 10px;
    border-radius: 999px;
    font-size: 0.74rem;
    font-weight: 600;
    color: #ff8a8a;
    background: rgba(255, 93, 93, 0.12);
    border: 1px solid rgba(255, 93, 93, 0.35);
  }

  /* slide down from the top instead of up from the bottom */
  .hud-enter-from,
  .hud-leave-to {
    transform: translate(-50%, -16px) scale(0.96);
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
/*.launch-rocket {
  position: absolute;
  left: 50%;
  bottom: 18vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  transform: translate(-50%, 0);
  animation: rocketLaunch 2.2s ease-in infinite;
}

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
*/

/* =====================================================
   REALISTIC ROCKET LAUNCH
===================================================== */

.launch-rocket {
  position: absolute;

  left: 50%;
  bottom: 16vh;

  width: 120px;
  height: 260px;

  display: flex;
  flex-direction: column;
  align-items: center;

  transform: translate(-50%, 0);

  animation: realisticLaunch 3.4s cubic-bezier(0.22, 0.8, 0.35, 1) forwards;

  filter: drop-shadow(0 0 25px rgba(211, 245, 118, 0.18));
}

/* =====================================================
   ROCKET GLOW
===================================================== */

.rocket-glow {
  position: absolute;

  top: 45px;

  width: 100px;
  height: 100px;

  border-radius: 50%;

  background: radial-gradient(
    circle,
    rgba(211, 245, 118, 0.22),
    rgba(255, 160, 50, 0.08) 35%,
    transparent 70%
  );

  filter: blur(12px);

  animation: rocketGlow 0.45s ease-in-out infinite alternate;
}

@keyframes rocketGlow {
  from {
    transform: scale(0.85);
    opacity: 0.55;
  }

  to {
    transform: scale(1.15);
    opacity: 1;
  }
}

/* =====================================================
   ROCKET BODY
===================================================== */

.rocket-body {
  position: relative;
  z-index: 5;

  display: flex;
  align-items: center;
  justify-content: center;

  width: 90px;
  height: 90px;

  border-radius: 50%;
}

.launch-rocket-icon {
  color: #e9f7ff;

  transform: rotate(-45deg);

  filter: drop-shadow(0 0 4px rgba(255, 255, 255, 0.8))
    drop-shadow(0 0 14px rgba(211, 245, 118, 0.45));

  animation: rocketVibration 0.08s linear infinite alternate;
}

@keyframes rocketVibration {
  from {
    transform: rotate(-45deg) translate(0, 0);
  }

  to {
    transform: rotate(-45deg) translate(1px, -1px);
  }
}

/* =====================================================
   ENGINE
===================================================== */

.rocket-engine {
  position: relative;

  width: 42px;
  height: 22px;

  margin-top: -7px;

  display: flex;
  justify-content: center;
}

/* hottest center */

.engine-core {
  position: absolute;

  top: 0;

  width: 8px;
  height: 25px;

  border-radius: 50%;

  background: linear-gradient(
    to bottom,
    #ffffff,
    #fff7a8 35%,
    #ffd23f 70%,
    transparent
  );

  filter: blur(1px);

  animation: coreFlame 0.08s ease-in-out infinite alternate;

  z-index: 5;
}

@keyframes coreFlame {
  from {
    height: 19px;
    opacity: 0.85;
  }

  to {
    height: 29px;
    opacity: 1;
  }
}

/* =====================================================
   FLAME LAYERS
===================================================== */

.engine-flame {
  position: absolute;

  top: 0;

  clip-path: polygon(
    20% 0,
    80% 0,
    100% 45%,
    65% 100%,
    50% 72%,
    35% 100%,
    0 45%
  );

  transform-origin: top center;

  animation: flameMovement 0.12s ease-in-out infinite alternate;
}

/* white/yellow hottest layer */

.flame-inner {
  width: 16px;
  height: 52px;

  background: linear-gradient(
    to bottom,
    #ffffff 0%,
    #fff8b0 28%,
    #ffd43b 65%,
    transparent 100%
  );

  filter: blur(1px);

  z-index: 4;
}

/* orange combustion layer */

.flame-middle {
  width: 29px;
  height: 75px;

  background: linear-gradient(
    to bottom,
    #fff2a1 0%,
    #ffb21c 25%,
    #ff6a00 65%,
    rgba(255, 72, 0, 0) 100%
  );

  filter: blur(1px);

  z-index: 3;
}

/* outer red/orange flame */

.flame-outer {
  width: 42px;
  height: 100px;

  background: linear-gradient(
    to bottom,
    rgba(255, 142, 35, 0.95),
    rgba(255, 69, 0, 0.65) 45%,
    rgba(255, 45, 0, 0) 100%
  );

  filter: blur(3px);

  z-index: 2;
}

@keyframes flameMovement {
  from {
    transform: scaleY(0.8) scaleX(0.9);
  }

  to {
    transform: scaleY(1.15) scaleX(1.08);
  }
}

/* =====================================================
   EXHAUST TRAIL
===================================================== */

.rocket-exhaust {
  position: absolute;

  top: 190px;

  width: 18px;
  height: 170px;

  background: linear-gradient(
    to bottom,
    rgba(255, 255, 255, 0.8),
    rgba(211, 245, 118, 0.4) 18%,
    rgba(211, 245, 118, 0.12) 45%,
    transparent 100%
  );

  filter: blur(4px);

  opacity: 0.65;

  animation: exhaustPulse 0.3s ease-in-out infinite alternate;
}

@keyframes exhaustPulse {
  from {
    transform: scaleX(0.75);
    opacity: 0.4;
  }

  to {
    transform: scaleX(1.3);
    opacity: 0.8;
  }
}

/* =====================================================
   EXHAUST PARTICLES
===================================================== */

.rocket-exhaust span {
  position: absolute;

  top: 30px;

  width: 4px;
  height: 4px;

  border-radius: 50%;

  background: #d3f576;

  box-shadow: 0 0 8px rgba(211, 245, 118, 0.8);

  animation: exhaustParticle 0.8s ease-out infinite;
}

.rocket-exhaust span:nth-child(1) {
  left: -8px;
}

.rocket-exhaust span:nth-child(2) {
  left: 8px;
  animation-delay: 0.2s;
}

.rocket-exhaust span:nth-child(3) {
  left: 20px;
  animation-delay: 0.4s;
}

@keyframes exhaustParticle {
  0% {
    transform: translateY(0) scale(1);
    opacity: 0.9;
  }

  100% {
    transform: translateY(100px) scale(0);
    opacity: 0;
  }
}

/* =====================================================
   SMOKE
===================================================== */

.rocket-smoke {
  position: absolute;

  bottom: -10px;

  width: 150px;
  height: 90px;

  pointer-events: none;
}

.rocket-smoke i {
  position: absolute;

  bottom: 0;

  width: 35px;
  height: 35px;

  border-radius: 50%;

  background: radial-gradient(
    circle,
    rgba(210, 220, 225, 0.32),
    rgba(120, 130, 140, 0.08),
    transparent 70%
  );

  filter: blur(5px);

  animation: smokeRise 1.6s ease-out infinite;
}

.rocket-smoke i:nth-child(1) {
  left: 15px;
}

.rocket-smoke i:nth-child(2) {
  left: 40px;
  animation-delay: 0.25s;
}

.rocket-smoke i:nth-child(3) {
  left: 65px;
  animation-delay: 0.45s;
}

.rocket-smoke i:nth-child(4) {
  left: 90px;
  animation-delay: 0.7s;
}

.rocket-smoke i:nth-child(5) {
  left: 115px;
  animation-delay: 0.9s;
}

@keyframes smokeRise {
  0% {
    transform: translateY(0) scale(0.5);
    opacity: 0.5;
  }

  60% {
    opacity: 0.25;
  }

  100% {
    transform: translateY(55px) scale(1.8);
    opacity: 0;
  }
}

/* =====================================================
   REALISTIC LAUNCH SEQUENCE
===================================================== */

@keyframes realisticLaunch {
  /* ignition */
  0% {
    transform: translate(-50%, 0);
    opacity: 0;
  }

  /* engine lights */
  8% {
    transform: translate(-50%, 0);
    opacity: 1;
  }

  /* vibration on launch pad */
  12% {
    transform: translate(calc(-50% - 3px), 0);
  }

  16% {
    transform: translate(calc(-50% + 3px), 0);
  }

  20% {
    transform: translate(calc(-50% - 2px), 0);
  }

  24% {
    transform: translate(-50%, 0);
  }

  /* slow initial lift */
  35% {
    transform: translate(-50%, -8vh);
  }

  /* acceleration */
  55% {
    transform: translate(-50%, -30vh);
  }

  72% {
    transform: translate(-50%, -65vh);
  }

  /* rapid ascent */
  88% {
    transform: translate(-50%, -105vh);
  }

  /* leave atmosphere */
  100% {
    transform: translate(-50%, -155vh);
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

/* reduced motion: keep things calm and static */
@media (prefers-reduced-motion: reduce) {
  .launch-rocket {
    animation: none;
    opacity: 1;
  }
  .launch-stars,
  .launch-trail,
  .hud-smoke {
    display: none;
  }
  .launch-flame,
  .hud-flame,
  .hud-stripe,
  .hud-rocket-icon,
  .submit.sending .submit-rocket,
  .submit.abort,
  .submit.abort .submit-rocket,
  .input.shake {
    animation: none;
  }
}
</style>
