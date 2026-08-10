<template>
  <div class="resume-ai">
    <!-- Floating AI Button -->
    <button
      v-if="!isOpen"
      class="ai-trigger"
      aria-label="Open Shubhank AI"
      @click="openChat"
    >
      <span class="trigger-ring"></span>

      <span class="ai-symbol">✦</span>

      <span class="trigger-label">AI</span>
    </button>

    <!-- Chat Window -->
    <Transition name="chat">
      <div v-if="isOpen" class="chat-window">
        <!-- Header -->
        <div class="chat-header">
          <div class="header-left">
            <div class="ai-avatar">
              <span>✦</span>
            </div>

            <div>
              <h3>Shubhank AI</h3>
              <p>
                <span class="status-dot"></span>
                Resume Assistant
              </p>
            </div>
          </div>

          <button
            class="close-button"
            aria-label="Close chat"
            @click="closeChat"
          >
            ×
          </button>
        </div>

        <!-- Messages -->
        <div ref="messagesContainer" class="messages">
          <!-- Welcome -->
          <div v-if="messages.length === 0" class="welcome">
            <div class="welcome-icon">✦</div>

            <h2>Hey there.</h2>

            <p>
              I'm Shubhank's AI resume assistant. Ask me about his skills,
              experience, projects or education.
            </p>

            <!-- Suggested Questions -->
            <div class="suggestions">
              <button
                v-for="suggestion in suggestions"
                :key="suggestion"
                @click="sendMessage(suggestion)"
              >
                {{ suggestion }}
              </button>
            </div>
          </div>

          <!-- Chat Messages -->
          <div
            v-for="(message, index) in messages"
            :key="index"
            class="message-wrapper"
            :class="message.role"
          >
            <div class="message">
              {{ message.content }}
            </div>
          </div>

          <!-- Typing Indicator -->
          <div v-if="isTyping" class="message-wrapper assistant">
            <div class="typing">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        </div>

        <!-- Input -->
        <div class="input-area">
          <input
            v-model="input"
            type="text"
            placeholder="Ask about Shubhank..."
            @keydown.enter="handleEnter"
          />

          <button
            class="send-button"
            :disabled="!input.trim() || isTyping"
            aria-label="Send message"
            @click="sendMessage()"
          >
            ↑
          </button>
        </div>

        <div class="powered">
          <span>POWERED BY</span>
          <span class="powered-ai">SHUBHANK AI</span>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { nextTick, ref, watch, onBeforeUnmount } from "vue";
const isOpen = ref(false);
const input = ref("");
const isTyping = ref(false);

const sessionId = ref(localStorage.getItem("aura_session_id") || null);
const config = useRuntimeConfig();

const API_URL = config.public.apiBase;
const messages = ref([]);
const messagesContainer = ref(null);

const suggestions = [
  "What are your frontend skills?",
  "Tell me about your experience",
  "What projects have you built?",
  "What are you studying?",
];

const openChat = () => {
  isOpen.value = true;
};

const closeChat = () => {
  isOpen.value = false;
};

watch(isOpen, (open) => {
  if (typeof document === "undefined") return;

  if (open) {
    document.body.style.overflow = "hidden";
    document.body.style.touchAction = "none";
  } else {
    document.body.style.overflow = "";
    document.body.style.touchAction = "";
  }
});

onBeforeUnmount(() => {
  if (typeof document === "undefined") return;

  document.body.style.overflow = "";
  document.body.style.touchAction = "";
});

const scrollToBottom = async () => {
  await nextTick();

  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
  }
};

const sendMessage = async (suggestion = null) => {
  const message = suggestion || input.value.trim();

  if (!message || isTyping.value) {
    return;
  }

  messages.value.push({
    role: "user",
    content: message,
  });

  input.value = "";

  await scrollToBottom();

  isTyping.value = true;

  try {
    const response = await $fetch(`${API_URL}/chat`, {
      method: "POST",

      body: {
        message,
        session_id: sessionId.value,
      },
    });
    if (response.session_id) {
      sessionId.value = response.session_id;

      localStorage.setItem("aura_session_id", response.session_id);
    }

    messages.value.push({
      role: "assistant",
      content: response.answer,
    });
  } catch (error) {
    console.error("AURA API error:", error);

    messages.value.push({
      role: "assistant",
      content:
        "I couldn't connect to my knowledge system right now. Please try again in a moment.",
    });
  } finally {
    isTyping.value = false;

    await scrollToBottom();
  }
};

