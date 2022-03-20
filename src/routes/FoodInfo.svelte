<script>
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonEdit from "$lib/components/buttons/ButtonEdit.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="Customers"/>
        </div>
        <div class="column is-3  ml-6">
            <p class="text has-text-link">
                Food's Information
            </p>
        </div>
        <div class="column is-4">
            <ButtonEdit link="FoodInfo"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <FieldWithValue name="Product Name" value="Hotdog" isReadOnly={true}/>
        <FieldWithValue name="Price" value="30.00" isReadOnly={true}/>
        <div class="column is-12"></div>
        <FieldWithValue name="Product Stock" value="10" isReadOnly={true}/>

        <!-- wala pang file upload for image and also yung dropdown para sa product type-->

    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>

