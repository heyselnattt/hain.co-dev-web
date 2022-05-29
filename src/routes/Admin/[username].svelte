<script context="module">
    import axios from "$lib/api/index"

    export async function load({fetch, params}) {
        try {
            const username = params.username;
            const admin = await axios.get(`/admin/${username}`);
            const oldUsername = admin.data.admin_username
            console.log(admin)
            return {
                props: {
                    admin,
                    oldUsername
                }
            }
        } catch (e) {
            return {
                error: new Error('Can\'t fetch the admin')
            }
        }
    }
</script>

<script>
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import {goto} from "$app/navigation";

    export let admin;
    export let oldUsername;

    let newAdmin = {
        admin_full_name: null,
        admin_username: null,
        admin_password: null,
        admin_position: 1,
        admin_is_active: true,
    }

    const updateAdminToDatabase = async () => {
        try {
            let response = await axios.put(`/admin/update_admin/${oldUsername}`, newAdmin)
            console.log(response)
            await goto('../Admin');
        } catch (e) {
            console.log(e);
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
            <p class="text has-text-link">
                Admin's Information
            </p>
        </div>
        <div class="column is-3 ml-6">
            <button class="button is-rounded is-info btn-txt" on:click={updateAdminToDatabase}>
                <p class="ml-4 mr-4 has-text-white">
                    Save
                </p>
            </button>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12">
            <div class="has-text-centered pText">Make sure to fill up all information boxes</div>
        </div>
        {#await admin}
            Waiting data
        {:then admin}
            <!-- TODO switch to bound inputs -->
            <!-- TODO: yung is active pa na checkbox ilagay -->
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    Current Name: {admin.data.admin_full_name}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newAdmin.admin_full_name}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    Current Username: {admin.data.admin_username}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newAdmin.admin_username}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    Current Password: {admin.data.admin_password}
                </p>
                <input class="pText input is-rounded" type="password" bind:value={newAdmin.admin_password}/>
            </div>
        {:catch e}
            {e}
        {/await}
        <div class="column is-12">
            <div class="columns is-centered has-text-link pb-6">
                {#await admin}
                    Waiting data
                {:then admin}
                    <div class="field">
                        {#if admin.data.admin_is_active}
                            <div class="pText has-text-centered">Admin Currently Active</div>
                        {:else}
                            <div class="pText has-text-centered">Admin Currently Inactive</div>
                        {/if}
                        <input id="switchLarge switchColorDefault switchRoundedDefault"
                               type="checkbox"
                               name="switchLarge switchColorDefault switchRoundedDefault"
                               class="switch is-large is-link is-rounded"
                               bind:checked={newAdmin.admin_is_active}>
                        {#if newAdmin.admin_is_active}
                            <label for="switchLarge switchColorDefault switchRoundedDefault">Active</label>
                        {:else}
                            <label for="switchLarge switchColorDefault switchRoundedDefault">Inactive</label>
                        {/if}
                    </div>
                {:catch e}
                    {e}
                {/await}
            </div>
        </div>
    </div>
</div>


<style>
    .text {
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