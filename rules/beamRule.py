import ifcopenshell

def checkRule(model):
    beams = model.by_type('IfcBeam')

    result = f"Beams: {len(beams)}"

    return result