<script lang="ts">
    export let recordID;
    export let dateRange;
    export let recordType;
</script>

<tbody>
<tr class="text is-clickable">
    <th>{recordID}</th>
    <td>{dateRange}</td>
    <td>{recordType}</td>
    <td><img src="images/downloadIcon.png" alt="download"></td>
</tr>
</tbody>

<style>
    .text {
        font-size: 17px;
    }

    img {
        max-width: 25px;
    }
</style>