import {readable} from 'svelte/store';
import axios from '$lib/api/index';

export const orders = readable(null, function start(set) {
    const orderList = getOrders();
    set(orderList);

    return function stop() {
        console.log('Ended');
    }
});

async function getOrders() {
    try {
        const {data} = await axios.get('/order');
        return data.orders
    } catch (e) {
        console.log(e);
    }
}