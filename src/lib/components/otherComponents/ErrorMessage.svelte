<script>
    export let message;
    let close = false;
</script>

<div class="notification is-danger {close ? "close" : ""}">
    <button on:click={()=>{close=true}} class="delete"></button>
    {message}
</div>

<style>
    .notification{
        min-height: 50px;
    }
    .close {
        display: none;
    }
</style>