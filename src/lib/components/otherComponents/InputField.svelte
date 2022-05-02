<script>
    export let value;
    export let name;
    export let defaultValue = "";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<div class="column is-3 is-offset-2">
    <p class="pText has-text-link ml-4 mb-1">
        {name}
    </p>
    <input class="pText input is-rounded" type="text" bind:value={value} placeholder={defaultValue}/>
</div>

<style>
    .pText {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }
</style>