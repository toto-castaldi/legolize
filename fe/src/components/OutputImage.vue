<template>
  <div v-bind:class="{ 'bg-light': current }" class="mb-3">
    <legend>Result : {{state}}</legend>
    <div class="mb-3" v-if="dimension">
      <canvas id="the-canvas" v-bind:width="dimension['w']*64" v-bind:height="dimension['h']*64">
      </canvas>
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
      state : 'Loading',
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
      const getCtx = () => {
        const canvas = document.getElementById('the-canvas');
        return canvas.getContext('2d');
      }
      
      const eventData = JSON.parse(event.data);
      switch (eventData.action) {
        case 'size' : {
          this.state = 'Dimension';
          this.dimension = eventData; 
          break;
        }
        case 'point' : {
          this.state = 'Clusterization';
          const ctx = getCtx();
          ctx.fillStyle = `rgba(${eventData.color[0]},${eventData.color[1]},${eventData.color[2]},${eventData.color[3]})`;
          ctx.fillRect(eventData.x * 64, eventData.y * 64, 64, 64);
          break;
        }
        case 'palette' : {
          this.state = 'Apply palette';
          const ctx = getCtx();
          ctx.fillStyle = `rgba(${eventData.color[0]},${eventData.color[1]},${eventData.color[2]},${eventData.color[3]})`;
          ctx.fillRect(eventData.x * 64, eventData.y * 64, 64, 64);
          break;
        }  
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
canvas {
  border: 1px solid black;
}
</style>