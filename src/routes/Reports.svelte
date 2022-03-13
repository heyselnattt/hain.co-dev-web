<script>
    import ButtonBack from "$lib/components/ButtonBack.svelte";
    import NavbarWithSearch from "$lib/components/NavbarWithSearch.svelte";
    import ReportsTableRow from "$lib/components/ReportsTableRow.svelte";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarWithSearch/>

<div class="container">
    <div class="columns has-text-centered pt-5">
        <div class="column is-4 has-text-centered">
            <a href="Database">
                <ButtonBack/>
            </a>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Reports
            </p>
        </div>
    </div>

    <div class="column is-10 is-offset-1 pl-5 pt-0">
        <table class="table is-hoverable is-fullwidth">
            <thead>
            <tr>
                <th>Record ID</th>
                <th>Date Range</th>
                <th>Record Type</th>
                <th></th>
            </tr>
            </thead>
            <ReportsTableRow recordID="0001" dateRange="11 Nov - 17 Nov" recordType="Weekly"/>
            <ReportsTableRow recordID="0002" dateRange="12 Feb - 24 Feb" recordType="Monthly"/>
            <ReportsTableRow recordID="0003" dateRange="9 Sept - 15 Sept" recordType="Monthly"/>
            <ReportsTableRow recordID="0004" dateRange="26 Oct - 30 Oct" recordType="Weekly"/>
            <ReportsTableRow recordID="0005" dateRange="12 Jan - 21 Jan" recordType="Weekly"/>
            <ReportsTableRow recordID="0006" dateRange="20 Dec - 25 Dec" recordType="Weekly"/>
            <ReportsTableRow recordID="0007" dateRange="1 Mar - 10 Mar" recordType="Monthly"/>
            <ReportsTableRow recordID="0008" dateRange="4 Apr - 16 Apr" recordType="Weekly"/>
        </table>
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }

    table {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }
</style>