const handleEnter = () => {
  sendMessage();
};
</script>

<style scoped>
/* =========================================================
   CONTAINER
========================================================= */

.resume-ai {
  position: fixed;

  right: 28px;
  bottom: 28px;

  z-index: 9999;

  font-family: inherit;
}

/* =========================================================
   FLOATING BUTTON
========================================================= */

.ai-trigger {
  position: relative;

  width: 64px;
  height: 64px;

  border: 1px solid rgba(211, 245, 118, 0.35);

  border-radius: 50%;

  background:
    radial-gradient(
      circle at 35% 30%,
      rgba(211, 245, 118, 0.18),
      transparent 40%
    ),
    rgba(3, 7, 18, 0.92);

  color: #d3f576;

  display: flex;
  align-items: center;
  justify-content: center;

  cursor: pointer;

  backdrop-filter: blur(16px);

  box-shadow:
    0 0 25px rgba(211, 245, 118, 0.08),
    0 15px 45px rgba(0, 0, 0, 0.45);

  transition:
    transform 0.35s ease,
    border-color 0.35s ease,
    box-shadow 0.35s ease;
}

.ai-trigger:hover {
  transform: translateY(-5px) scale(1.05);

  border-color: rgba(211, 245, 118, 0.75);

  box-shadow:
    0 0 30px rgba(211, 245, 118, 0.18),
    0 20px 55px rgba(0, 0, 0, 0.5);
}

.ai-symbol {
  font-size: 22px;

  line-height: 1;

  text-shadow:
    0 0 10px rgba(211, 245, 118, 0.8),
    0 0 25px rgba(211, 245, 118, 0.35);
}

.trigger-label {
  position: absolute;

  right: -4px;
  bottom: -3px;

  width: 22px;
  height: 22px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 50%;

  background: #d3f576;

  color: #030712;

  font-size: 9px;
  font-weight: 800;

  letter-spacing: 0.05em;
}

.trigger-ring {
  position: absolute;

  inset: -8px;

  border: 1px solid rgba(211, 245, 118, 0.08);

  border-radius: 50%;

  animation: pulseRing 2.5s ease-in-out infinite;
}

@keyframes pulseRing {
  50% {
    transform: scale(1.12);

    opacity: 0.25;
  }
}

/* =========================================================
   CHAT WINDOW
========================================================= */

.chat-window {
  width: min(390px, calc(100vw - 32px));
  height: min(600px, calc(100vh - 40px));

  display: flex;
  flex-direction: column;

  overflow: hidden;

  border: 1px solid rgba(255, 255, 255, 0.1);

  border-radius: 28px;

  background: linear-gradient(
    145deg,
    rgba(10, 17, 32, 0.97),
    rgba(3, 7, 18, 0.98)
  );

  backdrop-filter: blur(25px);

  box-shadow:
    0 30px 100px rgba(0, 0, 0, 0.65),
    0 0 50px rgba(211, 245, 118, 0.04);

  position: relative;
  overflow: hidden;
}

/* Blue / lime atmosphere */

.chat-window::before {
  content: "";

  position: absolute;

  width: 250px;
  height: 250px;

  top: -180px;
  right: -100px;

  background: radial-gradient(
    circle,
    rgba(59, 130, 246, 0.15),
    transparent 70%
  );

  filter: blur(30px);

  pointer-events: none;
}

/* =========================================================
   HEADER
========================================================= */

.chat-header {
  position: relative;

  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: 18px 20px;

  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
}

.header-left {
  display: flex;
  align-items: center;

  gap: 12px;
}

.ai-avatar {
  width: 40px;
  height: 40px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 13px;

  background: linear-gradient(
    135deg,
    rgba(211, 245, 118, 0.18),
    rgba(59, 130, 246, 0.16)
  );

  border: 1px solid rgba(211, 245, 118, 0.2);

  color: #d3f576;

  font-size: 18px;

  box-shadow: 0 0 20px rgba(211, 245, 118, 0.08);
}

.header-left h3 {
  margin: 0;

  color: white;

  font-size: 14px;

  font-weight: 700;

  letter-spacing: 0.02em;
}

.header-left p {
  display: flex;
  align-items: center;

  gap: 6px;

  margin: 3px 0 0;

  color: rgba(255, 255, 255, 0.38);

  font-size: 9px;

  letter-spacing: 0.08em;

  text-transform: uppercase;
}

