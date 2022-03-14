<script lang="ts">
    export let num;
    export let name: string;
    export let contactNum: string;
    export let email: string;
</script>

<tbody>
<tr class="text is-clickable">
    <th>{num}</th>
    <td>{name}</td>
    <td>{contactNum}</td>
    <td>{email}</td>
</tr>
</tbody>

<style>
    .text {
        font-size: 17px;
    }
</style>