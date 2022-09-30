<script context="module">
    import axios from "$lib/api/index"

    export async function load({params}) {
        try {
            const productCode = params.code;
            const product = await axios.get(`/product/${productCode}`);
            const oldProductCode = product.data.product_code;
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

    let newProduct = {
        product_name: null,
        product_price: null,
        product_image_link: null,
        product_stock: null,
        product_description: null,
        product_type: null,
        product_is_active: true,
        product_code: null
    }

    let types = [
        {value: 1, type: "BREAKFAST"},
        {value: 2, type: "LUNCH"},
        {value: 3, type: "DESSERT"},
        {value: 4, type: "EXTRA"}
    ]

    const updateProductToDatabase = async () => {
        try {
            let response = await axios.put(`/product/update_product/${oldProductCode}`, newProduct)
            console.log(response)
            await goto('../Food');
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
            <button class="button is-rounded is-info btn-txt" on:click={updateProductToDatabase}>
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
        {#await product}
            Waiting data
        {:then food}

            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Name: {food.data.product_name}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newProduct.product_name}/>
            </div>
            <!-- TODO number validation -->
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Price: {food.data.product_price}
                </p>
                <input class="pText input is-rounded" type="number" bind:value={newProduct.product_price}/>
            </div>
            <!-- TODO number validation -->
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Stock: {food.data.product_stock}
                </p>
                <input class="pText input is-rounded" type="number" bind:value={newProduct.product_stock}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Type: {identifyType(food.data.product_type)}
                </p>
                <select bind:value={newProduct.product_type} class="pText input is-rounded">
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
                    <span>*</span> Current Code: {food.data.product_code}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newProduct.product_code}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Link: {food.data.product_image_link}
                </p>
                <input class="pText input is-rounded" type="text" bind:value={newProduct.product_image_link}/>
            </div>
            <div class="column is-3 is-offset-2">
                <p class="pText has-text-link ml-4 mb-1">
                    <span>*</span> Current Description: {food.data.product_description}
                </p>
                <textarea class="pText input tall-textarea" bind:value={newProduct.product_description}></textarea>
            </div>
            <div class="column is-3 is-offset-2">
                <div class="pText has-text-link ml-4 mb-1">
                    <p>Image Preview</p>
                    <figure class="mt-4 avatar food-image">
                        {#if isNaN(newProduct.product_image_link)}
                            <img src="{newProduct.product_image_link}" alt="" style="border-radius: 20px; border: hsl(223, 85%, 41%)  5px double"/>
                        {/if}
                    </figure>
                </div>
            </div>

            <div class="column is-12"></div>

            <div class="column is-12 has-text-centered">
                <div class="field">
                    {#if food.data.product_is_active}
                        <div class="pText has-text-centered"><span>*</span> Product Currently Active</div>
                    {:else}
                        <div class="pText has-text-centered"><span>*</span> Product Currently Inactive</div>
                    {/if}
                    <input id="switchLarge switchColorDefault switchRoundedDefault"
                           type="checkbox"
                           name="switchLarge switchColorDefault switchRoundedDefault"
                           class="switch is-large is-link is-rounded"
                           bind:checked={newProduct.product_is_active}>
                    {#if newProduct.product_is_active}
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

