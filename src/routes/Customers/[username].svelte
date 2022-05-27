<script context="module">
    import axios from "$lib/api/index"

    export async function load({fetch, params}) {
        try {
            const emailAddress = params.username;
            const customer = await axios.get(`/customer/${emailAddress}`);
            const oldEmail = customer.data.customer_email
            console.log(customer)
            return {
                props: {
                    customer,
                    oldEmail
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
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import {goto} from "$app/navigation";

    export let customer;
    export let oldEmail;

    let newCustomer = {
        customer_first_name: null,
        customer_middle_name: null,
        customer_last_name: null,
        customer_password: null,
        customer_email: null,
        customer_contact_number: null,
        customer_is_active: true
    };

    const updateCustomerToDatabase = async () => {
        try {
            console.log(newCustomer)
            let response = await axios.put(`/customer/update_customer/${oldEmail}`, newCustomer)
            console.log(response)
            await goto('../Customers');
        } catch (e) {
            console.log(e);
        }
    }
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>
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
            <button class="button is-rounded is-info btn-txt" on:click={updateCustomerToDatabase}>
                <p class="ml-4 mr-4 has-text-white">
                    Save
                </p>
            </button>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12">
            <div class="has-text-centered pText">Make sure to fill up all information boxes</div>
        </div>
        {#await customer}
            Waiting data
        {:then customer}
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    Current First Name: {customer.data.customer_first_name}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newCustomer.customer_first_name}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    Current Middle Name: {customer.data.customer_middle_name}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newCustomer.customer_middle_name}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    Current Last Name: {customer.data.customer_last_name}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newCustomer.customer_last_name}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    Current Email: {customer.data.customer_email}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newCustomer.customer_email}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    Current Contact Number: {customer.data.customer_contact_number}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newCustomer.customer_contact_number}/>
            </div>

            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    Current Password: {customer.data.customer_password}
                </p>
                <input class="pText input is-rounded" type="password" bind:value={newCustomer.customer_password}/>
            </div>
        {:catch e}
            {e}
        {/await}
        <div class="column is-12">
            <div class="columns is-centered has-text-link pb-6">
                {#await customer}
                    Waiting data
                {:then customer}
                    <div class="field">
                        {#if customer.data.customer_is_active}
                            <div class="pText has-text-centered">Customer Currently Active</div>
                        {:else}
                            <div class="pText has-text-centered">Customer Currently Inactive</div>
                        {/if}
                        <input id="switchLarge switchColorDefault switchRoundedDefault"
                               type="checkbox"
                               name="switchLarge switchColorDefault switchRoundedDefault"
                               class="switch is-large is-link is-rounded"
                               bind:checked={newCustomer.customer_is_active}>
                        {#if newCustomer.customer_is_active}
                            <label for="switchLarge switchColorDefault switchRoundedDefault">Active</label>
                        {:else}
                            <label for="switchLarge switchColorDefault switchRoundedDefault">Inactive</label>
                        {/if}
                    </div>
                {:catch e}
                    {e}
                {/await}
            </div>
        </div>
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }

    .pText {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }

    .btn-txt {
        font-size: 20px;
        font-family: 'Karla', sans-serif;
    }
</style>