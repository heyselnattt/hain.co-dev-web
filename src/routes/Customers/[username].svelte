<script context="module">
    import axios from "$lib/api/index"

    export async function load({params}) {
        try {
            const emailAddress = params.username;
            const customer = await axios.get(`/customer/auth/${emailAddress}`);
            const oldEmail = customer.data.customerDetails.customer_email
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
    import { notifs } from "$lib/stores/notificationStore";
    import NotificationContainer from "$lib/components/systemNotification/notification-container.svelte";
    import validators from "$lib/validators";

    export let customer;
    export let oldEmail;
    let updating = false

    let customerDetails = customer.data.customerDetails;

    let newCustomer = {
        customerFirstName: null,
        customerLastName: null,
        customerPassword: null,
        customerEmail: null,
        customerGcashNumber: null,
        customerGcashName: null,
        customerIsActive: true
    };

    const isEmailValid = (email) => {
        const emailRegexp = new RegExp(
            /^[a-zA-Z0-9][\~\!\$\%\^\&\*_\=\+\}\{\'\?\-\.\\\#\/\`\|]{0,1}([a-zA-Z0-9][\~\!\$\%\^\&\*_\=\+\}\{\'\?\-\.\\\#\/\`\|]{0,1})*[a-zA-Z0-9]@[a-zA-Z0-9][-\.]{0,1}([a-zA-Z][-\.]{0,1})*[a-zA-Z0-9]\.[a-zA-Z0-9]{1,}([\.\-]{0,1}[a-zA-Z]){0,}[a-zA-Z0-9]{0,}$/i
        )
        return emailRegexp.test(email)
    }

    const isPassValid = (pass) => {
        const passRegexp = new RegExp(/([a-zA-z0-9!@#$%^&*(),.;'\\_\\]{6,})/)
        return passRegexp.test(pass)
    }

    const updateCustomerToDatabase = async () => {
        let msg = ''
        let errors = 0
        Object.keys(newCustomer).map(prop => {
            if(!newCustomer[prop]) {
                msg += !errors ? `${prop.split('customer').join('')}` : `, ${prop.split('customer').join('')}`
                errors++
            }
        })
        msg += errors > 1 ? ' are required fields' : ' is a required field'

        if(errors) {
            $notifs = [...$notifs, {
                msg,
                type: 'error',
                id: `${Math.random() * 99}${new Date().getTime()}`
            }]
            return
        }

        if(!validators.isEmailValid(newCustomer.customerEmail)) {
            $notifs = [...$notifs, {
                msg: 'Email is invalid',
                type: 'error',
                id: `${(Math.random() * 99) + 1}${new Date().getTime()}`
            }]
            return
        }

        if(!validators.isPassValid(newCustomer.customerPassword)) {
            $notifs = [...$notifs, {
                msg: 'Password does not meet the criteria for the security',
                type: 'error',
                id: `${(Math.random() * 99) + 1}${new Date().getTime()}`
            }]
            return
        }

        if(validators.containsLettersAndCharacters(newCustomer.customerGcashNumber)) {
            $notifs = [...$notifs, {
                msg: 'Gash number cannot have a letter or special characters',
                type: 'error',
                id: `${(Math.random() * 99) + 1}${new Date().getTime()}`
            }]
            return
        }

        if(newCustomer.customerGcashNumber.length != 11) {
            $notifs = [...$notifs, {
                msg: 'Gash number must be exactly 11 numbers e.g 09xx-xxx-xxxx',
                type: 'error',
                id: `${(Math.random() * 99) + 1}${new Date().getTime()}`
            }]
            return
        }

        if(!newCustomer.customerGcashNumber.substring(0, 2).match('09')) {
            $notifs = [...$notifs, {
                msg: 'Gcash number must be start with 09 e.g 09xx-xxx-xxxx',
                type: 'error',
                id: `${(Math.random() * 99) + 1}${new Date().getTime()}`
            }]
            return
        }

        try {
            updating = true
            console.log(newCustomer)
            let response = await axios.put(`/customer/updateCustomer/${oldEmail}`, newCustomer)
            if(response.status == 200) {
                updating = false
                $notifs = [...$notifs, {
                    msg: `Canteen customer: ${newCustomer.customerFirstName} ${newCustomer.customerLastName} is updated`,
                    type: 'success',
                    id: (Math.random() * 100) + 1
                }]
                await goto('../Customers');
            }else {
                updating = false
                $notifs = [...$notifs, {
                    msg: `Error in updating customer data`,
                    type: 'error',
                    id: `${Math.random() * 99}${new Date().getTime()}`
                }]
            }
            // console.log(response)
        } catch (e) {
            updating = false
            $notifs = [...$notifs, {
                msg: `Error in updating customer data`,
                type: 'error',
                id: `${Math.random() * 99}${new Date().getTime()}`
            }]
            console.log(e);
        }
    }
</script>

<NavbarSolo/>
<NotificationContainer />

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
            <button class="button {updating ? 'is-loading' : ''} is-rounded is-info btn-txt" on:click={updateCustomerToDatabase}>
                <p class="ml-4 mr-4 has-text-white {updating ? 'is-hidden' : ''}">
                    Save
                </p>
            </button>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12">
            <div class="has-text-centered pText">Make sure to fill up all required information boxes</div>
        </div>
        {#await customer}
            Waiting data
        {:then customer}
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current First Name: {customerDetails.customer_first_name}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newCustomer.customerFirstName}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Last Name: {customerDetails.customer_last_name}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newCustomer.customerLastName}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Email: {customerDetails.customer_email}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newCustomer.customerEmail}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Password: {customerDetails.customer_password}
                </p>
                <input class="pText input is-rounded" type="password" bind:value={newCustomer.customerPassword}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Gcash Name: {customerDetails.customer_gcash_name}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newCustomer.customerGcashName}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Gcash Number: {customerDetails.customer_gcash_number}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newCustomer.customerGcashNumber}/>
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
                        {#if customerDetails.customer_is_active}
                            <div class="pText has-text-centered"> <span>*</span> Customer Currently Active</div>
                        {:else}
                            <div class="pText has-text-centered"> <span>*</span> Customer Currently Inactive</div>
                        {/if}
                        <input id="switchLarge switchColorDefault switchRoundedDefault"
                               type="checkbox"
                               name="switchLarge switchColorDefault switchRoundedDefault"
                               class="switch is-large is-link is-rounded"
                               bind:checked={newCustomer.customerIsActive}>
                        {#if newCustomer.customerIsActive}
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
        font-family: 'Montserrat', sans-serif;
        font-size: 40px;
    }

    .pText {
        font-family: 'Montserrat', sans-serif;
        font-size: 20px;
    }

    .btn-txt {
        font-size: 20px;
        font-family: 'Montserrat', sans-serif;
    }

    span {
        color: red;
    }
</style>