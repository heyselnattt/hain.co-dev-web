import {readable} from 'svelte/store';
import axios from '$lib/api/index';

export const products = readable(null, function start(set) {
    const productList = getProducts();
    set(productList);

    return function stop() {
        console.log('Ended');
    }
});

async function getProducts() {
    try {
        return await axios.get('/product');
    } catch (e) {
        console.log(e);
    }
}