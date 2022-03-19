<script lang="ts">
    import NavbarSolo from "$lib/components/NavbarSolo.svelte";
    import Card from "$lib/components/Card.svelte";
    import ButtonBack from "$lib/components/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/ButtonAddRecord.svelte";

    import {admins} from '$lib/stores/adminStore';
</script>

<NavbarSolo/>

<div class="container">
    <div class="columns has-text-centered pt-5">
        <div class="column is-4 has-text-centered">
            <a href="Database">
                <ButtonBack/>
            </a>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Administrators
            </p>
        </div>
        <div class="column is-3 ml-4">
            <a href="AddNewAdmin">
                <ButtonAddRecord/>
            </a>
        </div>
    </div>

    <div class="columns is-centered is-multiline pt-5">
        {#await $admins}
            <!-- waiting for data component -->
            <p>Waiting for data</p>
        {:then admin}
            {#each admin.data as info}
                <Card
                    name={info.admin_username}
                    sub={info.admin_full_name}
                    image="images/adminIcon.png"
                    link="Admin/{info.admin_id}"/>
            {/each}
        {:catch err}
            <p>{err.message}</p>
            <!-- error message component -->
        {/await}
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>