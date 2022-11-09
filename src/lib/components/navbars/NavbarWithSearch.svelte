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
            <div class="field is-grouped">
                <p class="control is-expanded">
                    <input class="input is-rounded" type="text" placeholder="Search">
                </p>
                <p class="control">
                    <a class="text button has-text-link is-rounded" href="/">
                        Search
                    </a>
                </p>
            </div>
        </div>
    </div>
</nav>

<style>
    .title {
        font-family: 'Titan One', cursive;
        font-size: 50px;
    }

    .text {
        font-family: 'Montserrat', sans-serif;
    }
</style>