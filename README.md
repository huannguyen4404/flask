# Initial setup
1. Create an `venv` with command `python3.8 -m venv .venv`
2. Enter the `venv` with command `source .venv/bin/activate`
3. Install all dependencies with command `python3.8 -m pip install -r requirements.txt`

# Config MongoDB
1. Edit MONGODB_SETTINGS in file `config.py`

# Set write permission for upload directory
1. Set write permission for upload dir: `chmod -R 755 /media/uploads/`

# Run the Flask-RestX server
1. When in the `venv`, run the command `flask run --port <PORT>`
2. Flask server should be running with output
```
 * Running on http://127.0.0.1:<PORT>/ (Press CTRL+C to quit)
```
3. Open a browser and enter the URL