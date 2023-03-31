import os
from my_app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.route('/status', methods=['GET'])
def status():
    return 'Running!'


if __name__ == '__main__':
    app.run()
