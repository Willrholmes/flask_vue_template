<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Hello></Hello>
    <Hello2></Hello2>
  </div>
</template>

<script>
import Hello from './components/Hello.vue';
import Hello2 from './components/Hello2.vue';

export default {
  name: 'app',
  components: {
    Hello,
    Hello2,
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
