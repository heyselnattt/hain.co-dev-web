<script>
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import Discard from "$lib/components/buttons/Discard.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import axios from "$lib/api";
    import {goto} from "$app/navigation";

    let staff = {
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

    const addStaffToDatabase = async () => {
        try {
            console.log(staff)
            let response = await axios.post('/staff/createStaff', staff)
            console.log(response)
            alert('Staff added successfully!')
            await goto("../CanteenStaff")
        } catch (e) {
            console.log(e)
        }
    }
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo/>

<div class="container">
    <div class="columns pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../CanteenStaff"/>
        </div>
        <div class="column is-4">
            <p class="text1 has-text-link">
                New Canteen Staff
            </p>
        </div>
        <div class="column is-3 ml-6">
            <Discard link="../CanteenStaff"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Full Name
            </p>
            <input class="pText input is-rounded" type="text" bind:value={staff.staffFullName} required/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Contact No.
            </p>
            <input class="pText input is-rounded" type="text" bind:value={staff.staffContactNumber} required/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Username
            </p>
            <input class="pText input is-rounded" type="text" bind:value={staff.staffUsername} required/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Password
            </p>
            <input class="pText input is-rounded" type="password" bind:value={staff.staffPassword} required/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Position
            </p>
            <select bind:value={staff.staffPosition} class="pText input is-rounded">
                {#each positions as pos}
                    <option value={pos.value}>
                        {pos.position}
                    </option>
                {/each}
            </select>
        </div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
    </div>
    <!-- Add record button -->
    <div class="mb- has-text-centered">
        <button class="btn-txt button is-link is-rounded" on:click={addStaffToDatabase}>Add Canteen Staff</button>
    </div>
</div>

<style>
    .text1 {
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
        color: red;
    }
</style>