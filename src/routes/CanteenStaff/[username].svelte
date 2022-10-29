<script context="module">
    import axios from "$lib/api/index"

    export async function load({fetch, params}) {
        try {
            const username = params.username;
            const canteenStaff = await axios.get(`/staff/auth/${username}`);
            const oldUsername = canteenStaff.data.staffDetails.staff_username;
            console.log(canteenStaff)
            return {
                props: {
                    canteenStaff,
                    oldUsername
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
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import {goto} from "$app/navigation";

    export let canteenStaff;
    export let oldUsername;

    let canteenStaffDetails = canteenStaff.data.staffDetails;

    let newStaff = {
        staffFullName: null,
        staffContactNumber: null,
        staffUsername: null,
        staffPassword: null,
        staffPosition: 1,
        staffIsActive: true
    }

    let positions = [
        {value: 1, position: "CHEF"},
        {value: 2, position: "CASHIER"},
        {value: 3, position: "SERVER"}
    ]

    const identifyType = (code) => {
        switch (code) {
            case 1:
                return "Chef"

            case 2:
                return "Cashier"

            case 3:
                return "Server"
        }
    }

    const updateStaffToDatabase = async () => {
        try {
            console.log(newStaff)
            let response = await axios.put(`/staff/updateStaff/${oldUsername}`, newStaff);
            console.log(response)
            alert('Staff added successfully!')
            await goto('../CanteenStaff');
        } catch (e) {
            console.log(e);
        }
    }
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../CanteenStaff"/>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Canteen Staff's Information
            </p>
        </div>
        <div class="column is-3 ml-6">
            <button class="button is-rounded is-info btn-txt" on:click={updateStaffToDatabase}>
                <p class="ml-4 mr-4 has-text-white">
                    Save
                </p>
            </button>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12">
            <div class="has-text-centered pText">Make sure to fill up all information boxes</div>
        </div>
        {#await canteenStaff}
            Waiting data
        {:then staff}
            <!-- TODO switch to bound inputs -->
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Name: {canteenStaffDetails.staff_full_name}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newStaff.staffFullName}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Position: {identifyType(canteenStaffDetails.staff_position)}
                </p>
                <select bind:value={newStaff.staffPosition} class="pText input is-rounded">
                    {#each positions as pos}
                        <option value={pos.value}>
                            {pos.position}
                        </option>
                    {/each}
                </select>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Contact Number: {canteenStaffDetails.staff_contact_number}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newStaff.staffContactNumber}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Username: {canteenStaffDetails.staff_username}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newStaff.staffUsername}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Password: {canteenStaffDetails.staff_password}
                </p>
                <input class="pText input is-rounded" type="password" bind:value={newStaff.staffPassword}/>
            </div>
        {:catch e}
            {e}
        {/await}
        <div class="column is-12">
            <div class="columns is-centered has-text-link pb-6">
                {#await canteenStaff}
                    Waiting data
                {:then staff}
                    <div class="field">
                        {#if canteenStaffDetails.staff_is_active}
                            <div class="pText has-text-centered"> <span>*</span> Staff Currently Active</div>
                        {:else}
                            <div class="pText has-text-centered"> <span>*</span> Staff Currently Inactive</div>
                        {/if}
                        <input id="switchLarge switchColorDefault switchRoundedDefault"
                               type="checkbox"
                               name="switchLarge switchColorDefault switchRoundedDefault"
                               class="switch is-large is-link is-rounded"
                               bind:checked={newStaff.staffIsActive}>
                        {#if newStaff.staffIsActive}
                            <label for="switchLarge switchColorDefault switchRoundedDefault">Active</label>
                        {:else}
                            <label for="switchLarge switchColorDefault switchRoundedDefault">Inactive</label>
                        {/if}
                    </div>
                {:catch e}
                    {e}
                {/await}
            </div>
        </div>
        <div class="column is-12"></div>
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }

    .pText {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }

    .btn-txt {
        font-size: 20px;
        font-family: 'Karla', sans-serif;
    }

    span {
        color: red
    }
</style>