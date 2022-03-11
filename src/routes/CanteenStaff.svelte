<script>
    import BtnAddRecord from "$lib/components/BtnAddRecord.svelte";
    import BtnBack from "$lib/components/BtnBack.svelte";
    import NavbarWithSearch from "$lib/components/NavbarWithSearch.svelte";
    import CsTableRow from "$lib/components/CSTableRow.svelte";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarWithSearch/>

<div class="container">
    <div class="columns has-text-centered pt-5">
        <div class="column is-4 has-text-centered">
            <a href="Database"><BtnBack/></a>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Canteen Staffs
            </p>
        </div>
        <div class="ml-6 pl-6">
            <a href="AddNewCS"> <BtnAddRecord/> </a>
        </div>
    </div>

    <div class="column is-10 is-offset-1 pl-5 pt-0">
        <table class="table is-hoverable is-fullwidth">
            <thead>
                <tr>
                    <th>No.</th>
                    <th>Name</th>
                    <th>Position</th>
                    <th>Contact No.</th>
                    <th>Address</th>
                </tr>
            </thead>
            <CsTableRow num="1" name="Salaveria, Rence" position="Cook" contactNum="09123456789" address="02 Toronto St. Malinta, Valenzuela City"/>
            <CsTableRow num="2" name="Delica, Lean O." position="Cook" contactNum="09523648951" address="211 Maple St. Pateros, Metro Manila"/>
            <CsTableRow num="3" name="Briguel, Jen" position="Cleaner" contactNum="09152463894" address="123 Canada Compd., Quezon City"/>
            <CsTableRow num="4" name="Monton, Che" position="Cleaner" contactNum="09681125433" address="45 Mexico St. Po.."/>
            <CsTableRow num="5" name="Baguio, Janine" position="Dishwasher" contactNum="09352264871" address="#1 Thesis St. Punturin, Valenzuela City"/>
            <CsTableRow num="6" name="Fernando, Angela" position="Cashier" contactNum="09256855497" address="Blk. 2 Phase 2 Amabelle Homes, Caloocan City"/>
            <CsTableRow num="7" name="Roche, Razelle" position="Server" contactNum="09055964325" address="78 Maysan Rd. Maysan, Valenzuela City"/>
            <CsTableRow num="8" name="Lee, Mark" position="Server" contactNum="09994563221" address="024 Buenavista St. Malinta, Valenzuela City"/>
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