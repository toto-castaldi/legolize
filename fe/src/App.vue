<template>
  <div class="container">
    <h1>Legolize</h1>
    <div class="row show-grid">
      <div class="col-12">
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
          <button
            type="submit"
            v-on:click="submitFile()"
            class="btn btn-primary"
          >
            load
          </button>
        </fieldset>
      </div>
    </div>
    <div class="row show-grid justify-content-between">
      <div class="col-5">
        <img
          class="img-fluid"
          alt="input"
          src="https://fakeimg.pl/440x230/282828/eae0d0/?retina=1&text=Input"
        />
      </div>
      <div class="col-5">
        <img
          class="img-fluid"
          alt="input"
          src="https://fakeimg.pl/440x230/282828/eae0d0/?retina=1&text=Output"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { setUrl, postFormData } from './store/helpers';

export default {
  data() {
    return {
      file: "",
    };
  },

  async created() {
    const configRes = await fetch("config.json").catch(e => console.error('error', e));
    const configJson = await configRes.json();
    setUrl(configJson.api_url.value);
  },

  methods: {
    async submitFile() {
      let formData = new FormData();
      formData.append("file", this.file);

      const res = await postFormData(`upload`, {
        formData
      });

      const json = await res.json();

      console.log(json);
    },

    handleFileUpload() {
      this.file = this.$refs.file.files[0];
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
