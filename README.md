# Restaurant Monitoring Application

This project provides an API to monitor the uptime and downtime of restaurants based on their business hours.

## Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)
- Flask
- pandas

## Setup

1. **Clone the repository and navigate to the project directory:**

   ```
   git clone <repository-url>
   cd restaurant_monitoring
   ```
 
2. **Create and activate a virtual environment:**

    On Windows:

    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```

    On macOS/Linux:
    
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
    
3. **Install the required packages:**

    ```
    pip install Flask pandas
    ```
4. **Ensure the necessary CSV files are in the project directory:**

- store_status.csv
- Menu_hours.csv
- bq-results-20230125-202210-1674678181880.csv


Your project directory should look like this:

```
restaurant_monitoring/
├── venv/
├── store_status.csv
├── Menu_hours.csv
├── bq-results-20230125-202210-1674678181880.csv
├── initialize_database.py
├── ingest_data.py
├── app.py
```

## Running the Application

1. **Initialize the database:**

    ```
    python initialize_database.py
    ```
2. **Ingest data into the database:**

    ```
    python ingest_data.py
    ```
    
3. **Run the Flask application:**
    
    ```
    python app.py
    ```

The Flask server will start running on http://127.0.0.1:5000.

## Testing the Application

### Using Command Prompt or Git Bash

1. **Trigger report generation:**

    ```
    curl -X POST http://127.0.0.1:5000/trigger_report
    ```
    
    **Expected Output:**

    ```
    {
        "report_id": "some-unique-report-id"
    }
    ```
    
2. **Check report status:**

    After receiving the report_id from the previous command, use it in the following command:

    ```
    curl -X GET "http://127.0.0.1:5000/get_report?report_id=<report_id>"
    ```
    Replace <report_id> with the actual report ID you received.
    

    **Expected Output if Report is Still Running:**
    
    ```
    {
        "status": "Running"
    }
    ```
    **Expected Output if Report is Complete:**

    ```
    {
        "status": "Complete",
        "report": "Generated report data"
    }
    ```

### Using Postman

1. **Trigger report generation:**

- Method: POST
- URL: http://127.0.0.1:5000/trigger_report
- Click Send
- You will receive a response with the report_id.

    **Expected Response:**

    ```
    {
        "report_id": "some-unique-report-id"
    }
    ```
    
2. **Check report status:**

- Method: GET
- URL: http://127.0.0.1:5000/get_report?report_id=<report_id>
- Replace <report_id> with the actual report ID you received.
- Click Send

    **Expected Response if Running:**

    ```
    {
        "status": "Running"
    }
    ```

    **Expected Response if Complete:**

    ```
    {
        "status": "Complete",
        "report": "Generated report data"
    }
    ```
    
## Example Results

1. **Trigger report generation:**

    ```
    curl -X POST http://127.0.0.1:5000/trigger_report
    ```

    **Response:**

    ```
    {
        "report_id": "123e4567-e89b-12d3-a456-426614174000"
    }
    ```

2. **Check report status:**

    ```
    curl -X GET "http://127.0.0.1:5000/get_report?report_id=123e4567-e89b-12d3-a456-426614174000"
    ```

    **Response if Running:**

    ```
    {
        "status": "Running"
    }
    ```

    **Response if Complete:**
    
    ```
    {
        "status": "Complete",
        "report": "Generated report data"
    }
    ```