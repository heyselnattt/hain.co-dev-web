<script lang="ts">
    import Homepage from "./Homepage.svelte";
    import LoadingScreen from "$lib/components/otherComponents/LoadingScreen.svelte"
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
    <LoadingScreen/>
{/if}