.status-dot {
  width: 5px;
  height: 5px;

  border-radius: 50%;

  background: #d3f576;

  box-shadow: 0 0 8px rgba(211, 245, 118, 0.8);
}

.close-button {
  width: 32px;
  height: 32px;

  border: 1px solid rgba(255, 255, 255, 0.08);

  border-radius: 50%;

  background: rgba(255, 255, 255, 0.03);

  color: rgba(255, 255, 255, 0.6);

  font-size: 20px;

  line-height: 1;

  cursor: pointer;

  transition:
    background 0.25s ease,
    color 0.25s ease;
}

.close-button:hover {
  background: rgba(255, 255, 255, 0.08);

  color: white;
}

/* =========================================================
   MESSAGES
========================================================= */

.messages {
  flex: 1;

  overflow-y: auto;

  padding: 22px 18px;

  scrollbar-width: thin;

  scrollbar-color: rgba(211, 245, 118, 0.2) transparent;
}

.messages::-webkit-scrollbar {
  width: 4px;
}

.messages::-webkit-scrollbar-thumb {
  background: rgba(211, 245, 118, 0.2);

  border-radius: 10px;
}

/* =========================================================
   WELCOME
========================================================= */

.welcome {
  min-height: 100%;

  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: center;

  text-align: center;

  padding: 20px;
}

.welcome-icon {
  width: 54px;
  height: 54px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 18px;

  color: #d3f576;

  font-size: 24px;

  background: linear-gradient(
    135deg,
    rgba(211, 245, 118, 0.12),
    rgba(59, 130, 246, 0.1)
  );

  border: 1px solid rgba(211, 245, 118, 0.15);

  box-shadow: 0 0 35px rgba(211, 245, 118, 0.06);

  margin-bottom: 18px;
}

.welcome h2 {
  margin: 0;

  color: white;

  font-size: 25px;

  font-weight: 700;
}

.welcome p {
  max-width: 300px;

  margin: 10px 0 24px;

  color: rgba(255, 255, 255, 0.45);

  font-size: 12px;

  line-height: 1.7;
}

/* =========================================================
   SUGGESTIONS
========================================================= */

.suggestions {
  display: flex;

  flex-direction: column;

  width: 100%;

  gap: 8px;
}

.suggestions button {
  width: 100%;

  padding: 11px 14px;

  border: 1px solid rgba(255, 255, 255, 0.08);

  border-radius: 12px;

  background: rgba(255, 255, 255, 0.025);

  color: rgba(255, 255, 255, 0.6);

  font-size: 11px;

  text-align: left;

  cursor: pointer;

  transition:
    border-color 0.25s ease,
    background 0.25s ease,
    color 0.25s ease,
    transform 0.25s ease;
}

.suggestions button:hover {
  transform: translateX(4px);

  border-color: rgba(211, 245, 118, 0.25);

  background: rgba(211, 245, 118, 0.05);

  color: #d3f576;
}

/* =========================================================
   MESSAGE
========================================================= */

.message-wrapper {
  display: flex;

  margin-bottom: 12px;
}

.message-wrapper.user {
  justify-content: flex-end;
}

.message-wrapper.assistant {
  justify-content: flex-start;
}

.message {
  max-width: 82%;

  padding: 11px 14px;

  border-radius: 16px;

  font-size: 12px;

  line-height: 1.65;
}

.user .message {
  border-bottom-right-radius: 5px;

  background: #d3f576;

  color: #030712;

  font-weight: 500;
}

.assistant .message {
  border-bottom-left-radius: 5px;

  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.055),
    rgba(255, 255, 255, 0.025)
  );

  border: 1px solid rgba(255, 255, 255, 0.07);

  color: rgba(255, 255, 255, 0.72);
}

/* =========================================================
   TYPING
========================================================= */

.typing {
  display: flex;

  align-items: center;

  gap: 4px;

  padding: 13px 15px;

  border-radius: 16px;

  border-bottom-left-radius: 5px;

  background: rgba(255, 255, 255, 0.04);

  border: 1px solid rgba(255, 255, 255, 0.07);
}

.typing span {
  width: 5px;
  height: 5px;

  border-radius: 50%;

  background: #d3f576;

  animation: typing 1.2s infinite ease-in-out;
}

