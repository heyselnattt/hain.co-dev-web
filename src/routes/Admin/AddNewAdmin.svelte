<script>
    import Discard from "$lib/components/buttons/Discard.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import axios from "$lib/api/index";
    import ButtonSwitch from "$lib/components/buttons/ButtonSwitch.svelte";
    import {goto} from "$app/navigation";
  import { notifs } from "$lib/stores/notificationStore";
  import NotificationContainer from "$lib/components/systemNotification/notification-container.svelte";
  import validators from "$lib/validators";

    let admin = {
        admin_full_name: null,
        admin_username: null,
        admin_password: null,
        admin_position: 1,
        admin_is_active: true,
    }

    const addAdminToDatabase = async () => {
        let msg = ''
        let errors = 0
        Object.keys(admin).map(prop => {
            if(!admin[prop]) {
                msg += !errors ? `${prop.split('admin_').join('').split('_').join(' ')}` : `, ${prop.split('admin_').join('')}`
                errors++
            }
        })
        msg += errors ? ' are a required fields' : 'is a required field'
        if(errors) {
            $notifs = [...$notifs, {
                msg,
                type: 'error',
                id: `${Math.random() * 99}${new Date().getTime()}`
            }]
            return
        }

        if(!validators.isPassValid(admin.admin_password)) {
            $notifs = [...$notifs, {
                msg: 'Password does not meet the criteria for security',
                type: 'error',
                id: `${Math.random() * 99}${new Date().getTime()}`
            }]
            return
        }
        try {
            let response = await axios.post('/admin/new_admin', admin)
            console.log(response)
            await goto("../Admin")
        } catch (e) {
            $notifs = [...$notifs, {
                msg: 'Error adding a new admin',
                type: 'error',
                id: `${Math.random() * 99}${new Date().getTime()}`
            }]
            console.log(e)
        }
    }
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo/>
<NotificationContainer />

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../Admin"/>
        </div>
        <div class="column is-4">
            <p class="text1 has-text-link">
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
        <div class="column is-12"></div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Full Name
            </p>
            <input class="pText input is-rounded" type="text" bind:value={admin.admin_full_name}/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Username
            </p>
            <input class="pText input is-rounded" type="text" bind:value={admin.admin_username}/>
        </div>
        <div class="column is-12"></div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Password
            </p>
            <input class="pText input is-rounded" type="password" bind:value={admin.admin_password}/>
        </div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <div class="column is-12"></div>
    </div>
    <!-- Add record button -->
    <div class="mb- has-text-centered">
        <button class="btn-txt button is-link is-rounded" on:click={addAdminToDatabase}>Add Admin</button>
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