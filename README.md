# Json-Model-Variation-Generator
A simple but efficient tool to generate multiple variations of a single Minecraft .json model and its textures from reference textures.

# How to use
1: Place the desired input model and its textures in a folder named "inputs" (the model should correctly reference the textures) and create another folder name "outputs"

2: Place your reference textures in folder named "references" (the ones that will be used as texture 'tint' references; Their name is extremely important as they will be used as the suffix of the generated textures and models and **should not contain underscores**)

3: Run 'TexturePaletteMix.py' and wait for the generation to complete. This will first generated the various textures (Note that you can totally use this tool alone, generating the alternate models is just a way to speed up implementation)

4: Run 'ModelAdapter.py' and enter the desired texture location that will be specified in each .json model (e.g: "blocks", "items", "custom" etc..) and wait for the generation to complete.

5: If needed, run 'FolderOrganizer.py' to reorganize all models and textures based on their prefixes.

6: Everything generated should be located in a folder name "outputs".

*Notes: 
-Multiple models can be generated and organized at once.
-If you really need some variation to have a suffix containing an underscore (e.g: "dark_oak"), I highly recommend using PowerToys's Power Rename feature alongside this tool.*
