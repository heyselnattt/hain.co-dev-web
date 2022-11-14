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
        const {data} = await axios.get('/staff');
        return data.staffs
    } catch (e) {
        console.log(e);
    }
}