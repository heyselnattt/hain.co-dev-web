<script>
    import Discard from "$lib/components/buttons/Discard.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import axios from "$lib/api/index";
    import {goto} from "$app/navigation";
    import uploadImageToAPI from "../../lib/helper/uploadImageToAPI.js";

    let product = {
        productCode: "",
        productName: "",
        productDescription: "",
        productPrice: 0,
        productIsActive: true,
        productImage: "",
        productType: 1
    }

    let selectedImage;

    let types = [
        {value: 1, type: "BREAKFAST"},
        {value: 2, type: "LUNCH"},
        {value: 3, type: "DESSERT"},
        {value: 4, type: "EXTRA"}
    ]

    const addProductToDatabase = async () => {
        try {
            product.productImage = await uploadImageToAPI(selectedImage);
            console.log(product.productImage);
            let response = await axios.post('/product/createProduct', product)
            console.log(response)
            alert("Product Added Successfully")
            await goto("../Food")
        } catch (e) {
            console.log(e)
        }
    }

    function onImageSelect(e) {
        selectedImage = e.target.files[0]
        console.log(selectedImage)
    }

    let input;
    let container;
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarSolo/>

<div class="container">
    <div class="columns  pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../Food"/>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                New Product
            </p>
        </div>
        <div class="column is-3 ml-6">
            <Discard link="../Food"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Product Name
            </p>
            <input class="pText input is-rounded" type="text" bind:value={product.productName}/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Product Price
            </p>
            <input class="pText input is-rounded" type="number" bind:value={product.productPrice}/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Product Type
            </p>
            <select bind:value={product.productType} class="pText input is-rounded">
                {#each types as pos}
                    <option value={pos.value}>
                        {pos.type}
                    </option>
                {/each}
            </select>
        </div>
        <!-- TODO make sure unique -->
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Product Code
            </p>
            <input class="pText input is-rounded" type="text" bind:value={product.productCode}/>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Product Description
            </p>
            <textarea class="pText input tall-textarea" bind:value={product.productDescription}></textarea>
        </div>
        <div class="column is-3 is-offset-2">
            <p class="pText has-text-link ml-4 mb-1">
                <span>*</span> Product Image
            </p>
            <input class="pText input is-rounded"
                   type="file"
                   accept="image/*"
                   on:change={onImageSelect}/>
        </div>
    </div>
    <div class="has-text-centered">
        <div class="field">
            <input id="switchLarge switchColorDefault switchRoundedDefault"
                   type="checkbox"
                   name="switchLarge switchColorDefault switchRoundedDefault"
                   class="switch is-large is-link is-rounded"
                   bind:checked={product.product_is_active}>
            {#if product.product_is_active}
                <label for="switchLarge switchColorDefault switchRoundedDefault"> <span>*</span> Active</label>
            {:else}
                <label for="switchLarge switchColorDefault switchRoundedDefault"> <span>*</span> Inactive</label>
            {/if}
        </div>
    </div>
    <div class="has-text-centered">
        <div class="mb- has-text-centered">
            <button class="btn-txt button is-link is-rounded" on:click={addProductToDatabase}>Add Product</button>
        </div>
    </div>

    <div class="column is-12"></div>
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

    .avatar {
        display: flex;
        aspect-ratio: 4 / 5 auto;
        max-width: 250px;
        margin-top: 1.5rem;
    }

    .btn-txt {
        font-size: 20px;
        font-family: 'Karla', sans-serif;
    }

    .tall-textarea {
        height: 18rem;
        border-radius: 20px;
    }

    span {
        color: red
    }
</style>