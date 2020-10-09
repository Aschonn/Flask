# this will specifically target __init__.py file in flasklexus
import os
from flaskdraft import create_app, db


app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
