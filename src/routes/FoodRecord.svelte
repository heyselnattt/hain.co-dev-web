<script>
    import NavbarSolo from "$lib/components/NavbarSolo.svelte";
    import BtnBack from "$lib/components/BtnBack.svelte";
    import FieldWithValue from "$lib/components/FieldWithValue.svelte";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo />

<div class="container">
    <div class="columns pt-5 is-multiline has-text-centered">
        <div class="column is-4"> 
            <a href="Food"> <BtnBack /> </a> 
        </div>
        <div class="column is-3  ml-6">
            <p class="text has-text-link">
                Food's Information
            </p>
        </div>
        <div class="column is-4">
            <a class="btn-txt button is-link is-rounded" href="/">
                <p class="ml-5 mr-5">
                   Save <!--save button-->
                </p>
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
    .btn-txt {
        font-size: 20px;
        font-family: 'Karla', sans-serif;
    }
</style>

