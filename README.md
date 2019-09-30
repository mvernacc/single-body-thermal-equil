# single-body-thermal-equil

Find the equilibirium temperature of a conductive body with multiple conductive and radiative boundaries.

## Install

```bash
pip install -e .
```

## Example

What is the equilibrium temperature of a ingot being heated by a torch?

Assume:
 - The ingot has a surface area of 0.1 m^2.
 - The torch gas is at a temperature of 2000 K, and its convection
   coefficient to the ingot is 100 W m^-2 K^-1.
 - The ingot is radiating to a room with average temperature 300 K.
   The torch and torch gases around the ingot do not radiate signficantly
   to it.
 - The ingot's emissivity is 0.5.


```python
from single_body_thermal_equil import Conductive, Radiative, equilibrium_temperature
area = 0.1 # units: meter**2
T_flame = 2000 # units: kelvin
h = 100 # units: watt meter**-2 kelvin**-1
emis = 0.5 # units: dimensionless
T_room = 300 # units: kelvin

torch_gas = Conductive(T=T_flame, res=1 / (h * area))
rad = Radiative(T=T_room, eA=emis * area)

T_ingot = equilibrium_temperature((torch_gas, rad))
print('The ingot equilibrium temperature is {:.0f} K'.format(T_ingot))
```

```
The ingot equilibrium temperature is 1268 K
```
