<template>
  <component :is="layout">
    <router-view/>
  </component>
</template>


<script>
  import EmptyLayout from '@/layouts/EmptyLayout';

  export default {
    computed: {
      layout() {
        return (this.$route.meta.layout || 'empty-layout')
      }
    },
    components: {
      EmptyLayout,
    }
  }
</script>


<style>
/* Сюда вставляем css */
@import "bootstrap/dist/css/bootstrap.min.css";
@import "bootstrap";

@import 'assets/css/index.css';
</style>
