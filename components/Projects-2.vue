<template>
  <section class="projects-section">
    <v-container fluid class="projects-container">
      <!-- HEADER -->
      <div class="projects-header" data-aos="fade-up" data-aos-duration="1200">
        <div class="header-left">
          <span class="section-label"> 02 / SELECTED WORK </span>

          <h2 class="projects-heading bebas-Bold-h1">
            SELECTED
            <span>PROJECTS.</span>
          </h2>
        </div>

        <div class="header-right">
          <p class="manrope-regular-h5">
            A collection of digital products, experiments and applications I've
            designed and engineered.
          </p>

          <div class="project-count">
            <span>PROJECTS</span>

            <strong>
              {{ String(projects.length).padStart(2, "0") }}
            </strong>
          </div>
        </div>
      </div>

      <!-- PROJECT GRID -->
      <div class="projects-grid">
        <article
          v-for="(item, index) in projects"
          :key="item.title"
          class="project-card"
          :class="getCardClass(index)"
          data-aos="fade-up"
          :data-aos-delay="index * 100"
          data-aos-duration="1000"
        >
          <!-- IMAGE -->
          <v-img
            :src="item.src"
            :alt="item.title"
            cover
            class="project-image"
          />

          <!-- OVERLAY -->
          <div class="card-overlay"></div>

          <!-- TOP INFORMATION -->
          <div class="card-top">
            <span class="project-index">
              {{ String(index + 1).padStart(2, "0") }}
            </span>

            <span class="project-year">
              {{ item.year }}
            </span>
          </div>

          <!-- CONTENT -->
          <div class="card-content">
            <div class="card-meta">
              <span>{{ item.role }}</span>
            </div>

            <h3 class="project-title">
              {{ item.title }}
            </h3>

            <p class="project-description">
              {{ item.shortDescription }}
            </p>

            <!-- TECH STACK -->
            <div class="tech-stack">
              <span v-for="tech in item.tech" :key="tech" class="tech-tag">
                {{ tech }}
              </span>
            </div>

            <!-- ACTION -->
            <div class="project-action">
              <!-- LIVE DEMO -->
              <a
                v-if="item.liveDemo"
                :href="item.liveDemo"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link"
              >
                <span>VIEW PROJECT</span>

                <span class="arrow-circle">
                  <v-icon size="18"> mdi-arrow-top-right </v-icon>
                </span>
              </a>

              <!-- GITHUB ONLY -->
              <a
                v-else-if="item.github"
                :href="item.github"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link"
              >
                <span>VIEW ON GITHUB</span>

                <span class="arrow-circle">
                  <v-icon size="18"> mdi-arrow-top-right </v-icon>
                </span>
              </a>
            </div>
          </div>
        </article>
      </div>

      <!-- FOOTER -->
      <div class="projects-footer">
        <div class="footer-left">
          <span class="footer-dot"></span>
          MORE PROJECTS COMING
        </div>

        <div class="footer-line"></div>

        <span> SHUBHANK.AMIN / 2025 </span>
      </div>

      <v-divider :thickness="3" class="border-opacity-50 mt-10" color="white" />
    </v-container>
  </section>
</template>

<script setup>
const projects = [
  {
    src: "/images/project-1.png",
    title: "Phoenix Academy Website",
    shortDescription:
      "Full-stack education platform with client and admin experiences.",
    year: "2025",
    role: "FULL-STACK",
    tech: ["Nuxt 3", "Vue 3", "Supabase"],
    liveDemo: "https://pheonixacademy.in/",
    github: "https://github.com/Shubhankamin/Pheonix",
  },

  {
    src: "/images/project-2.png",
    title: "Interactive Birthday Experience",
    shortDescription:
      "Immersive interactive experience built around animation and visual storytelling.",
    year: "2025",
    role: "FRONT-END",
    tech: ["Nuxt 3", "Vue 3", "Vuetify"],
    liveDemo: "https://mymadamji.netlify.app/",
    github: "https://github.com/Shubhankamin/Madam-Ji",
  },

  {
    src: "/images/project-3.jpg",
    title: "AgriMart E-commerce",
    shortDescription:
      "Role-based eCommerce platform connecting farmers and customers.",
    year: "2025",
    role: "FRONT-END",
    tech: ["HTML", "CSS", "JavaScript"],
    liveDemo: "https://agrimaart.netlify.app",
    github: "https://github.com/Shubhankamin/Agri_Mart",
  },

  {
    src: "/images/project-4.jpg",
    title: "Lost & Found Portal",
    shortDescription:
      "College platform for reporting, managing and claiming lost items.",
    year: "2025",
    role: "FULL-STACK",
    tech: ["Vue 3", "Nuxt 3", "Firebase"],
    liveDemo: "https://lostorfound.netlify.app",
    github: "https://github.com/Shubhankamin/Find",
  },

  {
    src: "/images/project-5.jpg",
    title: "Lost & Found Admin",
    shortDescription:
      "Administrative dashboard for managing listings, users and verification.",
    year: "2025",
    role: "FULL-STACK",
    tech: ["Vue 3", "Nuxt 3", "Firebase"],
    github: "https://github.com/Shubhankamin/Find-Admin",
  },
];

