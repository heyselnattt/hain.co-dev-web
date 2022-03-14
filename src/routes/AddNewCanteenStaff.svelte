<script lang="ts">
    import ButtonAddRecord from "$lib/components/ButtonAddRecord.svelte";
    import ButtonBack from "$lib/components/ButtonBack.svelte";
    import Discard from "$lib/components/Discard.svelte";
    import FieldWithValue from "$lib/components/FieldWithValue.svelte";
    import NavbarSolo from "$lib/components/NavbarSolo.svelte";
</script>

<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <a href="CanteenStaff">
                <ButtonBack/>
            </a>
        </div>
        <div class="column is-4  ml-4">
            <p class="text has-text-link">
                New Canteen Staff
            </p>
        </div>
        <div class="column is-3 ml-6">
            <a href="/">
                <Discard/>
            </a>
        </div>

        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <FieldWithValue name="Name" value=""/>
        <FieldWithValue name="Position" value=""/>
        <div class="column is-12"></div>
        <FieldWithValue name="Contact No." value=""/>
        <FieldWithValue name="Address" value=""/>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
    </div>

    <!-- Add record button -->
    <div class="mb- has-text-centered">
        <a href="CanteenStaff">
            <ButtonAddRecord/>
        </a>
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>