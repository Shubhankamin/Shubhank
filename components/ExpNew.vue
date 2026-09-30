<template>
  <section class="experience-section">
    <v-container fluid class="experience-container">
      <!-- HEADER -->
      <div
        class="experience-header"
        data-aos="fade-up"
        data-aos-duration="1200"
      >
        <div class="section-label">
          <span>05</span>
          <span>EXPERIENCE</span>
        </div>

        <div class="experience-heading-wrap">
          <h1 class="experience-heading bebas-Bold-h1">
            MY
            <span>JOURNEY.</span>
          </h1>

          <p class="experience-intro manrope-regular-h5">
            A look at my professional experience, the roles I've taken on, and
            the work I've been part of.
          </p>
        </div>
      </div>

      <!-- TIMELINE -->
      <div class="experience-timeline">
        <article
          v-for="(experience, index) in experiences"
          :key="index"
          class="experience-item"
          data-aos="fade-up"
          data-aos-duration="1000"
          :data-aos-delay="index * 100"
        >
          <!-- LEFT META -->
          <div class="experience-meta">
            <span class="experience-number">
              {{ String(index + 1).padStart(2, "0") }}
            </span>

            <span class="experience-year">
              {{ experience.shortDate }}
            </span>
          </div>

          <!-- CENTER CONTENT -->
          <div class="experience-content">
            <div class="experience-topline">
              <span>{{ experience.type }}</span>
              <span class="topline-dot"></span>
              <span>{{ experience.location }}</span>
            </div>

            <h2 class="experience-role">
              {{ experience.title }}
            </h2>

            <h3 class="experience-company">
              {{ experience.company }}
            </h3>

            <p class="experience-description">
              {{ experience.description }}
            </p>

            <div class="experience-points">
              <div
                v-for="(point, i) in experience.points"
                :key="i"
                class="experience-point"
              >
                <span class="point-marker"></span>
                <p>{{ point }}</p>
              </div>
            </div>

            <div class="experience-tags">
              <span v-for="tech in experience.technologies" :key="tech">
                {{ tech }}
              </span>
            </div>
          </div>

          <!-- RIGHT YEAR -->
          <div class="experience-date">
            {{ experience.dates }}
          </div>
        </article>
      </div>

      <!-- FOOTER -->
      <div
        class="experience-footer"
        data-aos="fade-up"
        data-aos-duration="1000"
      >
        <span class="footer-label">THE JOURNEY</span>

        <p class="manrope-Bold-h5">
          From building interfaces
          <span>to building complete systems.</span>
        </p>
      </div>
    </v-container>
  </section>
</template>

<script setup>
const experiences = [
  {
    title: "Front-End Developer",
    company: "Exelon Circuits Private Limited",
    dates: "JAN 2024 — MAY 2025",
    shortDate: "2024 — 25",
    type: "FULL-TIME",
    location: "SURATHKAL",
    description:
      "Worked on production web applications across e-commerce, administration, real estate and portfolio platforms.",
    points: [
      "Developed responsive web applications using Nuxt.js and Vue.js.",
      "Integrated REST APIs and used Postman for debugging and testing workflows.",
      "Built cross-browser interfaces with a focus on performance, accessibility and responsive behaviour.",
      "Collaborated with teams to deliver scalable UI systems and production-ready applications.",
    ],
    technologies: ["Vue.js", "Nuxt.js", "REST APIs", "Postman"],
  },

  {
    title: "Web Development Intern",
    company: "Amdox Technologies",
    dates: "DEC 2025 — JAN 2026",
    shortDate: "2025 — 26",
    type: "INTERNSHIP",
    location: "BANGALORE",
    description:
      "Contributed to real-world web application development while working with modern frontend workflows and API-driven features.",
    points: [
      "Contributed to responsive interface development and frontend feature implementation.",
      "Worked with API integrations across application features.",
      "Collaborated with development teams on scalable and maintainable web solutions.",
      "Gained hands-on experience with modern development and project delivery workflows.",
    ],
    technologies: ["Frontend", "APIs", "Responsive UI", "Web Development"],
  },

  {
    title: "Full-Stack App Development Intern",
    company: "aiRender Technology Pvt. Ltd.",
    dates: "MAY 2026 — PRESENT",
    shortDate: "2026 —",
    type: "INTERNSHIP",
    location: "INDIA",
    description:
      "Currently contributing to full-stack and AI-driven applications, working across interfaces, backend services and intelligent product features.",
    points: [
      "Contributing to full-stack and AI-driven application development.",
      "Building frontend interfaces and integrating backend services.",
      "Working on intelligent software features and real-world business solutions.",
      "Collaborating with the development team on scalable architecture and modern development practices.",
    ],
    technologies: ["Full Stack", "AI Applications", "Frontend", "Backend"],
  },

  {
    title: "Freelance Developer",
    company: "Independent Projects",
    dates: "NOV 2024 — APR 2025",
    shortDate: "2024 — 25",
    type: "FREELANCE",
    location: "REMOTE",
    description:
      "Designed, developed and deployed custom digital experiences for independent projects and client requirements.",
    points: [
      "Built custom websites and database-driven applications.",
      "Worked across frontend architecture, API integrations and responsive UI systems.",
      "Managed projects independently from development through deployment.",
      "Delivered solutions aligned with project requirements and business goals.",
    ],
    technologies: ["Web Development", "UI Development", "APIs", "Deployment"],
  },
];
</script>

