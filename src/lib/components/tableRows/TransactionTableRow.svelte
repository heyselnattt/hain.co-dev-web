<script lang="ts">
    export let id;
    export let agent;
    export let description;
    export let type;
    export let amount;
    export let date;
</script>

<tbody>
    <tr class="text is-clickable" >
        <th>{id}</th>
        <td>{agent}</td>
        <td>{description}</td>
        <td>{amount}</td>
        <td>{type}</td>
        <td>{date}</td>
    </tr>
</tbody>

<style>
    .text {
        font-size: 17px;
    }
</style>