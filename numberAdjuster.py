def numberAdjuster(number: int, degits: int) -> str:
    num = str(number)
    return (degits - len(num)) * "0" + num