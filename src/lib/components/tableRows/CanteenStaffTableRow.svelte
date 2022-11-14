<script lang="ts">
    import ButtonEditTable from "../buttons/ButtonEditTable.svelte";

    export let num: string;
    export let name: string;
    export let position: string;
    export let contactNum: string;
    export let link: string;
</script>

<tbody>
    <tr class="text is-clickable">
        <th>{num}</th>
        <td>{name}</td>
        <td>{position}</td>
        <td>{contactNum}</td>
        <td><ButtonEditTable link={link}/></td>
    </tr>
</tbody>

<style>
    .text {
        font-family: 'Montserrat', sans serif;
        font-size: 17px;
    }
</style>