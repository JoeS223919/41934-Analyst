import ifcopenshell
import ifcopenshell.util.classification

from rules import windowRule
from rules import doorRule
from rules import beamRule
from rules import BeamClassifications

model = ifcopenshell.open("samples/25-16-D-STR.ifc")

# windowResult = windowRule.checkRule(model)
# doorResult = doorRule.checkRule(model)
# beamResult = beamRule.checkRule(model)
beamClassificationsResult = BeamClassifications.checkRule(model, 1)

# print("Window result:", windowResult)
# print("Door result:", doorResult)
# print("Beam result:", beamResult)
print("Beam classifications:", beamClassificationsResult)
