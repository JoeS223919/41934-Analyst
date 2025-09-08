import ifcopenshell

from rules import windowRule
from rules import doorRule
from rules import beamRule

model = ifcopenshell.open("data/25-16-D-STR.ifc")

windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)
beamResult = beamRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
print("Beam result:", beamResult)

