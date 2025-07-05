// src/audioManager.js

class AudioManager {
  constructor() {
    this.audio = new Audio(require('@/assets/Pokémon_ Ruby, Sapphire  Emerald - Pokémon Center (Stereo).mp3'));
    this.audio.loop = true;
    this.isInitialized = false;
  }

  play() {
    if (!this.audio) return;
    this.audio.currentTime = 0;
    this.audio.play().catch(err => {
      console.warn("Audio playback failed:", err);
    });
    this.isInitialized = true;
  }

  pause() {
    if (!this.audio) return;
    this.audio.pause();
  }

  stop() {
    if (!this.audio) return;
    this.audio.pause();
    this.audio.currentTime = 0;
  }

  isPlaying() {
    return this.audio && !this.audio.paused;
  }
}

export default new AudioManager(); // Singleton instance
