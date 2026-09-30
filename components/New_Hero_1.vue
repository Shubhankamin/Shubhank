```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, viewport-fit=cover"
    />

    <title>Hero — Helmet Interaction</title>

    <script type="importmap">
      {
        "imports": {
          "three": "https://cdn.jsdelivr.net/npm/three@0.185.0/build/three.module.js",
          "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.185.0/examples/jsm/"
        }
      }
    </script>

    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

    <link
      href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;700&family=Space+Grotesk:wght@400;500;700&display=swap"
      rel="stylesheet"
    />

    <style>
      :root {
        --bg: #f7fafb;
        --fg: #090a0b;
        --dark: #0e0f14;
        --accent: #02d2e3;

        --sans: "Space Grotesk", system-ui, sans-serif;
        --display: "Oswald", Impact, sans-serif;

        --ease: cubic-bezier(0.2, 0, 0, 1);
      }

      * {
        box-sizing: border-box;
      }

      html,
      body {
        width: 100%;
        min-height: 100%;
      }

      body {
        margin: 0;
        background: var(--bg);
        color: var(--fg);
        font-family: var(--sans);
        min-height: 100lvh;
      }

      a {
        color: inherit;
        text-decoration: none;
      }

      /* =========================
       HERO
    ========================= */

      .hero {
        position: relative;
        min-height: 100lvh;
        overflow: hidden;
        isolation: isolate;
        background: var(--bg);
      }

      .hero-canvas {
        position: absolute;
        inset: 0;
        z-index: 0;
        pointer-events: none;
      }

      .hero-canvas canvas {
        display: block;
        width: 100%;
        height: 100%;
      }

      .hero-content {
        position: relative;
        z-index: 20;

        min-height: 100lvh;

        display: flex;
        flex-direction: column;

        padding: 24px;

        pointer-events: none;
      }

      .hero-content a {
        pointer-events: auto;
      }

      /* =========================
       HEADER
    ========================= */

      header {
        position: relative;

        display: flex;
        align-items: center;
        justify-content: space-between;
      }

      .brand {
        font: 700 22px var(--display);
        letter-spacing: 0.04em;
        text-transform: uppercase;
      }

      .nav {
        position: absolute;
        left: 50%;
        top: 50%;

        transform: translate(-50%, -50%);

        display: flex;
        gap: 56px;

        font-size: 16px;
        text-transform: uppercase;
      }

      .nav a,
      .garage {
        transition: color 0.15s var(--ease);
      }

      .nav a:hover,
      .garage:hover {
        color: var(--accent);
      }

      .garage {
        font-weight: 700;
        text-transform: uppercase;
      }

      /* =========================
       MAIN CONTENT
    ========================= */

      .middle {
        flex: 1;

        display: flex;
        align-items: center;
        justify-content: space-between;

        position: relative;
      }

      .identity-id {
        font-size: 16px;
        color: rgb(9 10 11 / 35%);
        text-transform: uppercase;
        margin-bottom: 9px;
      }

      .identity h1 {
        margin: 0;

        font: 700 96px/0.95 var(--display);
        letter-spacing: -0.025em;

        max-width: 6em;

        text-transform: uppercase;
      }

      .meta {
        list-style: none;

        padding: 0;
        margin: 22px 0 0;

        display: grid;
        gap: 16px;

        font-size: 18px;
        text-transform: uppercase;
      }

      /* =========================
       INFO PANELS
    ========================= */

      .panels {
        width: 218px;

        display: grid;
        gap: 32px;
      }

      .bracket {
        position: relative;
        padding: 16px;
      }

      .bracket::before,
      .bracket::after,
      .bracket i,
      .bracket b {
        content: "";

        position: absolute;

        width: 10px;
        height: 10px;

        border: 0 solid currentColor;
      }

      .bracket::before {
        left: 0;
        top: 0;

        border-left-width: 1px;
        border-top-width: 1px;
      }

      .bracket::after {
        right: 0;
        bottom: 0;

        border-right-width: 1px;
        border-bottom-width: 1px;
      }

      .bracket i {
        right: 0;
        top: 0;

        border-right-width: 1px;
        border-top-width: 1px;
      }

      .bracket b {
        left: 0;
        bottom: 0;

        border-left-width: 1px;
        border-bottom-width: 1px;
      }

      .eyebrow {
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: -0.02em;
      }

      .bracket dl {
        margin: 16px 0 0;

        display: grid;
        gap: 6px;

        font-size: 14px;
        line-height: 0.9;

        text-transform: uppercase;
      }

      .bracket dt {
        font-weight: 700;
      }

      .bracket dd {
        margin: 0;
      }

      .stats {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;

        text-align: center;
      }

      .stats dt {
        font-size: 12px;
        letter-spacing: -0.04em;
      }

      .stats dd {
        margin-top: 12px;

        font: 400 38px/0.72 var(--display);
        letter-spacing: -0.08em;
      }

      /* =========================
       CTA
    ========================= */

      .actions {
        display: flex;
        align-items: flex-end;
        justify-content: center;

        margin-top: 8px;
      }

      .cta {
        position: relative;

        width: 220px;
        height: 50px;

        display: flex;
        align-items: center;
        justify-content: center;

        gap: 1.4em;

        font-size: 20px;
        text-transform: uppercase;

        color: var(--accent);
        background: var(--dark);

        overflow: hidden;

        clip-path: polygon(0 0, 100% 0, 100% 84%, 96.5% 100%, 0 100%);
      }

      .cta::before {
        content: "";

        position: absolute;
        inset: 0;

        background: var(--accent);

        transform: scaleX(0);
        transform-origin: left;

        transition: transform 0.25s var(--ease);
      }

      .cta:hover::before {
        transform: scaleX(1);
      }

      .cta:hover {
        color: var(--fg);
      }

      .cta span {
        position: relative;
        z-index: 1;
      }

      /* =========================
       BOTTOM EFFECTS
    ========================= */

      .ramp {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;

        height: 22%;

        z-index: 11;

        pointer-events: none;

        background: linear-gradient(
          to bottom,
          transparent,
          rgba(247, 250, 251, 0.2) 46%,
          rgba(247, 250, 251, 0.74) 80%,
          var(--bg)
        );
      }

      .hint {
        position: absolute;

        left: 50%;
        bottom: 28px;

        transform: translateX(-50%);

        z-index: 25;

        margin: 0;

        font-size: 12px;
        letter-spacing: 0.14em;

        text-transform: uppercase;

        color: rgb(9 10 11 / 45%);

        pointer-events: none;

        transition: opacity 0.25s ease;
      }

      /* =========================
       REVEAL
    ========================= */

      .reveal {
        opacity: 0;

        transform: translateY(20px);

        transition:
          opacity 0.7s var(--ease),
          transform 0.7s var(--ease);
      }

      .reveal.on {
        opacity: 1;
        transform: none;
      }

      /* =========================
       ERROR MESSAGE
    ========================= */

      .note {
        position: fixed;

        left: 16px;
        right: 16px;
        bottom: 16px;

        z-index: 200;

        background: #ff6b00;

        padding: 12px 16px;

        font: 700 12px var(--sans);

        text-transform: uppercase;

        display: none;
      }

      /* =========================
       TABLET
    ========================= */

      @media (max-width: 1279px) {
        .nav,
        .garage {
          display: none;
        }

        .middle {
          align-items: flex-end;
          padding-bottom: 80px;
        }

        .identity h1 {
          font-size: 70px;
        }

        .panels {
          display: none;
        }
      }

      /* =========================
       MOBILE
    ========================= */

      @media (max-width: 767px) {
        .hero-content {
          padding: 18px;
        }

        .middle {
          display: block;

          padding-top: 18vh;
          padding-bottom: 80px;
        }

        .identity h1 {
          font-size: 52px;
        }

        .meta {
          font-size: 16px;
          gap: 10px;
        }

        .cta {
          width: 100%;
        }

        .hint {
          bottom: 20px;
        }
      }

      /* =========================
       REDUCED MOTION
    ========================= */

      @media (prefers-reduced-motion: reduce) {
        .reveal {
          transition: none;
        }
      }
    </style>
  </head>

  <body>
    <div class="note" id="note"></div>

    <section class="hero" aria-labelledby="hero-title">
      <!-- THREE.JS CANVAS -->
      <div class="hero-canvas" id="heroCanvas"></div>

      <!-- CONTENT -->
      <div class="hero-content">
        <header>
          <a class="brand" href="#"> Your Name </a>

          <nav class="nav" aria-label="Primary">
            <a href="#">Work</a>
            <a href="#">About</a>
            <a href="#">Journal</a>
            <a href="#">Contact</a>
          </nav>

          <a class="garage" href="#"> [ Resume → ] </a>
        </header>

        <div class="middle">
          <div class="identity reveal">
            <div class="identity-id">dev_001</div>

            <h1 id="hero-title">Shubhank Amin</h1>

            <ul class="meta">
              <li>India</li>
              <li>Front-End Developer</li>
              <li>MCA · MIT Manipal</li>
            </ul>
          </div>

          <div class="panels reveal">
            <div class="bracket">
              <i></i>
              <b></b>

              <div
                class="eyebrow"
                style="color: var(--accent); font-weight: 500"
              >
                Currently
              </div>

              <dl>
                <dt>Nuxt 3 · Vue 3</dt>
                <dd>Production web apps</dd>
              </dl>
            </div>

            <div class="bracket">
              <i></i>
              <b></b>

              <div class="eyebrow">Stats</div>

              <dl class="stats" style="margin-top: 16px">
                <div>
                  <dt>Projects</dt>
                  <dd>12</dd>
                </div>

                <div>
                  <dt>Stacks</dt>
                  <dd>6</dd>
                </div>

                <div>
                  <dt>Years</dt>
                  <dd>2</dd>
                </div>
              </dl>
            </div>
          </div>
        </div>

        <div class="actions reveal">
          <a class="cta" href="#">
            <span>View work</span>
            <span>→</span>
          </a>
        </div>
      </div>

      <div class="ramp"></div>

      <p class="hint" id="hint">Hover to reveal</p>
    </section>

    <script type="module">
      import * as THREE from "three";

      import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

      import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";

      import { RGBELoader } from "three/addons/loaders/RGBELoader.js";

      /* =========================================
       ASSETS
    ========================================= */

      const ASSETS = {
        base: "https://storage.getlayers.ai/assets/kimi-04a9449ab2/hero/scene",

        diffuse: "/person-diffuse.webp",

        alpha: "/person-alpha.webp",

        helmet: "/helmet3.glb",

        env: "/studio-light.hdr",
      };

      /* =========================================
       INTERACTION
    ========================================= */

      const FOLLOW = 0.17;

      const ROT_Y = 0.035;
      const ROT_X = 0.043;

      const MOVE_X = 0.08;
      const MOVE_Y = 0.06;

      /* =========================================
       HELMET SETTINGS
    ========================================= */

      const HELMET = {
        scale: 2.15,

        startScale: 0.6,

        restY: -1.6,

        shownY: -0.65,

        spin: 1.6,

        speed: 0.075,

        lookX: 0.55,

        lookY: 0.3,
      };

      /* =========================================
       DOM
    ========================================= */

      const host = document.getElementById("heroCanvas");

      const note = document.getElementById("note");

      const heroEl = document.querySelector(".hero");

      const hint = document.getElementById("hint");

      /* =========================================
       TEXT REVEAL
    ========================================= */

      const reveal = () => {
        document.querySelectorAll(".reveal").forEach((el, i) => {
          setTimeout(() => el.classList.add("on"), 150 + i * 160);
        });
      };

      /* =========================================
       THREE.JS
    ========================================= */

      try {
        const isTouch = matchMedia("(hover:none) and (pointer:coarse)").matches;

        /* -----------------------------------------
         RENDERER
      ----------------------------------------- */

        const renderer = new THREE.WebGLRenderer({
          antialias: !isTouch,

          alpha: true,

          powerPreference: "high-performance",
        });

        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));

        renderer.setSize(window.innerWidth, window.innerHeight);

        renderer.outputColorSpace = THREE.SRGBColorSpace;

        renderer.toneMapping = THREE.ACESFilmicToneMapping;

        renderer.toneMappingExposure = 1;

        host.appendChild(renderer.domElement);

        /* -----------------------------------------
         SCENE
      ----------------------------------------- */

        const scene = new THREE.Scene();

        /* -----------------------------------------
         CAMERA
      ----------------------------------------- */

        const camera = new THREE.PerspectiveCamera(
          26,
          window.innerWidth / window.innerHeight,
          0.1,
          50,
        );

        camera.position.set(0, 0, 10);

        /* -----------------------------------------
         LIGHTING
      ----------------------------------------- */

        const hemisphere = new THREE.HemisphereLight(0xffffff, 0x222222, 2);

        scene.add(hemisphere);

        const key = new THREE.DirectionalLight(0xffffff, 3);

        key.position.set(2, 3, 5);

        scene.add(key);

        /* -----------------------------------------
         MAIN GROUP
      ----------------------------------------- */

        const group = new THREE.Group();

        scene.add(group);

        /* =========================================
         LOAD PORTRAIT
      ========================================= */

        const textureLoader = new THREE.TextureLoader();

        const [diffuse, alpha] = await Promise.all([
          textureLoader.loadAsync(ASSETS.base + ASSETS.diffuse),

          textureLoader.loadAsync(ASSETS.base + ASSETS.alpha),
        ]);

        diffuse.colorSpace = THREE.SRGBColorSpace;

        alpha.colorSpace = THREE.NoColorSpace;

        const portraitGeometry = new THREE.PlaneGeometry(7.4, 7.4);

        const portraitMaterial = new THREE.MeshBasicMaterial({
          map: diffuse,

          alphaMap: alpha,

          transparent: true,

          depthWrite: false,

          side: THREE.DoubleSide,
        });

        const portrait = new THREE.Mesh(portraitGeometry, portraitMaterial);

        portrait.position.set(0, -0.15, -0.15);

        group.add(portrait);

        /* =========================================
         LOAD HELMET
      ========================================= */

        const draco = new DRACOLoader();

        draco.setDecoderPath(
          "https://cdn.jsdelivr.net/npm/three@0.185.0/examples/jsm/libs/draco/gltf/",
        );

        const gltfLoader = new GLTFLoader();

        gltfLoader.setDRACOLoader(draco);

        const gltf = await gltfLoader.loadAsync(ASSETS.base + ASSETS.helmet);

        const helmet = gltf.scene;

        helmet.position.set(0, HELMET.restY, 0.35);

        helmet.scale.setScalar(HELMET.scale * HELMET.startScale);

        helmet.visible = false;

        group.add(helmet);

        /* =========================================
         HELMET MATERIALS
      ========================================= */

        const materials = [];

        helmet.traverse((object) => {
          if (!object.isMesh) {
            return;
          }

          const original = Array.isArray(object.material)
            ? object.material
            : [object.material];

          const cloned = original.map((material) => {
            const clone = material.clone();

            clone.transparent = true;

            clone.opacity = 0;

            return clone;
          });

          object.material = Array.isArray(object.material) ? cloned : cloned[0];

          materials.push(...cloned);
        });

        /* =========================================
         MODEL ANIMATION
      ========================================= */

        const mixer = gltf.animations.length
          ? new THREE.AnimationMixer(helmet)
          : null;

        if (mixer) {
          gltf.animations.forEach((animation) => {
            mixer.clipAction(animation).play();
          });
        }

        /* =========================================
         HDR ENVIRONMENT
      ========================================= */

        const hdr = await new RGBELoader().loadAsync(ASSETS.base + ASSETS.env);

        hdr.mapping = THREE.EquirectangularReflectionMapping;

        scene.environment = hdr;

        /* =========================================
         POINTER
      ========================================= */

        let px = 0;
        let py = 0;

        let sx = 0;
        let sy = 0;

        window.addEventListener(
          "pointermove",
          (event) => {
            px = (event.clientX / window.innerWidth) * 2 - 1;

            py = (event.clientY / window.innerHeight) * 2 - 1;
          },
          { passive: true },
        );

        /* =========================================
         RESIZE
      ========================================= */

        window.addEventListener("resize", () => {
          const width = window.innerWidth;

          const height = window.innerHeight;

          camera.aspect = width / height;

          camera.updateProjectionMatrix();

          renderer.setSize(width, height);

          renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
        });

        /* =========================================
         HELMET REVEAL
      ========================================= */

        let target = 0;

        let progress = 0;

        const coarse = matchMedia("(hover:none)").matches;

        if (!coarse) {
          heroEl.addEventListener("pointerenter", () => {
            target = 1;
          });

          heroEl.addEventListener("pointerleave", () => {
            target = 0;
          });
        } else {
          hint.textContent = "Tap to reveal";

          heroEl.addEventListener("click", (event) => {
            if (event.target.closest("a")) {
              return;
            }

            target = target === 1 ? 0 : 1;
          });
        }

        /* =========================================
         REDUCED MOTION
      ========================================= */

        const reducedMotion = matchMedia(
          "(prefers-reduced-motion: reduce)",
        ).matches;

        const revealSpeed = reducedMotion ? 0.25 : HELMET.speed;

        /* =========================================
         ANIMATION
      ========================================= */

        const clock = new THREE.Clock();

        const ease = (value) => 1 - Math.pow(1 - value, 3);

        renderer.setAnimationLoop(() => {
          const dt = clock.getDelta();

          /* ---------------------------------------
             SMOOTH POINTER
          --------------------------------------- */

          sx += (px - sx) * FOLLOW;

          sy += (py - sy) * FOLLOW;

          /* ---------------------------------------
             GROUP PARALLAX
          --------------------------------------- */

          group.rotation.y = sx * ROT_Y;

          group.rotation.x = -sy * ROT_X;

          group.position.x = sx * MOVE_X;

          group.position.y = -sy * MOVE_Y;

          /* ---------------------------------------
             HELMET REVEAL
          --------------------------------------- */

          progress += (target - progress) * revealSpeed;

          if (Math.abs(target - progress) < 0.001) {
            progress = target;
          }

          const eased = ease(progress);

          helmet.visible = progress > 0.002;

          /* ---------------------------------------
             POSITION
          --------------------------------------- */

          helmet.position.y =
            HELMET.restY + (HELMET.shownY - HELMET.restY) * eased;

          /* ---------------------------------------
             SCALE
          --------------------------------------- */

          helmet.scale.setScalar(
            HELMET.scale *
              (HELMET.startScale + (1 - HELMET.startScale) * eased),
          );

          /* ---------------------------------------
             ROTATION
          --------------------------------------- */

          helmet.rotation.y =
            (1 - eased) * -HELMET.spin + sx * HELMET.lookX * eased;

          helmet.rotation.x = sy * HELMET.lookY * eased;

          /* ---------------------------------------
             MATERIAL FADE
          --------------------------------------- */

          materials.forEach((material) => {
            material.opacity = eased;
          });

          /* ---------------------------------------
             HINT
          --------------------------------------- */

          hint.style.opacity = String(1 - eased);

          /* ---------------------------------------
             MODEL ANIMATION
          --------------------------------------- */

          if (mixer && helmet.visible) {
            mixer.update(dt);
          }

          /* ---------------------------------------
             RENDER
          --------------------------------------- */

          renderer.render(scene, camera);
        });
      } catch (error) {
        console.error("3D scene error:", error);

        host.style.display = "none";

        note.textContent =
          "3D scene failed to load: " + (error?.message || error);

        note.style.display = "block";
      }

      /* =========================================
       START UI REVEAL
    ========================================= */

      reveal();
    </script>
  </body>
</html>
```
