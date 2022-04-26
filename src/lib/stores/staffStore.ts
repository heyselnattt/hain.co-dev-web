import {readable} from 'svelte/store';
import axios from '$lib/api/index';

export const staffs = readable(null, function start(set) {
    const staffList = getStaffs();
    set(staffList);

    return function stop() {
        console.log('Ended');
    }
});

async function getStaffs() {
    try {
        return await axios.get('/staff');
    } catch (e) {
        console.log(e);
    }
}