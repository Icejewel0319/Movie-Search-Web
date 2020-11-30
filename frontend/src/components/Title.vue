<template>
  <div id="nar">
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <img class="logo" src="../assets/clapperboard.png" alt="logo">
    <b-navbar-brand href="/">Movie Search</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav >
        <router-link to="/searchActor" class="link">Actor </router-link>
        <router-link to="/searchMovie" class="link">Movie Title </router-link>
        <router-link to="/searchYear" class="link">Released Year </router-link>
        <router-link to="/member" class="link">Members </router-link>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <b-button variant="link" href="https://github.com/Icejewel0319/Movie-Search-Web">
        <img src="../assets/GitHub-Mark-32px.png" alt="Github">
        </b-button>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.link {
  color: white;
  margin-right: 20px;
}

.logo {
  margin-right: 10px;
}
</style>
