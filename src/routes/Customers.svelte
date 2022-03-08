<script>
    import NavbarWithSearch from "$lib/components/NavbarWithSearch.svelte";
    import TableRow from "$lib/components/TableRow.svelte";
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarWithSearch/>

<div class="container">
    <div class="columns has-text-centered pt-5">
        <div class="column is-4">
            <a class="btn-txt button is-link is-rounded" href="Database">
                <img class="img1" src="back.png" alt="back"/>
                <p class="ml-3">
                   Back
                </p>
            </a>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Customers
            </p>
        </div>
        <div class="column is-4">
            <a class="btn-txt button is-link is-rounded" href="/">
                <img class="img2" src="add.png" alt="back"/>
                <p class="ml-2">
                   Add Record
                </p>
            </a>
        </div>
    </div>

    <div class="column is-10 is-offset-1 pl-5 pt-0">
        <table class="table is-hoverable is-fullwidth">
            <thead>
                <tr>
                    <th>No.</th>
                    <th>Name</th>
                    <th>Contact No.</th>
                    <th>Email</th>
                </tr>
            </thead>
            <TableRow num="1" name="Taylor Swift" contactNum="09254698852" email="taylorswift@gmail.com"/>
            <TableRow num="2" name="Cecil Uy" contactNum="09252236478" email="uy.cecil@gmail.com"/>
            <TableRow num="3" name="Adrian Tan" contactNum="09154223687" email="adriantan123@gmail.com"/>
            <TableRow num="4" name="Trixie Cruz" contactNum="09356684521" email="cruztrixie@gmail.com"/>
            <TableRow num="5" name="Mark Johnson" contactNum="09054865523" email="markjohnson1@gmail.com"/>
            <TableRow num="6" name="Ralph Tirao" contactNum="09683105246" email="tirao_ralph@gmail.com"/>
            <TableRow num="7" name="Mhea Niere" contactNum="09685233451" email="mheaniere@gmail.com"/>
            <TableRow num="8" name="Rhea Valdez" contactNum="09352648551" email="rhea.valdez@gmail.com"/>
            <TableRow num="9" name="Charles Maverick" contactNum="09302922012" email="charlesmaverick@gmail.com"/>
            <TableRow num="10" name="Angel Lawson" contactNum="09684521404" email="angel_lawson@gmail.com"/>
            <TableRow num="11" name="Marco De Jesus" contactNum="09156324521" email="marco.dejesus@gmail.com"/>
        </table>
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
    .btn-txt {
        font-size: 20px;
        font-family: 'Karla', sans-serif;
    }
    .img1 {
        width: 20px;
    }
    .img2 {
        width: 30px;
    }
    table {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }
</style>