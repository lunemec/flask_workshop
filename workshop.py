from app import app

import admin
from user.views import hello_world


if __name__ == '__main__':
    app.run(debug=True)
