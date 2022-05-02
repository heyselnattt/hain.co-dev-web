<script>
    import Discard from "$lib/components/buttons/Discard.svelte";
    import FieldWithoutValue from "$lib/components/otherComponents/FieldWithoutValue.svelte";
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/buttons/ButtonAddRecord.svelte";
    import axios from "$lib/api/index";
    import ButtonSwitch from "$lib/components/buttons/ButtonSwitch.svelte";

    let product = {
        product_name: null,
        product_price: null,
        product_image_link: null,
        product_stock: null,
        product_description: null,
        product_type: null,
        product_is_active: true,
        product_code: null
    }

    const addProductToDatabase = async () => {
        try {
            let response = await axios.post('/product/new_product', product)
            console.log(response)
        } catch (e) {
            console.log(e)
        }
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
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <FieldWithoutValue 
            name="Name"
            type='text'
            bind:value={product.product_name} />
        <FieldWithoutValue 
            name="Price"
            type='number'
            bind:value={product.product_price} />
        <FieldWithoutValue 
            name="Stock"
            type='number'
            bind:value={product.product_stock} />
        <FieldWithoutValue 
            name="Product Type"
            type='number'
            bind:value={product.product_type} />
        <FieldWithoutValue 
            name="Product Description"
            type='number'
            bind:value={product.product_description} />
        <FieldWithoutValue 
            name="Product Code"
            type='text'
            bind:value={product.product_code} />
        <FieldWithoutValue
            name="Food Image Link"
            type='text'
            bind:value={product.product_image_link} />
        <div class="column is-3 is-offset-2 pt-5 pl-4 has-text-link">
            <ButtonSwitch 
                isOn={product.product_is_active}/>
        </div>
        <div class="column is-3 is-offset-2">
            <div class="pText has-text-link ml-4 mb-1">
                <p>Image Preview</p>
                <figure class="avatar mt-2">
                    <img src="{product.product_image_link}" alt=""/>
                </figure>
            </div>
        </div>
    </div>

    <div class="column is-12"></div>
    <div class="column is-12"></div>

    <div class="has-text-centered">
        <ButtonAddRecord
            click={addProductToDatabase}
            link="../Food" />
    </div>

    <div class="column is-12"></div>
    <div class="column is-12"></div>
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

    img {
        display: flex;
        max-height: 300px;
        margin-bottom: 1.5rem;
    }
</style>