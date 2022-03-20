import {readable, writable} from 'svelte/store';
import axios from '$lib/api/index';

export const row_count = readable(null, function start(set) {
    const rowCounts = getRowCounts()
    set(rowCounts)

    return function stop() {
        console.log('Ended')
    }
});

async function getRowCounts() {
    /**
     * This function returns an array of JSONs that has the table name and rows.
     * The way the row counts will be accessed will be referencing the exp['data'][array_position]['rows']
     * The query returns the table names in an alphabetical order ensuring that the mapping with the array position
     * and the corresponding records won't be broken
     */
    try {
        return await axios.get('/meta/row_count')
    } catch (e) {
        console.log(e);
    }
}