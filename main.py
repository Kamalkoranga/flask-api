import json
import time
from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))  # /user/?user=USER_NAME
    print(user_query)
    data_set = {
        'Page': 'Request', 'Message': f'Successfully got the request for {user_query}', 'Timestamp': time.time()
    }
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run(debug=True)
