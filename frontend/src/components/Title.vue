<template>
  <div id="nar">
  <b-navbar toggleable="lg" type="dark" variant="primary">
    <img class="logo" src="../assets/clapperboard.png" alt="logo">
    <b-navbar-brand href="/">Movie Search</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <router-link to="/member">Members</router-link>
        <router-link to="/search">search</router-link>
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

.nav {
  
}

.logo {
  margin-right: 10px;
}
</style>
