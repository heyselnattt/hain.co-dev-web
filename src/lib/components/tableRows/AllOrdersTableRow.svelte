<script lang="ts">
    export let productCode      : string
    export let customerEmail    : string
    export let orderRequest     : string
    export let orderDate        : Date
    export let staffUsername    : string
    export let orderStatus      : number
    export let orderNumber      : number
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