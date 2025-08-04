#!/bin/bash

echo "Opening InGaN/GaN HEMT Thermal Modeling Framework in vim..."
echo ""
echo "Vim Navigation Tips:"
echo "  - :tabn or gt - Next tab"
echo "  - :tabp or gT - Previous tab" 
echo "  - :tabs - List all tabs"
echo "  - :q - Close current tab"
echo "  - :qa - Close all tabs and exit"
echo ""
echo "Press Enter to open all project files in vim tabs..."
read

# Open all key files in vim tabs
vim -p \
    README.md \
    PROJECT_SUMMARY.md \
    demo_thermal_fixed.py \
    demo_power_sweep.py \
    demo_visual.py \
    materials/gan_properties.py \
    device_structures/hemt_structure.py \
    simulations/python/thermal_models.py \
    simulations/python/thermal_simulation.py \
    visualization/thermal_visualization.py \
    simulations/sentaurus/hemt_thermal.cmd \
    simulations/sentaurus/hemt_material.par \
    docs/thermal_modeling_guide.md \
    index.html