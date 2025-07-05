<template>
  <audio ref="player" loop>
    <source src="@/assets/Pokémon_ Ruby, Sapphire  Emerald - Pokémon Center (Stereo).mp3" type="audio/mp3" />
    Your browser does not support the audio element.
  </audio>
</template>

<script>
export default {
  name: 'AudioPlayer',
};
</script>

<style scoped>
audio {
  display: none; /* Hide the audio element but keep it functional */
}
</style>
