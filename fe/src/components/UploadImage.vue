<template>
  <fieldset>
    <legend>Load image</legend>
    <div class="mb-3">
      <label for="file" class="form-label">Select file</label>
      <input
        type="file"
        id="file"
        ref="file"
        v-on:change="handleFileUpload()"
      />
    </div>
    <div class="mb-3">
      <input
        type="range"
        min="10"
        max="100"
        value="50"
        class="slider"
        id="precision"
        ref="precision"
        v-on:change="handlePrecision()"
      />
    </div>
    <button type="submit" v-on:click="submitFile()" class="btn btn-primary">
      load
    </button>
  </fieldset>
</template>

<script>
import { postFormData } from "@/store/helpers";
import { eventBus } from "@/store/eventBus";

export default {
  data() {
    return {
      file: "",
      precision: 10
    };
  },

  methods: {
    async submitFile() {
      let formData = new FormData();
      formData.append("file", this.file);

      const res = await postFormData(`upload/${this.precision}`, {
        formData,
      });

      const json = await res.json();

      eventBus.$emit("loaded", json.uid);
    },

    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },

    handlePrecision() {
      this.precision = 110 - this.$refs.precision.value;
    },
  },
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
