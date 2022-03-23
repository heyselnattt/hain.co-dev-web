<script lang="ts">
    export let link: string = " ";
</script>

<a href="{link}">
    <button class="btn-txt button is-link is-rounded">
        <img class="img2" src="../static/images/add.png" alt="Add record"/>
        <p class="ml-2">
            Add Record
        </p>
    </button>
</a>

<style>
    .img2 {
        width: 30px;
    }

    .btn-txt {
        font-size: 20px;
        font-family: 'Karla', sans-serif;
    }
</style>
