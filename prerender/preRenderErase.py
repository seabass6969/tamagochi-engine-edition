import os
cache_file = []
def newCacheReporting(directory):
    cache_file.append(directory)

def cleanCache():
    print("Cleaning pre-render cache.")
    for file in cache_file:
        os.remove(file)