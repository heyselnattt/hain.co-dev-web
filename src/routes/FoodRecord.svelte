<script>
    import NavbarSolo from "$lib/components/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/ButtonBack.svelte";
    import FieldWithValue from "$lib/components/FieldWithValue.svelte";
    import ButtonSave from "$lib/components/ButtonSave.svelte";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo/>

<div class="container">
    <div class="columns pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <a href="Food">
                <ButtonBack/>
            </a>
        </div>
        <div class="column is-3  ml-6">
            <p class="text has-text-link">
                Food's Information
            </p>
        </div>
        <div class="column is-3 ml-6">
            <a href="/">
                <ButtonSave/>
            </a>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <FieldWithValue name="Product Name" value="Hotdog"/>
        <FieldWithValue name="Price" value="30.00"/>
        <div class="column is-12"></div>
        <FieldWithValue name="Product Stock" value="10"/>

        <!-- wala pang file upload for image and also yung dropdown para sa product type-->

    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>

