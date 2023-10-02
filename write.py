import csv
import json
import datetime


def write_to_csv(results, filename):
    print("lookhere")
    # res = []
    # for item in results:
    try:
        fieldnames = [
            "datetime_utc",
            "distance_au",
            "velocity_km_s",
            "designation",
            "name",
            "diameter_km",
            "potentially_hazardous",
        ]
        with open(filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for item in results:
                time = item.time
                pha = "True" if item.neo.hazardous else "False"
                diameter = "" if item.neo.diameter == "" else item.neo.diameter
                name = item.neo.name if item.neo.name else ""

                d = {
                    "datetime_utc": time,
                    "distance_au": item.distance,
                    "velocity_km_s": item.velocity,
                    "designation": item.neo.designation,
                    "name": name,
                    "diameter_km": diameter,
                    "potentially_hazardous": pha,
                }
                writer.writerow(d)
    except Exception as e:
        print("an error accored", e)


def write_to_json(results, filename):
    json_res = []
    for item in results:
        time = item.time.isoformat()
        pha = "True" if item.neo.hazardous else "False"
        diameter = "" if item.neo.diameter == "" else item.neo.diameter
        name = item.neo.name if item.neo.name else ""

        d = {
            "datetime_utc": time,
            "distance_au": item.distance,
            "velocity_km_s": item.velocity,
            "designation": item.neo.designation,
            "name": name,
            "diameter_km": diameter,
            "potentially_hazardous": pha,
        }
        json_res.append(d)
    with open(filename, "w") as f:
        json.dump(json_res, f, indent=4)
