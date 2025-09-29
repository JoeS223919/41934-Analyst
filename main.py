import ifcopenshell
import ifcopenshell.util.classification

from rules import HowManyBeams
from rules import BeamClassifications
from rules import checkIfBeamHasClassification
from rules import Dimensions
from rules import GeoDimensions


model = ifcopenshell.open("samples/25-16-D-STR.ifc")
model1 = ifcopenshell.open("samples/Exercise9_Group10.ifc")



DimensionsResult = Dimensions.beam_dimensions(model)

GeoDimensionsResult = GeoDimensions.checkRule(model)

print(DimensionsResult)
print(GeoDimensionsResult)




# for beam_info in DimensionsResult:
#     print(f"GlobalId: {beam_info['GlobalId']}, Name: {beam_info['Name']}")
#     print(f"  Dimensions: {beam_info['Dimensions']}")
#     print(f"  Cut Length: {beam_info['CutLength']}")
#     print()