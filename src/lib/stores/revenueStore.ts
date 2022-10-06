import {readable, writable} from 'svelte/store';
import axios from '$lib/api/index';

export const revenue = readable(null, function start(set) {
    const revenue = getRevenue()
    set(revenue)

    return function stop() {
        console.log('Ended')
    }
})

async function getRevenue() {
    try {
        const {data} = await axios.get('/order/revenue')
        return data
    } catch (e) {
        console.log(e);
    }
}