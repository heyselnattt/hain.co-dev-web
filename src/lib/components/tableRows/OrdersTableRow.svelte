<script lang="ts">
    import axios from '$lib/api/index';
    export let productCode;
    export let customerEmail;
    export let orderRequest;
    export let orderDate;
    export let staffUsername;
    export let orderStatus;
    export let orderNumber;


    let orderStatuses = [
        {value: 1, label: "INCOMING"},
        {value: 2, label: "UNFULFILLED"},
        {value: 3, label: "PROCESSING"},
        {value: 4, label: "FULFILLED"}
    ]

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

    let newStatus;

    const updateOrderStatus = async () => {
        const newStatusInt = parseInt(newStatus);
        const response = await axios.patch(`/order/updateOrderStatus/${orderNumber}`, {
            orderStatus: newStatusInt
        })
        console.log(response)
    }
</script>

<tbody>
    <tr class="text is-clickable">
        <th>{orderNumber}</th>
        <th>{productCode}</th>
        <th>{customerEmail}</th>
        <th>{orderRequest}</th>
        <th>{new Date(orderDate).toLocaleDateString()}</th>
        <th>{staffUsername}</th>
        <th>{orderStatus}</th>
        <td>
            <div class="select is-small">
                <select bind:value={newStatus}
                        on:change={updateOrderStatus}>
                    {#if orderStatus === 1}
                        <option selected disabled>INCOMING</option>
                    {:else if orderStatus === 2}
                        <option selected disabled>UNFULFILLED</option>
                    {:else if orderStatus === 3}
                        <option selected disabled>PROCESSING</option>
                    {:else if orderStatus === 4}
                        <option selected disabled>FULFILLED</option>
                    {/if}
                    <option value="1">INCOMING</option>
                    <option value="2">UNFULFILLED</option>
                    <option value="3">PROCESSING</option>
                    <option value="4">FULFILLED</option>
                </select>
            </div>
        </td>
    </tr>
</tbody>

<style>
    .text {
        font-size: 17px;
    }
</style>