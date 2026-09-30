<template>
  <div class="projects-section">
    <v-container fluid class="projects-container text-white">
      <!-- HEADER -->
      <div class="projects-header" data-aos="fade-up" data-aos-duration="1200">
        <div>
          <span class="section-index">02 / SELECTED WORK</span>

          <h1 class="projects-heading bebas-Bold-h1">
            PROJECT
            <span>ARCHIVE.</span>
          </h1>
        </div>

        <p class="projects-intro manrope-regular-h5">
          A selection of projects I've designed and developed across frontend,
          full-stack applications, and experimental experiences.
        </p>
      </div>

      <!-- PROJECTS -->
      <div class="project-list">
        <div
          v-for="(item, index) in projects"
          :key="item.title"
          class="project-row"
          data-aos="fade-up"
          data-aos-duration="1000"
        >
          <!-- NUMBER -->
          <div class="project-number">
            {{ String(index + 1).padStart(2, "0") }}
          </div>

          <!-- CONTENT -->
          <div class="project-info">
            <div class="project-meta">
              <span>{{ item.year }}</span>

              <span class="meta-divider"></span>

              <span class="role">
                {{ item.role }}
              </span>
            </div>

            <h2 class="project-title">
              {{ item.title }}
            </h2>

            <p class="project-description">
              {{ item.description }}
            </p>

            <!-- TECH STACK -->
            <div class="tech-stack">
              <span v-for="tech in item.tech" :key="tech" class="tech-tag">
                {{ tech }}
              </span>
            </div>

            <!-- LINKS -->
            <div class="project-links">
              <a
                v-if="item.liveDemo"
                :href="item.liveDemo"
                target="_blank"
                rel="noopener noreferrer"
              >
                <span>LIVE PROJECT</span>
                <v-icon size="16"> mdi-arrow-top-right </v-icon>
              </a>

              <a
                v-if="item.github"
                :href="item.github"
                target="_blank"
                rel="noopener noreferrer"
              >
                <span>GITHUB</span>
                <v-icon size="16"> mdi-github </v-icon>
              </a>
            </div>
          </div>

          <!-- IMAGE -->
          <div class="project-preview">
            <v-img :src="item.src" :alt="item.title" cover />

            <div class="preview-overlay"></div>

            <span class="preview-index">
              {{ String(index + 1).padStart(2, "0") }}
            </span>

            <span class="preview-arrow"> ↗ </span>
          </div>
        </div>
      </div>

      <!-- FOOTER -->
      <div class="projects-footer">
        <span>END OF PROJECT ARCHIVE</span>

        <div class="footer-line"></div>

        <span>
          {{ String(projects.length).padStart(2, "0") }}
          PROJECTS
        </span>
      </div>

      <v-divider :thickness="3" class="border-opacity-50 mt-10" color="white" />
    </v-container>
  </div>
</template>

<script setup>
const projects = [
  {
    src: "/images/project-1.png",
    title: "Phoenix Academy Website",
    description:
      "A full-stack education platform developed for Phoenix Academy, covering both client and admin experiences. Built with Nuxt 3 and Vue 3, with Supabase powering backend data and Resend handling email communication.",
    year: "2025",
    role: "Full-Stack Developer",
    tech: ["Nuxt 3", "Vue 3", "Supabase", "Resend"],
    liveDemo: "https://pheonixacademy.in/",
    github: "https://github.com/Shubhankamin/Pheonix",
  },

  {
    src: "/images/project-2.png",
    title: "Interactive Birthday Experience",
    description:
      "An immersive interactive experience focused on animation, visual storytelling and responsive UI. Developed with Nuxt 3, Vue 3 and Vuetify with emphasis on fluid transitions and frontend interaction.",
    year: "2025",
    role: "Front-End Developer",
    tech: ["Nuxt 3", "Vue 3", "Vuetify"],
    liveDemo: "https://mymadamji.netlify.app/",
    github: "https://github.com/Shubhankamin/Madam-Ji",
  },

  {
    src: "/images/project-3.jpg",
    title: "AgriMart E-commerce Website",
    description:
      "A role-based eCommerce platform connecting farmers and customers. Built entirely with HTML, CSS and JavaScript with client-side persistence and shopping functionality.",
    year: "2025",
    role: "Front-End Developer",
    tech: ["HTML", "CSS", "JavaScript", "IndexedDB"],
    liveDemo: "https://agrimaart.netlify.app",
    github: "https://github.com/Shubhankamin/Agri_Mart",
  },

  {
    src: "/images/project-4.jpg",
    title: "Lost & Found Management Portal",
    description:
      "A college-focused lost and found platform allowing students to report and claim items while providing administrators with tools to manage listings and users.",
    year: "2025",
    role: "Full-Stack Developer",
    tech: ["Vue 3", "Nuxt 3", "Vuetify", "Firebase"],
    liveDemo: "https://lostorfound.netlify.app",
    github: "https://github.com/Shubhankamin/Find",
  },

  {
    src: "/images/project-5.jpg",
    title: "Lost & Found Admin Portal",
    description:
      "The administrative interface for the Lost & Found ecosystem, providing management functionality for listings, users and verification workflows.",
    year: "2025",
    role: "Full-Stack Developer",
    tech: ["Vue 3", "Nuxt 3", "Vuetify", "Firebase"],
    github: "https://github.com/Shubhankamin/Find-Admin",
  },
];
</script>

