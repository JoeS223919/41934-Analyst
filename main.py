import ifcopenshell
import ifcopenshell.util.classification

from rules import windowRule
from rules import doorRule
from rules import beamRule
from rules import BeamClassifications
from rules import checkClassification
from rules import checkBeamClassification

model = ifcopenshell.open("samples/25-16-D-STR.ifc")
model1 = ifcopenshell.open("samples/Exercise9_Group10.ifc")


# windowResult = windowRule.checkRule(model)
# doorResult = doorRule.checkRule(model)
# beamResult = beamRule.checkRule(model)
checkBeamClassificationResult = checkBeamClassification.checkRule(model1)
beamClassificationsResult = BeamClassifications.checkRule(model1, 1)


# print("Window result:", windowResult)
# print("Door result:", doorResult)
# print("Beam result:", beamResult)
print("Beam classifications:", beamClassificationsResult)
print('--------------------------------------------------')
print('Number of beams with classification: ', len(checkBeamClassificationResult[0]), 
      'Number of beams without classification: ', len(checkBeamClassificationResult[1]),
      'Total number of beams: ', len(model1.by_type("IfcBeam")))
