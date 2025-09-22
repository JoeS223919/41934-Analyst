import ifcopenshell

ifc_file = ifcopenshell.open("samples/Exercise9_Group10.ifc")
beams = ifc_file.by_type("IfcBeam")


for beam in beams:
    # Access the shape representation
    rep = beam.Representation
    if not rep:
        continue
    for rep_item in rep.Representations:
        for item in rep_item.Items:
            if item.is_a("IfcExtrudedAreaSolid"):
                profile = item.SweptArea
                if profile.is_a("IfcRectangleProfileDef"):
                    print("Beam:", beam.GlobalId)
                    print("Width:", profile.XDim)
                    print("Height:", profile.YDim)
                    print("Length:", item.Depth)  # extrusion depth



