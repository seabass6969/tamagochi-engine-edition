import jsonschema
import json
import os

DATA_TEMPLATE = {"done_tutorial": False, "yourself": False, "pet": False}
SCHEMA = {
    "type": "object",
    "properties": {
        "done_tutorial": {"type": "boolean"},
        "yourself": {"type": "boolean"},
        "pet": {"type": "boolean"},
    },
    "required": ["done_tutorial", "yourself", "pet"],
    "additionalProperties": False,
}


def missing_property_checker(instance: dict, schema: dict) -> list:
    v = jsonschema.Draft202012Validator(SCHEMA)
    errors = sorted(v.iter_errors(instance), key=lambda e: e.path)
    properties = []
    for error in errors:
        if error.validator == "required":
            properties.append(error.message.split("'")[1])
    return properties


def fill_missing_properties(original: dict, missing: [str], default: dict) -> dict:
    for prop in missing:
        original[prop] = default.get(prop)
    return original


class Datahandler:
    def __init__(self):
        self.STOREPATH = os.path.join("../", "store.json")
        if os.path.isfile(self.STOREPATH):
            self.FILEOPEN = open(self.STOREPATH)
        else:
            # if the file is not exist
            self.FILEOPEN = open(self.STOREPATH)
            self.FILEOPEN.write(json.dumps(DATA_TEMPLATE))
        data = json.loads(self.FILEOPEN.read())
        missing = missing_property_checker(data, SCHEMA)
        data = fill_missing_properties()

    def end(self):
        self.FILEOPEN.close()


data = Datahandler()
