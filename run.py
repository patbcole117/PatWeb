from app import app
import os

if __name__=='__main__':
    app.run(debug=False, host=os.getenv('FLASK_HOST'), port=os.getenv('FLASK_PORT'))