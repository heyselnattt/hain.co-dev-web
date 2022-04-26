<script context="module">
    export async function load({ fetch, params }) {

        const id = params.id;
        const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        const food = await res.json()

        if (res.ok) {
            return {
                props: {
                    food
                }
            }
        }

        return {
            status: res.status,
            error: new Error('Could not fetch the food.')
        }
    }
</script>

<script>
    import NavbarSolo from "$lib/components/navbars/NavbarSolo.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import FieldWithValue from "$lib/components/otherComponents/FieldWithValue.svelte";
    import ButtonSave from "$lib/components/buttons/ButtonSave.svelte";

    export let food;
</script>

<NavbarSolo />

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
        <div class="column is-12"></div>
        <div class="column is-12"></div>
        <FieldWithValue name="Product Name" value={food.name}/>
        <FieldWithValue name="Price" value={food.phone}/>
        <div class="column is-12"></div>
        <FieldWithValue name="Product Stock" value={food.phone}/>

        <!-- wala pang file upload for image and also yung dropdown para sa product type
             + yung stock wala sa actual table-->
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }
</style>

