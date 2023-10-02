"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
import datetime


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a CSV file, following the specification in the instructions.
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
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
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

    # TODO: Write the results to a JSON file, following the specification in the instructions.
