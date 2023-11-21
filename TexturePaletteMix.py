# This program takes multiple images as inputs and outputs a new image that has the average hue, saturation, and value of the first images with the pixels of the second images.

from PIL import Image
import numpy as np
import os





def importImage(imageName):
    # Import the image
    image = Image.open(imageName)
    # Convert the image to HSV
    image = image.convert('HSV')
    # Convert the image to a numpy array
    image = np.array(image)
    # Return the image
    return image

def exportImage(image, imageName="output.png"):
    # Convert the image to a PIL image
    image = Image.fromarray(image, 'HSV')
    # Convert the image to HSV
    image = image.convert('RGBA')

    # For each pixel in the image, if the pixel is black, change it to a transparent pixel
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if image.getpixel((x, y))[0] == 0 and image.getpixel((x, y))[1] == 0 and image.getpixel((x, y))[2] == 0:
                image.putpixel((x, y), (0, 0, 0, 0))

    # Save the image
    image.save('outputs/'+ imageName)





def getAverageHUE(image):
    # Get the average HUE of the image (ignore all black pixels)
    averageHUE = 0
    pixelCount = 0
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x, y, 2] != 0:
                averageHUE += image[x, y, 0]
                pixelCount += 1
    averageHUE /= pixelCount
    # Return the average HUE
    return averageHUE

def setAverageHUE(image, wantedHUE):
    # Get the HUE of the image
    currentHUE = getAverageHUE(image)
    # Get the difference between the wanted and current HUE
    difference = wantedHUE - currentHUE
    # For each pixel in the image, change the HUE by the difference
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x, y, 0] != 0:
                image[x, y, 0] += difference
                if image[x, y, 0] < 0:
                    image[x, y, 0] += 255
                elif image[x, y, 0] > 255:
                    image[x, y, 0] -= 255

    # Return the image
    return image





def getAverageSAT(image):
    # Get the average SAT of the image (ignore all black pixels)
    averageSAT = 0
    pixelCount = 0
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x, y, 2] != 0:
                averageSAT += image[x, y, 1]
                pixelCount += 1
    averageSAT /= pixelCount
    # Return the average SAT
    return averageSAT

def setAverageSAT(image, wantedSAT):
    # Get the SAT of the image
    currentSAT = getAverageSAT(image)
    # Get the difference between the wanted and current SAT
    difference = wantedSAT - currentSAT
    # For each pixel in the image, change the SAT by the difference
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x, y, 1] != 0:
                image[x, y, 1] += difference
                if image[x, y, 1] < 0:
                    image[x, y, 1] += 255
                elif image[x, y, 1] > 255:
                    image[x, y, 1] -= 255

    # Return the image
    return image





def getAverageVAL(image):
    # Get the average VAL of the image (ignore all black pixels)
    averageVAL = 0
    pixelCount = 0
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x, y, 2] != 0:
                averageVAL += image[x, y, 2]
                pixelCount += 1
    averageVAL /= pixelCount
    # Return the average VAL
    return averageVAL

def setAverageVAL(image, wantedVAL):
    # Get the VAL of the image
    currentVAL = getAverageVAL(image)
    # Get the difference between the wanted and current VAL
    difference = wantedVAL - currentVAL
    # For each pixel in the image, change the VAL by the difference
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x, y, 2] != 0:
                image[x, y, 2] += difference
                if image[x, y, 2] < 0:
                    image[x, y, 2] += 255
                elif image[x, y, 2] > 255:
                    image[x, y, 2] -= 255

    # Return the image
    return image





def mixImages(reference, image):
    
    averageHUE = getAverageHUE(reference)
    averageSAT = getAverageSAT(reference)
    averageVAL = getAverageVAL(reference)

    # Changes the HUE, SAT, and VAL of the second image to match the average of the first image
    image = setAverageHUE(image, averageHUE)
    image = setAverageSAT(image, averageSAT)
    image = setAverageVAL(image, averageVAL)

    # Return the image
    return image





# Main function
def main():

    # Clears the outputs folder of all .png files
    for file in os.listdir("outputs"):
        if file.endswith(".png"):
            os.remove("outputs/" + file)

    # Gets all the images in the references folder
    referenceImages = []
    referenceSuffix = []

    for file in os.listdir("references"):
        if file.endswith(".png"):
            referenceImages.append(importImage("references/" + file))
            referenceSuffix.append(file.split(".")[0].split("_")[len(file.split(".")[0].split("_"))-1])
    
    # Gets all the images in the inputs folder
    inputImageNames = []

    for file in os.listdir("inputs"):
        if file.endswith(".png"):
            inputImageNames.append(file)

    # For each image in the references folder
    currentRef = 0
    for referenceImage in referenceImages:

        currentRef += 1
        print("Generating images for reference " + str(currentRef) + "/" + str(len(referenceImages)))
        # For each image in the inputs folder

        currentInput = 0
        for inputImageName in inputImageNames:

            currentInput += 1

            # Import the image
            inputImage = importImage("inputs/" + inputImageName)
            # Mix the images
            result = mixImages(referenceImage, inputImage)
            # Export the image
            exportImage(result, inputImageName.split(".")[0] + "_" + referenceSuffix[currentRef-1] + ".png")
            print("Image generated. "+ str(currentInput) + "/" + str(len(inputImageNames)))

    print("All images have been generated.")
    print("Press enter to exit.")
    input()

main()