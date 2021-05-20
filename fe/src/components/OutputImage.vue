<template>
  <div v-bind:class="{ 'bg-light': current }" class="mb-3">
    <legend>Result : {{state}}</legend>
    <div id="canvas-container" class="mb-3" >
      <canvas id="the-canvas" >
      </canvas>
    </div>
    {{pieces}}
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
      palette : {},
      piecesTemp : {},
      pieces : undefined,
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
          if (!this.palette[eventData.palette_id]) {
            const image = new Image();
            image.src = "data:image/png;base64," + eventData.palette_img;
            this.palette[eventData.palette_id] = image;
          }
          break;
        }  
        case 'endPalette' : {
          this.state = 'Lego points';
          const ctx = getCtx();
          ctx.scale(this.tileDimension / 62, this.tileDimension / 62);
          for (const p of this.paletteRects) {
            const paletteId = p.paletteId;
            const x = p.x;
            const y = p.y;
            ctx.drawImage(this.palette[paletteId], x * 62 , y * 62);
          }
          
          break;
        }  
        case 'piece' : {
          this.state = 'Pieces';
          const ctx = getCtx();
          ctx.fillStyle = `rgba(0,0,0,0.7)`;
          ctx.fillRect(eventData.position[0] * 62, eventData.position[1] * 62, eventData.size[0] * 62, eventData.size[1] * 62);
          const keySize = `${eventData.size[0]}x${eventData.size[1]}`;
          const keyColor = `${eventData.color[0]}-${eventData.color[1]}-${eventData.color[2]}-${eventData.color[3]}`;
          if (!this.piecesTemp[keySize]) this.piecesTemp[keySize] = {};
          if (!this.piecesTemp[keySize][keyColor]) this.piecesTemp[keySize][keyColor] = 0;
          this.piecesTemp[keySize][keyColor] ++;
          break;
        }

        case 'endPiece' : {
          this.pieces = this.piecesTemp;

          const ctx = getCtx();

          for (const p of this.paletteRects) {
            const paletteId = p.paletteId;
            const x = p.x;
            const y = p.y;
            ctx.drawImage(this.palette[paletteId], x * 62 , y * 62);
          }
          this.paletteRects = []; //clear memory 
          this.palette = {}; //clear memory 
          
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