<style scoped>
.projects-section {
  width: 100%;
  overflow: hidden;
}

.projects-container {
  padding-top: 80px;
  padding-bottom: 40px;
}

/* HEADER */

.projects-header {
  display: grid;
  grid-template-columns: 1fr 0.8fr;
  align-items: end;
  gap: 80px;

  padding: 0 6% 70px;
}

.section-index {
  display: block;
  margin-bottom: 15px;

  color: #d3f576;

  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.projects-heading {
  margin: 0;

  color: #ffffff;

  font-size: clamp(55px, 7vw, 100px);
  line-height: 0.82;
  letter-spacing: -0.04em;

  text-transform: uppercase;
}

.projects-heading span {
  display: block;
  color: #d3f576;
}

.projects-intro {
  max-width: 500px;
  margin: 0;

  color: rgba(255, 255, 255, 0.55);

  line-height: 1.8;
}

/* PROJECT ROW */

.project-list {
  width: 100%;
}

.project-row {
  position: relative;

  display: grid;
  grid-template-columns: 70px minmax(300px, 1fr) minmax(350px, 0.8fr);

  align-items: center;
  gap: 50px;

  min-height: 430px;

  padding: 55px 6%;

  border-top: 1px solid rgba(255, 255, 255, 0.1);

  transition: background 0.4s ease;
}

.project-row:last-child {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.project-row:hover {
  background: rgba(211, 245, 118, 0.015);
}

/* NUMBER */

.project-number {
  align-self: start;
  padding-top: 8px;

  color: rgba(255, 255, 255, 0.25);

  font-size: 13px;
  font-weight: 800;
  letter-spacing: 0.08em;

  transition: color 0.3s ease;
}

.project-row:hover .project-number {
  color: #d3f576;
}

/* INFO */

.project-info {
  position: relative;
  z-index: 2;
}

.project-meta {
  display: flex;
  align-items: center;
  gap: 12px;

  margin-bottom: 18px;

  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.08em;
}

.project-meta > span:first-child {
  color: #d3f576;
}

.meta-divider {
  width: 1px;
  height: 12px;

  background: rgba(255, 255, 255, 0.2);
}

.role {
  color: rgba(255, 255, 255, 0.35);
  text-transform: uppercase;
}

/* TITLE */

.project-title {
  margin: 0;

  color: #ffffff;

  font-size: clamp(30px, 3vw, 48px);
  font-weight: 800;

  line-height: 1;
  letter-spacing: -0.04em;

  transition: color 0.3s ease;
}

.project-row:hover .project-title {
  color: #d3f576;
}

/* DESCRIPTION */

.project-description {
  max-width: 600px;

  margin: 20px 0;

  color: rgba(255, 255, 255, 0.55);

  font-size: 13px;
  line-height: 1.8;
}

/* TECH */

.tech-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;

  margin-top: 20px;
}

.tech-tag {
  padding: 5px 10px;

  border: 1px solid rgba(211, 245, 118, 0.18);
  border-radius: 20px;

  background: rgba(211, 245, 118, 0.035);

  color: rgba(211, 245, 118, 0.75);

  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.05em;
}

/* LINKS */

.project-links {
  display: flex;
  align-items: center;
  gap: 22px;

  margin-top: 28px;
}

.project-links a {
  display: flex;
  align-items: center;
  gap: 7px;

  color: #d3f576;

  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.08em;

  text-decoration: none;

  transition:
    transform 0.25s ease,
    opacity 0.25s ease;
}

.project-links a:hover {
  transform: translateX(4px);
  opacity: 0.7;
}

/* IMAGE */

.project-preview {
  position: relative;

  width: 100%;
  aspect-ratio: 16 / 10;

  overflow: hidden;

  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 22px;

  background: #0b1220;

  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);

  transform: rotate(1deg) scale(0.96);

  transition:
    transform 0.55s cubic-bezier(0.2, 0, 0, 1),
    border-color 0.4s ease,
    box-shadow 0.4s ease;
}

