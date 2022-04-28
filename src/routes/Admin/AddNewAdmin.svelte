<script>
    import Discard from "$lib/components/buttons/Discard.svelte";
    import FieldWithoutValue from "$lib/components/otherComponents/FieldWithoutValue.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/buttons/ButtonAddRecord.svelte";
    import axios from "$lib/api/index";
import ButtonSwitch from "$lib/components/buttons/ButtonSwitch.svelte";

    let admin = {
        admin_full_name: null,
        admin_username: null,
        admin_password: null,
        admin_position: 1,
        admin_is_active: true,
    }

    const addAdminToDatabase = async () => {
        try {
            let response = await axios.post('/admin/new_admin', admin)
            console.log(response)
        } catch (e) {
            console.log(e)
        }
    }
</script>

<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../Admin"/>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                New Administrator
            </p>
        </div>
        <div class="column is-3 ml-6">
            <Discard link="../Admin"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <div class="column is-12"></div>
            <!-- TODO add confirm password logic-->
<!--        <div class="column is-12"></div>-->
<!--        <div class="column is-12"></div>-->
<!--        <div class="column is-12"></div>-->
<!--        <FieldWithValue name="Name" value="" bind:value={admin.admin_full_name}/>-->
<!--        <FieldWithValue name="Password" value="" bind:value={admin.admin_password}/>-->
<!--        <div class="column is-12"></div>-->
<!--        <FieldWithValue name="Username" value="" bind:value={admin.admin_username}/>-->
<!--        <FieldWithValue name="Confirm Password" value=""/>-->
<!--        <div class="column is-12"></div>-->
<!--        <div class="column is-12"></div>-->
<!--        <div class="column is-12"></div>-->
<!--        <div class="column is-12"></div>-->
        <!-- TODO Style text fields and buttons -->
        <!-- Name
        <input type="text" bind:value={admin.admin_full_name}/>
        Username
        <input type="text" bind:value={admin.admin_username}/>
        Password
        <input type="password" bind:value={admin.admin_password}/> -->
        <FieldWithoutValue 
            name="Name"
            type='text'
            bind:value={admin.admin_full_name} />
        <FieldWithoutValue 
            name="Username"
            type='text'
            bind:value={admin.admin_username} />
        <FieldWithoutValue 
            name="Password"
            type='password'
            bind:value={admin.admin_password} />
    </div>

    <div class="has-text-centered">
        <ButtonSwitch 
            isOn={admin.admin_is_active}/>
    </div>

    <!-- Add record button -->
    <!-- <div class="mb- has-text-centered">
        <ButtonAddRecord link="../Admin"/>
        TODO redirect pabalik sa parent page
        <button on:click={addAdminToDatabase}>Add Admin</button>
    </div> -->

    <div class="column is-12"></div>
    <div class="column is-12"></div>
    <div class="column is-12"></div>

    <div class="has-text-centered">
        <ButtonAddRecord
            click={addAdminToDatabase}
            link="../Admin" />
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>