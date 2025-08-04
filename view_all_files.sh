#!/bin/bash

echo "======================================================================="
echo "InGaN/GaN HEMT THERMAL MODELING FRAMEWORK - COMPLETE VIEW"
echo "======================================================================="
echo ""
echo "Press any key to view each file, or 'q' to skip to the next file"
echo ""

# Function to view file with header
view_file() {
    echo ""
    echo "======================================================================="
    echo "FILE: $1"
    echo "======================================================================="
    if [ -f "$1" ]; then
        # Show file info
        echo "Size: $(ls -lh "$1" | awk '{print $5}'), Lines: $(wc -l < "$1")"
        echo "----------------------------------------------------------------------"
        echo ""
        # Use less for better navigation
        less -N "$1"
    else
        echo "File not found: $1"
    fi
    echo ""
}

# Main project files
echo "=== MAIN PROJECT FILES ==="
echo "1. README.md - Project overview"
echo "2. requirements.txt - Python dependencies"
echo "3. PROJECT_SUMMARY.md - Complete framework summary"
echo ""
read -p "Press Enter to start viewing files..."

view_file "README.md"
view_file "requirements.txt"
view_file "PROJECT_SUMMARY.md"

# Material properties
echo ""
echo "=== MATERIAL PROPERTIES ==="
view_file "materials/gan_properties.py"

# Device structures
echo ""
echo "=== DEVICE STRUCTURES ==="
view_file "device_structures/hemt_structure.py"

# Simulation models
echo ""
echo "=== SIMULATION MODELS ==="
view_file "simulations/python/thermal_models.py"
view_file "simulations/python/thermal_simulation.py"

# Sentaurus TCAD files
echo ""
echo "=== SENTAURUS TCAD FILES ==="
view_file "simulations/sentaurus/hemt_thermal.cmd"
view_file "simulations/sentaurus/hemt_material.par"

# Visualization
echo ""
echo "=== VISUALIZATION TOOLS ==="
view_file "visualization/thermal_visualization.py"

# Demo files
echo ""
echo "=== DEMONSTRATION SCRIPTS ==="
view_file "demo_thermal_fixed.py"
view_file "demo_power_sweep.py"
view_file "demo_visual.py"

# Documentation
echo ""
echo "=== DOCUMENTATION ==="
view_file "docs/thermal_modeling_guide.md"

# HTML interface
echo ""
echo "=== WEB INTERFACE ==="
view_file "index.html"

echo ""
echo "======================================================================="
echo "VIEW COMPLETE"
echo "======================================================================="
echo ""
echo "To edit any file, use: vim <filename>"
echo "To run demos, use: python3 <demo_filename>"
echo ""