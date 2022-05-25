<script context="module">
    import axios from "$lib/api/index"

    export async function load({fetch, params}) {
        try {
            const productCode = params.code;
            const product = await axios.get(`/product/${productCode}`);
            console.log(product)
            return {
                props: {
                    product
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
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";
    import ButtonSave from "$lib/components/buttons/ButtonSave.svelte";
    import ButtonSwitch from "$lib/components/buttons/ButtonSwitch.svelte";
    import Dropdown from "$lib/components/otherComponents/Dropdown.svelte";
    import Food from "../Food.svelte";

    const identifyType = (code) => {
        switch (code) {
            case 1:
                return "Breakfast"

            case 2:
                return "Lunch"

            case 3:
                return "Drinks"

            case 4:
                return "Desserts"
        }
    }

    export let product;
</script>

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
            <ButtonSave link="../Food"/>
        </div>
    </div>

    <div class="columns pt-5 is-multiline">
        <div class="column is-12"></div>
        {#await product}
            Waiting data
        {:then food}
            <!-- TODO switch to bound inputs -->
            <FieldWithValue
                name="Product Name"
                value={food.data.product_name}/>
            <FieldWithValue
                name="Price"
                value={food.data.product_price}/>
            <FieldWithValue
                name="Stock"
                value={food.data.product_stock}/>
            <Dropdown
                name="Product Type"
                type={food.data.product_type}/>
            <FieldWithValue
                name="Product Description"
                value={food.data.product_description}/>
            <FieldWithValue
                name="Product Code"
                value={food.data.product_code}/>
            <FieldWithValue
                name="Food image Link"
                value={food.data.product_image_link}/>
            <div class="column is-3 is-offset-2 pt-5 pl-4 has-text-link">
                <ButtonSwitch
                    isOn={food.data.product_is_active}/>
            </div>
            <div class="column is-3 is-offset-2">
                <div class="pText has-text-link ml-4 mb-1">
                    <p>Image Preview</p>
                    <figure class="avatar mt-2">
                        <img src="{food.data.product_image_link}" alt=""/>
                    </figure>
                </div>
            </div>

            <div class="column is-12"></div>
            <div class="column is-12"></div>
        {:catch e}
            {e}
        {/await}

        <!-- wala pang file upload for image and also yung dropdown para sa product type -->
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
        height: 150px;
        width: 150px;
        margin-bottom: 1.5rem;
    }
</style>

