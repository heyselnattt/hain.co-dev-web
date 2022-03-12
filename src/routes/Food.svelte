<script>
    import NavbarSolo from "$lib/components/NavbarSolo.svelte";
    import Discard from "$lib/components/Discard.svelte";
    import ButtonBack from "$lib/components/ButtonBack.svelte";

</script>

<NavbarSolo />

<div class="grouped-columns is-flex is-justify-content-space-between py-6 my-2">
    <div></div>
    <div class="column1">
        <ButtonBack />
    </div>
    <div class="column2">
        <p class="text has-text-link">
            Food
        </p>
    </div>
    <div class="column3">
        <Discard />
    </div>
    <div></div>
</div>

<div class="grouped-columns-2 is-flex is is-justify-content-space-between py-6">
    <div></div>
    <div class="column4">
        <div class="file is-normal has-name">
            <label class="file-label">
              <input class="file-input" type="file" name="resume">
              <span class="file-cta">
                <span class="file-icon">
                  <i class="fas fa-upload"></i>
                </span>
                <span class="file-label">
                  Normal file…
                </span>
              </span>
              <span class="file-name">
                Screen Shot 2017-07-29 at 15.54.25.png
              </span>
            </label>
          </div>
    </div>
    <div class="column5">

    </div>
    <div class="column6">

    </div>
    <div></div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>