<script>
    import ButtonBack from "$lib/components/ButtonBack.svelte";
    import ButtonSave from "$lib/components/ButtonSave.svelte";

    import FieldWithValue from "$lib/components/FieldWithValue.svelte";
    import NavbarSolo from "$lib/components/NavbarSolo.svelte";
</script>

<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <a href="CanteenStaffInfo">
                <ButtonBack/>
            </a>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Canteen Staff's Information
            </p>
        </div>
        <div class="column is-3 ml-6">
            <a href="CanteenStaffInfo">
                <ButtonSave/>
            </a>
        </div>

        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <FieldWithValue name="Name" value="Salaveria, Rence"/>
        <FieldWithValue name="Position" value="Cook"/>
        <div class="column is-12"></div>
        <FieldWithValue name="Contact No." value="09123456789"/>
        <FieldWithValue name="Address" value="02 Toronto St. Malinta Valenzuela City"/>
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