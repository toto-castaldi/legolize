<template>
  <div v-bind:class="{ 'bg-light': current }" class="mb-3">
    <legend>Result : {{state}}</legend>
    <div id="canvas-container" class="mb-3" >
      <canvas id="the-canvas" >
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
      paletteRects : [],
      tileDimension : 8,
      palette : {}
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

    this.connection.onmessage =  (event) => {
      const getCtx = () => {
        const canvas = document.getElementById('the-canvas');
        return canvas.getContext('2d');
      }

     
      const eventData = JSON.parse(event.data);
      switch (eventData.action) {
        case 'size' : {
          this.state = 'Dimension';

          const canvas = document.getElementById('the-canvas');
          
          const tileY = canvas.clientHeight / eventData.h;
          const tileX = canvas.clientWidth / eventData.w;

          canvas.height = canvas.clientHeight;
          canvas.width = canvas.clientWidth;

          if (tileX < tileY) {
            this.tileDimension = Math.floor(tileX);
          } else {
            this.tileDimension = Math.floor(tileY);
          }

          break;
        }
        case 'point' : {
          this.state = 'Clusterization';
          const ctx = getCtx();
          ctx.fillStyle = `rgba(${eventData.color[0]},${eventData.color[1]},${eventData.color[2]},${eventData.color[3]})`;
          ctx.fillRect(eventData.x * this.tileDimension, eventData.y * this.tileDimension, this.tileDimension, this.tileDimension);
          break;
        }
        case 'palette' : {
          this.state = 'Apply palette';
          const ctx = getCtx();
          ctx.fillStyle = `rgba(${eventData.color[0]},${eventData.color[1]},${eventData.color[2]},${eventData.color[3]})`;
          ctx.fillRect(eventData.x * this.tileDimension, eventData.y * this.tileDimension, this.tileDimension, this.tileDimension);
          this.paletteRects.push({ x : eventData.x, y: eventData.y, paletteId : eventData.palette_id });
          this.palette[eventData.palette_id] = eventData.palette_img;
          break;
        }  
        case 'end' : {
          console.log(this.palette);
          this.state = 'Lego points';
          /* for (const p of this.paletteRects) {
            const id = p.id;
            const x = p.x;
            const y = p.y;
            if (imagePalete[id] === undefined) {
              console.log(id,x,y)
            }
          } */
          
          break;
        }  
      }
    };
  },
};
</script>
<style scoped>
canvas {
	height: 100%; 
  width: 100%;
}
</style>