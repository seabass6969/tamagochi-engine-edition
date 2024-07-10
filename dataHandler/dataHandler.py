import jsonschema
import json
import os
import Level

DATA_TEMPLATE = {
    "done_tutorial": False,
    "health": 10,
    "oilLevel": 1,
    "level": 0,
    "progression": 0,
    "gotchiPoint": 0,
    "emotion": "happy",
    "fuel_filter_functional": False,
    "spark_plug_functional": False,
    "battery_level": 1,
    "gears_missing": 0,
}
SCHEMA = {
    "type": "object",
    "properties": {
        "done_tutorial": {"type": "boolean"},
        "health": {"type": "number", "minimum": 0, "maximum": 10},
        "oilLevel": {"type": "number", "minimum": 0, "maximum": 1},
        "level": {"type": "number", "minimum": 0},
        "progression": {"type": "number", "minimum": 0, "maximum": 1},
        "gotchiPoint": {"type": "number", "minimum": 0},
        "emotion": {"type": "string", "enum": ["happy", "sad", "ill", "mid", "angry"]},
        "fuel_filter_functional": {"type": "boolean"},
        "spark_plug_functional": {"type": "boolean"},
        "battery_level": {"type": "number", "minimum": 0, "maximum": 1},
        "gears_missing": {"type": "number", "minimum": 0},
    },
    "required": [
        "done_tutorial",
        "health",
        "oilLevel",
        "level",
        "progression",
        "gotchiPoint",
        "emotion",
        "fuel_filter_functional",
        "spark_plug_functional",
        "battery_level",
        "gears_missing",
    ],
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
        self.done_tutorial = DATA_TEMPLATE.get("done_tutorial")
        self.health = DATA_TEMPLATE.get("health")
        self.oilLevel = DATA_TEMPLATE.get("oilLevel")
        self.level = Level.Level(
            DATA_TEMPLATE.get("level"), DATA_TEMPLATE.get("progression")
        )
        self.gotchiPoint = DATA_TEMPLATE.get("gotchiPoint")
        self.emotion = DATA_TEMPLATE.get("emotion")

        self.fuel_filter_functional = DATA_TEMPLATE.get("fuel_filter_functional")
        self.spark_plug_functional = DATA_TEMPLATE.get("spark_plug_functional")
        self.battery_level = DATA_TEMPLATE.get("battery_level")
        self.gears_missing = DATA_TEMPLATE.get("gears_missing")

        self.STOREPATH = os.path.join("../", "store.json")
        if os.path.exists(self.STOREPATH) == False:
            # if file not exist
            self.FILEOPEN = open(self.STOREPATH, "w")
            json.dump(DATA_TEMPLATE, self.FILEOPEN, indent=0)
            self.FILEOPEN = open(self.STOREPATH, "r")
        else:
            self.FILEOPEN = open(self.STOREPATH, "r")

        self.data = json.load(self.FILEOPEN)
        print("loading data")
        print(self.data)
        missing = missing_property_checker(self.data, SCHEMA)
        self.data = fill_missing_properties(self.data, missing, DATA_TEMPLATE)
        self.load()
        self.save()

    def end(self):
        self.FILEOPEN.close()

    def save(self):
        self.data = {
            "done_tutorial": self.getDoneTutorial(),
            "health": self.getHealth(),
            "oilLevel": self.getOilLevel(),
            "level": self.getLevel().getLevel(),
            "progression": self.getLevel().getProgression(),
            "gotchiPoint": self.getGotchiPoint(),
            "emotion": self.getEmotion(),
            "fuel_filter_functional": self.getFilter(),
            "spark_plug_functional": self.getSparkPlug(),
            "battery_level": self.getBatteryLevel(),
            "gears_missing": self.getGearMissing(),
        }
        self.FILEOPEN = open(self.STOREPATH, "w")
        self.FILEOPEN.write(json.dumps(self.data))
        self.FILEOPEN = open(self.STOREPATH, "r")

    def load(self):
        self.done_tutorial = self.data.get("done_tutorial")
        self.health = self.data.get("health")
        self.oilLevel = self.data.get("oilLevel")
        self.level = Level.Level(self.data.get("level"), self.data.get("progression"))
        self.gotchiPoint = self.data.get("gotchiPoint")
        self.emotion = self.data.get("emotion")
        self.fuel_filter_functional = self.data.get("fuel_filter_functional")
        self.spark_plug_functional = self.data.get("spark_plug_functional")
        self.battery_level = self.data.get("battery_level")
        self.gears_missing = self.data.get("gears_missing")

    def getDoneTutorial(self):
        return self.done_tutorial

    def setDoneTutorial(self, done_tutorial):
        self.done_tutorial = done_tutorial
        self.save()

    def getHealth(self):
        return self.health

    def setHealth(self, health):
        self.health = health
        self.save()

    def increaseHealth(self, by):
        self.health += by
        self.save()

    def decreaseHealth(self, by):
        self.health -= by
        self.save()

    def getOilLevel(self):
        return self.oilLevel

    def setOilLevel(self, oilLevel):
        self.oilLevel = oilLevel
        self.save()

    def getLevel(self):
        return self.level

    def setLevel(self, level, progression):
        self.level = Level(level, progression)
        self.save()

    def getGotchiPoint(self):
        return self.gotchiPoint

    def setGotchiPoint(self, gotchiPoint):
        self.gotchiPoint = gotchiPoint
        self.save()

    def increaseGotchiPoint(self, by):
        self.gotchiPoint += by
        self.save()

    def decreaseGotchiPoint(self, gotchiPoint):
        self.gotchiPoint += by
        self.save()

    def getEmotion(self):
        return self.emotion

    def setEmotion(self, emotion):
        self.emotion = emotion
        self.save()

    def getFilter(self):
        return self.fuel_filter_functional

    def setFilter(self, filter):
        self.fuel_filter_functional = filter
        self.save()

    def getSparkPlug(self):
        return self.spark_plug_functional

    def setSparkPlug(self, spark):
        self.spark_plug_functional = spark
        self.save()

    def getBatteryLevel(self):
        return self.battery_level

    def setBatteryLevel(self, battery):
        self.battery_level = battery
        self.save()

    def getGearMissing(self):
        return self.gears_missing

    def setGearMissing(self, gear):
        self.gears_missing = gear
        self.save()


# data = Datahandler()


# data.setDoneTutorial(True)
# print(data.getDoneTutorial())
