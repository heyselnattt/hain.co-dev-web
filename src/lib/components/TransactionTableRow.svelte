<script lang="ts">
    export let num;
    export let name;
    export let desc;
    export let amount;
    export let type;
</script>

<tbody>
    <tr class="text is-clickable" >
        <th>{num}</th>
        <td>{name}</td>
        <td>{desc}</td>
        <td>{amount}</td>
        <td>{type}</td>
    </tr>
</tbody>

<style>
    .text {
        font-size: 17px;
    }
</style>