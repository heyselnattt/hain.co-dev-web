<script context="module">
    export async function load({ fetch, params }) {

        const id = params.id;
        const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        const customer = await res.json()

        if (res.ok) {
            return {
                props: {
                    customer
                }
            }
        }

        return {
            status: res.status,
            error: new Error('Could not fetch the customer.')
        }
    }
</script>

<script>
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonSave from "$lib/components/buttons/ButtonSave.svelte";
    import ButtonSwitch from "$lib/components/buttons/ButtonSwitch.svelte";
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";

    export let customer
</script>

<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../Customers"/>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Customer's Information
            </p>
        </div>
        <div class="column is-3 ml-6">
            <ButtonSave link="../Customers"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <FieldWithValue name="Name" value={customer.name} />
        <FieldWithValue name="Contact No." value={customer.phone} />
        <div class="column is-12"></div>
        <FieldWithValue name="Email" value={customer.email} />
        <FieldWithValue name="Password" value="*****" />
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
    </div>
</div>

<div class="columns is-centered has-text-link pb-6">
    <p class="switch-labels mt-3 mr-4">Inactive</p>
    <ButtonSwitch/>
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