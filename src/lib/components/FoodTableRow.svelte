<script>
    export let num;
    export let productName;
    export let price;
    export let type;
</script>

<tbody>
<tr class="text is-clickable">
    <th>{num}</th>
    <td>{productName}</td>
    <td>{price}</td>
    <td>{type}</td>
</tr>
</tbody>

<style>
    .text {
        font-size: 17px;
    }
</style>