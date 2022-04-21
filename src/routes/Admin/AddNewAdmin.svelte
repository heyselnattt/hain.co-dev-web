<script>
    import Discard from "$lib/components/buttons/Discard.svelte";
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/buttons/ButtonAddRecord.svelte";
    import Inaccessible from "$lib/components/otherComponents/Inaccessible.svelte";

    let loggedIn = false;
</script>

{#if !loggedIn}
    <Inaccessible/>
    {:else}
<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../Admin"/>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                New Administrator
            </p>
        </div>
        <div class="column is-3 ml-6">
            <Discard link="../Admin"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <FieldWithValue name="Name" value=""/>
        <FieldWithValue name="Contact No." value=""/>
        <div class="column is-12"></div>
        <FieldWithValue name="Email" value=""/>
        <FieldWithValue name="Password" value=""/>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
    </div>

    <!-- Add record button -->
    <div class="mb- has-text-centered">
        <ButtonAddRecord link="../Admin"/>
    </div>
</div>
{/if}

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>