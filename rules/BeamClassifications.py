import ifcopenshell
import ifcopenshell.util.classification

def checkRule(model, Beamid):
    
    element = model.by_type('IfcBeam')[Beamid]

    references = ifcopenshell.util.classification.get_references(element)
    
    for reference in references:
        system = ifcopenshell.util.classification.get_classification(reference)
        print("This reference is part of the system", system.Name)
        print("The element has a classification reference of", reference.Identification)

    result = f"Element: {element.Name}, System: {system.Name}, Reference: {reference.Identification}"   
    return result
