<script>
    export let num;
    export let name;
    export let position;
    export let contactNum;
    export let address;
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