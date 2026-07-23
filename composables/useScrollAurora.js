import { onMounted, onUnmounted } from "vue";

export const useScrollAurora = () => {
  let ticking = false;

  const sectionConfigs = [
    { id: "hero", x: "15%", y: "20%", colors: "59,130,246|132,204,22" }, // blue/green top-left
    { id: "work", x: "70%", y: "30%", colors: "132,204,22|59,130,246" }, // green center-right
    { id: "specialize", x: "50%", y: "50%", colors: "147,51,234|132,204,22" }, // purple/green
    { id: "skills", x: "40%", y: "60%", colors: "132,204,22|59,130,246" }, // tight green
    { id: "about", x: "50%", y: "70%", colors: "59,130,246|147,51,234" }, // large soft blue/purple
    { id: "connect", x: "50%", y: "85%", colors: "132,204,22|147,51,234" },
  ];

  const updateAurora = () => {
    const viewportCenter = window.innerHeight / 2;
    let closest = null;
    let closestDist = Infinity;

    sectionConfigs.forEach((config) => {
      const el = document.getElementById(config.id);
      if (!el) return;

      const rect = el.getBoundingClientRect();
      const sectionCenter = rect.top + rect.height / 2;
      const dist = Math.abs(sectionCenter - viewportCenter);

      if (dist < closestDist) {
        closestDist = dist;
        closest = config;
      }
    });

    if (closest) {
      const root = document.documentElement.style;
      root.setProperty("--aurora-x", closest.x);
      root.setProperty("--aurora-y", closest.y);
      root.setProperty("--aurora-color-1", closest.colors.split("|")[0]);
      root.setProperty("--aurora-color-2", closest.colors.split("|")[1]);
    }

    ticking = false;
  };

  const handleScroll = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(updateAurora);
  };

  onMounted(() => {
    updateAurora(); // set initial position on load
    window.addEventListener("scroll", handleScroll, { passive: true });
  });

  onUnmounted(() => {
    window.removeEventListener("scroll", handleScroll);
  });
};
