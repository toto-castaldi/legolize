<template>
  <div v-bind:class="{ 'bg-light': current }" class="mb-3" >
    <legend>Load image</legend>
    <div class="mb-3">
      <label for="file" class="form-label">Select file</label>
      <input
        type="file"
        id="file"
        ref="file"
        v-on:change="handleFileUpload()"
        :disabled="!current"
      />
    </div>
    <button type="submit" :disabled="file.length == 0 || !current" @click="submitFile()" class="btn btn-primary">
      load
    </button>
  </div>
</template>

<script>
import { postFormData } from "@/store/helpers";
import { eventBus } from "@/store/eventBus";

export default {
  props : ['current'],
  data() {
    return {
      file: ""
    };
  },

  methods: {
    async submitFile() {
      let formData = new FormData();
      formData.append("file", this.file);

      const res = await postFormData(`upload`, {
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
