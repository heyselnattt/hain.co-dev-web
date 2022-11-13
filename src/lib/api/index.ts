import axios from 'axios';

export default axios.create({
	// baseURL:"https://hainco-api.herokuapp.com/",
	// baseURL: "https://sb-hainco.herokuapp.com/api"
	// baseURL: "https://hainco-sb.herokuapp.com/api",
	baseURL: "http://localhost:8092/api",
});
