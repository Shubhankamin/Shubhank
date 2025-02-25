<template>
  <div>
    <v-container fluid class="main text-white">
      <v-divider
        :thickness="3"
        class="border-opacity-50 my-5"
        color="white"
      ></v-divider>
      <div data-aos="fade-up" data-aos-duration="3000">
        <v-row class="px-md-14">
          <v-col cols="12" md="6">
            <h1 class="heading bebas-Bold-h1">EDUCATION</h1>
          </v-col>
        </v-row>
        <v-row class="d-none d-md-block">
          <v-col>
            <v-timeline align="start">
              <!-- Timeline item for 1960 -->
              <v-timeline-item dot-color="#d3f576" size="small">
                <template v-slot:opposite>
                  <div>2018</div>
                </template>
                <div>
                  <p class="bebas-Bold-h3">SSLC</p>
                </div>
                <div class="card mt-5">
                  <div class="card-content">
                    <p class="card-title manrope-Bold-h4">
                      SMS ENGLISH MEDIUM SCHOOL
                    </p>
                    <p class="card-para manrope-regular-h5">
                      SMS English Medium School is a reputed institution located
                      in Brahmavar. I completed my SSLC board examination here
                      with an impressive **88.88%**.
                    </p>
                  </div>
                </div>
              </v-timeline-item>

              <!-- Timeline item for 1970 -->
              <v-timeline-item dot-color="#d3f576" size="small">
                <template v-slot:opposite>
                  <div>2020</div>
                </template>
                <div>
                  <p class="bebas-Bold-h3 left-text">PRE-UNIVERSITY</p>
                </div>
                <div class="card left-card">
                  <div class="card-content">
                    <p class="card-title manrope-Bold-h4">MGM PU COLLEGE</p>
                    <p class="card-para manrope-regular-h5">
                      MGM PU College is a well-known institution located in
                      Udupi. I pursued **Commerce with Computer Science** here
                      and successfully completed my PU education with **83%**.
                    </p>
                  </div>
                </div>
              </v-timeline-item>

              <!-- Timeline item for 1980 -->
              <v-timeline-item dot-color="#d3f576" size="small">
                <template v-slot:opposite>
                  <div>2023</div>
                </template>
                <div>
                  <p class="bebas-Bold-h3">BACHELOR'S</p>
                </div>
                <div class="card mt-5">
                  <div class="card-content">
                    <p class="card-title manrope-Bold-h4">MGM COLLEGE</p>
                    <p class="card-para manrope-regular-h5">
                      MGM College is a renowned institution located in Udupi. I
                      pursued a **Bachelor of Computer Applications (BCA)** here
                      and successfully completed the course with a **CGPA of
                      8.62**.
                    </p>
                  </div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </v-col>
        </v-row>
        <v-row class="d-block d-md-none">
          <v-col cols="12" class="mt-5">
            <div>
              <p class="bebas-Bold-h3 mb-2">SSLC - 2018</p>
            </div>
            <div class="card">
              <div class="card-content">
                <p class="card-title manrope-Bold-h4">
                  SMS ENGLISH MEDIUM SCHOOL
                </p>
                <p class="card-para manrope-regular-h5">
                  SMS English Medium School is a reputed institution located in
                  Brahmavar. I completed my SSLC board examination here with an
                  impressive **88.88%**.
                </p>
              </div>
            </div>
          </v-col>
          <v-col cols="12" class="mt-5">
            <div>
              <p class="bebas-Bold-h3 mb-2">PRE-UNIVERSITY - 2020</p>
            </div>
            <div class="card">
              <div class="card-content">
                <p class="card-title manrope-Bold-h4">MGM PU COLLEGE</p>

                <p class="card-para manrope-regular-h5">
                  MGM PU College is a well-known institution located in Udupi. I
                  pursued **Commerce with Computer Science** here and
                  successfully completed my PU education with **83%**.
                </p>
              </div>
            </div>
          </v-col>
          <v-col cols="12" class="mt-5">
            <div>
              <p class="bebas-Bold-h3 mb-2">BACHELOR'S - 2023</p>
            </div>
            <div class="card">
              <div class="card-content">
                <p class="card-title manrope-Bold-h4">MGM COLLEGE</p>

                <p class="card-para manrope-regular-h5">
                  MGM College is a renowned institution located in Udupi. I
                  pursued a **Bachelor of Computer Applications (BCA)** here and
                  successfully completed the course with a **CGPA of 8.62**.
                </p>
              </div>
            </div>
          </v-col>
        </v-row>
      </div>
    </v-container>
  </div>
</template>

<style scoped>
.timeline-container {
  display: flex;
  justify-content: center;
  padding: 20px;
}

.timeline {
  display: flex;
  align-items: center;
  position: relative;
}

.main {
  background-image: url("/images/meteor.png");
  background-size: cover;
  height: 100%;
  width: 100%;
}

.timeline-line {
  width: 2px;
  background-color: black;
  position: absolute;
  height: 100%;
  left: 50%;
  transform: translateX(-50%);
}

.timeline-item {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  margin: 20px 0;
}

.left-card {
  position: absolute;
  left: 48%;
}

.left-text {
  position: absolute;
  left: 26%;
  top: 31%;
  z-index: 999999;
}

.timeline-box {
  background-color: black;
  color: white;
  padding: 20px;
  border-radius: 10px;
  width: 200px;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
}

:deep(.v-timeline--vertical .v-timeline-divider__after) {
  background-color: white;
}

.left-box {
  margin-right: 50px;
}

.right-box {
  margin-left: 50px;
}

/* Card styles */
.card {
  width: 350px;
  height: 200px;
  background-color: #4158d0;
  background-image: linear-gradient(
    43deg,
    #04c65e 0%,
    #669b21 30%,
    #d3f576 70%,
    #ffcc70 100%
  );
  border-radius: 8px;
  color: white;
  overflow: hidden;
  position: relative;
  transform-style: preserve-3d;
  perspective: 1000px;
  transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
  cursor: pointer;
}

.card-content {
  padding: 20px;
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
  color: white;
  align-items: center;
  justify-content: center;
  text-align: center;
  height: 100%;
}

.card-content .card-title {
  color: inherit;
  text-transform: uppercase;
}

.card-content .card-para {
  color: inherit;
  opacity: 0.8;
}

.card:hover {
  transform: rotateY(10deg) rotateX(10deg) scale(1.05);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.card:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.1));
  transition: transform 0.5s cubic-bezier(0.23, 1, 0.32, 1);
  z-index: 1;
}

.card:hover:before {
  transform: translateX(-100%);
}

.card:after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.1));
  transition: transform 0.5s cubic-bezier(0.23, 1, 0.32, 1);
  z-index: 1;
}

.card:hover:after {
  transform: translateX(100%);
}
</style>
