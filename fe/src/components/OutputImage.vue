<template>
  <div v-bind:class="{ 'bg-light': current }" class="mb-3">
    <legend>Result</legend>
    <div class="mb-3" v-if="dimension">
      <div class="row" v-for="y in dimension['h']" :key="y">
        <div :id="x + '-' + y" class="el" v-for="x in dimension['w']" :key="x">
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <button
          type="submit"
          :disabled="!current"
          @click="back()"
          class="btn btn-primary"
        >
          back
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { websocketUrl } from "@/store/helpers";
import { eventBus } from "@/store/eventBus";

export default {
  props: ["uid", "current", "size"],
  data() {
    return {
      connection: undefined,
      dimension: undefined,
    };
  },
  methods: {
    back() {
      if (this.connection) {
        this.connection.close();
      }
      eventBus.$emit("back", {});
    },
    startGeneration: function () {
      this.connection.send(JSON.stringify({ uid: this.uid, size: this.size }));
    },
  },
  destroyed() {
    if (this.connection) {
      this.connection.close();
    }
  },
  created() {
    this.connection = new WebSocket(websocketUrl("fullgenerate"));

    this.connection.onopen = () => {
      this.startGeneration();
    };

    this.connection.onmessage = (event) => {
      if (this.dimension == undefined) {
        this.dimension = JSON.parse(event.data);
      } else {
        const el = JSON.parse(event.data);
        document.getElementById(`${el.x+1}-${el.y+1}`).style.backgroundColor = `rgba(${el.color[0]},${el.color[1]},${el.color[2]},${el.color[3]})`;
      }
    };
  },
};
</script>
<style scoped>
div.el {
  border: 1px solid black;
  display: inline-block;
  width: 20px;
  height: 20px;
}
</style>