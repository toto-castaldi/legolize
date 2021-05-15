<template>
  <div>
    <legend>Choose size</legend>
    <div class="mb-3">
      <img class="" alt="input" :src="imageSrc" />
    </div>
    <div class="mb-3">
      <label for="size" class="form-label">Select size</label>
      <select id="size" name="size" ref="size" v-on:change="handleSize()">
        <option value="10">10</option>
        <option value="20">20</option>
        <option value="30">30</option>
        <option value="40">40</option>
        <option value="50">50</option>
        <option value="60">60</option>
        <option value="70">70</option>
        <option value="80">80</option>
      </select>
    </div>
    <div class="row">
      <div class="col">
        <button type="submit" :disabled="!current" @click="back()" class="btn btn-primary">
          back
        </button>
      </div>
      <div class="col-6"></div>
      <div class="col">
        <button type="submit" :disabled="!current" @click="next()" class="btn btn-primary">
          generate
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiInputImage } from "@/store/helpers";
import { post } from "@/store/helpers";
import { eventBus } from "@/store/eventBus";

export default {
  props: ["uid", "current"],
  methods: {
    back() {
      eventBus.$emit("back", {});
    },
    async next() {
      await post(`generate`, {
        body: { size: this.size, uid: this.uid },
      });
      eventBus.$emit("next");
    },
    handleSize() {
      this.size = this.$refs.size.value;
    },
  },
  data() {
    return {
      imageSrc: apiInputImage(this.uid),
      size: 10,
    };
  },
};
</script>