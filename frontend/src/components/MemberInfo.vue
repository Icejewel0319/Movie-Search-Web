<template>
  <b-card
    :title="memberInfo.name"
    :img-src="memberInfo.img"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      {{memberInfo.intro}}
    </b-card-text>

    <b-button variant="link" :href="memberInfo.github">
        <img src="../assets/GitHub-Mark-32px.png" alt="Github">
    </b-button>
  </b-card>

</template>

<script>
export default {
  name: 'member',
  props: {
    memberInfo: Object,
  },
  data() {
    return {
      
    }
  },
  methods: {
    
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
