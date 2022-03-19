<script>
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonEdit from "$lib/components/buttons/ButtonEdit.svelte";
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <a href="Admin">
                <ButtonBack/>
            </a>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Admin's Information
            </p>
        </div>
        <div class="column is-3 ml-6">
            <a href="EditAdminInfo">
                <ButtonEdit/>
            </a>
        </div>

        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <FieldWithValue name="Name" value="Del Valle, Deib Lohr H."/>
        <FieldWithValue name="Contact No." value="Cook"/>
        <div class="column is-12"></div>
        <FieldWithValue name="ID No." value="09123456789"/>
        <FieldWithValue name="Password" value="*****"/>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>