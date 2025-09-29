import ifcopenshell

def checkRule(beam_info):
    """
    Calculates the maximum uniform load capacity (kN/m) of a concrete beam.
    
    Parameters:
    - Dictionary with beam dimensions:
    
    Returns:
    - Maximum uniform load in kN/m
    """

    # Extract dimensions
    width_mm = beam_info['Dimensions'].get('b')
    height_mm = beam_info['Dimensions'].get('h')
    length_cm = beam_info['CutLength']
    concrete_strength_mpa = 25 # Example concrete strength in MPa

    # Convert mm to meters
    width_m = width_mm / 1000
    height_m = height_mm / 1000
    length_m = length_cm / 100

    # Convert MPa to N/m²
    f_c = concrete_strength_mpa * 10**6

    # Allowable bending stress (approximate factor for concrete)
    allowable_stress = 0.45 * f_c

    # Section modulus (S) for rectangular section
    section_modulus = (width_m * height_m**2) / 6  # in m³

    # Maximum uniform load formula: w = (8 * f * S) / L²
    max_uniform_load_n_per_m = (8 * allowable_stress * section_modulus) / (length_m**2)

    # Convert N/m to kN/m
    max_uniform_load_kn_per_m = max_uniform_load_n_per_m / 1000

    return max_uniform_load_kn_per_m
