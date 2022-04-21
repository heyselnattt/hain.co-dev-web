<script context="module">
    export async function load({ fetch }) {
        const res = await fetch('https://jsonplaceholder.typicode.com/users')
        const canteenStaffs = await res.json()

        if (res.ok) {
            return {
                props: {
                    canteenStaffs
                }
            }
        }

        return {
            status: res.status,
            error: new Error('Could not fetch the cateen staffs.')
        }
    }
</script>

<script lang="ts">
    import NavbarWithSearch from "$lib/components/navbars/NavbarWithSearch.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/buttons/ButtonAddRecord.svelte";
    import CanteenStaffTableRow from "$lib/components/tableRows/CanteenStaffTableRow.svelte";

    export let canteenStaffs;
</script>

<NavbarWithSearch />

<div class="container">
    <div class="columns has-text-centered pt-5">
        <div class="column is-4">
            <ButtonBack link="Database"/>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Canteen Staffs
            </p>
        </div>
        <div class="column is-3 ml-6">
            <ButtonAddRecord link="CanteenStaff/AddNewCanteenStaff" />
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
                    <th></th>
                </tr>
            </thead>

            <!-- <CanteenStaffTableRow num="1" name="Salaveria, Rence" position="Cook" contactNum="09123456789"
                                  address="02 Toronto St. Malinta, Valenzuela City"/>
            <CanteenStaffTableRow num="2" name="Delica, Lean O." position="Cook" contactNum="09523648951"
                                  address="211 Maple St. Pateros, Metro Manila"/>
            <CanteenStaffTableRow num="3" name="Briguel, Jen" position="Cleaner" contactNum="09152463894"
                                  address="123 Canada Compd., Quezon City"/>
            <CanteenStaffTableRow num="4" name="Monton, Che" position="Cleaner" contactNum="09681125433"
                                  address="45 Mexico St. Po.."/>
            <CanteenStaffTableRow num="5" name="Baguio, Janine" position="Dishwasher" contactNum="09352264871"
                                  address="#1 Thesis St. Punturin, Valenzuela City"/>
            <CanteenStaffTableRow num="6" name="Fernando, Angela" position="Cashier" contactNum="09256855497"
                                  address="Blk. 2 Phase 2 Amabelle Homes, Caloocan City"/>
            <CanteenStaffTableRow num="7" name="Roche, Razelle" position="Server" contactNum="09055964325"
                                  address="78 Maysan Rd. Maysan, Valenzuela City"/>
            <CanteenStaffTableRow num="8" name="Lee, Mark" position="Server" contactNum="09994563221"
                                  address="024 Buenavista St. Malinta, Valenzuela City"/> -->

            {#each canteenStaffs as canteenStaff}
                <CanteenStaffTableRow
                    num={canteenStaff.id}
                    name={canteenStaff.name}
                    position={canteenStaff.username}
                    contactNum={canteenStaff.phone}
                    address={canteenStaff.email}
                    link={`/CanteenStaff/${canteenStaff.id}`}
                />
            {/each}

            <!-- Temporary placeholders:
                    Position - username
                    Address - email -->
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