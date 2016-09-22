# limelight_rest_wrapper
Wrapper of Limelight REST API

Usage:
```
ll = limelight_rest_wrapper.LimelightRESTWrapper("<limelight_id>", "<limelight_api_key>")
# sample: Geographical reporting by cities in US
endpoint = "https://control.llnw.com/geo-reporting-api/v1/countries/1/cities"    
query_params = {
    "shortname": "odkmmdod",    # service name
    "service": "http",
    "reportDuration": "week",
    "startDate": "2016-08-07",  # if datetime is needed, use isoformat() method
    "dataLimit": 50000,
}
ll.api_call(endpoint, query_params)
```
