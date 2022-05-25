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
        return await axios.get('/order');
    } catch (e) {
        console.log(e);
    }
}