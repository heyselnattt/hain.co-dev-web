import {readable} from 'svelte/store';
import axios from '$lib/api/index';

export const admins = readable(null, function start(set) {
    const adminList = getAdmin()
    set(adminList)

    return function stop() {
        console.log('Ended')
    }
});

async function getAdmin() {
    try {
        return await axios.get('/admin');
    } catch (e) {
        console.log(e);
    }
}