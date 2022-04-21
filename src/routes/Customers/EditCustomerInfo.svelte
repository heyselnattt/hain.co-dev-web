<script>
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonSave from "$lib/components/buttons/ButtonSave.svelte";
    import ButtonSwitch from "$lib/components/buttons/ButtonSwitch.svelte";
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import Inaccessible from "$lib/components/otherComponents/Inaccessible.svelte";

    let loggedIn = false;
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

{#if !loggedIn}
    <Inaccessible/>
    {:else}
<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="CustomerInfo"/>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Customer's Information
            </p>
        </div>
        <div class="column is-3 ml-6">
            <ButtonSave link="CustomerInfo"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <FieldWithValue name="Name" value="Swift, Taylor"/>
        <FieldWithValue name="Contact No." value="09123456789"/>
        <div class="column is-12"></div>
        <FieldWithValue name="Email" value="taylorswift@gmail.com"/>
        <FieldWithValue name="Password" value="*****"/>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
    </div>
</div>

<div class="columns is-centered has-text-link pb-6">
    <p class="switch-labels mt-3 mr-4">Inactive</p>
    <ButtonSwitch/>
    <p class="switch-labels mt-3 ml-4">Active</p>
</div>
{/if}

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }

    .switch-labels {
        font-family: 'Karla', sans-serif;
        font-size: 25px;
    }
</style>