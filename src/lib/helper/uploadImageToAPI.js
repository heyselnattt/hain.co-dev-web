import axios from 'axios';

export default async function uploadImageToAPI(file) {
    console.log('trying to upload image to API');
    const API_URL = `https://api.imgbb.com/1/upload?&key=b5d04ecbac8901993c32b47f4ec083da`
    const formData = new FormData();
    formData.append('image', file);
    const response = await axios.post(API_URL, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
    return response.data.data.display_url;
}