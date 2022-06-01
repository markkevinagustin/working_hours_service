from flask import Flask, jsonify
import os
import requests
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def today_working_hours():
    url = os.environ['time_service_url']

    payload = json.dumps({
      "time_string": "9AM"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    starting_hour = requests.request("POST", url,
                                     headers=headers, data=payload)

    payload = json.dumps({
      "time_string": "6PM"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    ending_hour = requests.request("POST", url, headers=headers, data=payload)
    return jsonify({"starting_hour": starting_hour.json()['response'],
                    "ending_hour": ending_hour.json()['response']})


@app.route("/", methods=["GET"])
def today_working_hours_docker():
    url = os.environ['time_service_url_docker']

    payload = json.dumps({
      "time_string": "9AM"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    starting_hour = requests.request("POST", url,
                                     headers=headers, data=payload)

    payload = json.dumps({
      "time_string": "6PM"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    ending_hour = requests.request("POST", url, headers=headers, data=payload)
    return jsonify({"starting_hour": starting_hour.json()['response'],
                    "ending_hour": ending_hour.json()['response']})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(debug=True, host='0.0.0.0', port=port)
