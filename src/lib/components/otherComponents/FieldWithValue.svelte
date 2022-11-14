<script lang="ts">
    export let value;
    export let name;
    export let isReadOnly = false;
</script>

<div class="column is-3 is-offset-2">
    <p class="pText has-text-link ml-4 mb-1">
        {name}
    </p>
    <input class="pText input is-rounded" type="text" value={value} readonly={isReadOnly}/>
</div>

<style>
    .pText {
        font-family: 'Montserrat', sans-serif;
        font-size: 20px;
    }
</style>