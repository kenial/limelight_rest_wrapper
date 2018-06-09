# Limelight REST API samples to get statistics
import time
import os.path
import datetime
import json

import llutil
import limelight_rest_wrapper
llrest = limelight_rest_wrapper.LimelightRESTWrapper("keniallee", "XXXXXXXXXXXXXXXXXXX")

LL_API_PREFIX_TRAFFIC = "https://control.llnw.com/traffic-reporting-api/v2"
LL_API_PREFIX_METADATA = "https://control.llnw.com/metadata-reporting-api/v1"
LL_API_PREFIX_CATEGORY = "https://control.llnw.com/category-reporting-api/v1"
LL_API_PREFIX_GEO = "https://control.llnw.com/geo-reporting-api/v1/"
LL_API_PREFIX_HTTP_STREAMING = "https://control.llnw.com/http-streaming-reporting-api/v1"
LL_API_PREFIX_LAMA = "https://control.llnw.com/lama-reporting-api/v1/daily"
LL_API_PREFIX_PURGE = "https://purge.llnw.com/purge/v1"




endpoint = "https://control.llnw.com/geo-reporting-api/v1/countries/1/cities"    # US
query_params = {
    "shortname": "service_name",    # service name
    "service": "http",
    "reportDuration": "week",
    "startDate": "2016-08-07",  # if datetime is needed, use isoformat() method
    "dataLimit": 50000,
}
res = llrest.api_get(endpoint, query_params)



# ll stats by geo (city level)
for dt in [
    "2016-09-01",
    "2016-09-02",
    "2016-09-03",
    "2016-09-04",
    "2016-09-05",
    "2016-09-06",
    "2016-09-07",
    "2016-09-08",
    "2016-09-09",
    "2016-09-10",
    "2016-09-11",
    "2016-09-12",
    "2016-09-13",
    "2016-09-14",
    "2016-09-15",
    "2016-09-16",
    "2016-09-17",
    "2016-09-18",
    "2016-09-19",
    "2016-09-20",
    "2016-09-21",
    "2016-09-22",
    "2016-09-23",
    "2016-09-24",
    "2016-09-25",
    "2016-09-26",
    "2016-09-27",
    "2016-09-28",
    "2016-09-29",
    "2016-09-30",
    "2016-10-01",
    "2016-10-02",
    "2016-10-03",
    "2016-10-04",
    "2016-10-05",
    "2016-10-06",
    "2016-10-07",
]:
    print("fetching %s ..." % dt)
    endpoint = "https://control.llnw.com/geo-reporting-api/v1/cities"    # world
    query_params = {
        "shortname": "service_name",    # service name
        "service": "hls",
        "reportDuration": "day",
        "startDate": dt,  # if datetime is needed, use isoformat() method
        "dataLimit": 50000,
    }
    res = llrest.api_get(endpoint, query_params)
    obj = json.loads(res.text)
    #
    data = []
    for continent in obj["Continent"]:
        for country in continent["Country"]:
           for state in country["State"]:
               for city in state["City"]:
                    # {'bytes':     7036213669870.709,
                    # 'id': 23,
                    # 'inBytes':    4080656812558.3086,
                    # 'name': 'San Jose',
                    # 'requests': 3130449.9160715262,
                    # 'seconds': 2467422.8442425025,
                    # 'totalBytes': 11116870482429.018}
                    d = {
                        "continent": continent["name"],
                        "country": country["name"],
                        "state": state["name"],
                        "city": city["name"],
                        "bytes_per_sec": city["bytes"]/city["seconds"],
                        "bytes_per_req": city["bytes"]/city["requests"],
                        "bytes": city["bytes"],
                        "seconds": city["seconds"],
                        "requests": city["requests"],
                        "totalBytes": city["totalBytes"],
                    }
                    data.append(d)
    #for d in sorted(data, key=lambda d: d["bytes_per_sec"]):
    for d in data:
        output_text = "%s, %s, %s, %s, %s, %.1f, %.1f, %.1f, %.1f" % (
            dt,
            d["continent"],
            d["country"],
            d["state"],
            d["city"],
            d["bytes"],
            d["totalBytes"],
            d["requests"],
            d["seconds"],
        )
        with open("ll_stats_by_geo_0901_1007_hls.csv", "a") as f:
            f.write(output_text+"\n")



