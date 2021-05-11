<template>
  <div class="container">
    <h1>Legolize</h1>
    <div class="row show-grid">
      <div class="col-12">
        <upload-image />
      </div>
    </div>
    <div class="row show-grid justify-content-between">
      <div class="col-5">
        <input-image />
      </div>
      <div class="col-5">
        <img
          class="img-fluid"
          alt="input"
          src="https://fakeimg.pl/440x230/282828/eae0d0/?retina=1&text=Output"
        />
      </div>
      {{ name }}
    </div>
  </div>
</template>

<script>
import { setUrl } from '@/store/helpers';
import { eventBus } from '@/store/eventBus';
import UploadImage from '@/components/UploadImage.vue'
import InputImage from './components/InputImage.vue';

export default {
  components: { UploadImage, InputImage },
  data() {
    return {
      name : 'toto'
    }
  },
  async created() {
    const configRes = await fetch("config.json").catch(e => console.error('error', e));
    const configJson = await configRes.json();
    setUrl(configJson.api_url.value);

    eventBus.$on('loaded', uid => this.name = uid);
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
