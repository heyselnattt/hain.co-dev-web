<script lang="ts">
    import Homepage from "./Homepage.svelte";
    import {onMount} from 'svelte';

    let isLoaded: boolean = false

    onMount(async () => {
        setTimeout(() => isLoaded = true, 5000)
    })
</script>

{#if isLoaded}
    <Homepage/>
    <style>
        :global(body) {
            background-color: white;
        }
    </style>
{:else}
    load screen component here
{/if}
