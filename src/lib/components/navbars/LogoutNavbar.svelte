<script>
    import {goto} from "$app/navigation";

    const logout = async () => {
        localStorage.removeItem("admin")
        await goto("/")
    }
</script>
<svelte:head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lobster&display=swap"/>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<nav class="navbar has-background-link">
    <div class="navbar-start ml-6">
        <p class="title navbar-item has-text-weight-light has-text-white">
            Hain.co Admin
        </p>
    </div>
    <div class="navbar-end mr-6 buttons">
        <div class="navbar-item">
            <button class="text button has-text-link" on:click={logout}>
                Logout
            </button>
        </div>
    </div>
</nav>

<style>
    .title {
        font-family: 'Lobster', cursive;
        font-size: 50px;
    }

    .text {
        font-family: 'Karla', sans-serif;
    }
</style>