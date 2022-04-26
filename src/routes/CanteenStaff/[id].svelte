<script context="module">
    export async function load({ fetch, params }) {

        const id = params.id;
        const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        const canteenStaff = await res.json()

        if (res.ok) {
            return {
                props: {
                    canteenStaff
                }
            }
        }

        return {
            status: res.status,
            error: new Error('Could not fetch the canteen staff.')
        }
    }
</script>

<script>
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonSave from "$lib/components/buttons/ButtonSave.svelte";
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";

    export let canteenStaff
</script>

<NavbarSolo />

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../CanteenStaff" />
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Canteen Staff's Information
            </p>
        </div>
        <div class="column is-3 ml-6">
            <ButtonSave link="../CanteenStaff" />
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <FieldWithValue name="Name" value={canteenStaff.name} />
        <FieldWithValue name="Position" value={canteenStaff.username} />
        <div class="column is-12"></div>
        <FieldWithValue name="Contact No." value={canteenStaff.phone} />
        <FieldWithValue name="Address" value={canteenStaff.email} />
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