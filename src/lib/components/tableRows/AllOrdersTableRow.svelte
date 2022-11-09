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
        <th>{new Date(orderDate).toLocaleString()}</th>
        <th>{staffUsername}</th>
        <th>
           {orderStatus}
        </th>
    </tr>
</tbody>

<style>
    .text {
        font-family: 'Montserrat', sans serif;
        font-size: 17px;
    }
</style>