from exceptions import InvalidValueError

"""
Basic unit constants
"""
avogadro = 6.02214129E+23    # NIST 2010
au_to_ev = 27.21138505       # NIST 2010
au_to_joule = 4.35974434E-18 # NIST 2010
cal_to_joule = 4.184
bohr = 0.52917721067e-10 # meter, 2014 CODATA
bohr_to_ang = bohr * 1.0e10 # 0.52 ang / 1 bohr
ang_to_bohr = 1/bohr_to_ang # 1.82 bohr / 1 ang
"""
Constants derived from basic unit constants
"""                                                                      
au_to_kcal = au_to_joule * avogadro * 1E-03 / cal_to_joule
ev_to_kcal = au_to_kcal / au_to_ev
au_times_bohr6_to_kcal_times_ang6 = au_to_kcal * (bohr_to_ang ** 6) # Converts au*(bohr^6) to (kcal/mol)*(angstrom^6)

# list of atomic symbols listed in order of atomic number, 0th item has atomic number 1, 1st item has atomic number 2, etc.
atomic_symbols = [
    "H",                                                                                                                                    "He",
    "Li",   "Be",                                                                                   "B",    "C",    "N",    "O",    "F",    "Ne",
    "Na",   "Mg",                                                                                   "Al",   "Si",   "P",    "S",    "Cl",   "Ar",
    "K",    "Ca",   "Sc",   "Ti",   "V",    "Cr",   "Mn",   "Fe",   "Co",   "Ni",   "Cu",   "Zn",   "Ga",   "Ge",   "As",   "Se",   "Br",   "Kr",
]

# list of atomic masses listed in order of atomic number
atomic_masses = [ # Source ptable.com (not a final source)
    1.008,                                                                                                                                  4.0026,
    6.94,   9.0122,                                                                                 10.81,  12.011, 14.007, 15.999, 18.998, 20.180,
    22.990, 24.305,                                                                                 26.982, 28.085, 30.974, 32.06,  35.45,  39.948,
    39.098, 40.078, 44.956, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933, 58.693, 63.546, 65.38,  69.723, 72.630, 74.922, 78.971, 79.904, 83.798,
]

def symbol_to_number(symbol):
    """
    Converts an atomic symbol to an atomic number.

    Args:
        symbol - The 1 or 2 letter atomic symbol to convert to an atomic number. For example: "He", "F". Case non-sensitive.

    Returns:
        The atomic number for the atom specified by the given symbol.
    """

    # Make first letter uppercase and second letter (if exists) lowercase
    symbol = symbol[:1].upper() + symbol[1:].lower()

    try:
        # convert atomic symbol to number by performing a look-up in the list of atomic symbols
        return atomic_symbols.index(symbol) + 1
    except ValueError:
        # if the given symbol was not found in the list, then it is an invalid symbol
        raise InvalidValueError("atomic symbol", symbol, "a valid 1 or 2 letter atomic symbol") from None

def number_to_symbol(number):
    """
    Converts an atomic number to an atomic symbol.

    Args:
        number - the atomic number to convert to an atomic symbol.

    Returns:
        The atomic symbol of the atom with the given atomic number.
    """

    # if the number is 0 or less, it is an invalid atomic number
    if number < 1:
        raise ValueError("{} is not a recognized atomic number".format(number))

    try:
        # find this atomic number's symbol, by looking at the list of atomic symbols
        return atomic_symbols[number - 1]
    except IndexError:
        # if this atomic number was out of range, then it is an invalid atomic number
        raise InvalidValueError("atomic number", number, "less than {}".format(len(atomic_symbols))) from None

def symbol_to_mass(symbol):
    """
    Finds the atomic mass of the atom with a given atomic symbol

    Args:
        symbol - The 1 or 2 letter atomic symbol to find the mass of. For example: "He", "F". Case non-sensitive.

    Returns:
        The atomic mass of the given atom.
    """

    # the atomic mass is indexed in the list atomic_masses as the symbol's atomic number minus 1
    return atomic_masses[symbol_to_number(symbol) - 1]
