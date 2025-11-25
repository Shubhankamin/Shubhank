import vuetify, { transformAssetUrls } from "vite-plugin-vuetify";

export default defineNuxtConfig({
  css: ["vuetify/styles", "@/assets/css/style.css"],
  build: { transpile: ["vuetify"] },
  modules: ["nuxt-aos", "nuxt-simple-sitemap", "@nuxtjs/robots"],

  sitemap: {},

  vite: {
    vue: { template: { transformAssetUrls } },
    plugins: [vuetify({ autoImport: true })],
  },

  compatibilityDate: "2025-11-24",
});
