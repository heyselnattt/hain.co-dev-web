<script>
    import BtnBack from "$lib/components/BtnBack.svelte";
    import BtnEdit from "$lib/components/BtnEdit.svelte";
    import BtnSwitch from "$lib/components/BtnSwitch.svelte";
    import FieldWithValue from "$lib/components/FieldWithValue.svelte";
    import NavbarSolo from "$lib/components/NavbarSolo.svelte";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4"> 
            <a href="Customers"> <BtnBack /> </a> 
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Customer's Information
            </p>
        </div>
        <div class="column is-3 ml-6">
            <a href="/"> <BtnEdit /> </a>
        </div>

        <div class="column is-12"></div>
        <div class="column is-12"></div>
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
    <BtnSwitch/>
    <p class="switch-labels mt-3 ml-4">Active</p>
</div>

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