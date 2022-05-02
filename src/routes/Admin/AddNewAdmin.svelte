<script>
    import Discard from "$lib/components/buttons/Discard.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import axios from "$lib/api/index";
    import {goto} from "$app/navigation";

    export let value;
    export let name;
    export let confirmPassword = "";
    let admin = {
        admin_full_name: null,
        admin_username: null,
        admin_password: null,
        admin_position: 1,
        admin_is_active: true,
    }

    const addAdminToDatabase = async () => {
        try {
            let response = await axios.post('/admin/new_admin', admin)
            console.log(response)
            await goto("../Admin")
        } catch (e) {
            console.log(e)
        }
    }
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../Admin"/>
        </div>
        <div class="column is-4">
            <p class="text1 has-text-link">
                New Administrator
            </p>
        </div>
        <div class="column is-3 ml-6">
            <Discard link="../Admin"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
               Full Name
            </p>
            <input class="pText input is-rounded" type="text" bind:value={admin.admin_full_name}/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                Username
            </p>
            <input class="pText input is-rounded" type="text" bind:value={admin.admin_username}/>
        </div>
        <div class="column is-12"></div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                Password
            </p>
            <input class="pText input is-rounded" type="password" bind:value={admin.admin_password}/>
        </div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
    </div>

    <!-- Add record button -->
    <div class="mb- has-text-centered">
        <button class="btn-txt button is-link is-rounded" on:click={addAdminToDatabase}>Add Admin</button>
    </div>
</div>

<style>
    .text1 {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
    .pText {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }
    .btn-txt {
        font-size: 20px;
        font-family: 'Karla', sans-serif;
    }
</style>