<template>
  <div class="main">
    <v-container fluid class="pa-5">
      <v-row>
        <!-- LEFT -->

        <v-col cols="12" md="12">
          <div class="sticky-heading">
            <h1 class="heading bebas-Bold-h1 text-white">My Experience</h1>

            <p class="subtitle manrope-regular-h5 pt-5">
              Experience building modern web applications, scalable frontend
              systems, and responsive UI across startup and freelance
              environments.
            </p>
          </div>
        </v-col>

        <!-- RIGHT -->

        <v-col cols="12" md="12">
          <div
            v-for="(experience, index) in experiences"
            :key="index"
            class="experience-card mb-8"
          >
            <!-- TOP -->

            <div class="card-top">
              <div>
                <h2 class="role-title">
                  {{ experience.title }}
                </h2>

                <p class="company">
                  {{ experience.company }}
                </p>
              </div>

              <div class="date-pill">
                {{ experience.dates }}
              </div>
            </div>

            <!-- DESCRIPTION -->

            <ul class="experience-list">
              <li v-for="(point, i) in experience.points" :key="i">
                {{ point }}
              </li>
            </ul>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
const experiences = [
  {
    title: "Front-End Developer",

    company: "Exelon Circuits Private Limited",

    dates: "Jan 2024 — May 2025",

    points: [
      "Developed e-commerce websites, admin dashboards, portfolios, and real estate platforms using Nuxt.js and Vue.js.",

      "Integrated REST APIs and used Postman for debugging and testing workflows.",

      "Built responsive, cross-browser-compatible interfaces optimized for performance and accessibility.",

      "Collaborated with teams to deliver scalable UI systems and production-ready applications.",
    ],
  },

  {
    title: "Web Development Intern",

    company: "Amdox Technologies",

    dates: "Dec 2025 — Jan 2026",

    points: [
      "Contributed to web application development and responsive user interface implementation.",

      "Worked on API integrations and frontend feature development for real-world software projects.",

      "Collaborated with development teams to build scalable and maintainable web solutions.",

      "Gained hands-on experience with modern frontend workflows and project delivery processes.",
    ],
  },

  {
    title: "Full-Stack App Development Intern",

    company: "aiRender Technology Pvt. Ltd.",

    dates: "May 2026 — Present",

    points: [
      "Contributing to full-stack and AI-driven application development.",

      "Building frontend interfaces and integrating backend services for production applications.",

      "Working on intelligent software features and real-world business solutions.",

      "Collaborating with the development team on scalable architecture and modern development practices.",
    ],
  },

  {
    title: "Freelance Developer",

    company: "Independent Projects",

    dates: "Nov 2024 — Apr 2025",

    points: [
      "Built and deployed custom websites and database-driven applications for clients.",

      "Worked on frontend architecture, API integrations, and responsive UI systems.",

      "Managed multiple freelance projects independently with focus on quality and maintainability.",

      "Delivered scalable web experiences aligned with client requirements and business goals.",
    ],
  },
];
</script>

<style scoped>
/* SECTION */

.main {
  position: relative;

  overflow: hidden;
}

/* GLOW */

.main::before {
  content: "";

  position: absolute;

  width: 600px;
  height: 600px;

  top: -200px;
  right: -200px;

  background: radial-gradient(
    circle,
    rgba(132, 204, 22, 0.08),
    transparent 70%
  );

  filter: blur(120px);

  z-index: -1;
}

/* HEADING */

.heading {
  text-transform: uppercase;

  line-height: 0.95;
}

.subtitle {
  color: rgba(255, 255, 255, 0.68);

  line-height: 1.8;
}

/* STICKY */

.sticky-heading {
  position: sticky;
}

/* CARD */

.experience-card {
  position: relative;

  padding: 36px;

  border-radius: 32px;

  background: rgba(255, 255, 255, 0.03);

  border: 1px solid rgba(255, 255, 255, 0.08);

  backdrop-filter: blur(14px);

  transition:
    transform 0.4s ease,
    border-color 0.4s ease,
    box-shadow 0.4s ease;

  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.35);

  overflow: hidden;
}

/* CARD HOVER */

.experience-card:hover {
  transform: translateY(-8px);

  border-color: rgba(211, 245, 118, 0.16);

  box-shadow: 0 25px 80px rgba(0, 0, 0, 0.45);
}

/* CARD GLOW */

.experience-card::before {
  content: "";

  position: absolute;

  width: 250px;
  height: 250px;

  top: -120px;
  right: -120px;

  background: radial-gradient(
    circle,
    rgba(211, 245, 118, 0.08),
    transparent 70%
  );

  filter: blur(60px);

  opacity: 0;

  transition: opacity 0.4s ease;
}

.experience-card:hover::before {
  opacity: 1;
}

/* TOP */

.card-top {
  display: flex;

  justify-content: space-between;

  gap: 20px;

  flex-wrap: wrap;

  margin-bottom: 30px;
}

/* ROLE */

.role-title {
  color: white;

  font-size: 1.8rem;

  font-weight: 700;

  line-height: 1.1;
}

/* COMPANY */

.company {
  color: rgba(255, 255, 255, 0.55);

  margin-top: 8px;
}

/* DATE */

.date-pill {
  height: fit-content;

  padding: 10px 18px;

  border-radius: 999px;

  background: rgba(255, 255, 255, 0.05);

  border: 1px solid rgba(255, 255, 255, 0.08);

  color: #d3f576;

  font-size: 14px;

  white-space: nowrap;
}

/* LIST */

.experience-list {
  padding-left: 20px;

  display: flex;

  flex-direction: column;

  gap: 18px;
}

.experience-list li {
  color: rgba(255, 255, 255, 0.72);

  line-height: 1.8;
}

/* MOBILE */

@media (max-width: 960px) {
  .main {
    padding: 80px 0;
  }

  .sticky-heading {
    position: relative;

    top: 0;

    margin-bottom: 50px;
  }

  .experience-card {
    padding: 28px;
  }

  .role-title {
    font-size: 1.5rem;
  }
}
</style>
