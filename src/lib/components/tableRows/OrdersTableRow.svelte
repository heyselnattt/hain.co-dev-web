<script lang="ts">
    export let productCode;
    export let customerEmail;
    export let orderRequest;
    export let orderDate;
    export let staffUsername;
    export let orderStatus;
    export let orderNumber;
</script>

<tbody>
    <tr class="text is-clickable">
        <th>{productCode}</th>
        <td>{customerEmail}</td>
        <td>{orderRequest}</td>
        <td>{orderDate}</td>
        <td>{staffUsername}</td>
        <td>{orderStatus}</td>
        <td>{orderNumber}</td>
    </tr>
</tbody>

<style>
    .text {
        font-size: 17px;
    }
</style>