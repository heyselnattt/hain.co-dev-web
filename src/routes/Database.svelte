<script>
    import Card from "$lib/components/Card.svelte";
    import LogoutNavbar from "$lib/components/LogoutNavbar.svelte";
  </script>
  
  <svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
  </svelte:head>
  
  <LogoutNavbar />
  
  <div class="container">
    <p class="text has-text-centered has-text-link has-text-weight- mt-5">
      Database
    </p>

    <div class="columns is-centered is-multiline pt-5">
            <Card name="Customers" entries="230" sub="customers" image="images/customersIcon.png" link="Customers"/>
            <Card name="Canteen Staff" entries="15" sub="staff entries" image="images/canteenStaffIcon.png"/>
            <Card name="Food" entries="15" sub="items" image="images/foodIcon.png" link="Food"/>
            <Card name="Administrators" entries="4" sub="records" image="images/adminIcon.png" link="Admin"/>
            <Card name="Reports" entries="130" sub="entries" image="images/reportIcon.png"/>
            <Card name="Transactions" entries="370" sub="entries" image="images/transactionIcon.png"/>
            <!-- {#each Array(100) as a}
            <Card name="{a}" sub="{a}-sub" link="/"/>
            {/each} -->
    </div>
  </div>
  
  <style>
    .text {
      font-family: 'Karla', sans-serif;
      font-size: 40px;
    }
  </style>