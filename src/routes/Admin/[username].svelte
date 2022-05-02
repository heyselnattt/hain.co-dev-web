<script context="module">
    import axios from "$lib/api/index"
    export async function load({ fetch, params }) {
        try {
            const username = params.username;
            const admin = await axios.get(`/admin/${username}`);
            console.log(admin)
            return {
                props: {
                    admin
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
    import ButtonSave from "$lib/components/buttons/ButtonSave.svelte";
    import ButtonSwitch from "$lib/components/buttons/ButtonSwitch.svelte";
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";

    export let admin;
</script>

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
            <ButtonSave link="../Admin"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        {#await admin}
            Waiting data
        {:then admin}
            <!-- TODO switch to bound inputs -->
            <!-- TODO: yung is active pa na checkbox ilagay -->
            <FieldWithValue 
                name="Name"
                value={admin.data.admin_full_name}/>
            <FieldWithValue
                name="Username"
                value={admin.data.admin_username}/>
            <FieldWithValue 
                name="Password"
                value={admin.data.admin_password}/>
            {:catch e} 
                {e}
            {/await}

        <div class="column is-12"></div>
    </div>
</div>

<div class="columns is-centered has-text-link pb-6">
    {#await admin}
        Waiting data
    {:then admin}
        <ButtonSwitch 
            isOn={admin.data.admin_is_active}
        />
    {:catch e}
        {e}
    {/await}
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>