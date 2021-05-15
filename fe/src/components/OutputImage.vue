<template>
  <div>
    <legend>Result</legend>
    <div class="mb-3">
      <img class="img-fluid" alt="input" :src="imageSrc" />
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
import { get, apiOutpuImage } from "@/store/helpers";
import { eventBus } from "@/store/eventBus";


export default {
  props: ["uid", "current"],
  data() {
    return {
      imageSrc:
        "https://fakeimg.pl/440x230/282828/eae0d0/?retina=1&text=Loading",
      checkInterval: -1,
    };
  },
  methods: {
    back() {
      if (this.checkInterval > -1) {
        clearInterval(this.checkInterval);
      }
      eventBus.$emit("back", {});
    },
    async checkOutputFinish() {
      const res = await get(`outputcheck/${this.uid}`);
      const json = await res.json();
      if (json.finished) {
        clearInterval(this.checkInterval);
        this.imageSrc = apiOutpuImage(this.uid);
      }
    },
  },
  created() {
    this.checkInterval = setInterval(this.checkOutputFinish, 3000);
  },
};
</script>