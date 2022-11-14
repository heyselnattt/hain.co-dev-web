<script lang="ts">
    import ButtonEditTable from "../buttons/ButtonEditTable.svelte";

    export let num: number;
    export let productName: string;
    export let price: number;
    export let type: string;
    export let code: string;
    export let link: string;
</script>

<tbody>
    <tr class="text is-clickable">
        <th>{num}</th>
        <td>{productName}</td>
        <td>{price}</td>
        <td>{type}</td>
        <td>{code}</td>
        <td><ButtonEditTable link={link}/></td>
    </tr>
</tbody>

<style>
    .text {
        font-family: 'Montserrat', sans serif;
        font-size: 17px;
    }
</style>