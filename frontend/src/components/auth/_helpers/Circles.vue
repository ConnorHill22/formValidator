<template>
  <div id = "circles">
      <span class = "active circle"></span>
      <span v-bind:class="{ active: twoActive }" class = "circle"></span>
      <span  v-bind:class="{ active: threeActive }" class = "circle"></span>
  </div>
</template>

<script>
export default {
    name: "Circles",
    props: {
        solid_green: Number
    },
    computed: {
        twoActive: function () {
            return this.solid_green == 2 || this.solid_green == 3 ? true : false;
        },
        threeActive: function () {
            return this.solid_green ==3 ? true : false;
        }
    }

}
</script>

<style lang="scss" scoped>
#circles {
    display: grid;
    grid-template-columns: 20% 20% 20%;
    grid-template-rows: auto; 
    width: 100%;
    justify-content: center;
    justify-items: center;	
    //align-content: center;
}

.active {
    background-color: var(--primary-color);
}
.circle {
  height: 25px;
  width: 25px;
  border-radius: 50%;
  border: var(--primary-color) solid 2px;
  display: inline-block;
}

</style>