endpoint = "https://control.llnw.com/geo-reporting-api/v1/countries/1/cities"    # US
query_params = {
    "shortname": "service_name",    # service name
    "service": "http",
    "reportDuration": "week",
    "startDate": "2016-08-07",  # if datetime is needed, use isoformat() method
    "dataLimit": 50000,
}
res = llrest.api_get(endpoint, query_params)


# get_disk_usage - not working
endpoint = os.path.join(LL_API_PREFIX_TRAFFIC, "storage")
query_params = {
    "shortname": "service_name",    # service name
    "service": "http",
    "reportDuration": "custom",
    "startDate": "2016-09-01",  # if datetime is needed, use isoformat() method
    "endDate": "2016-09-29",  # if datetime is needed, use isoformat() method
    "dataLimit": 50000,
}
res = llrest.api_get(endpoint, query_params)
print(res.text)

# summary - peak bytes, peak connection
endpoint = os.path.join(LL_API_PREFIX_TRAFFIC, "summary")
query_params = {
    "shortname": "service_name",    # service name
    "service": "http",
    "reportDuration": "hour",
    "startDate": "2016-09-29",  # if datetime is needed, use isoformat() method
    "endDate": "2016-09-29",  # if datetime is needed, use isoformat() method
    "dataLimit": 50000,
}
res = llrest.api_get(endpoint, query_params)
print(res.text)




# File Types Report
for d in [
    "2016-09-22",
    "2016-09-23",
    "2016-09-24",
    "2016-09-25",
    "2016-09-26",
    "2016-09-27",
    "2016-09-28",
    "2016-09-29",
]:
    endpoint = os.path.join(LL_API_PREFIX_CATEGORY, "content/file_types")
    query_params = {
        "shortname": "service_name",    # service name
        "service": "http",
        "reportDuration": "day",
        "startDate": d,  # if datetime is needed, use isoformat() method
        "endDate": d,  # if datetime is needed, use isoformat() method
        "dataLimit": 50000,
    }
    res = llrest.api_get(endpoint, query_params)
    print(res.text)



# Hourly Report
for d in [
    "2016-09-22",
    "2016-09-23",
    "2016-09-24",
    "2016-09-25",
    "2016-09-26",
    "2016-09-27",
    "2016-09-28",
    "2016-09-29",
]:
    endpoint = os.path.join(LL_API_PREFIX_CATEGORY, "traffic/hourly")
    query_params = {
        "shortname": "service_name",    # service name
        "service": "hls",
        "reportDuration": "day",
        "startDate": d,  # if datetime is needed, use isoformat() method
        "dataLimit": 50000,
    }
    res = llrest.api_get(endpoint, query_params)
    print(res.text)


# missing file
for d in [
    "2016-09-22",
]:
    endpoint = os.path.join(LL_API_PREFIX_CATEGORY, "content/missing_files")
    query_params = {
        "shortname": "service_name",    # service name
        "service": "hls",
        "startDate": d,  # if datetime is needed, use isoformat() method
        "endDate": "2016-09-29",  # if datetime is needed, use isoformat() method
        "dataLimit": 50000,
    }
    res = llrest.api_get(endpoint, query_params)
    print(res.text)

# file error
# status code
# session duration

endpoint = os.path.join(LL_API_PREFIX_PURGE, "account/service_name/requests")
query_params = {
    "patterns":[
        {
            "pattern":"http://*/hls_segment/v1/201610/variety/playlist_*.m3u8",
            "evict":False,
            "exact":False,
            "incqs":False
        },
    ],
    "notes": "from API, %s" % datetime.datetime.now()
}
res = llrest.api_post(endpoint, query_params)



# livestats
endpoint = os.path.join(LL_API_PREFIX_TRAFFIC, "livestats")
query_params = {
    "shortname": "service_name",    # service name
    "service": "http",
    "reportDuration": "custom",
    "startDate": int(time.time()) - 3600,
    "endDate": int(time.time()),
    "displayPopDat": 1,
}
res = llrest.api_get(endpoint, query_params)
print(res.text)

