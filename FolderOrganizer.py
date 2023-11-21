# This program takes the textures and .json model files corresponding to a specific model variation and sorts them into folders. (format: "baseModelName/variationName")

import os
import shutil
import json


def main():

    variations = []
    baseModelNames = []

    for file in os.listdir("references"):
        if file.endswith(".png"):
            variations.append(file.split(".")[0].split("_")[len(file.split(".")[0].split("_"))-1])

    for file in os.listdir("inputs"):
        if file.endswith(".json"):
            baseModelNames.append(file.split(".")[0])

    print("Found " + str(len(variations)) + " variations and " + str(len(baseModelNames)) + " base models.")

    # Deletes all the folders in the outputs folder
    for file in os.listdir("outputs"):
        if os.path.isdir("outputs/" + file):
            shutil.rmtree("outputs/" + file)

    # Creates the folders and copies the corresponding .json files
    for baseModelName in baseModelNames:
        os.mkdir("outputs/" + baseModelName)
        for variation in variations:
            os.mkdir("outputs/" + baseModelName + "/" + baseModelName + "_" + variation)

            # Copies the .json files from the outputs folder to the new folders
            shutil.copy("outputs/" + baseModelName + "_" + variation + ".json", "outputs/" + baseModelName + "/" + baseModelName + "_" + variation)

            # Reads which textures are used in the .json file and copies them to the new folders
            
            with open("outputs/" + baseModelName + "_" + variation + ".json", "r+") as modelFile:
                model = json.load(modelFile)

                for texture in model["textures"]:
                    rawTextureName = model["textures"][texture].split(".")[0]
                    shutil.copy("outputs/" + rawTextureName + ".png", "outputs/" + baseModelName + "/" + baseModelName + "_" + variation)

            print("Copied " + baseModelName + "_" + variation + ".json and its textures to " + baseModelName + "/" + baseModelName + "_" + variation)

    # Deletes the unused .json and .png files in the outputs folder
    for file in os.listdir("outputs"):
        if file.endswith(".json") or file.endswith(".png"):
            os.remove("outputs/" + file)

    print("Press enter to exit.")
    input()

main()