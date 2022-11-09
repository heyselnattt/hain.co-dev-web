<script> 
    export let name;
    export let type;

    let value = type;
	let items = []

    setTimeout(()=>{
		items = [1, 2, 3, 4]
	})
</script>

<div class="column is-3 is-offset-2">
    <p class="pText has-text-link ml-4 mb-1">
        {name}: {value}
    </p>

    <select class="pText button is-rounded" bind:value>
        {#each items as item}
            <option value={item}>{item}</option>
        {/each}
    </select>
</div>

<style>
    .pText {
        font-family: 'Montserrat', sans-serif;
        font-size: 20px;
    }
</style>