.typing span:nth-child(2) {
  animation-delay: 0.15s;
}

.typing span:nth-child(3) {
  animation-delay: 0.3s;
}

@keyframes typing {
  0%,
  60%,
  100% {
    transform: translateY(0);

    opacity: 0.35;
  }

  30% {
    transform: translateY(-4px);

    opacity: 1;
  }
}

/* =========================================================
   INPUT
========================================================= */

.input-area {
  display: flex;

  align-items: center;

  gap: 8px;

  margin: 0 14px;

  padding: 7px 7px 7px 14px;

  border: 1px solid rgba(255, 255, 255, 0.08);

  border-radius: 15px;

  background: rgba(255, 255, 255, 0.035);
}

.input-area input {
  flex: 1;

  min-width: 0;

  border: none;

  outline: none;

  background: transparent;

  color: white;

  font-size: 12px;
}

.input-area input::placeholder {
  color: rgba(255, 255, 255, 0.28);
}

.send-button {
  width: 34px;
  height: 34px;

  flex-shrink: 0;

  border: none;

  border-radius: 10px;

  background: #d3f576;

  color: #030712;

  font-size: 17px;

  font-weight: 700;

  cursor: pointer;

  transition:
    transform 0.25s ease,
    opacity 0.25s ease;
}

.send-button:hover:not(:disabled) {
  transform: translateY(-2px) scale(1.04);
}

.send-button:disabled {
  opacity: 0.25;

  cursor: not-allowed;
}

/* =========================================================
   POWERED
========================================================= */

.powered {
  display: flex;
  justify-content: center;
  gap: 5px;

  padding: 10px;

  color: rgba(255, 255, 255, 0.2);

  font-family: monospace;

  font-size: 7px;

  letter-spacing: 0.12em;
}

.powered-ai {
  color: rgba(211, 245, 118, 0.4);
}

/* =========================================================
   OPEN / CLOSE ANIMATION
========================================================= */

.chat-enter-active,
.chat-leave-active {
  transition:
    opacity 0.3s ease,
    transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.chat-enter-from,
.chat-leave-to {
  opacity: 0;

  transform: translateY(20px) scale(0.92);
}

/* =========================================================
   MOBILE
========================================================= */

/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 600px) {
  .resume-ai {
    right: 16px;
    bottom: 16px;
    z-index: 99999;
  }

  /* Floating button */

  .ai-trigger {
    width: 58px;
    height: 58px;
  }

  /* Chat window */

  .chat-window {
    width: calc(100vw - 32px);

    /*
      Don't use almost the entire viewport height.
      Keep it as a compact bottom-sheet style chat.
    */
    height: min(560px, 72dvh);

    min-height: 420px;

    max-height: 72dvh;

    border-radius: 22px;

    /*
      Keep the chat above the bottom edge.
    */
    margin-bottom: 0;

    /*
      Prevent the chat itself from moving with
      the document.
    */
    position: fixed;

    right: 16px;
    bottom: 16px;

    /*
      Make sure only the messages area scrolls.
    */
    overscroll-behavior: contain;
    touch-action: pan-y;
  }

  /*
    The messages area is the ONLY scrollable
    area inside the chatbot.
  */

  .messages {
    min-height: 0;
    overscroll-behavior: contain;
    -webkit-overflow-scrolling: touch;
    touch-action: pan-y;
  }

  /*
    Slightly reduce spacing on small screens.
  */

  .chat-header {
    padding: 15px 16px;
  }

  .messages {
    padding: 18px 14px;
  }

  .input-area {
    margin: 0 12px;
  }

  .powered {
    padding: 8px;
  }
}

@media (max-width: 380px) {
  .chat-window {
    width: calc(100vw - 24px);
    right: 12px;
    bottom: 12px;

    height: 68dvh;
    max-height: 520px;
    min-height: 380px;

    border-radius: 20px;
  }

  .resume-ai {
    right: 12px;
    bottom: 12px;
  }

  .message {
    max-width: 88%;
    font-size: 11px;
  }

  .welcome h2 {
    font-size: 22px;
  }

  .welcome p {
    font-size: 11px;
  }
}

/* =========================================================
   REDUCED MOTION
========================================================= */

@media (prefers-reduced-motion: reduce) {
  .trigger-ring,
  .typing span {
    animation: none;
  }

  .chat-enter-active,
  .chat-leave-active {
    transition: none;
  }
}
</style>
