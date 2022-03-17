<script lang="ts">
    export let name: string;
    export let sub: string;
    export let link = " ";
    export let imagePath;
    export let entries;
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<div class="column is-2 mx-5">
    <a href={link}>
        <div class="card">
            <div class="card-image is-flex is-justify-content-center pt-4">
                <img src={imagePath} alt="logo"/>
            </div>
            <div class="card-content pt-3 pb-4">
                <p class="text is-4 has-text-centered has-text-link">{name}</p>
                <p class="text1 is-6 has-text-centered">{entries} {sub}</p>
            </div>
        </div>
    </a>
</div>

<style>
    .card {
        border: 3px solid hsl(222, 4%, 52%);
        border-radius: 20px;
    }

    .text {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }

    .text1 {
        font-family: 'Karla', sans-serif;
        font-size: 15px;
    }

    img {
        max-width: 130px;
    }
</style>