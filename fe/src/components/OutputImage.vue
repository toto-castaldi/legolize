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
      const eventData = JSON.parse(event.data);
      switch (eventData.action) {
        case 'size' : this.dimension = eventData; break;
        case 'point' : document.getElementById(`${eventData.x+1}-${eventData.y+1}`).style.backgroundColor = `rgba(${eventData.color[0]},${eventData.color[1]},${eventData.color[2]},${eventData.color[3]})`; break;
        case 'palette' : document.getElementById(`${eventData.x+1}-${eventData.y+1}`).style.backgroundColor = `rgba(${eventData.color[0]},${eventData.color[1]},${eventData.color[2]},${eventData.color[3]})`; break;
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