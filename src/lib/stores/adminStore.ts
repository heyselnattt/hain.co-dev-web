import {readable} from 'svelte/store';
import axios from '$lib/api/index';

export const admins = readable(null, function start(set) {
    const adminList = getAdmin();
    set(adminList);

    return function stop() {
        console.log('Ended');
    }
});

async function getAdmin() {
    try {
        const {data} = await axios.get('/admin');
        return data.admins
    } catch (e) {
        console.log(e);
    }
}