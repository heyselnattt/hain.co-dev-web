<script lang="ts">
    export let name;
    export let value;
    export let type = 'text';
</script>

<div class="column is-3 is-offset-2">
    <!-- <input type={type} class="pText input is-rounded" bind:value={value}/> -->

    {#if type === 'password'}
        <p class="pText has-text-link ml-4 mb-1">
            {name}
        </p>
        <input type="password" class="pText input is-rounded" bind:value={value} />
    {:else if type === 'email'}
        <p class="pText has-text-link ml-4 mb-1">
            {name}
        </p>
        <input type="email" class="pText input is-rounded" bind:value={value} />
    {:else if type === 'number'}
        <p class="pText has-text-link ml-4 mb-1">
            {name}
        </p>
        <input type="number" class="pText input is-rounded" bind:value={value} />
    {:else if type === 'date'}
        <p class="pText has-text-link ml-4 mb-1">
            {name}
        </p>
        <input type="date" class="pText input is-rounded" bind:value />
    {:else}
        <p class="pText has-text-link ml-4 mb-1">
            {name}
        </p>
        <input type="text" class="pText input is-rounded" bind:value={value} />
    {/if}

</div>

<style>
    .pText {
        font-family: 'Montserrat', sans-serif;
        font-size: 20px;
    }
</style>