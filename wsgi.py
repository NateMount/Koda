#[MAIN]

from koda import create_app
from os import environ

if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0', 
        port=int(environ.get("PORT", 5000))
    )