# Flask-Vue.JS template
Flask and Vue.js template designed as a starting point to enable quick web-app development.

# Development environment setup
### server side:
```
cd server
python -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### client side:
```
npm install -g @vue/cli
vue create frontend
cd frontend
npm install
```

# Server

## Run dev server
```
python main.py
```

# Frontend

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

# Google App Engine
Set up GAE for new project, TL;DR version of GAE docs. 
[See here for more details.](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
```
gcloud components update
gcloud auth login
gcloud app create --project=[YOUR_PROJECT_ID]
gcloud components install app-engine-python
```

# Deployment
Ensure `./frontend/vue.config.js` `publicPath` is updated to the path of the project.
Ideally more work needs to be put into having this as an environment variable.

```
# build frontend
cd frontend
npm run build

# switch to backend directory
cd ../backend
gcloud app deploy
```