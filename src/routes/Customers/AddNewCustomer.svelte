<script lang="ts">
    import Discard from "$lib/components/buttons/Discard.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import axios from "$lib/api";
    import {goto} from "$app/navigation";

    let customer = {
        customer_first_name: null,
        customer_last_name: null,
        customer_password: null,
        customer_email: null,
        customer_contact_number: null,
        customer_is_active: true
    };

    const addCustomerToDatabase = async () => {
        try {
            let response = await axios.post('/customer/new_customer', customer);
            console.log(response);
            await goto("../Customers");
        } catch (e) {
            console.log(e);
        }
    }

    let pattern = "([a-zA-z0-9!@#$%^&*(),.;'\\_\\\\]{6,})"
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
            <p class="text1 has-text-link">
                New Customer
            </p>
        </div>
        <div class="column is-3 ml-6">
            <Discard link="../Customers"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> First Name
            </p>
            <input class="pText input is-rounded" type="text" bind:value={customer.customer_first_name} required/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Last Name
            </p>
            <input class="pText input is-rounded" type="text" bind:value={customer.customer_last_name} required/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Email Address
            </p>
            <input class="pText input is-rounded" type="email" bind:value={customer.customer_email} required/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Contact Number
            </p>
            <input class="pText input is-rounded" type="text" bind:value={customer.customer_contact_number} required/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Password
            </p>
            <input class="pText input is-rounded" type="password" pattern="{pattern}" title="6 or more characters" bind:value={customer.customer_password} required/>
        </div>
        <div class="column is-12"></div>
    </div>

    <div class="has-text-centered">
        <div class="field">
            <input id="switchLarge switchColorDefault switchRoundedDefault"
                   type="checkbox"
                   name="switchLarge switchColorDefault switchRoundedDefault"
                   class="switch is-large is-link is-rounded"
                   bind:checked={customer.customer_is_active}>
            {#if customer.customer_is_active}
                <label for="switchLarge switchColorDefault switchRoundedDefault"><span>*</span> Active</label>
            {:else}
                <label for="switchLarge switchColorDefault switchRoundedDefault"><span>*</span> Inactive</label>
            {/if}
        </div>
        <div class="column is-12"></div>
    </div>

    <!-- Add record button -->
    <div class="mb- has-text-centered">
        <button class="btn-txt button is-link is-rounded" type="submit" on:click={() => console.log("Helow")}>Add Customer</button>
    </div>
</div>

<style>
    .text1 {
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

    span {
        color: red;
    }
</style>