import {readable} from 'svelte/store';
import axios from '$lib/api/index';

export const customers = readable(null, function start(set) {
    const customerList = getCustomer();
    set(customerList);

    return function stop() {
        console.log('Ended');
    }
});

async function getCustomer() {
    try {
        return await axios.get('/customer');
    } catch (e) {
        console.log(e);
    }
}