<template>
  <div class="container">
    <h1>Legolize</h1>
    <div class="row show-grid">
      <div class="col-12">
        <form>
          <fieldset>
            <legend>Load image</legend>
            <div class="mb-3">
              <label for="fileInput" class="form-label">Select file</label>
              <input type="file" id="fileInput" />
            </div>
            <button type="submit" class="btn btn-primary">load</button>
          </fieldset>
        </form>
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
export default {
  name: "App",
  methods: {
    inputFile() {
      console.log("aaaa!");
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
