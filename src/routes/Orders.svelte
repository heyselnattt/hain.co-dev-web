<script lang="ts">
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import NavbarWithSearch from "$lib/components/navbars/NavbarWithSearch.svelte";
    import OrdersTableRow from "$lib/components/tableRows/OrdersTableRow.svelte";
    import TableLoadingScreen from "$lib/components/otherComponents/TableLoadingScreen.svelte"
    import {orderToday} from "$lib/stores/orderStore";
    import {onMount} from "svelte";
    import {goto} from "$app/navigation";

    const link: string = " ";

    onMount(async () => {
        if (!localStorage.getItem("admin")) {
            await goto("/");
        }
    })

    let orderNumber = 1;
    const counter = (): number => (
        orderNumber++
    )

    const identifyType = (code: number): string => {
        switch(code) {
            case 1:
                return "Incoming"

            case 2:
                return "Unfulfilled"

            case 3:
                return "Processing"

            case 4:
                return "Fulfilled"
        }
    }

    const identifyPaymentMethod = (code: number): string => {
        switch(code) {
            case 1:
                return "CASH"

            case 2:
                return "GCASH"
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
            <p class="text has-text-link has-text-weight-bold">
                Orders Today
            </p>
        </div>
        <div class="column is-4">
            <a href="/ViewAllOrders">
                <button class="button is-rounded is-link btn-txt">
                    <p class="ml-4 mr-4">
                        View all orders
                    </p>
                </button>
            </a>
        </div>
    </div>

    <div class="column is-10 is-offset-1 pl-5 pt-0">
        <table class="table is-hoverable is-fullwidth">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Code</th>
                    <th>Customer Email</th>
                    <th>Order Request</th>
                    <th>Order Date</th>
                    <th>Payment Method</th>
                    <th>Order Status</th>
                </tr>
            </thead>
            {#await $orderToday}
                <TableLoadingScreen/>
            {:then order}
                {#each order as info}
                    <OrdersTableRow
                        productCode={info.order_product_code}
                        customerEmail={info.order_customer_email}
                        orderRequest={info.order_requests}
                        orderDate={info.order_date}
                        staffUsername={identifyPaymentMethod(info.order_payment_method)}
                        orderStatus={info.order_status}
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

    .btn-txt {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }
</style>