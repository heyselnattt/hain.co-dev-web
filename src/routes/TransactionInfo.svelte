<script>
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import Discard from "$lib/components/buttons/Discard.svelte";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo />

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4"> 
            <ButtonBack link="Transaction"/>
        </div>
        <div class="column is-4  ml-4">
            <p class="text has-text-link">
                0001
            </p>
            <p class="text has-text-link">
                Transaction ID
            </p>
        </div>
        <div class="column is-3">
            <Discard link="Transaction"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-1"></div>
        <div class="column is-4">
            <p class="text has-text-link">
                Name
            </p>
            <p class="text has-text-black">
                Bantugan, Dea
            </p>
        </div>
        <div class="column is-3"></div>
        <div class="column is-4">
            <p class="text has-text-link">
                Transaction Date
            </p>
            <p class="text has-text-black">
                10/15/2022
            </p>
        </div>
        <div class="column is-0"></div>
        <div class="column is-2">
            <p class="text has-text-link">
                Type
            </p>
            <p class="text has-text-black">
                Order
            </p>
        </div>
        <div class="column is-2"></div>
        <div class="column is-4">
            <p class="text has-text-link">
                Description
            </p>
            <p class="text has-text-black">
                buy rice and adobo
            </p>
        </div>
        <div class="column is-1"></div>
        <div class="column is-2">
            <p class="text has-text-link">
                Amount
            </p>
            <p class="text has-text-black">
                40.00
            </p>
        </div>
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }

    p {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>