<script lang="ts">
    import HomeNavbar from "$lib/components/navbars/HomeNavbar.svelte";
    import ErrorMessage from "$lib/components/otherComponents/ErrorMessage.svelte";
    import ErrorMessageContainer from "$lib/components/otherComponents/ErrorMessageContainer.svelte";

    let username: string
    let password: string
    let loggedIn = false;
</script>

<svelte:head>
    <link
        href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap"
        rel="stylesheet"
    />
    <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Lobster&display=swap"
    />
</svelte:head>

<HomeNavbar/>

<div class="container">
    <div class="columns is-multiline">
        <div class="column is-4 is-offset-2">
            <section class="section pt-0"></section>
            <section class="section is-flex is-justify-content-center pb-3">
                <img src="images/Blue_Circle.png" alt="logo" class="logo"/>
            </section>
            <section class="section is-medium pb-0 has-text-centered is-paddingless">
                <h1 class="has-text-link">
                    Hain.co
                </h1>
            </section>
        </div>

        <div class="c1 column is-5">
            <div class="column is-12"></div>
            <div class="column is-12"></div>
            <div class="column is-12"></div>
            <div class="column is-12"></div>
            <div class="column is-12"></div>
            <div class="column is-12"></div>
            <div class="container is-flex is-justify-content-center is-flex-wrap-wrap">
                <h1 class="has-text-link has-text-centered mb-5">
                    Login to Application
                </h1>
                <section class="section is-paddingless">
                    <div class="container px-5 is-flex is-flex-wrap-wrap">
                        <p class="text has-text-link ml-6 mb-2 pl-3">
                            Username
                        </p>
                        <input class="input is-rounded mx-6 mb-3"
                               type="text"
                               placeholder="ID Number"
                               bind:value={username}/>
                        <p class="text has-text-link ml-6 mb-2 pl-3">
                            Password
                        </p>
                        <input class="input is-rounded mx-6"
                               type="password"
                               placeholder="Password"
                               bind:value={password}/>
                    </div>
                </section>
                <!-- TODO add the session for logging in -->
                    <button class="button is-link is-rounded mt-5">Login</button>
            </div>
        </div>
    </div>
</div>

<!-- draft error message -->
<!-- <ErrorMessageContainer>
    {#if er}
        {#each Array(1) as a}    
            <ErrorMessage message="tanga mo mali!"/>
        {/each}
    {/if}
</ErrorMessageContainer> -->

<style>
    h1 {
        font-family: 'Lobster', cursive;
        font-size: 45px;
    }

    .text {
        font-family: 'Karla', sans-serif;
        font-size: 18px;
    }

    .logo {
        max-width: 350px;
    }
</style>