<template>

  <div id="member" class="container">
    <b-row>
      <b-col><MemberInfoCom :memberInfo="Hao"/></b-col>
      <b-col><MemberInfoCom :memberInfo="Siyuan"/></b-col>
      <b-col><MemberInfoCom :memberInfo="Xin"/></b-col>
    </b-row>
  
  
  
  </div>
</template>

<script>
import MemberInfoCom from './MemberInfo'
export default {
  name: 'member',
  components :{ MemberInfoCom },
  props: {
    
  },
  data() {
    return {
      Hao:{
        name: "Hao Yang",
        github: "https://github.com/HaoYang980424",
        img:"https://avatars0.githubusercontent.com/u/49030962?s=460&v=4",
        intro: "Master student in the Applied Data Science Program. He has experience in Java, Python, and C#, has worked on projects like machine learning algorithms and graduate school recommendation systems."
      },
      Siyuan:{
        name: "Siyuan Lin",
        github: "https://github.com/Icejewel0319",
        img:"https://avatars1.githubusercontent.com/u/26959390?s=460&u=9f7205f05c1f2e3e6ce381c66e3ea0921a26103a&v=4",
        intro:"Master student in the Scientists and Engineers Program. She has experience in web technologies, like Node.js, React, and big data technologies"
      },
      Xin:{
        name: "Xin Wen",
        github: "https://github.com/wenx9308",
        img:"https://avatars0.githubusercontent.com/u/15935966?s=460&u=faf5847da2b158b1e9a18c1592b64228f1df196d&v=4",
        intro: "Master student in the Applied Data Science Program. She has experience in python, SQL, data retrieval, data cleaning and statistics."
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #member {
    margin-top: 30px;
  }
</style>
