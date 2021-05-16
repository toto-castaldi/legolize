<template>

  <div class="d-flex flex-column h-100">
    <nav-bar />
    <div class="container">
      <div v-if="this.step >= 1" class="row">
        <div class="col-12">
          <upload-image v-bind:current="step == 1" />
        </div>
      </div>
      <div v-if="this.step >= 2" class="row">
        <div class="col-12">
          <input-image v-bind:uid="uid" v-bind:current="step == 2" />
        </div>
      </div>
      <div v-if="step >= 3" class="row">
        <div class="col-12">
          <output-image v-bind:uid="uid" v-bind:current="step == 3" />
        </div>
      </div>
    </div>
    <bottom-bar />
  </div>
</template>

<script>
import { setUrl } from "@/store/helpers";
import { eventBus } from "@/store/eventBus";
import UploadImage from "@/components/UploadImage.vue";
import InputImage from "./components/InputImage.vue";
import OutputImage from "./components/OutputImage.vue";
import NavBar from "./components/NavBar.vue";
import BottomBar from "./components/BottomBar.vue";

export default {
  components: { UploadImage, InputImage, OutputImage, NavBar, BottomBar },
  data() {
    return {
      uid: undefined,
      step: 1,
    };
  },
  async created() {
    const configRes = await fetch("config.json").catch((e) =>
      console.error("error", e)
    );
    const configJson = await configRes.json();
    setUrl(configJson.api_url.value);

    eventBus.$on("loaded", (uid) => {
      this.uid = uid;
      this.step = 2;
    });

    eventBus.$on("back", () => {
      this.step--;
    });

    eventBus.$on("next", () => {
      this.step++;
      setTimeout(() => {
        window.scrollTo(0, document.body.scrollHeight);
      }, 0);
    });
  },
};
</script>