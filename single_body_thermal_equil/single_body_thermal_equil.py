from collections import namedtuple
import numpy as np
from scipy import constants

# Types of boundaries
"""Create a conductive boundary.
Arguments:
    T (real number): Temperature of the "other side" of the boundary
        [units: kelvin].
    res (real number): Thermal resistance of the boundary [units: kelvin watt**-1].
        For a convective boundary layer, this is 1 / ((convection coef)(area))
"""
Conductive = namedtuple('Conductive', ['T', 'res'])
"""Create a radiative boundary.
Arguments:
    T (real number): Temperature of the "other side" of the boundary
        [units: kelvin].
    eA (real number): (emissivity * area) of the surface of the body
        viewing this boundary [units: meter**2].
"""
Radiative = namedtuple('Radiative', ['T', 'eA'])


def equilibrium_temperature(boundaries):
    """Find the equilibrium temperature of the body.

    Arguments:
        boundaries (list of Conductive or Radiative): Boundaries on the body.

    Returns:
        T_eq (real number): the equilibrium temperature of the body
            [units: kelvin].
    """
    # Find the coefficients of the zero net heat flow equation.
    # This is a 4th-order polynominal on the body's temperature
    coef0 = 0
    coef1 = 0
    coef4 = 0
    for boundary in boundaries:
        if isinstance(boundary, Radiative):
            coef0 += constants.Stefan_Boltzmann * boundary.eA * boundary.T**4
            coef4 += -constants.Stefan_Boltzmann * boundary.eA
        elif isinstance(boundary, Conductive):
            coef0 += boundary.T / boundary.res
            coef1 += -1 / boundary.res
        else:
            raise ValueError()
    poly_coefs = [coef4, 0, 0, coef1, coef0]

    # Solve the polynomial for the equilibrium temperature.
    roots = np.roots(poly_coefs)

    # Discard bogus roots
    # print(roots)
    roots = roots[roots > 0]
    roots = roots[np.isreal(roots)]
    assert len(roots) == 1

    # The body's equilibrium temperature [units: kelvin]
    T_eq = np.real(roots[0])
    return T_eq


def demo():
    """Demonstration:

    What is the equilibrium temperature of a ingot being heated by a
    torch?

    Assume:
     - The ingot has a surface area of 0.1 m^2.
     - The torch gas is at a temperature of 2000 K, and its convection
       coefficient to the ingot is 100 W m^-2 K^-1.
     - The ingot is radiating to a room with average temperature 300 K.
       The torch and torch gases around the ingot do not radiate signficantly
       to it.
     - The ingot's emissivity is 0.5.
    """
    area = 0.1 # units: meter**2
    T_flame = 2000 # units: kelvin
    h = 100 # units: watt meter**-2 kelvin**-1
    emis = 0.5 # units: dimensionless
    T_room = 300 # units: kelvin

    torch_gas = Conductive(T=T_flame, res=1 / (h * area))
    rad = Radiative(T=T_room, eA=emis * area)

    T_ingot = equilibrium_temperature((torch_gas, rad))
    print('The ingot equilibrium temperature is {:.0f} K'.format(T_ingot))
    return T_ingot


if __name__ == '__main__':
    demo()
