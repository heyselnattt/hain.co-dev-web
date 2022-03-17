<script lang="ts">
    export let num: string;
    export let name: string;
    // TODO add position enum
    export let position;
    export let contactNum: string;
    export let address: string;
</script>

<tbody>
<tr class="text is-clickable">
    <th>{num}</th>
    <td>{name}</td>
    <td>{position}</td>
    <td>{contactNum}</td>
    <td>{address}</td>
</tr>
</tbody>

<style>
    .text {
        font-size: 17px;
    }
</style>