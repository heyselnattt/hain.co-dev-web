<script>
    import NavbarWithSearch from "$lib/components/navbars/NavbarWithSearch.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import TransactionTableRow from "$lib/components/tableRows/TransactionTableRow.svelte";
    import Inaccessible from "$lib/components/otherComponents/Inaccessible.svelte";

    let loggedIn = false;
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

{#if !loggedIn}
    <Inaccessible/>
    {:else}
<NavbarWithSearch />

<div class="container">
    <div class="columns has-text-centered pt-5">
        <div class="column is-4 has-text-centered">
            <ButtonBack link="Database"/>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Transactions
            </p>
        </div>
    </div>

    <div class="column is-10 is-offset-1 pl-5 pt-0">
        <table class="table is-hoverable is-fullwidth">
            <thead>
                <tr>
                    <th>Transaction ID</th>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Amount</th>
                    <th>Type</th>
                </tr>
            </thead>
            <TransactionTableRow num="0001" name="Bantugan, Dea" desc="buy rice and adobo" amount="40.00" type="Order"/>
            <TransactionTableRow num="0002" name="Beltran, Sheng" desc="buy RC" amount="10.00" type="Buy"/>
            <TransactionTableRow num="0003" name="Albis, Anne" desc="buy sopas" amount="20.00" type="Order"/>
            <TransactionTableRow num="0004" name="Perry, Katy" desc="buy royal, rice, hotdog" amount="50.00" type="Order"/>
            <TransactionTableRow num="0005" name="Mendes Shawn" desc="buy clover, buy RC" amount="18.00" type="Order"/>
            <TransactionTableRow num="0006" name="Cabello, Camilla" desc="buy pork steak" amount="40.00" type="Order"/>
            <TransactionTableRow num="0007" name="Gomez, Selena" desc="edit the student's info" amount="----" type="Admin"/>
            <TransactionTableRow num="0008" name="Mendoza, Maine" desc="buy 5 RC" amount="50.00" type="Buy"/>
            <TransactionTableRow num="0009" name="Kim, Sunwoo" desc="buy rice" amount="15.00" type="Buy"/>
        </table>
    </div>
</div>
{/if}

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