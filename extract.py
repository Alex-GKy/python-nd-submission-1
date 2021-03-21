"""Extract data on near-Earth objects and close approaches from CSV and JSON
files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
    near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    neos = list()

    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        # next(reader) #skip header

        for row in reader:
            neos.append(NearEarthObject(pdes=row['pdes'],
                                        name=row['name'],
                                        diameter=row['diameter'],
                                        hazardous=row['pha']))

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close
    approaches.
    :return: A collection of `CloseApproach`es.
    """

    cads = list()

    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)

        for row in contents['data']:
            cads.append(CloseApproach(des=row[0],
                                      time=row[3],
                                      dist=row[5],  # using min distance here
                                      vrel=row[7]))
    return cads
