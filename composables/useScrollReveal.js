import { onMounted, onUnmounted } from "vue";

export const useScrollReveal = () => {
  let observer;

  onMounted(() => {
    observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");

            // if this heading declares an accent color, apply it globally
            const accent = entry.target.dataset.accent;
            if (accent) {
              document.documentElement.style.setProperty(
                "--accent-color",
                accent,
              );
            }
          } else {
            entry.target.classList.remove("is-visible");
          }
        });
      },
      {
        threshold: 0.35,
      },
    );

    document.querySelectorAll(".scroll-heading").forEach((element) => {
      observer.observe(element);
    });
  });

  onUnmounted(() => {
    observer?.disconnect();
  });
};
