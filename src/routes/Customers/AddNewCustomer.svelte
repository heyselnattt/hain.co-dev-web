<script lang="ts">
    import Discard from "$lib/components/buttons/Discard.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/buttons/ButtonAddRecord.svelte";

    export let value;
    export let name;
    export let defaultValue = "";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../Customers"/>
        </div>
        <div class="column is-4">
            <p class="text1 has-text-link">
                New Customer
            </p>
        </div>
        <div class="column is-3 ml-6">
            <Discard link="../Customers"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                Name
            </p>
            <input class="pText input is-rounded" type="text" bind:value={value}/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                Contact No.
            </p>
            <input class="pText input is-rounded" type="text" bind:value={value}/>
        </div>
        <div class="column is-12"></div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                Email
            </p>
            <input class="pText input is-rounded" type="text" bind:value={value}/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                Address
            </p>
            <input class="pText input is-rounded" type="text" bind:value={value}/>
        </div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
    </div>

    <!-- Add record button -->
    <div class="mb- has-text-centered">
        <ButtonAddRecord link="../Customers"/>
    </div>
</div>

<style>
    .text1 {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
    .pText {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }
</style>