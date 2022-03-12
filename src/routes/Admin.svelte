<script>
    import NavbarSolo from "$lib/components/NavbarSolo.svelte";
    import Card from "$lib/components/Card.svelte";
    import ButtonBack from "$lib/components/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/ButtonAddRecord.svelte";
</script>
    
    <svelte:head>
        <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
    </svelte:head>
    
    <NavbarSolo />

    <div class="container">
        <div class="columns has-text-centered pt-5">
            <div class="column is-4 has-text-centered">
                <a href="Database"><ButtonBack /></a>
            </div>
            <div class="column is-4">
                <p class="text has-text-link">
                    Administrators
                </p>
            </div>
            <div>
                <a href="/"> <ButtonAddRecord /> </a>
            </div>
        </div>
    </div>

    <div class="columns is-centered is-multiline pt-5">
        <Card name="001" entries="230" sub="customers" image="images/adminIcon.png"/>
        <Card name="002" entries="15" sub="staff entries" image="images/adminIcon.png"/>
        <Card name="003" entries="15" sub="items" image="images/adminIcon.png"/>
        <Card name="004" entries="4" sub="records" image="images/adminIcon.png"/>
        <Card name="005" entries="130" sub="entries" image="images/adminIcon.png"/>
        <Card name="006" entries="370" sub="entries" image="images/adminIcon.png"/>
        <!-- {#each Array(100) as a}
        <Card name="{a}" sub="{a}-sub" link="/"/>
        {/each} -->
    </div>

    <style>
        .text {
            font-family: 'Karla', sans-serif;
            font-size: 40px;
        }
    </style>