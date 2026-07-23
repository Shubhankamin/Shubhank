import { onMounted, onUnmounted, ref } from "vue";

export const useMouseFollower = () => {
  const followerX = ref(0);
  const followerY = ref(0);

  let mouseX = 0;
  let mouseY = 0;
  let rafId;

  const handleMouseMove = (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  };

  const animate = () => {
    // ease toward the real cursor position instead of snapping to it
    followerX.value += (mouseX - followerX.value) * 0.12;
    followerY.value += (mouseY - followerY.value) * 0.12;

    document.documentElement.style.setProperty(
      "--follower-x",
      `${followerX.value}px`,
    );
    document.documentElement.style.setProperty(
      "--follower-y",
      `${followerY.value}px`,
    );

    rafId = requestAnimationFrame(animate);
  };

  onMounted(() => {
    window.addEventListener("mousemove", handleMouseMove, { passive: true });
    rafId = requestAnimationFrame(animate);
  });

  onUnmounted(() => {
    window.removeEventListener("mousemove", handleMouseMove);
    cancelAnimationFrame(rafId);
  });
};
