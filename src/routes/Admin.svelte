<script lang="ts">
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import Card from "$lib/components/otherComponents/Card.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/buttons/ButtonAddRecord.svelte";
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
        <Card name="001" entries="" sub="" imagePath="images/adminIcon.png" link="AdminInfo"/>
        <Card name="002" entries="" sub="" imagePath="images/adminIcon.png" link="AdminInfo"/>
        <Card name="003" entries="" sub="" imagePath="images/adminIcon.png" link="AdminInfo"/>
        <Card name="004" entries="" sub="" imagePath="images/adminIcon.png" link="AdminInfo"/>
        <Card name="005" entries="" sub="" imagePath="images/adminIcon.png" link="AdminInfo"/>
        <Card name="006" entries="" sub="" imagePath="images/adminIcon.png" link="AdminInfo"/>
        <!-- {#each Array(100) as a}
        <Card name="{a}" sub="{a}-sub" link="/"/>
        {/each} -->
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>