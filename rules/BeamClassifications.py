import ifcopenshell


def checkRule(model):
    element = ifcopenshell.util.element.get_element(model, "IfcBeam")

    references = ifcopenshell.util.classification.get_references(element)
    
    for reference in references:
        system = ifcopenshell.util.classification.get_classification(reference)
        print("This reference is part of the system", system.Name)
        print("The element has a classification reference of", reference.Identification)

    result = f"Element: {element.Name}, System: {system.Name}, Reference: {reference.Identification}"   
    return result
