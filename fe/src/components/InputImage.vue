<template>
  <img
          class="img-fluid"
          alt="input"
          :src="imageSrc"
        />
</template>

<script>
import { eventBus } from '@/store/eventBus';
import { apiInputImage } from '@/store/helpers';


export default {
  data() {
    return {
      imageSrc: "https://fakeimg.pl/440x230/282828/eae0d0/?retina=1&text=Input",
    };
  },
  created() {
    eventBus.$on('loaded', uid => this.imageSrc = apiInputImage(uid));
  }

};
</script>