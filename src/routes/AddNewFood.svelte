<script>
    import NavbarSolo from "$lib/components/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/ButtonAddRecord.svelte";
    import Discard from "$lib/components/Discard.svelte";
    import FieldWithValue from "$lib/components/FieldWithValue.svelte";
</script>

<NavbarSolo/>

<div class="container">
    <div class="columns pt-5 is-multiline has-text-centered">
        <div class="column is-4 py-5">
            <a href="Food">
                <ButtonBack/>
            </a>
        </div>
        <div class="column is-4 ml-4">
            <p class="text has-text-link">
                New Food
            </p>
        </div>
        <div class="column is-3">
            <a href="/">
                <Discard/>
            </a>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <FieldWithValue name="Product Name" value=""/>
        <FieldWithValue name="Price" value=""/>
        <div class="column is-12"></div>
        <FieldWithValue name="Product Stock" value=""/>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>

        <!-- wala pang dropdown for product type, and file upload para sa image-->

    </div>

    <div class="mb- has-text-centered">
        <a href="Food">
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