const getCardClass = (index) => {
  const classes = [
    "card-large",
    "card-medium",
    "card-medium",
    "card-large",
    "card-full",
  ];

  return classes[index] || "card-medium";
};
</script>

<style scoped>
/* =========================================================
   SECTION
========================================================= */

.projects-section {
  position: relative;
  width: 100%;
  overflow: hidden;
  background: transparent;
}

.projects-container {
  padding-top: 90px;
  padding-bottom: 50px;
}

/* =========================================================
   HEADER
========================================================= */

.projects-header {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  align-items: end;
  gap: 80px;

  padding: 0 7% 65px;
}

.section-label {
  display: block;
  margin-bottom: 14px;

  color: #d3f576;

  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.projects-heading {
  margin: 0;

  color: #ffffff;

  font-size: clamp(60px, 7vw, 105px);
  line-height: 0.82;
  letter-spacing: -0.04em;

  text-transform: uppercase;
}

.projects-heading span {
  display: block;
  color: #d3f576;
}

.header-right {
  max-width: 470px;
  justify-self: end;
}

.header-right p {
  margin: 0;

  color: rgba(255, 255, 255, 0.58);

  line-height: 1.8;
}

.project-count {
  display: flex;
  align-items: center;
  gap: 12px;

  margin-top: 25px;
  padding-top: 15px;

  border-top: 1px solid rgba(255, 255, 255, 0.1);

  font-size: 9px;
  letter-spacing: 0.1em;
}

.project-count span {
  color: rgba(255, 255, 255, 0.3);
}

.project-count strong {
  color: #d3f576;
  font-size: 14px;
}

/* =========================================================
   GRID
========================================================= */

.projects-grid {
  display: grid;

  grid-template-columns: 1.3fr 0.9fr;

  grid-auto-rows: 430px;

  gap: 22px;

  padding: 0 7%;
}

/* =========================================================
   CARD
========================================================= */

.project-card {
  position: relative;

  overflow: hidden;

  border-radius: 28px;

  background: #0b1220;

  border: 1px solid rgba(255, 255, 255, 0.1);

  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35);

  cursor: pointer;

  isolation: isolate;

  transition:
    transform 0.5s cubic-bezier(0.2, 0, 0, 1),
    border-color 0.4s ease,
    box-shadow 0.5s ease;
}

.project-card:hover {
  transform: translateY(-8px);

  border-color: rgba(211, 245, 118, 0.3);

  box-shadow:
    0 30px 70px rgba(0, 0, 0, 0.5),
    0 0 50px rgba(211, 245, 118, 0.06);
}

/* =========================================================
   CARD SIZES
========================================================= */

.card-large {
  grid-column: span 1;
}

.card-medium {
  grid-column: span 1;
}

.card-full {
  grid-column: 1 / -1;
}

/* =========================================================
   IMAGE
========================================================= */

.project-image {
  position: absolute;

  inset: 0;

  width: 100%;
  height: 100%;

  z-index: -3;

  transition: transform 0.8s cubic-bezier(0.2, 0, 0, 1);
}

.project-card:hover .project-image {
  transform: scale(1.07);
}

/* =========================================================
   OVERLAY
========================================================= */

