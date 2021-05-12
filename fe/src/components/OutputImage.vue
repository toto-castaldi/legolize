<template>
  <img
          class="img-fluid"
          alt="input"
          :src="imageSrc"
        />
</template>

<script>
import { eventBus } from '@/store/eventBus';
import { get, apiOutpuImage } from "@/store/helpers";

export default {
  data() {
    return {
      imageSrc: "https://fakeimg.pl/440x230/282828/eae0d0/?retina=1&text=Output",
      uid : "",
      checkInterval : -1
    };
  },
  methods : {
    async checkOutputFinish() {
      const res = await get(`outputcheck/${this.uid}`);
      const json = await res.json();
      if (json.finished) {
        clearInterval(this.checkInterval);
        this.imageSrc =  apiOutpuImage(this.uid);
      }
    }
  },
  created() {
    eventBus.$on('loaded', uid => {
      this.imageSrc = "https://fakeimg.pl/440x230/282828/eae0d0/?retina=1&text=Loading....",
      this.uid = uid;
      this.checkInterval = setInterval(this.checkOutputFinish, 3000)
    });
  }

};
</script>