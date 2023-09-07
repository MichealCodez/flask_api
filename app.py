from flask import Flask, jsonify, request
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if slack_name is None or track is None:
        return jsonify({"error": "Both slack_name and track are required."}), 400


    current_day_of_week = datetime.datetime.now(pytz.utc).strftime("%A")
    current_utc_time = datetime.datetime.now(pytz.utc)

    # utc_time_check = abs(current_utc_time.second) <= 120

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day_of_week,
        "utc_time": current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": track,
        "github_file_url": "https://github.com/MichealDavid1/Task1_HNGX/blob/main/app.py",
        "github_repo_url": "https://github.com/MichealDavid1/Task1_HNGX.git",
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
