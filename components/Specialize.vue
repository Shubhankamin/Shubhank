<template>
  <div>
    <v-container fluid class="main text-white px-md-15">
      <div data-aos="fade-up" data-aos-duration="3000">
        <v-row>
          <v-col cols="12" md="6">
            <h1 class="heading bebas-Bold-h1">SPECIALIZED</h1>
          </v-col>
        </v-row>
        <v-row>
          <v-col
            v-for="(card, index) in cardData"
            :key="index"
            cols="12"
            md="4"
            class="d-flex justify-center"
          >
            <div class="flip-card cursor-pointer">
              <div class="flip-card-inner">
                <div
                  class="flip-card-front"
                  :style="{ backgroundImage: `url(${card.frontImage})` }"
                ></div>
                <div
                  class="flip-card-back"
                  :style="{ backgroundImage: `url(${card.backImage})` }"
                >
                  <p class="title">{{ card.backText }}</p>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>
      </div>
    </v-container>
  </div>
</template>

<script setup>
const cardData = [
  {
    frontImage: "/images/admin-2.jpg",
    backImage: "/images/back-image1.jpg",
    backText: "ADMIN PANEL DEVELOPMENT",
  },
  {
    frontImage: "/images/app.jpg",
    backImage: "/images/back-image2.jpg",
    backText: "MOBILE APP DEVELOPMENT",
  },

  {
    frontImage: "/images/web.jpg",
    backImage: "/images/back-image2.jpg",
    backText: "WEBSITE  DEVELOPMENT",
  },
];
</script>

<style scoped>
.flip-card {
  background-color: transparent;
  width: 350px;
  height: 400px;
  perspective: 1000px;
  font-family: sans-serif;
}

.main {
  background-image: url("images/meteor.png");
  background-size: cover;
  height: 100%;
  width: 100%;
}

.title {
  font-size: 1.5em;
  font-weight: 900;
  text-align: center;
  margin: 0;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
  box-shadow: 0 8px 14px 0 rgba(0, 0, 0, 0.2);
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border: 1px solid #d3f576;
  border-radius: 1rem;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.flip-card-front {
  color: black;
}

.flip-card-back {
  color: white;
  transform: rotateY(180deg);
}
</style>
