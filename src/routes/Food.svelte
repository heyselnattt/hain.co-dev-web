<script>
    import NavbarWithSearch from "$lib/components/navbars/NavbarWithSearch.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import ButtonAddRecord from "$lib/components/buttons/ButtonAddRecord.svelte";
    import FoodTableRow from "$lib/components/tableRows/FoodTableRow.svelte";
</script>

<NavbarWithSearch/>

<div class="container">
    <div class="columns has-text-centered pt-5">
        <div class="column is-4">
            <a href="Database">
                <ButtonBack/>
            </a>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Food
            </p>
        </div>
        <div class="column is-3 ml-6">
            <a href="AddNewFood">
                <ButtonAddRecord/>
            </a>
        </div>
    </div>

    <div class="column is-10 is-offset-1 pl-5 pt-0">
        <table class="table is-hoverable is-fullwidth">
            <thead>
            <tr>
                <th>No.</th>
                <th>Product Name</th>
                <th>Price</th>
                <th>Type</th>
            </tr>
            </thead>
            <FoodTableRow num="1" productName="Hotdog" price="30.00" type="Breakfast"/>
            <FoodTableRow num="2" productName="Egg" price="25.00" type="Breakfast"/>
            <FoodTableRow num="3" productName="Adobo" price="30.00" type="Lunch"/>
            <FoodTableRow num="4" productName="Turon" price="35.00" type="Meryenda"/>
            <FoodTableRow num="5" productName="Nova" price="40.00" type="Snacks"/>
            <FoodTableRow num="6" productName="Menudo" price="40.00" type="Lunch"/>
            <FoodTableRow num="7" productName="RC" price="50.00" type="Drinks"/>
            <FoodTableRow num="8" productName="C2" price="20.00" type="Drinks"/>
            <FoodTableRow num="9" productName="Banana Cue" price="20.00" type="Meryenda"/>
        </table>
    </div>
</div>


<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }

    table {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }
</style>