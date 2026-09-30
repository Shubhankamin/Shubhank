<template>
  <div class="error-page">
    <!-- Background -->
    <div class="grid"></div>

    <!-- Corner system information -->
    <div class="corner-info top-left">
      <span>X: 404.00</span>
      <span>Y: 000.00</span>
    </div>

    <div class="corner-info top-right">SYS_ERR // 04</div>

    <div class="corner-info bottom-left">
      SHUBHANK.AMIN
      <small>SYSTEM://PORTFOLIO</small>
    </div>

    <div class="corner-info bottom-right">
      STATUS:
      <span>ONLINE</span>
    </div>

    <!-- Main -->
    <main class="error-container">
      <!-- Header -->
      <div class="error-header">
        <div class="header-label">
          <span class="status-dot"></span>
          NAVIGATION ERROR
        </div>

        <div class="header-code">ERROR / 404</div>
      </div>

      <!-- Main content -->
      <section class="error-main">
        <!-- LEFT -->
        <div class="error-visual">
          <div class="number-wrap">
            <span class="number-glow"></span>

            <h1 class="error-number">404</h1>

            <div class="scan-line"></div>
          </div>

          <div class="visual-caption">
            <span>ERR_CODE</span>
            <strong>ROUTE_NOT_FOUND</strong>
          </div>
        </div>

        <!-- RIGHT -->
        <div class="error-content">
          <h2>
            This route
            <span>doesn't exist.</span>
          </h2>

          <p class="description">
            The page you're looking for has either moved, disappeared, or was
            never deployed.
          </p>

          <!-- Requested path -->
          <div class="route-box">
            <div class="route-header">
              <span>REQUESTED_PATH</span>
              <span class="not-found">NOT FOUND</span>
            </div>

            <div class="route-value">
              <span>~/</span>
              <strong>{{ currentPath }}</strong>
            </div>
          </div>

          <!-- Actions -->
          <div class="actions">
            <button class="home-button" type="button" @click="goHome">
              <span>RETURN HOME</span>
              <span class="arrow">→</span>
            </button>

            <button class="back-button" type="button" @click="goBack">
              GO BACK
            </button>
          </div>

          <!-- Status -->
          <div class="status-row">
            <div>
              <span class="green-dot"></span>
              SYSTEM OPERATIONAL
            </div>

            <div>ERROR 404</div>

            <div>
              <span class="lime">●</span>
              CONNECTION LOST
            </div>
          </div>
        </div>
      </section>

      <!-- Bottom divider -->
      <div class="bottom-line">
        <span>PORTFOLIO://404</span>

        <div class="line"></div>

        <span>PAGE_NOT_FOUND</span>

        <div class="line"></div>

        <span>SHUBHANK.AMIN</span>
      </div>
    </main>
  </div>
</template>

<script setup>
const error = useError();

const currentPath = computed(() => {
  if (error.value?.url) {
    return error.value.url.replace(/^\/+/, "") || "home";
  }

  if (import.meta.client) {
    return window.location.pathname.replace(/^\/+/, "") || "home";
  }

  return "unknown-route";
});

const goHome = async () => {
  await clearError({
    redirect: "/",
  });
};

const goBack = () => {
  if (import.meta.client && window.history.length > 1) {
    window.history.back();
  } else {
    goHome();
  }
};
</script>

<style scoped>
/* =========================================================
   BASE
========================================================= */

.error-page {
  --bg: #070b13;
  --card: #0b1220;
  --accent: #d3f576;
  --green: #22c55e;
  --white: #ffffff;
  --muted: rgba(255, 255, 255, 0.55);
  --subtle: rgba(255, 255, 255, 0.3);
  --border: rgba(255, 255, 255, 0.1);

  position: relative;
  width: 100%;
  min-height: 100svh;

  overflow: hidden;

  background:
    radial-gradient(
      circle at 72% 48%,
      rgba(211, 245, 118, 0.055),
      transparent 28%
    ),
    var(--bg);

  color: var(--white);

  font-family: "Manrope", Arial, sans-serif;
}

/* =========================================================
   BACKGROUND GRID
========================================================= */

