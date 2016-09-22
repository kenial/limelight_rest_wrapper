# limelight_rest_wrapper
Wrapper of Limelight REST API (supports Python 3 only)

Usage:
```
# sample: Geographical reporting by cities in US (GET)
ll = limelight_rest_wrapper.LimelightRESTWrapper("<limelight_id>", "<limelight_api_key>")
endpoint = "https://control.llnw.com/geo-reporting-api/v1/countries/1/cities"
query_params = {
    "shortname": "test_service",    # service name - usually, your host name on limelight
    "service": "http",
    "reportDuration": "week",
    "startDate": "2016-08-07",  # if datetime format is needed, use isoformat() method of datetime
    "dataLimit": 50000,
}
ll.api_get(endpoint, query_params)
```

```
# sample: SmartPurge (POST)
ll = limelight_rest_wrapper.LimelightRESTWrapper("<limelight_id>", "<limelight_api_key>")
endpoint = "https://purge.llnw.com/purge/v1/account/{account}/requests"
query_params = {
    "patterns":[
        {
            "pattern":"http://test.site.com/temp/purge/*.jpg",
            "evict":False,  # False: invalidate, True: evict (remove from cache entirely)
            "exact":False,  # False: partial pattern, True: exact match
            "incqs":False,  # False: on, True: include query string
        },
    ],
    # "email":{
    #     "subject":"purge results",
    #     "to":"user@example.com"
    # },
    # "callback":{"url":"http://test.example.com/my_callback.php" },
    "notes": "Test purge thru API",
}
res = ll.api_post(endpoint, query_params)
