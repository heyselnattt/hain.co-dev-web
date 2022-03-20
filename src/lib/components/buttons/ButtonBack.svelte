<script lang="ts">
    export let link: string = " ";
</script>

<a href="{link}">
    <button class="button is-rounded is-link btn-txt">
        <img class="img1" src="images/back.png" alt="back"/>
        <p class="ml-3">
            Back
        </p>
    </button>
</a>

<style>
    .btn-txt {
        font-size: 20px;
        font-family: 'Karla', sans-serif;
    }

    .img1 {
        width: 20px;
    }
</style>