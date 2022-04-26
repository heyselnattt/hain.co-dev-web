<script lang="ts">

    import NavbarWithSearch from "$lib/components/navbars/NavbarWithSearch.svelte";
    import CustomersTableRow from "$lib/components/tableRows/CustomersTableRow.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/buttons/ButtonAddRecord.svelte";
    import FixedLoadingScreen from "$lib/components/otherComponents/FixedLoadingScreen.svelte";
    import {customers} from "$lib/stores/customerStores";

    let itemNumber = 1;
    const counter = (): number => {
        return itemNumber++;
    }
</script>

<NavbarWithSearch />

<div class="container">
    <div class="columns has-text-centered pt-5">
        <div class="column is-4">
            <ButtonBack link="Database" />
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Customers
            </p>
        </div>
        <div class="column is-3 ml-6">
            <ButtonAddRecord link="Customers/AddNewCustomer" />
        </div>
    </div>

    <div class="column is-10 is-offset-1 pl-5 pt-0">
        <table class="table is-hoverable is-fullwidth">
            <thead>
                <tr>
                    <th>No.</th>
                    <th>Name</th>
                    <th>Contact No.</th>
                    <th>Email</th>
                    <th></th>
                </tr>
            </thead>
            {#await $customers}
                <FixedLoadingScreen/>
            {:then customer}

                {#each customer.data as info}
                    <!--TODO add property for the link for the individual product-->
                    <CustomersTableRow
                        num={counter()}
                        name={`${info.customer_first_name} ${info.customer_middle_name} ${info.customer_last_name}`}
                        contactNum={info.customer_contact_number}
                        email={info.customer_email}
                        link={`/Customers/${info.customer_id}`}/>
                {/each}
            {:catch err}
                <p>{err.message}</p>
            {/await}
        </table>
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }

    table {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }
</style>