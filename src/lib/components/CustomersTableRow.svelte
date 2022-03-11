<script>
    export let num;
    export let name;
    export let contactNum;
    export let email;
</script>

<tbody>
    <tr class="text is-clickable" >
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