<style scoped>
/* =========================================
   EXPERIENCE
========================================= */

.experience-section {
  position: relative;
  width: 100%;
  overflow: hidden;
  padding: 150px 0 120px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}

.experience-section::before {
  content: "";
  position: absolute;
  width: 500px;
  height: 500px;
  top: 10%;
  right: -250px;
  border-radius: 50%;
  background: radial-gradient(
    circle,
    rgba(211, 245, 118, 0.08),
    transparent 70%
  );
  filter: blur(100px);
  pointer-events: none;
}

.experience-container {
  position: relative;
  z-index: 1;
}

/* =========================================
   HEADER
========================================= */

.section-label {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 45px;

  color: rgba(255, 255, 255, 0.4);

  font-family: "Manrope", sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.14em;
}

.section-label span:first-child {
  color: #d3f576;
}

.experience-heading-wrap {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 8vw;
  align-items: end;
  margin-bottom: 110px;
}

.experience-heading {
  margin: 0;

  color: #ffffff;

  font-size: clamp(75px, 10vw, 150px);
  line-height: 0.78;

  text-transform: uppercase;
}

.experience-heading span {
  display: block;
  color: #d3f576;
}

.experience-intro {
  max-width: 520px;
  margin: 0;

  color: rgba(255, 255, 255, 0.48);

  line-height: 1.8;
}

/* =========================================
   TIMELINE
========================================= */

.experience-timeline {
  position: relative;
  border-top: 1px solid rgba(255, 255, 255, 0.16);
}

/* vertical line */

.experience-timeline::before {
  content: "";
  position: absolute;

  top: 0;
  bottom: 0;
  left: 77px;

  width: 1px;

  background: rgba(255, 255, 255, 0.1);
}

/* =========================================
   EXPERIENCE ITEM
========================================= */

