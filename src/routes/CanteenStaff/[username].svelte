<script context="module">
    import axios from "$lib/api/index"
    export async function load({ fetch, params }) {
        try {
            const username = params.username;
            const canteenStaff = await axios.get(`/staff/${username}`);
            console.log(canteenStaff)
            return {
                props: {
                    canteenStaff
                }
            }
        } catch (e) {
            return {
                error: new Error('Can\'t fetch the canteen staff')
            }
        }
    }
</script>

<script lang="ts">
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonSave from "$lib/components/buttons/ButtonSave.svelte";
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";

    export let canteenStaff;
    const identifyType = (code) => {
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

<NavbarSolo />

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../CanteenStaff" />
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Canteen Staff's Information
            </p>
        </div>
        <div class="column is-3 ml-6">
            <ButtonSave link="../CanteenStaff" />
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>

        {#await canteenStaff}
            Waiting data
        {:then staff}
            <!-- TODO switch to bound inputs -->
            <FieldWithValue
                name="Name"
                value={staff.data.staff_full_name}/>
            <FieldWithValue
                name="Position"
                value={identifyType(staff.data.staff_position)}/>
            <FieldWithValue
                name="Contact No."
                value={staff.data.staff_contact_number} />
            <FieldWithValue
                name="Address"
                value={staff.data.staff_address} />
            <FieldWithValue
                name="Username"
                value={staff.data.staff_username} />
            <FieldWithValue
                name="Password"
                value={staff.data.staff_password_hash} />
        {:catch e}
            {e}
        {/await}
        <div class="column is-12"></div>
        <div class="column is-12"></div>
    </div>
</div>

<div class="columns is-centered has-text-link pb-6">
    <p class="switch-labels mt-3 mr-4">Inactive</p>
    <ButtonSwitch/>
    <p class="switch-labels mt-3 ml-4">Active</p>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>