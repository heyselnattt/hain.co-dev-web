<script context="module">
    import axios from "$lib/api/index"

    export async function load({params}) {
        try {
            const productCode = params.code;
            const product = await axios.get(`/product/${productCode}`);
            const oldProductCode = product.data.product.product_code;
            console.log(product)
            return {
                props: {
                    product,
                    oldProductCode
                }
            }
        } catch (e) {
            return {
                error: new Error('Can\'t fetch the food information')
            }
        }
    }
</script>

<script>
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import {goto} from "$app/navigation";
    import uploadImageToAPI from "$lib/helper/uploadImageToAPI.js";
    import { notifs } from "$lib/stores/notificationStore";
    import NotificationContainer from "$lib/components/systemNotification/notification-container.svelte";

    const identifyType = (code) => {
        switch (code) {
            case 1:
                return "Breakfast"

            case 2:
                return "Lunch"

            case 3:
                return "Desserts"

            case 4:
                return "Extra"
        }
    }

    export let product;
    export let oldProductCode;

    let productDetails = product.data.product;
    let updating = false
    let newProduct = {
        productCode: oldProductCode,
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

    const updateProductToDatabase = async () => {
        let msg = 'Product '
        let errors = 0
        Object.keys(newProduct).map(prop => {
            if(prop === 'productPrice') {
                if(newProduct[prop] <= 0) {
                    msg += !errors ? `${prop.split('product').join('')}` : `, ${prop.split('product').join('')}`
                    errors++
                }
            }
            if(prop !== 'productIsActive' && prop !== 'productType' && prop !== 'productPrice' && prop !== 'productCode') {
                if(!newProduct[prop]) {
                    msg += !errors ? `${prop.split('product').join('')}` : `, ${prop.split('product').join('')}`
                    errors++
                }
            }
        })
        msg += errors ? ' are a required fields' : ' is a required field'

        if(errors) {
            $notifs = [...$notifs, {
                msg,
                type: 'error',
                id: `${Math.random() * 99}${new Date().getTime()}`
            }]
            return
        }

        try {
            updating = true
            newProduct.productImage = await uploadImageToAPI(selectedImage);
            let response = await axios.put(`/product/updateProduct/${oldProductCode}`, newProduct)
            if(response.status == 200) {
                updating = false
                // alert(`Canteen product: ${newProduct.productName} (${newProduct.productCode}) is updated`)
                $notifs = [...$notifs, {
                    msg: `Canteen product: ${newProduct.productName} (${newProduct.productCode}) is updated`,
                    type: 'success',
                    id: `${Math.random() * 99}${new Date().getTime()}`
                }]
                await goto('../Food');
            }else{
                updating = false
                $notifs = [...$notifs, {
                    msg: 'Error in updating product',
                    type: 'error',
                    id: `${Math.random() * 99}${new Date().getTime()}`
                }]
            }
            // console.log(response)
        } catch (e) {
            updating = false
            $notifs = [...$notifs, {
                msg: 'Error in updating product',
                type: 'error',
                id: `${Math.random() * 99}${new Date().getTime()}`
            }]
            console.log(e);
        }
    }

    function onImageSelect(e) {
        selectedImage = e.target.files[0]
        newProduct.productImage = selectedImage
        console.log(selectedImage)
    }
</script>

<NavbarSolo/>
<NotificationContainer />

<div class="container">
    <div class="columns pt-5 is-multiline has-text-centered">
        <div class="column is-4">
            <ButtonBack link="../Food"/>
        </div>
        <div class="column is-3  ml-6">
            <p class="text has-text-link">
                Food's Information
            </p>
        </div>
        <div class="column is-3 ml-6">
            <button class="button {updating ? 'is-loading' : ''} is-rounded is-info btn-txt" on:click={updateProductToDatabase}>
                <p class="ml-4 mr-4 has-text-white {updating ? 'is-hidden' : ''}">
                    Save
                </p>
            </button>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12">
            <div class="has-text-centered pText">Make sure to fill up all information boxes</div>
        </div>
        {#await product}
            Waiting data
        {:then food}

            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Name: {productDetails.product_name}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newProduct.productName}/>
            </div>
            <!-- TODO number validation -->
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Price: {productDetails.product_price}
                </p>
                <input class="pText input is-rounded" type="number" bind:value={newProduct.productPrice}/>
            </div>
            <!-- TODO number validation -->
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Type: {identifyType(productDetails.product_type)}
                </p>
                <select bind:value={newProduct.productType} class="pText input is-rounded">
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
                    <span>*</span> Current Code: {oldProductCode}
                    <br>
                    <span class="note">You cannot modify product code once set</span>
                </p>
                <input class="pText input is-rounded" type="text" disabled bind:value={oldProductCode}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Description: {productDetails.product_description}
                </p>
                <textarea class="pText input tall-textarea" bind:value={newProduct.productDescription}></textarea>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-2">
                    <span>*</span> Current Product Image:
                </p>
                <img src={productDetails.product_image_link} alt="">
                <input class="pText input is-rounded mb-5"
                       type="file"
                       accept="image/*"
                       on:change={onImageSelect}/>
            </div>

            <div class="column is-12"></div>

            <div class="column is-12 has-text-centered">
                <div class="field">
                    {#if productDetails.product_is_active}
                        <div class="pText has-text-centered"><span>*</span> Product Currently Active</div>
                    {:else}
                        <div class="pText has-text-centered"><span>*</span> Product Currently Inactive</div>
                    {/if}
                    <input id="switchLarge switchColorDefault switchRoundedDefault"
                           type="checkbox"
                           name="switchLarge switchColorDefault switchRoundedDefault"
                           class="switch is-large is-link is-rounded"
                           bind:checked={newProduct.productIsActive}>
                    {#if newProduct.productIsActive}
                        <label class="pText" for="switchLarge switchColorDefault switchRoundedDefault">Active</label>
                    {:else}
                        <label class="pText" for="switchLarge switchColorDefault switchRoundedDefault">Inactive</label>
                    {/if}
                </div>
            </div>
        {:catch e}
            {e}
        {/await}
    </div>
</div>


<style>
    .text {
        font-family: 'Montserrat', sans-serif;
        font-size: 40px;
    }

    .pText {
        font-family: 'Montserrat', sans-serif;
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
        font-family: 'Montserrat', sans-serif;
    }

    .tall-textarea {
        height: 18rem;
        border-radius: 20px;
    }

    span {
        color: red
    }

    .note {
        color: gray;
        display: block;
        font-size: 13px;
    }
</style>

