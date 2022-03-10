# Hain.co Web Panel [Dev]

Hain.co is an Android based Canteen Ordering Application designed for school canteens aiming for a
better, contactless dining experience. 

This repository contains the web panel of the application designed for the administrators

## Developing

After cloning the repository, run `npm install` and `pip install -r requirements.txt` to install 
all dependencies. Start the development servers to start working on the project

```bash
# for the client application (separate terminal)
npm run dev 

# for the Python server (separate terminal)
uvicorn backend:server --reload --port 8080
```