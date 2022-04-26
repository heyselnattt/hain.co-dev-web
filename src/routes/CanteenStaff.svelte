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
    import FixedLoadingScreen from "$lib/components/otherComponents/FixedLoadingScreen.svelte";
    import {staffs} from "$lib/stores/staffStore";

    let staffNumber = 1;
    const counter = (): number => {
        return staffNumber++;
    }

    const identifyType = (code: number): string => {
        switch(code) {
            case 1:
                return "Chef"

            case 2:
                return "Cashier"

            case 3:
                return "Server"
        }
    }
</script>

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
          
            <!-- Temporary placeholders:
                    Position - username
                    Address - email -->
            {#await $staffs}
                <FixedLoadingScreen/>
            {:then staff}
                {#each staff.data as info}
                    <!--TODO add property for the link for the individual staff
                        TODO add property to access the object
                    -->
                    <CanteenStaffTableRow
                        num={counter()}
                        name={info.staff_full_name}
                        position={identifyType(info.staff_position)}
                        contactNum={info.staff_contact_number}
                        address={info.staff_address}
                        link={`/CanteenStaff/${info.staff_id}`}/>
                {/each}
            {:catch err}
                <p>{err.message}</p>
            {/await}
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