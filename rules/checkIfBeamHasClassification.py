import ifcopenshell
import ifcopenshell.util.classification


def checkRule(model):
    elements = model.by_type("IfcBeam")
    hasclassification = []
    noclassification = []

    for element in elements:
        if ifcopenshell.util.classification.get_references(element) == set():
            noclassification.append(element)
        else:
            hasclassification.append(element)
    return hasclassification, noclassification


