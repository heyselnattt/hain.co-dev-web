<script lang="ts">
    export let isOn: boolean;
    let checked: boolean = false;
</script>

<div class="field">
    <input id="switchLarge switchColorDefault switchRoundedDefault"
        type="checkbox"
        name="switchLarge switchColorDefault switchRoundedDefault"
        class="switch is-large is-link is-rounded"
        bind:checked={isOn}>

    {#if isOn}
        <label for="switchLarge switchColorDefault switchRoundedDefault">Active</label>
    {:else}
        <label for="switchLarge switchColorDefault switchRoundedDefault">Inactive</label>
    {/if}

</div>