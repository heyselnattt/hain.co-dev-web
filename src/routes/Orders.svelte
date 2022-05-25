<script lang="ts">
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import NavbarWithSearch from "$lib/components/navbars/NavbarWithSearch.svelte";
    import OrdersTableRow from "$lib/components/tableRows/OrdersTableRow.svelte";
    import TableLoadingScreen from "$lib/components/otherComponents/TableLoadingScreen.svelte"
    import {orders} from "$lib/stores/orderStore";

    let orderNumber = 1;
    const counter = (): number => {
        return orderNumber++;
    }

    const identifyType = (code: number): string => {
        switch(code) {
            case 1:
                return "Incoming"

            case 2:
                return "Processing"

            case 3:
                return "Fulfilled"

            case 4:
                return "Unprocessed"
        }
    }
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarWithSearch/>

<div class="container">
    <div class="columns has-text-centered pt-5">
        <div class="column is-4 has-text-centered">
            <ButtonBack link="Database"/>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Orders
            </p>
        </div>
    </div>

    <div class="column is-10 is-offset-1 pl-5 pt-0">
        <table class="table is-hoverable is-fullwidth">
            <thead>
                <tr>
                    <th>Product Code</th>
                    <th>Customer Email</th>
                    <th>Order Request</th>
                    <th>Order Date</th>
                    <th>Staff</th>
                    <th>Order Status</th>
                    <th>Order Number</th>
                </tr>
            </thead>
            {#await $orders}
                <TableLoadingScreen/>
            {:then order}
                {#each order.data as info}
                    <OrdersTableRow
                        productCode={info.order_product_code}
                        customerEmail={info.order_customer_email}
                        orderRequest={info.order_requests}
                        orderDate={info.order_product}
                        staffUsername={info.order_staff_username}
                        orderStatus={identifyType(info.order_status)}
                        orderNumber={info.order_number}/>
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