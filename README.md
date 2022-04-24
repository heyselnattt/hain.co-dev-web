# Hain.co Web Panel [Dev]

Hain.co is an Android based Canteen Ordering Application designed for school canteens aiming for a
better, contactless dining experience. 

This repository contains the web panel of the application designed for the administrators

## Developing the project
After downloading this repository, run `npm install` to install all node dependencies. Start the development servers to start working on the project

```bash
# for the client application (separate terminal)
npm run dev 
```

For the Python server, first you should create a Python virtual environment and activate it in your terminal

```bash
# create a venv
python -m venv venv

# activate the venv
cd venv/Scripts && activate 

# install dependencies
pip install -r requirements.txt
```

To start the python server, you can 

```bash
# for the Python server (separate terminal)
uvicorn backend.server:app --reload --port 8080
```