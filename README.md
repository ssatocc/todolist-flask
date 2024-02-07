# todolist-flask
Todolist app with Flask

## Setup

```bash
cd src/
```

```bash
bash migrate.sh
```

## Run Web server

```bash
python app.py
```

Open http://localhost:3000/ or https://localhost:3443/

## pytest

## Customizing flask and vue3 Delimiters

```python
app = Flask(__name__)
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'
```

```javascript
const app = Vue.createApp({
  delimiters: ['[[', ']]'],
  data() {
```
