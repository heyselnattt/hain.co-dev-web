<script context="module">
    import axios from "$lib/api/index"
    export async function load({ fetch, params }) {
        try {
            const email = params.email;
            const customer = await axios.get(`/customer/${email}`);
            console.log(customer)
            return {
                props: {
                    customer
                }
            }
        } catch (e) {
            return {
                error: new Error('Can\'t fetch the customer information')
            }
        }
    }
</script>

<script>
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonSave from "$lib/components/buttons/ButtonSave.svelte";
    import ButtonSwitch from "$lib/components/buttons/ButtonSwitch.svelte";
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";

    export let customer;
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
        {#await customer}
            Waiting data
        {:then customer}
            <!-- TODO switch to bound inputs -->
            <FieldWithValue
                name="First Name"
                value={customer.data.customer_first_name}/>
            <FieldWithValue
                name="Middle Name"
                value={customer.data.customer_middle_name} />
            <FieldWithValue
                name="Last Name"
                value={customer.data.customer_last_name} />
            <FieldWithValue
                name="Email"
                value={customer.data.customer_email} />
            <FieldWithValue
                name="Contact Number"
                value={customer.data.customer_contact_number} />
            <FieldWithValue
                name="Password"
                value={customer.data.customer_password_hash} />
        {:catch e}
            {e}
        {/await}
        <div class="column is-12"></div>
    </div>
</div>

<div class="columns is-centered has-text-link pb-6">
    <p class="switch-labels mt-3 mr-4">Inactive</p>
<!--    TODO FIX TO RENDER THE IS ACTIVE -->
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