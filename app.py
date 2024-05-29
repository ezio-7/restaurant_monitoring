from flask import Flask, request, jsonify
from threading import Thread
import time
import uuid

app = Flask(__name__)

report_status = {}

def generate_report(report_id):
    report_status[report_id] = ("Running", None)
    time.sleep(10)  # Simulate a delay in report generation
    
    # Generate report data (this is just an example)
    report_data = "Generated report data"
    
    # Update the report status and data
    report_status[report_id] = ("Complete", report_data)

@app.route('/trigger_report', methods=['POST'])
def trigger_report():
    report_id = str(uuid.uuid4())
    thread = Thread(target=generate_report, args=(report_id,))
    thread.start()
    return jsonify({"report_id": report_id})

@app.route('/get_report', methods=['GET'])
def get_report():
    report_id = request.args.get('report_id')
    status, report = report_status.get(report_id, (None, None))

    if status is None:
        return jsonify({"status": "Invalid report_id"}), 400

    if status == "Running":
        return jsonify({"status": "Running"})

    return jsonify({"status": "Complete", "report": report})

if __name__ == '__main__':
    app.run(debug=True)