.grid {
  position: absolute;
  inset: 0;

  background-image:
    linear-gradient(rgba(211, 245, 118, 0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(211, 245, 118, 0.025) 1px, transparent 1px);

  background-size: 70px 70px;

  mask-image: linear-gradient(
    to bottom,
    transparent,
    black 15%,
    black 85%,
    transparent
  );

  pointer-events: none;
}

/* =========================================================
   CORNER INFORMATION
========================================================= */

.corner-info {
  position: absolute;
  z-index: 5;

  display: flex;
  flex-direction: column;

  font-size: 10px;
  line-height: 1.5;

  letter-spacing: 0.08em;

  color: rgba(255, 255, 255, 0.35);

  text-transform: uppercase;
}

.corner-info small {
  font-size: 9px;
  color: rgba(255, 255, 255, 0.22);
}

.corner-info span {
  color: var(--accent);
}

.top-left {
  top: 28px;
  left: 32px;
}

.top-right {
  top: 28px;
  right: 32px;

  color: var(--accent);
}

.bottom-left {
  left: 32px;
  bottom: 28px;
}

.bottom-right {
  right: 32px;
  bottom: 28px;
}

/* =========================================================
   MAIN CONTAINER
========================================================= */

.error-container {
  position: relative;
  z-index: 2;

  width: min(1250px, calc(100% - 120px));

  min-height: 100svh;

  margin: 0 auto;

  display: flex;
  flex-direction: column;

  justify-content: center;

  padding: 70px 0;
}

/* =========================================================
   HEADER
========================================================= */

.error-header {
  display: flex;

  align-items: center;
  justify-content: space-between;

  padding-bottom: 18px;

  border-bottom: 1px solid var(--border);
}

.header-label {
  display: flex;

  align-items: center;

  gap: 9px;

  font-size: 10px;
  font-weight: 800;

  letter-spacing: 0.14em;

  color: rgba(255, 255, 255, 0.6);
}

.status-dot {
  width: 7px;
  height: 7px;

  border-radius: 50%;

  background: var(--accent);

  box-shadow: 0 0 12px rgba(211, 245, 118, 0.5);
}

.header-code {
  font-size: 10px;

  letter-spacing: 0.12em;

  color: rgba(255, 255, 255, 0.25);
}

/* =========================================================
   MAIN GRID
========================================================= */

.error-main {
  display: grid;

  grid-template-columns: 1.05fr 0.95fr;

  align-items: center;

  gap: 110px;

  padding: 90px 0;
}

/* =========================================================
   LEFT 404
========================================================= */

.error-visual {
  min-width: 0;
}

.number-wrap {
  position: relative;

  overflow: hidden;

  padding: 25px 0;

  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}

.error-number {
  position: relative;
  z-index: 2;

  margin: 0;

  font-family: "Bebas Neue", "Arial Narrow", sans-serif;

  font-size: clamp(180px, 20vw, 320px);

  font-weight: 900;

  line-height: 0.75;

  letter-spacing: -0.07em;

  color: var(--accent);

  text-shadow: 0 0 60px rgba(211, 245, 118, 0.06);
}

.number-glow {
  position: absolute;

  width: 260px;
  height: 260px;

  left: 35%;
  top: 50%;

  transform: translate(-50%, -50%);

  border-radius: 50%;

  background: rgba(211, 245, 118, 0.08);

  filter: blur(80px);
}

/* scan */

.scan-line {
  position: absolute;

  left: 0;
  right: 0;

  top: 45%;

  height: 1px;

  background: var(--accent);

  opacity: 0.45;

  animation: scan 4s ease-in-out infinite;
}

@keyframes scan {
  0% {
    transform: translateY(-100px);
  }

  50% {
    transform: translateY(100px);
  }

  100% {
    transform: translateY(-100px);
  }
}

/* caption */

.visual-caption {
  display: flex;

  align-items: center;

  gap: 12px;

  margin-top: 18px;

  font-size: 10px;

  letter-spacing: 0.1em;
}

.visual-caption span {
  color: rgba(255, 255, 255, 0.3);
}

.visual-caption strong {
  color: var(--accent);
}

/* =========================================================
   RIGHT CONTENT
========================================================= */

.error-content {
  width: 100%;

  max-width: 500px;
}

.error-content h2 {
  margin: 0;

  font-size: clamp(45px, 4.5vw, 70px);

  font-weight: 800;

  line-height: 0.95;

  letter-spacing: -0.045em;
}

.error-content h2 span {
  display: block;

  color: var(--accent);
}

.description {
  max-width: 460px;

  margin: 25px 0 30px;

  color: var(--muted);

  font-size: 14px;

  line-height: 1.75;
}

/* =========================================================
   ROUTE
========================================================= */

.route-box {
  width: 100%;

  padding: 16px;

  border: 1px solid var(--border);

  border-radius: 14px;

  background: rgba(255, 255, 255, 0.025);
}

.route-header {
  display: flex;

  justify-content: space-between;

  margin-bottom: 10px;

  font-size: 9px;
  font-weight: 800;

  letter-spacing: 0.1em;
}

.route-header span:first-child {
  color: rgba(255, 255, 255, 0.35);
}

.not-found {
  color: #ef4444;
}

.route-value {
  display: flex;

  align-items: center;

  min-width: 0;

  padding: 11px 13px;

  border-radius: 8px;

  background: rgba(0, 0, 0, 0.25);

  font-family: monospace;

  font-size: 12px;
}

.route-value span {
  color: var(--accent);

  flex-shrink: 0;
}

.route-value strong {
  overflow: hidden;

  text-overflow: ellipsis;

  white-space: nowrap;

  font-weight: 500;

  color: rgba(255, 255, 255, 0.7);
}

/* =========================================================
   BUTTONS
========================================================= */

.actions {
  display: flex;

  align-items: center;

  gap: 12px;

  margin-top: 22px;
}

.home-button {
  height: 48px;

  padding: 0 22px;

  display: inline-flex;

  align-items: center;

  justify-content: center;

  gap: 14px;

  border: none;

  border-radius: 30px;

  background: var(--accent);

  color: #070b13;

  font-size: 10px;
  font-weight: 900;

  letter-spacing: 0.08em;

  cursor: pointer;

  transition:
    transform 0.25s ease,
    box-shadow 0.25s ease;
}

.home-button:hover {
  transform: translateY(-2px);

  box-shadow: 0 8px 25px rgba(211, 245, 118, 0.15);
}

.arrow {
  font-size: 17px;
}

.back-button {
  height: 48px;

  padding: 0 20px;

  border: 1px solid var(--border);

  border-radius: 30px;

  background: transparent;

  color: rgba(255, 255, 255, 0.55);

  font-size: 10px;
  font-weight: 800;

  letter-spacing: 0.08em;

  cursor: pointer;

  transition: 0.25s ease;
}

.back-button:hover {
  border-color: rgba(211, 245, 118, 0.4);

  color: var(--accent);
}

/* =========================================================
   STATUS
========================================================= */

.status-row {
  display: grid;

  grid-template-columns: 1.4fr 0.7fr 1.2fr;

  gap: 15px;

  margin-top: 40px;

  padding-top: 15px;

  border-top: 1px solid var(--border);

  font-size: 9px;

  letter-spacing: 0.08em;

  color: rgba(255, 255, 255, 0.3);
}

.status-row div:nth-child(2) {
  text-align: center;
}

.status-row div:last-child {
  text-align: right;
}

.green-dot {
  display: inline-block;

  width: 5px;
  height: 5px;

  margin-right: 6px;

  border-radius: 50%;

  background: var(--green);
}

.lime {
  color: var(--accent);
}

/* =========================================================
   BOTTOM
========================================================= */

.bottom-line {
  display: grid;

  grid-template-columns: auto 1fr auto 1fr auto;

  align-items: center;

  gap: 15px;

  padding-top: 18px;

  border-top: 1px solid var(--border);

  font-size: 8px;

  letter-spacing: 0.12em;

  color: rgba(255, 255, 255, 0.2);
}

.line {
  height: 1px;

  background: rgba(255, 255, 255, 0.08);
}

/* =========================================================
   TABLET
========================================================= */

@media (max-width: 1000px) {
  .error-container {
    width: min(760px, calc(100% - 60px));
  }

  .error-main {
    grid-template-columns: 1fr;

    gap: 55px;

    padding: 65px 0;
  }

  .error-content {
    max-width: 600px;
  }

  .error-number {
    font-size: clamp(150px, 27vw, 250px);
  }
}

/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 600px) {
  .error-container {
    width: calc(100% - 36px);

    padding: 75px 0 55px;
  }

  .corner-info {
    font-size: 8px;
  }

  .top-left {
    top: 18px;
    left: 18px;
  }

  .top-right {
    top: 18px;
    right: 18px;
  }

  .bottom-left {
    left: 18px;
    bottom: 18px;
  }

  .bottom-right {
    right: 18px;
    bottom: 18px;
  }

  .error-header {
    padding-bottom: 14px;
  }

  .error-main {
    padding: 50px 0;
    gap: 45px;
  }

  .error-number {
    font-size: 42vw;
  }

  .error-content h2 {
    font-size: 46px;
  }

  .description {
    font-size: 13px;
  }

  .actions {
    flex-direction: column;

    align-items: stretch;
  }

  .home-button,
  .back-button {
    width: 100%;
  }

  .status-row {
    grid-template-columns: 1fr;

    gap: 9px;
  }

  .status-row div,
  .status-row div:nth-child(2),
  .status-row div:last-child {
    text-align: left;
  }

  .bottom-line {
    display: none;
  }
}
</style>
