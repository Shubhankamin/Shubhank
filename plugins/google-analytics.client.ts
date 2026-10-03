export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig();
  const measurementId = config.public.googleAnalyticsId;

  if (!measurementId) return;

  // Create dataLayer before loading Google Analytics
  window.dataLayer = window.dataLayer || [];

  window.gtag = function (...args: any[]) {
    window.dataLayer.push(args);
  };

  // Initialize Google Analytics
  window.gtag("js", new Date());

  window.gtag("config", measurementId, {
    send_page_view: false,
    debug_mode: true,
  });

  // Load Google Analytics script
  const script = document.createElement("script");

  script.async = true;
  script.src = `https://www.googletagmanager.com/gtag/js?id=${measurementId}`;

  document.head.appendChild(script);

  // Initial page view
  window.gtag("event", "page_view", {
    page_title: document.title,
    page_location: window.location.href,
    page_path: window.location.pathname,
  });

  // Track Nuxt route changes
  const router = useRouter();

  router.afterEach((to) => {
    window.gtag("event", "page_view", {
      page_title: document.title,
      page_location: window.location.origin + to.fullPath,
      page_path: to.fullPath,
    });
  });
});
