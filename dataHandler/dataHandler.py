import jsonschema
import json, os, math, random, time
from constants import Level
from constants.emotionConstant import (
    EMOTIONAL_PROGRESSION_NEGATIVELY,
    EMOTIONAL_PROGRESSION_POSITIVELY,
)
from constants.MarketPlaceItems import MarketPlaceItem

DATA_TEMPLATE = {
    "done_tutorial": False,
    "health": 10,
    "oilLevel": 100,
    "level": 0,
    "progression": 0,
    "gotchiPoint": 100,
    "emotion": "happy",
    "fuel_filter_functional": True,
    "spark_plug_functional": True,
    "battery_level": 100,
    "gears_missing": 0,
    "last_login": 1722081124,  # using the python time.time()
    "first_login": math.floor(time.time()),
    "purchased_gears": 0,
    "purchased_fuel_filters": 0,
    "purchased_spark_plugs": 0,
    "purchased_chargers": 0,
    "purchased_oil": 0,
}
SCHEMA = {
    "type": "object",
    "properties": {
        "done_tutorial": {"type": "boolean"},
        "health": {"type": "number", "minimum": 0, "maximum": 10},
        "oilLevel": {"type": "number", "minimum": 0, "maximum": 100},
        "level": {"type": "number", "minimum": 0},
        "progression": {"type": "number", "minimum": 0, "maximum": 1},
        "gotchiPoint": {"type": "number", "minimum": 0},
        "emotion": {"type": "string", "enum": ["happy", "sad", "ill", "mid", "angry"]},
        "fuel_filter_functional": {"type": "boolean"},
        "spark_plug_functional": {"type": "boolean"},
        "battery_level": {"type": "number", "minimum": 0, "maximum": 100},
        "gears_missing": {"type": "number", "minimum": 0},
        "last_login": {"type": "number"},
        "first_login": {"type": "number"},
        "purchased_gears": {"type": "number"},
        "purchased_fuel_filters": {"type": "number"},
        "purchased_spark_plugs": {"type": "number"},
        "purchased_chargers": {"type": "number"},
        "purchased_oil": {"type": "number"},
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
        "last_login",
        "first_login",
        "purchased_gears",
        "purchased_fuel_filters",
        "purchased_spark_plugs",
        "purchased_chargers",
        "purchased_oil",
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
        self.last_deduction_period = 0
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
        self.last_login = DATA_TEMPLATE.get("last_login")
        self.first_login = DATA_TEMPLATE.get("first_login")

        self.purchased_gears = DATA_TEMPLATE.get("purchased_gears")
        self.purchased_fuel_filters = DATA_TEMPLATE.get("purchased_fuel_filters")
        self.purchased_spark_plugs = DATA_TEMPLATE.get("purchased_spark_plugs")
        self.purchased_chargers = DATA_TEMPLATE.get("purchased_chargers")
        self.purchased_oil = DATA_TEMPLATE.get("purchased_oil")


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
        self.setLastLogin()
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
            "last_login": self.getLastLogin(),
            "first_login": self.getFirstLogin(),
            "purchased_gears": self.purchased_gears,
            "purchased_fuel_filters": self.purchased_fuel_filters,
            "purchased_spark_plugs": self.purchased_spark_plugs,
            "purchased_chargers": self.purchased_chargers,
            "purchased_oil": self.purchased_oil
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
        self.last_login = self.data.get("last_login")
        self.first_login = self.data.get("first_login")

        self.purchased_gears = self.data.get("purchased_gears")
        self.purchased_fuel_filters = self.data.get("purchased_fuel_filters")
        self.purchased_spark_plugs = self.data.get("purchased_spark_plugs")
        self.purchased_chargers = self.data.get("purchased_chargers")
        self.purchased_oil = self.data.get("purchased_oil")

    def getDataByID(self, ID):
        self.data.get(ID)

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
        if (self.health + by) <= 10:
            self.health += by
            self.save()

    def decreaseHealth(self, by):
        if (self.health - by) >= 0:
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
        self.level = Level.Level(level, progression)
        self.save()

    def increaseLevel(self, progression):
        left = progression
        while (
            self.getLevel().getLevelProgressionMax()
            - (self.getLevel().getProgression() + left)
        ) <= 0:
            left -= (
                self.getLevel().getLevelProgressionMax()
                - self.getLevel().getProgression()
            )
            self.setLevel(self.getLevel().getLevel() + 1, 0)
        self.setLevel(
            self.getLevel().getLevel(), self.getLevel().getProgression() + left
        )
        print(
            "level: {} and {} and {} away from next level".format(
                self.getLevel().getLevel(),
                self.getLevel().getProgression(),
                self.getLevel().getLevelProgressionMax()
                - self.getLevel().getProgression(),
            )
        )
        self.save()

    def getGotchiPoint(self):
        return self.gotchiPoint

    def getGotchiPointRequirementMet(self, price: int) -> bool:
        if (self.gotchiPoint - price) <= 0:
            return False
        else:
            return True
    def setGotchiPoint(self, gotchiPoint):
        self.gotchiPoint = gotchiPoint
        self.save()

    def increaseGotchiPoint(self, by):
        self.gotchiPoint += by
        self.save()

    def decreaseGotchiPoint(self, by):
        self.gotchiPoint -= by
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

    def decreaseGearMissing(self, by):
        self.gears_missing -= by 
        self.save()

    def getLastLogin(self):
        return self.last_login

    def setLastLogin(self):
        self.last_login = math.floor(time.time())
        self.save()

    def isDead(self):
        if self.health == 0:
            return True
        else:
            return False

    def getTimeTillLastLogin(self, unit):
        """
        get the time till last login in any unit
        - seconds (s)
        - minutes (m)
        - hours (h)
        failback will be second
        """
        period = math.floor(time.time()) - self.last_login  # this is in second
        match unit:
            case "s":
                return period
            case "m":
                return math.floor(period / 60)
            case "h":
                return math.floor(period / 60 / 60)
            case _:
                return period

    def getFirstLogin(self):
        return self.first_login

    def randomDeduction(self):
        last_login_time = self.getTimeTillLastLogin("s")
        if (
            last_login_time % (30) == 0
            and last_login_time != 0
            and last_login_time != self.last_deduction_period
        ):
            if (
                random.randint(1, 20) == 1 and self.getGearMissing() <= 10
            ):  # 1 in 20 chance - the gear will miss
                self.gears_missing += 1
            if (
                random.randint(1, 2) == 1 and self.getBatteryLevel() > 0
            ):  # 1 in 2 chance - battery level decrease by 1%
                self.setBatteryLevel(self.getBatteryLevel() - 1)
            if self.getOilLevel() > 0:  # oil level decrease by 1%
                self.setOilLevel(self.getOilLevel() - 1)
            if random.randint(1, 100) == 1:  # 1 in 100 chance spark plug go malfunction
                self.setSparkPlug(False)
            if random.randint(1, 100) == 1:  # 1 in 100 chance filter go malfunction
                self.setFilter(False)

            print("random Dedcution happened every 30 second", last_login_time)
            self.healthAndEmotionHandler()
            self.last_deduction_period = (
                last_login_time  # this is used to prevent double deduction
            )

    def healthAndEmotionHandler(self):
        if self.petHealth():
            print("health oh no")
        if self.petHealth() and random.randint(1, 5):
            self.EmotionTriggerer("-")
            self.decreaseHealth(1)

    def EmotionTriggerer(self, poles):
        """
        poles - parameter for + or - emotion
        """
        if poles == "-":
            self.setEmotion(random.choice(EMOTIONAL_PROGRESSION_NEGATIVELY))
        if poles == "+":
            self.setEmotion(random.choice(EMOTIONAL_PROGRESSION_POSITIVELY))

    def petHealth(self) -> bool:
        return (
            self.getBatteryLevel() < 5
            or self.getGearMissing() == 10
            or self.getOilLevel() < 5
        ) and (not self.getSparkPlug() or not self.getFilter())

    def petAge(self) -> str:
        times = math.floor(time.time() - self.getFirstLogin())

        seconds = (times) % 60
        minutes = (times // 60) % 60
        hours = (times // 60 // 60) % 24
        days = (times // 60 // 60 // 24)
        return "{}d - {}h - {}m - {}s".format(
            days,
            hours,
            minutes,
            seconds,
        )
    
    def purchaseItem(self, itemID):
        match itemID:
            case "SPARK_PLUG":
                self.purchased_spark_plugs += 1
            case "FUEL_FILTER":
                self.purchased_fuel_filters += 1
            case "GEAR":
                self.purchased_gears += 1
            case "BATTERY_CHARGER":
                self.purchased_chargers += 10
            case "OIL":
                self.purchased_oil += 10
        self.save()

    def usingItem(self, itemID):
        match itemID:
            case "SPARK_PLUG":
                self.purchased_spark_plugs -= 1
            case "FUEL_FILTER":
                self.purchased_fuel_filters -= 1
            case "GEAR":
                self.purchased_gears -= 1
            case "BATTERY_CHARGER":
                self.purchased_chargers -= 10
            case "OIL":
                self.purchased_oil -= 10
        self.save()
    

    def garagePartsRemaining(self, itemID):
        match itemID:
            case "SPARK_PLUG":
                return self.purchased_spark_plugs
            case "FUEL_FILTER":
                return self.purchased_fuel_filters
            case "GEAR":
                return self.purchased_gears
            case "BATTERY_CHARGER":
                return self.purchased_chargers
            case "OIL":
                return self.purchased_oil
                
    def garagePartsRepairer(self, itemID):
        match itemID:
            case "SPARK_PLUG":
                self.setSparkPlug(True)
                self.purchased_spark_plugs -= 1
            case "FUEL_FILTER":
                self.setFilter(True)
                self.purchased_fuel_filters -= 1
            case "GEAR":
                self.decreaseGearMissing(1)
                self.purchased_gears -= 1
            case "BATTERY_CHARGER":
                if (self.getBatteryLevel() + 10) > 100:
                    onlyAdd = 100 - self.getBatteryLevel()
                    self.setBatteryLevel(100)
                    self.purchased_chargers -= onlyAdd
                else:
                    self.setBatteryLevel(self.getBatteryLevel() + 10)
                    self.purchased_chargers -= 10
            case "OIL":
                if (self.getOilLevel() + 10) > 100:
                    onlyAdd = 100 - self.getOilLevel()
                    self.setOilLevel(100)
                    self.purchased_oil -= onlyAdd
                else:
                    self.setOilLevel(self.getOilLevel() + 10)
                    self.purchased_oil -= 10
                
        self.save()
    
    """
    True -> item is repaired
    """
    def isRepaired(self, itemID):
        match itemID:
            case "SPARK_PLUG":
                return self.getSparkPlug() == True
            case "FUEL_FILTER":
                return self.getFilter() == True
            case "GEAR":
                return self.getGearMissing() == 0
            case "BATTERY_CHARGER":
                return self.getBatteryLevel() == 100
            case "OIL":
                return self.getOilLevel() == 100
                
            

    def wipeData(self):
        os.remove(self.STOREPATH)


# data = Datahandler()


# data.setDoneTutorial(True)
# print(data.getDoneTutorial())
