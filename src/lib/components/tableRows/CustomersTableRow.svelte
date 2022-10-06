<script lang="ts">
    import ButtonEditTable from "../buttons/ButtonEditTable.svelte";

    export let num;
    export let name: string;
    export let customerLastName: string;
    export let email: string;
    export let link: string;
</script>

<tbody>
    <tr class="text is-clickable">
        <th>{num}</th>
        <td>{name}</td>
        <td>{customerLastName}</td>
        <td>{email}</td>
        <td><ButtonEditTable link={link}/></td>
    </tr>
</tbody>

<style>
    .text {
        font-size: 17px;
    }
</style>