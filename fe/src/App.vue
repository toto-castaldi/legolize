<template>
  <div class="container">
    <h1>Legolize</h1>
    <div v-if="this.step >= 1" class="row show-grid">
      <div class="col-12">
        <upload-image v-bind:current="step == 1" />
      </div>
    </div>
    <div v-if="this.step >= 2" class="row show-grid">
      <div class="col-12">
        <input-image v-bind:uid="uid" v-bind:current="step == 2" />
      </div>
    </div>
    <div v-if="step >= 3" class="row show-grid">
      <div class="col-12">
        <output-image v-bind:uid="uid" v-bind:current="step == 3"/>
      </div>
    </div>
  </div>
</template>

<script>
import { setUrl } from '@/store/helpers';
import { eventBus } from "@/store/eventBus";
import UploadImage from '@/components/UploadImage.vue'
import InputImage from './components/InputImage.vue';
import OutputImage from './components/OutputImage.vue';

export default {
  components: { UploadImage, InputImage, OutputImage },
  data() {
    return {
        uid : undefined,
        step : 1
    }
  },
  async created() {
    const configRes = await fetch("config.json").catch(e => console.error('error', e));
    const configJson = await configRes.json();
    setUrl(configJson.api_url.value);

    eventBus.$on('loaded', uid => {
      this.uid = uid;
      this.step = 2;
    });

    eventBus.$on('back', () => {
      this.step --;
    });

    eventBus.$on('next', () => {
      this.step ++;
      setTimeout(() => {
        window.scrollTo(0,document.body.scrollHeight);
      }, 0)
    });
  }
};


</script>

<style scoped>
.show-grid {
  margin-bottom: 15px;
}
.show-grid [class^="col-"] {
  padding-top: 10px;
  padding-bottom: 10px;
  background-color: rgba(156, 37, 156, 0.15);
  border: 1px solid rgba(156, 37, 156, 0.15);
}
</style>
