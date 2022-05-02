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

    let input;
    let container;
    let image;
    let placeholder;
    let showImage = false;

    function onChange() {
        const file = input.files[0];
        console.log(input.files);
        if (file) {
            showImage = true;

            const reader = new FileReader();
            reader.addEventListener("load", function () {
                image.setAttribute("src", reader.result);
            });
            reader.readAsDataURL(file);
            console.log()

            return;
        }
        showImage = false;
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

        <!-- File Picker -->
        <div class="column is-2">
            <input bind:this={input} on:change={onChange} multiple type="file" class="mb-4"/>
                <div class="new" bind:this={container}>
                    {#if showImage}
                        <img bind:this={image} src="" alt="Preview" />
                    {:else}
                        <span bind:this={placeholder}>Image Preview</span>
                    {/if}
                </div>
        </div>

        <div class="column is-12"></div>
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

    img {
        display: flex;
        max-height: 300px;
        margin-bottom: 1.5rem;
    }
</style>