.experience-item {
  position: relative;

  display: grid;
  grid-template-columns: 155px 1fr 180px;

  gap: 35px;

  padding: 55px 0;

  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.experience-item::before {
  content: "";

  position: absolute;

  top: 64px;
  left: 71px;

  width: 13px;
  height: 13px;

  border: 2px solid #d3f576;
  border-radius: 50%;

  background: #030712;

  box-shadow:
    0 0 0 5px rgba(211, 245, 118, 0.04),
    0 0 20px rgba(211, 245, 118, 0.15);

  z-index: 2;
}

/* =========================================
   META
========================================= */

.experience-meta {
  display: flex;
  flex-direction: column;
  gap: 10px;

  padding-left: 5px;
}

.experience-number {
  color: #d3f576;

  font-family: "Bebas Neue", sans-serif;
  font-size: 34px;
  line-height: 1;
}

.experience-year {
  color: rgba(255, 255, 255, 0.3);

  font-family: "Manrope", sans-serif;
  font-size: 9px;
  font-weight: 700;

  letter-spacing: 0.1em;
}

/* =========================================
   CONTENT
========================================= */

.experience-content {
  max-width: 780px;
}

.experience-topline {
  display: flex;
  align-items: center;
  gap: 10px;

  margin-bottom: 15px;

  color: rgba(255, 255, 255, 0.32);

  font-family: "Manrope", sans-serif;
  font-size: 10px;
  font-weight: 700;

  letter-spacing: 0.14em;
}

.topline-dot {
  width: 3px;
  height: 3px;

  border-radius: 50%;

  background: #d3f576;
}

.experience-role {
  margin: 0;

  color: #ffffff;

  font-family: "Bebas Neue", sans-serif;
  font-size: clamp(42px, 5vw, 70px);
  font-weight: 700;

  line-height: 0.9;
  text-transform: uppercase;
}

.experience-company {
  margin: 12px 0 0;

  color: #d3f576;

  font-family: "Manrope", sans-serif;
  font-size: 14px;
  font-weight: 700;
}

.experience-description {
  max-width: 650px;

  margin: 25px 0 0;

  color: rgba(255, 255, 255, 0.55);

  font-family: "Manrope", sans-serif;
  font-size: 14px;

  line-height: 1.8;
}

/* =========================================
   POINTS
========================================= */

.experience-points {
  display: flex;
  flex-direction: column;
  gap: 14px;

  margin-top: 30px;
}

.experience-point {
  display: flex;
  align-items: flex-start;
  gap: 14px;
}

.point-marker {
  flex-shrink: 0;

  width: 5px;
  height: 5px;

  margin-top: 8px;

  border-radius: 50%;

  background: rgba(211, 245, 118, 0.6);
}

.experience-point p {
  max-width: 650px;

  margin: 0;

  color: rgba(255, 255, 255, 0.43);

  font-family: "Manrope", sans-serif;
  font-size: 14px;

  line-height: 1.7;
}

/* =========================================
   TECHNOLOGIES
========================================= */

.experience-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;

  margin-top: 30px;
}

.experience-tags span {
  padding: 6px 0;

  color: rgba(255, 255, 255, 0.35);

  font-family: "Manrope", sans-serif;
  font-size: 10px;
  font-weight: 700;

  letter-spacing: 0.08em;

  text-transform: uppercase;
}

.experience-tags span:not(:last-child)::after {
  content: "/";
  margin-left: 8px;

  color: rgba(211, 245, 118, 0.35);
}

/* =========================================
   DATE
========================================= */

.experience-date {
  justify-self: end;
  align-self: start;

  padding-top: 4px;

  color: rgba(255, 255, 255, 0.35);

  font-family: "Manrope", sans-serif;
  font-size: 10px;
  font-weight: 700;

  letter-spacing: 0.12em;

  text-align: right;
  white-space: nowrap;
}

/* =========================================
   FOOTER
========================================= */

.experience-footer {
  display: grid;
  grid-template-columns: 155px 1fr;

  gap: 35px;

  margin-top: 70px;
  padding-top: 25px;

  border-top: 1px solid rgba(255, 255, 255, 0.12);
}

.footer-label {
  color: rgba(255, 255, 255, 0.28);

  font-family: "Manrope", sans-serif;
  font-size: 9px;
  font-weight: 700;

  letter-spacing: 0.14em;
}

.experience-footer p {
  margin: 0;

  color: rgba(255, 255, 255, 0.6);
}

.experience-footer p span {
  color: #d3f576;
}

/* =========================================
   HOVER
========================================= */

.experience-item {
  transition: padding-left 0.4s ease;
}

.experience-item:hover {
  padding-left: 12px;
}

.experience-item:hover::before {
  box-shadow:
    0 0 0 7px rgba(211, 245, 118, 0.05),
    0 0 25px rgba(211, 245, 118, 0.25);
}

.experience-item:hover .experience-number {
  color: #ffffff;
}

.experience-item:hover .experience-company {
  color: #ffffff;
}

/* =========================================
   TABLET
========================================= */

/* =========================================
   TABLET
========================================= */

