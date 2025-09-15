import ifcopenshell
import ifcopenshell.util.classification

from rules import windowRule
from rules import doorRule
from rules import beamRule
from rules import BeamClassifications
from rules import checkClassification

model = ifcopenshell.open("samples/25-16-D-STR.ifc")
model1 = ifcopenshell.open("samples/Exercise9_Group10.ifc")


# windowResult = windowRule.checkRule(model)
# doorResult = doorRule.checkRule(model)
# beamResult = beamRule.checkRule(model)
checkClassificationResult = checkClassification.checkRule(model1)
beamClassificationsResult = BeamClassifications.checkRule(model1, 1)


# print("Window result:", windowResult)
# print("Door result:", doorResult)
# print("Beam result:", beamResult)
print("Beam classifications:", beamClassificationsResult)
print('--------------------------------------------------')
print('Number of elements with classification: ', len(checkClassificationResult[0]), 
      'Number of elements without classification: ', len(checkClassificationResult[1]),
      'Total number of elements: ', len(model1.by_type("IfcElement")))
