```markdown
#Flask API for Current Information

This Flask API provides information about a user's Slack name, the current day of the week, the current UTC time, and their track. It accepts two GET request query parameters (`slack_name` and `track`) and returns the information in JSON format.

##API Endpoint

The API endpoint is `/api`.

##Usage

To use this API, make a GET request to the endpoint with the following parameters:

- `slack_name`: Your Slack name.
- `track`: Your chosen track (e.g., "backend").

Example URL:
```
https://task1-hngx.vercel.app/api?slack_name=example_name&track=backend
```

##Response

The API response will be in JSON format and will include the following fields:

- `slack_name`: The Slack name provided in the GET request.
- `current_day`: The current day of the week (e.g., "Monday").
- `utc_time`: The current UTC time (accurate within a +/-2 minute window) in ISO 8601 format (e.g., "2023-08-21T15:04:05Z").
- `track`: The track specified in the GET request.
- `status_code`: The HTTP status code, which will be 200 for success.

Example JSON response:
```json
{
  "slack_name": "example_name",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "backend",
  "github_file_url": "https://github.com/MichealDavid1/Task1_HNGX/blob/main/app.py","github_repo_url": "https://github.com/MichealDavid1/Task1_HNGX.git",
  "status_code": 200
}
```

##Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/your-flask-api.git
   ```

2. Install the required dependencies:

   ```
   pip install flask pytz
   ```

3. Run the Flask API:

   ```
   python app.py
   ```

The API will be accessible at `https://task1-hngx.vercel.app/api`.
