<script lang="ts">
    import moment from "moment/moment";
    export let id;
    export let agent;
    export let description;
    export let type;
    export let amount;
    export let date;
    const oldTimeString = moment(date);
    const adjustedDate = moment(oldTimeString).add(8, "hours").format("MM-DD-YYYY h:mma");
</script>

<tbody>
    <tr class="text is-clickable">
        <th>{id}</th>
        <td>{agent}</td>
        <td>{description}</td>
        <td>{amount}</td>
        <td>{type}</td>
        <td>{adjustedDate}</td>
    </tr>
</tbody>

<style>
    .text {
        font-size: 17px;
    }
</style>