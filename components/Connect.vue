<template>
  <div>
    <v-container fluid class="main text-white pt-0">
      <v-row
        class="px-md-10 pt-md-10"
        data-aos="fade-up"
        data-aos-duration="3000"
      >
        <v-col cols="12" md="6">
          <p class="heading text-white bebas-Bold-h1">Let’s connect</p>
          <p class="manrope-regular-h5">Say hello at robertgarcia@gmail.com</p>
          <p class="manrope-regular-h5">For more info, here’s my resume</p>
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
        <v-col cols="12" md="6" class="pr-md-10">
          <form
            action="https://formsubmit.co/shubhankamin20@gmail.com"
            method="POST"
          >
            <div>
              <p class="pb-5">Name</p>

              <input
                placeholder="Enter your Name"
                class="input w-75 py-1"
                type="text"
                name="name"
              />
            </div>
            <div>
              <p class="py-5">Email</p>

              <input
                class="input w-75 py-1"
                type="email"
                placeholder="Enter Email"
                name="email"
              />
            </div>
            <div>
              <p class="py-5">Subject</p>

              <input
                class="input w-75 py-1"
                type="email"
                placeholder=" Enter Subject"
                name="email"
              />
            </div>
            <div>
              <p class="py-5">Message</p>

              <textarea
                class="input w-75"
                placeholder="Message"
                name="message"
              />
            </div>
            <input type="hidden" name="_captcha" value="false" />
            <button class="submit py-2 px-12 my-10 manrope-Bold-h5">
              Submit
            </button>
          </form>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
const whatsappLink = "https://wa.me/9731837215";
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
  background-image: url("images/meteor.png");
  background-size: cover;
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

/* From Uiverse.io by SSpisso */
.input {
  background-color: #383838;
  border: 1ex solid none;
  border-top-width: 1.7em;
  margin: 0;
  padding: 0;
  color: #383838;
  word-wrap: break-word;
  outline: 7px solid #383838;
  font-size: 17px;
  text-align: center;
  transition: all 0.5s;
  font-weight: bold;
  font-family: "Courier New", Courier, monospace;
}

.input:hover {
  border-top-width: 0.2em;
  background-color: #f1e8e8;
}

.input:focus {
  border-top-width: 0.2em;
  background-color: #f1e8e8;
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
</style>
