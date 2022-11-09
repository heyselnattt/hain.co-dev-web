<script>
    import { fade } from 'svelte/transition'
    import { Rainbow } from 'svelte-loading-spinners'
    import { onMount } from 'svelte';

    let hide = false;
    export let infinite = false;

    onMount(() => {
        if (!infinite) {
            setTimeout(() => {
                hide = true;
            }, 5000);
        }
    })
</script>

{#if !hide}
<div out:fade class="hero is-white is-flex is-justify-content-center is-align-items-center">
    <div class="hero-body">
            <div class="container">
                <Rainbow size="100" color="#EA6227" unit="px" duration="1.7s"></Rainbow>
            </div>
            <p class="has-text-link">Loading</p>
    </div>
</div>
{/if}

<style>
    .container {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    p {
        position: absolute;
        font-family: 'Titan One', cursive;
        font-size: 30px;
        top: 55%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    .hero {
        position: fixed;
        z-index: 99;
        width: 100vw;
        height: 100%;
    }
</style>