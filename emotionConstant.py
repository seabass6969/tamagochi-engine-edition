from asset import IMAGE
EMOTIONAL_IMAGE = {
    "happy": [
        IMAGE.get("HAPPY1"),
        IMAGE.get("HAPPY2"),
        IMAGE.get("HAPPY3"),
    ],
    "ill": [
        IMAGE.get("ILL"),
    ],
    "mid": [
        IMAGE.get("MID"),
    ],
    "sad": [
        IMAGE.get("SAD"),
    ],
    "angry": [
        IMAGE.get("ANGRY"),
    ],
}
EMOTIONAL_PROGRESSION_NEGATIVELY = ["ill", "sad", "angry"]
EMOTIONAL_PROGRESSION_POSITIVELY = ["happy", "mid"]