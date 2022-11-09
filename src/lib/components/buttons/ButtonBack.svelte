<script lang="ts">
    export let link: string = " ";
</script>

<a href="{link}">
    <button class="button is-rounded is-link btn-txt">
        <img class="img1" src="../static/images/back.png" alt="back"/>
        <p class="ml-3">
            Back
        </p>
    </button>
</a>

<style>
    .btn-txt {
        font-size: 20px;
        font-family: 'Montserrat', sans-serif;
    }

    .img1 {
        width: 20px;
    }
</style>