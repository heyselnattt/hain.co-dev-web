<script lang="ts">
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/buttons/ButtonAddRecord.svelte";
    import Discard from "$lib/components/buttons/Discard.svelte";
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";

    let avatar, fileinput;

    const onFileSelected = (e) => {
        let image = e.target.files[0];
        let reader = new FileReader();
        reader.readAsDataURL(image);
        reader.onload = e => {
            avatar = e.target.result
        };
    }
</script>

<NavbarSolo/>

<div class="container">
    <div class="columns pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../Food"/>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                New Food
            </p>
        </div>
        <div class="column is-3 ml-6">
            <Discard link="../Food"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        <FieldWithValue name="Product Name" value=""/>
        <div class="column is-2"></div>
        <div class="column is-3 control">
            <p class="has-text-link"></p>
            <textarea class="textarea has-fixed-size" placeholder="Description"></textarea>
        </div>
        <FieldWithValue name="Price" value=""/>
        <div class="column is-2"></div>

        <div class="column is-3 file has-name">
            {#if avatar}
                <img class="avatar" src="{avatar}" alt="d"/>
            {:else}
                <img class="avatar" src="../static/images/imageUpload.svg" alt=""/>
            {/if}

            <input style="display:none" type="file" accept=".jpg, .jpeg, .png" on:change={(e)=>onFileSelected(e)}
                   bind:this={fileinput}>
            <label class="file-label">
                <input class="file-input" type="file" name="resume">
                <span class="file-cta">
                    <span class="file-icon">
                        <i class="fas fa-upload"></i>
                    </span>
                    <span class="upload" on:click={()=>{fileinput.click();}}>
                        Choose a file…
                    </span>
                </span>
            </label>
        </div>
        <div class="column is-12"></div>

        <!-- wala pang dropdown for product type, and file upload para sa image-->
    </div>

    <div class="mb-6 has-text-centered">
        <ButtonAddRecord link="../Food" />
    </div>
</div>


<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }

    p {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }

    .upload {
        display: flex;
        cursor: pointer;
    }

    .avatar {
        display: flex;
        height: 150px;
        width: 150px;
        margin-bottom: 1.5rem;
    }
</style>