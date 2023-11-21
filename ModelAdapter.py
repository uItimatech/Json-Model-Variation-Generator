# This program reads all the .json input files in the "input" folder and modifies them so the texture matches the different images in the "output" folder.
# It basically only affects the texture names within the .json files.

import os
import json

print("Enter the texture folder location: (default: none)")
textureFolder = input()

def main():

    # Clears the outputs folder of all .json files
    for file in os.listdir("outputs"):
        if file.endswith(".json"):
            os.remove("outputs/" + file)

    # Get the list of files in the "input" folder
    inputModelFiles = []
    referenceSuffix = []

    # Lists all the model variations
    for file in os.listdir("references"):
        if file.endswith(".png"):
            referenceSuffix.append(file.split(".")[0].split("_")[len(file.split(".")[0].split("_"))-1])

    # Lists all the models to be modified
    for file in os.listdir("inputs"):
        if file.endswith(".json"):

            # Copies the file to the "outputs" fcolder with all variations
            for variation in referenceSuffix:
                with open("inputs/" + file, "r+") as inputModelFile:
                    with open("outputs/" + file.split(".")[0] + "_" + variation + ".json", "w+") as outputModelFile:
                        outputModelFile.write(inputModelFile.read())

            # Adds the file to the list of files to be modified
            inputModelFiles.append(file.split(".")[0] + ".json")
                
            print("Found file: " + file)

    print("Registered " + str(len(inputModelFiles)) + " files to modify.")





    # For each model to be modified
    currentModel = 0
    for inputModelFile in inputModelFiles:

        # For each variation of the model
        for variation in referenceSuffix:
            currentModel += 1
            
            # Open the file
            with open("outputs/" + inputModelFile.split(".")[0] + "_" + variation + ".json", "r+") as modelFile:
                model = json.load(modelFile)

                # For each texture in the model
                for texture in model["textures"]:
                    # Modify the texture
                    rawTextureName = model["textures"][texture].split(".")[0]
                    model["textures"][texture] = textureFolder + rawTextureName + "_" + variation

                # Write the modified model
                modelFile.seek(0)
                json.dump(model, modelFile, indent=4)
                modelFile.truncate()
            
                print("Model modified. " + str(currentModel) + "/" + str(len(inputModelFiles)*len(referenceSuffix)))
                print("File: " + inputModelFile.split(".")[0] + "_" + variation + ".json")




    print("Press enter to exit.")
    input()

main()