.project-row:hover .project-preview {
  transform: rotate(0deg) scale(1);

  border-color: rgba(211, 245, 118, 0.25);

  box-shadow:
    0 30px 70px rgba(0, 0, 0, 0.55),
    0 0 45px rgba(211, 245, 118, 0.06);
}

.project-preview :deep(.v-img) {
  width: 100%;
  height: 100%;
}

.project-preview :deep(.v-img img) {
  transition: transform 0.7s cubic-bezier(0.2, 0, 0, 1);
}

.project-row:hover .project-preview :deep(.v-img img) {
  transform: scale(1.06);
}

/* IMAGE OVERLAY */

.preview-overlay {
  position: absolute;
  inset: 0;

  background: linear-gradient(
    135deg,
    rgba(211, 245, 118, 0.08),
    transparent 45%,
    rgba(0, 0, 0, 0.35)
  );

  pointer-events: none;
}

.preview-index {
  position: absolute;

  top: 15px;
  left: 18px;

  z-index: 2;

  color: rgba(255, 255, 255, 0.7);

  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.1em;
}

.preview-arrow {
  position: absolute;

  right: 18px;
  bottom: 15px;

  z-index: 2;

  width: 38px;
  height: 38px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 50%;

  background: #d3f576;

  color: #0b1220;

  font-size: 20px;

  opacity: 0;

  transform: translate(8px, 8px);

  transition:
    opacity 0.35s ease,
    transform 0.35s ease;
}

.project-row:hover .preview-arrow {
  opacity: 1;
  transform: translate(0, 0);
}

/* FOOTER */

.projects-footer {
  display: flex;
  align-items: center;
  gap: 15px;

  padding: 22px 6% 0;

  color: rgba(255, 255, 255, 0.25);

  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.12em;
}

.footer-line {
  flex: 1;
  height: 1px;

  background: rgba(255, 255, 255, 0.08);
}

/* TABLET */

@media (max-width: 1100px) {
  .projects-header {
    grid-template-columns: 1fr;
    gap: 25px;
  }

  .project-row {
    grid-template-columns: 50px 1fr;
    gap: 30px;
  }

  .project-preview {
    grid-column: 2;
    width: 85%;
  }
}

/* MOBILE */

@media (max-width: 700px) {
  .projects-container {
    padding-top: 50px;
  }

  .projects-header {
    padding: 0 20px 45px;
  }

  .projects-heading {
    font-size: 58px;
  }

  .project-row {
    grid-template-columns: 35px 1fr;
    gap: 15px;

    min-height: auto;

    padding: 40px 20px;
  }

  .project-title {
    font-size: 31px;
  }

  .project-description {
    font-size: 12px;
  }

  .project-preview {
    grid-column: 2;

    width: 100%;

    margin-top: 15px;

    aspect-ratio: 16 / 11;

    border-radius: 17px;
  }

  .project-links {
    flex-wrap: wrap;
    gap: 15px;
  }

  .projects-footer {
    padding-left: 20px;
    padding-right: 20px;
  }
}
</style>
