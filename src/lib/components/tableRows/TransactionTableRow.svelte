<script lang="ts">
    import moment from "moment/moment.js";
    export let id;
    export let agent;
    export let description;
    export let type;
    export let amount;
    export let date;
    const oldTimeString = moment(date).format("MM-DD-YYYY h:mma");
    const adjustedDate = moment(oldTimeString).add(8, "hours").format("MM-DD-YYYY h:mma");
</script>

<tbody>
    <tr class="text is-clickable">
        <th>{id}</th>
        <td>{agent}</td>
        <td>{description}</td>
        <td>{amount}</td>
        <td>{type}</td>
        <td>{oldTimeString}</td>
    </tr>
</tbody>

<style>
    .text {
        font-family: 'Montserrat', sans serif;
        font-size: 17px;
    }
</style>