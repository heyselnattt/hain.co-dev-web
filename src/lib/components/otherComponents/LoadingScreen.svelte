<script>
    import { fade } from 'svelte/transition'
    import { Rainbow } from 'svelte-loading-spinners'

    let hide = false;

    setTimeout(() => {
        hide = true;
    }, 5000);
</script>

<svelte:head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lobster&display=swap"/>
</svelte:head>

{#if !hide}
<div out:fade class="hero is-white is-flex is-justify-content-center is-align-items-center">
    <div class="hero-body">
            <div class="container">
                <Rainbow size="100" color="#1042C1" unit="px" duration="1.7s"></Rainbow>
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
        font-family: 'Lobster', cursive;
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