.card-overlay {
  position: absolute;

  inset: 0;

  z-index: -2;

  background: linear-gradient(
    180deg,
    rgba(7, 11, 19, 0.1) 0%,
    rgba(7, 11, 19, 0.05) 30%,
    rgba(7, 11, 19, 0.45) 55%,
    rgba(7, 11, 19, 0.97) 100%
  );

  transition: background 0.5s ease;
}

.project-card:hover .card-overlay {
  background: linear-gradient(
    180deg,
    rgba(7, 11, 19, 0.15),
    rgba(7, 11, 19, 0.9) 75%,
    rgba(7, 11, 19, 1) 100%
  );
}

/* =========================================================
   TOP
========================================================= */

.card-top {
  position: absolute;

  top: 22px;
  left: 22px;
  right: 22px;

  display: flex;

  align-items: center;
  justify-content: space-between;
}

.project-index {
  display: flex;

  align-items: center;
  justify-content: center;

  width: 38px;
  height: 38px;

  border-radius: 50%;

  background: rgba(7, 11, 19, 0.65);

  border: 1px solid rgba(255, 255, 255, 0.15);

  backdrop-filter: blur(10px);

  color: #d3f576;

  font-size: 10px;
  font-weight: 800;

  letter-spacing: 0.05em;
}

.project-year {
  padding: 7px 11px;

  border-radius: 20px;

  background: rgba(7, 11, 19, 0.65);

  border: 1px solid rgba(255, 255, 255, 0.12);

  backdrop-filter: blur(10px);

  color: rgba(255, 255, 255, 0.7);

  font-size: 9px;
  font-weight: 700;

  letter-spacing: 0.08em;
}

/* =========================================================
   CONTENT
========================================================= */

.card-content {
  position: absolute;

  left: 25px;
  right: 25px;
  bottom: 23px;

  z-index: 2;
}

.card-meta {
  margin-bottom: 8px;

  color: #d3f576;

  font-size: 9px;
  font-weight: 800;

  letter-spacing: 0.12em;
}

.project-title {
  margin: 0;

  max-width: 700px;

  color: #ffffff;

  font-size: clamp(27px, 3vw, 43px);

  font-weight: 800;

  line-height: 1;

  letter-spacing: -0.04em;
}

.project-description {
  max-width: 620px;

  margin: 11px 0 0;

  color: rgba(255, 255, 255, 0.62);

  font-size: 12px;

  line-height: 1.6;
}

/* =========================================================
   TECH STACK
========================================================= */

.tech-stack {
  display: flex;

  flex-wrap: wrap;

  gap: 6px;

  margin-top: 13px;

  opacity: 0;

  transform: translateY(8px);

  transition:
    opacity 0.35s ease,
    transform 0.35s ease;
}

.project-card:hover .tech-stack {
  opacity: 1;

  transform: translateY(0);
}

.tech-tag {
  padding: 5px 9px;

  border: 1px solid rgba(211, 245, 118, 0.25);

  border-radius: 20px;

  background: rgba(211, 245, 118, 0.08);

  color: #d3f576;

  font-size: 8px;
  font-weight: 700;

  letter-spacing: 0.05em;
}

/* =========================================================
   ACTION
========================================================= */

.project-action {
  position: absolute;

  right: 0;
  bottom: 0;
}

.project-link {
  display: flex;

  align-items: center;

  gap: 10px;

  color: #ffffff;

  font-size: 9px;
  font-weight: 800;

  letter-spacing: 0.08em;

  text-decoration: none;

  opacity: 0;

  transform: translateX(10px);

  transition:
    opacity 0.35s ease,
    transform 0.35s ease;
}

.project-card:hover .project-link {
  opacity: 1;

  transform: translateX(0);
}

.arrow-circle {
  width: 42px;
  height: 42px;

  display: flex;

  align-items: center;
  justify-content: center;

  border-radius: 50%;

  background: #d3f576;

  color: #0b1220;

  transition: transform 0.3s ease;
}

.project-link:hover .arrow-circle {
  transform: rotate(8deg) scale(1.05);
}

/* =========================================================
   FOOTER
========================================================= */

.projects-footer {
  display: flex;

  align-items: center;

  gap: 16px;

  margin: 25px 7% 0;

  padding-top: 18px;

  border-top: 1px solid rgba(255, 255, 255, 0.08);

  color: rgba(255, 255, 255, 0.25);

  font-size: 9px;
  font-weight: 700;

  letter-spacing: 0.12em;
}

