"""
### Objective

Imagine you work in Thoughtful’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

### Rules

Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

### Implementation

Implement the function **`sort(width, height, length, mass)`** (units are centimeters for the dimensions and kilogram for the mass). This function must return a string: the name of the stack where the package should go.
"""

class Solution():
    def __init__():
        pass
    def sort(width, height, length, mass):
        volume_limit = 1000000
        dimension_limit = 150
        pkg_volume = width * height * length
        pkg_stack_label = 'STANDARD'
        pkg_volume_label = 'normal'
        pkg_mass_label = 'normal'
        if mass >= 20:
            pkg_mass_label = 'heavy'
        if (pkg_volume >= volume_limit) or (width or height or length) >= 150: 
            pkg_volume_label = 'bulky'
        if pkg_volume_label == 'bulky' or pkg_mass_label == 'heavy':
            pkg_stack_label = 'SPECIAL'
        if pkg_volume_label == 'bulky' and pkg_mass_label == 'heavy':
            pkg_stack_label = 'REJECTED'
        return pkg_stack_label 


# Expect SPECIAL: width = 150 -> volume is bulky
print(Solution.sort(150, 100, 80, 15))
# Expect REJECTED: width = 150 -> volume is bulky and mass is heavy 
print(Solution.sort(150, 100, 80, 20))
# Expect STANDARD: nothing special 
print(Solution.sort(100, 100, 80, 10))
# Expect SPECIAL: volume is bulky (> 1000000)
print(Solution.sort(100, 100, 120, 10))
# Expect REJECTED: volume is bulky and mass is heavy
print(Solution.sort(100, 100, 120, 30))
