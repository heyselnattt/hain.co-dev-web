<script>
    import {row_count} from "$lib/stores/metaStore";
    import Card from "$lib/components/otherComponents/Card.svelte";
    import LogoutNavbar from "$lib/components/navbars/LogoutNavbar.svelte";
    import FixedLoadingScreen from "$lib/components/otherComponents/FixedLoadingScreen.svelte";

    export let todayAmount = 5000;
    export let thisWeekAmount = 8550;
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<LogoutNavbar/>

<div class="container">
    <p class="text has-text-centered has-text-link has-text-weight-bold mt-5">
        Database
    </p>

    <div class="columns is-0 mt-3 is-centered">
        {#await $row_count}
            <FixedLoadingScreen/>
        {:then row_count}
        <div class="column is-4 card p-3">
            <div class="is-align-items-center w-100p h-100p is-flex is-flex-direction-column">
                <!-- revenue -->
                <div class="karla has-text-black txt-weight-900 txt-size-50">
                    REVENUE
                </div>
                <!-- date -->
                <div class="karla has-text-black">
                    {new Date().toDateString()}
                </div>
                <!-- today's sales -->
                <div class="karla has-text-link txt-weight-900 txt-size-30 w-100p pl-5">
                    <br>TODAY:
                </div>
                <!-- today's amount -->
                <div class="karla has-text-link txt-weight-900 txt-size-70">
                    {todayAmount}
                </div>
                <!-- this week's sales -->
                <div class="karla has-text-black txt-size-30 w-100p pl-5">
                    <br>THIS WEEK:
                </div>
                <!-- this week's amount -->
                <div class="karla has-text-black txt-size-40">
                    {thisWeekAmount}
                </div>
            </div>
        </div>
        <div class="column is-8 p-0">
            <div class="columns is-centered is-multiline">
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
        
                <!-- {#each Array(100) as a}
                <Card name="{a}" sub="{a}-sub" link="/"/>
                {/each} -->
            </div>
        </div>
        {:catch error}
            <p>{error}</p>
        {/await}
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }

    .card {
        border: 3px solid hsl(222, 4%, 52%);
        border-radius: 20px;
    }
</style>