.footer-left {
  display: flex;

  align-items: center;

  gap: 7px;
}

.footer-dot {
  width: 5px;
  height: 5px;

  border-radius: 50%;

  background: #d3f576;

  box-shadow: 0 0 8px rgba(211, 245, 118, 0.5);
}

.footer-line {
  flex: 1;

  height: 1px;

  background: rgba(255, 255, 255, 0.08);
}

/* =========================================================
   TABLET
========================================================= */

@media (max-width: 1000px) {
  .projects-header {
    grid-template-columns: 1fr;

    gap: 25px;

    padding-left: 5%;
    padding-right: 5%;
  }

  .header-right {
    justify-self: start;
  }

  .projects-grid {
    grid-template-columns: 1fr 1fr;

    grid-auto-rows: 380px;

    padding: 0 5%;
  }

  .project-title {
    font-size: 30px;
  }
}

/* =========================================
   MOBILE
========================================= */

@media (max-width: 650px) {
  .projects-section {
    width: 100%;
  }

  .projects-container {
    width: 100%;
    padding-top: 55px;
    padding-left: 0 !important;
    padding-right: 0 !important;
  }

  /* HEADER */

  .projects-header {
    display: block;
    padding: 0 20px 45px;
  }

  .header-left {
    width: 100%;
  }

  .section-label {
    margin-bottom: 16px;
  }

  .projects-heading {
    font-size: clamp(56px, 17vw, 72px);
    line-height: 0.8;
  }

  .header-right {
    width: 100%;
    max-width: none;
    margin-top: 30px;
  }

  .header-right p {
    max-width: 100%;
    font-size: 13px;
    line-height: 1.75;
  }

  .project-count {
    margin-top: 22px;
  }

  /* =========================================
     PROJECT GRID
  ========================================= */

  .projects-grid {
    display: flex;
    flex-direction: column;
    width: 100%;
    gap: 16px;
    padding: 0 20px;
  }

  /* =========================================
     CARDS
  ========================================= */

  .project-card,
  .card-large,
  .card-medium,
  .card-full {
    position: relative;

    width: 100%;
    height: 430px;
    min-height: 430px;

    flex: none;

    grid-column: auto;

    border-radius: 22px;
  }

  /* =========================================
     IMAGE
  ========================================= */

  .project-image {
    position: absolute;
    inset: 0;

    width: 100%;
    height: 100% !important;
  }

  /* =========================================
     TOP
  ========================================= */

  .card-top {
    top: 16px;
    left: 16px;
    right: 16px;
  }

  .project-index {
    width: 34px;
    height: 34px;
    font-size: 9px;
  }

  .project-year {
    padding: 6px 9px;
    font-size: 8px;
  }

  /* =========================================
     CONTENT
  ========================================= */

  .card-content {
    position: absolute;

    left: 18px;
    right: 18px;
    bottom: 18px;

    width: auto;
  }

  .card-meta {
    margin-bottom: 7px;
    font-size: 8px;
  }

  .project-title {
    max-width: 100%;
    font-size: 30px;
    line-height: 0.95;
  }

  .project-description {
    max-width: 100%;
    margin-top: 10px;

    font-size: 11px;
    line-height: 1.6;
  }

  /* =========================================
     TECH STACK
  ========================================= */

  .tech-stack {
    display: flex;

    margin-top: 14px;

    opacity: 1;
    transform: none;
  }

  .tech-tag {
    padding: 4px 7px;
    font-size: 7px;
  }

  /* =========================================
     ACTION
  ========================================= */

  .project-action {
    position: static;

    margin-top: 15px;
  }

  .project-link {
    width: fit-content;

    opacity: 1;
    transform: none;

    font-size: 8px;
  }

  .arrow-circle {
    width: 34px;
    height: 34px;
  }

  /* =========================================
     FOOTER
  ========================================= */

  .projects-footer {
    display: flex;

    width: auto;

    margin: 25px 20px 0;
    padding-top: 18px;

    gap: 12px;

    flex-wrap: wrap;

    font-size: 8px;
  }

  .footer-line {
    min-width: 30px;
  }
}
</style>
