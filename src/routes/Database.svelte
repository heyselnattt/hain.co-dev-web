<script context="module">
    import {row_count} from "$lib/stores/metaStore";
    import Card from "$lib/components/otherComponents/Card.svelte";
    import LogoutNavbar from "$lib/components/navbars/LogoutNavbar.svelte";
    import FixedLoadingScreen from "$lib/components/otherComponents/FixedLoadingScreen.svelte";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<LogoutNavbar/>

<div class="container">
    <p class="text has-text-centered has-text-link has-text-weight- mt-5">
        Database
    </p>

    <div class="columns is-centered is-multiline pt-5">
        {#await $row_count}
            <FixedLoadingScreen/>
        {:then row_count}
            {console.log(row_count)}
            <Card name="Customers"
                  entries={row_count['data'][1]['rows']}
                  sub="customers"
                  imagePath="images/customersIcon.png"
                  link="Customers"/>
            <Card name="Canteen Staff"
                  entries={row_count['data'][4]['rows']}
                  sub="staff entries"
                  imagePath="images/canteenStaffIcon.png"
                  link="CanteenStaff"/>
            <Card name="Products"
                  entries={row_count['data'][3]['rows']}
                  sub="items"
                  imagePath="images/foodIcon.png"
                  link="Food"/>
            <Card name="Administrators"
                  entries={row_count['data'][0]['rows']}
                  sub="records"
                  imagePath="images/adminIcon.png"
                  link="Admin"/>
            <Card name="Orders"
                  entries={row_count['data'][2]['rows']}
                  sub="orders"
                  imagePath="images/ordersIcon.png"
                  link="Orders"/>
            <Card name="Transactions"
                  entries={row_count['data'][5]['rows']}
                  sub="entries"
                  imagePath="images/transactionIcon.png"
                  link="Transaction"/>
        {:catch error}
            <p>{error}</p>
        {/await}

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
