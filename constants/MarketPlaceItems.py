from constants.asset import IMAGE_MARKETPLACE


class MarketPlaceItem:
    def __init__(self, image, name, ID, price):
        self.image = IMAGE_MARKETPLACE.get(image)
        self.name = name
        self.ID = ID
        self.price = price


marketplaceItems_byID = {
    "SPARK_PLUG": MarketPlaceItem("SPARK_PLUG", "Spark Plug", "SPARK_PLUG", 10),
    "FUEL_FILTER": MarketPlaceItem("FUEL_FILTER", "Fuel Filter", "FUEL_FILTER", 10),
    "GEAR": MarketPlaceItem("GEAR", "Gear", "GEAR", 5),
    "BATTERY_CHARGER": MarketPlaceItem("BATTERY_CHARGER", "Charger {10%}", "BATTERY_CHARGER", 1),
    "OIL": MarketPlaceItem("OIL", "Oil {10%}", "OIL", 10),
}