@media (max-width: 960px) {
  .experience-section {
    padding: 100px 0 90px;
  }

  /* HEADER */

  .experience-heading-wrap {
    grid-template-columns: 1fr;
    gap: 35px;
    margin-bottom: 75px;
  }

  .experience-heading {
    font-size: clamp(80px, 12vw, 120px);
  }

  .experience-intro {
    max-width: 600px;
  }

  /* TIMELINE */

  .experience-timeline::before {
    left: 10px;
  }

  .experience-item {
    display: grid;
    grid-template-columns: 40px 1fr;
    gap: 25px;

    padding: 50px 0;
  }

  .experience-item::before {
    top: 58px;
    left: 4px;

    width: 13px;
    height: 13px;
  }

  /* META */

  .experience-meta {
    grid-column: 1;
    padding-left: 0;
  }

  .experience-number {
    font-size: 28px;
  }

  .experience-year {
    display: none;
  }

  /* CONTENT */

  .experience-content {
    grid-column: 2;
    max-width: none;
  }

  .experience-topline {
    margin-bottom: 14px;
  }

  .experience-role {
    font-size: clamp(42px, 7vw, 65px);
  }

  .experience-company {
    font-size: 13px;
  }

  .experience-description {
    max-width: 650px;
    font-size: 13px;
  }

  /* DATE */

  .experience-date {
    grid-column: 2;

    justify-self: start;

    margin-top: 25px;
    padding: 0;

    font-size: 9px;
    text-align: left;
  }

  /* FOOTER */

  .experience-footer {
    grid-template-columns: 40px 1fr;
    gap: 25px;
  }
}

/* =========================================
   MOBILE
========================================= */

@media (max-width: 600px) {
  .experience-section {
    padding: 75px 0 65px;
  }

  /* HEADER */

  .section-label {
    margin-bottom: 30px;
  }

  .experience-heading-wrap {
    display: block;
    margin-bottom: 60px;
  }

  .experience-heading {
    font-size: 72px;
    line-height: 0.8;
  }

  .experience-intro {
    max-width: 100%;
    margin-top: 30px;

    font-size: 13px;
    line-height: 1.75;
  }

  /* TIMELINE */

  .experience-timeline {
    margin-top: 0;
  }

  .experience-timeline::before {
    left: 8px;
  }

  /* EXPERIENCE ITEM */

  .experience-item {
    display: block;

    padding: 42px 0 45px 32px;
  }

  .experience-item:first-child {
    padding-top: 38px;
  }

  /* TIMELINE DOT */

  .experience-item::before {
    top: 48px;
    left: 2px;

    width: 12px;
    height: 12px;

    border-width: 1px;

    box-shadow:
      0 0 0 4px rgba(211, 245, 118, 0.04),
      0 0 15px rgba(211, 245, 118, 0.15);
  }

  /* META */

  .experience-meta {
    display: block;

    margin-bottom: 18px;
    padding: 0;
  }

  .experience-number {
    display: inline-block;

    font-size: 22px;
    line-height: 1;
  }

  .experience-year {
    display: inline-block;

    margin-left: 10px;

    color: rgba(255, 255, 255, 0.28);

    font-size: 8px;
  }

  /* CONTENT */

  .experience-content {
    width: 100%;
  }

  .experience-topline {
    flex-wrap: wrap;

    gap: 8px;

    margin-bottom: 14px;

    font-size: 7px;
    letter-spacing: 0.12em;
  }

  .topline-dot {
    width: 3px;
    height: 3px;
  }

  .experience-role {
    font-size: 39px;
    line-height: 0.9;
  }

  .experience-company {
    margin-top: 10px;

    font-size: 11px;
    line-height: 1.5;
  }

  .experience-description {
    margin-top: 20px;

    font-size: 11px;
    line-height: 1.75;
  }

  /* POINTS */

  .experience-points {
    gap: 12px;
    margin-top: 25px;
  }

  .experience-point {
    gap: 10px;
  }

  .point-marker {
    width: 4px;
    height: 4px;

    margin-top: 7px;
  }

  .experience-point p {
    font-size: 10px;
    line-height: 1.7;
  }

  /* TECHNOLOGIES */

  .experience-tags {
    gap: 4px 8px;

    margin-top: 23px;
  }

  .experience-tags span {
    padding: 3px 0;

    font-size: 8px;
    line-height: 1.4;
  }

  /* DATE */

  .experience-date {
    display: block;

    margin-top: 20px;

    font-size: 8px;
    letter-spacing: 0.1em;
  }

  /* FOOTER */

  .experience-footer {
    display: block;

    margin-top: 55px;
    padding-top: 20px;
  }

  .footer-label {
    display: block;

    margin-bottom: 14px;

    font-size: 8px;
  }

  .experience-footer p {
    font-size: 13px;
    line-height: 1.6;
  }

  /* DISABLE LARGE DESKTOP HOVER SHIFT */

  .experience-item:hover {
    padding-left: 32px;
  }
}
</style>
