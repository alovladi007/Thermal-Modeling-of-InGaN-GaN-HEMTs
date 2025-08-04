#!/usr/bin/env python3
"""
Project Viewer - Display all InGaN/GaN HEMT Thermal Modeling files
"""

import os
import subprocess

def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*80)
    print(f" {text} ")
    print("="*80)

def print_file_content(filepath, max_lines=50):
    """Print file content with line numbers"""
    if os.path.exists(filepath):
        print(f"\nFile: {filepath}")
        print(f"Size: {os.path.getsize(filepath)} bytes")
        print("-"*80)
        
        try:
            with open(filepath, 'r') as f:
                lines = f.readlines()
                total_lines = len(lines)
                
                if total_lines <= max_lines:
                    for i, line in enumerate(lines, 1):
                        print(f"{i:4d} | {line.rstrip()}")
                else:
                    # Show first 25 lines
                    for i in range(25):
                        if i < len(lines):
                            print(f"{i+1:4d} | {lines[i].rstrip()}")
                    
                    print(f"\n... ({total_lines - 50} lines omitted) ...\n")
                    
                    # Show last 25 lines
                    for i in range(total_lines - 25, total_lines):
                        if i >= 0:
                            print(f"{i+1:4d} | {lines[i].rstrip()}")
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print(f"File not found: {filepath}")

def show_project_structure():
    """Display project directory structure"""
    print_header("PROJECT STRUCTURE")
    
    # Use tree command if available, otherwise use a simple listing
    try:
        subprocess.run(['tree', '-L', '3', '--dirsfirst'], check=True)
    except:
        # Fallback to manual structure
        print("""
.
├── device_structures/
│   └── hemt_structure.py
├── materials/
│   └── gan_properties.py
├── simulations/
│   ├── python/
│   │   ├── thermal_models.py
│   │   └── thermal_simulation.py
│   └── sentaurus/
│       ├── hemt_thermal.cmd
│       └── hemt_material.par
├── visualization/
│   └── thermal_visualization.py
├── docs/
│   └── thermal_modeling_guide.md
├── results/
├── demo_thermal_fixed.py
├── demo_power_sweep.py
├── demo_visual.py
├── index.html
├── README.md
├── requirements.txt
└── PROJECT_SUMMARY.md
        """)

def main():
    """Main viewer function"""
    print_header("InGaN/GaN HEMT THERMAL MODELING FRAMEWORK")
    print("\nComplete Project View - All Files and Code")
    
    # Show project structure
    show_project_structure()
    
    # Define files to display in order
    files_to_show = [
        ("Project Overview", [
            "README.md",
            "PROJECT_SUMMARY.md",
            "requirements.txt"
        ]),
        ("Core Modules", [
            "materials/gan_properties.py",
            "device_structures/hemt_structure.py",
            "simulations/python/thermal_models.py",
            "simulations/python/thermal_simulation.py"
        ]),
        ("Demonstrations", [
            "demo_thermal_fixed.py",
            "demo_power_sweep.py",
            "demo_visual.py"
        ]),
        ("Visualization", [
            "visualization/thermal_visualization.py",
            "index.html"
        ]),
        ("Sentaurus TCAD", [
            "simulations/sentaurus/hemt_thermal.cmd",
            "simulations/sentaurus/hemt_material.par"
        ]),
        ("Documentation", [
            "docs/thermal_modeling_guide.md"
        ])
    ]
    
    # Display each category
    for category, files in files_to_show:
        print_header(category)
        for filepath in files:
            if os.path.exists(filepath):
                print_file_content(filepath)
                input("\nPress Enter to continue to next file...")
            else:
                print(f"\nFile not found: {filepath}")
    
    # Summary
    print_header("VIEWING COMPLETE")
    print("\nTo edit any file, use: vim <filename>")
    print("To run demos, use: python3 <demo_filename>")
    print("\nKey files:")
    print("  - demo_thermal_fixed.py : Main thermal analysis demo")
    print("  - index.html : Interactive web interface")
    print("  - materials/gan_properties.py : Material properties")
    print("  - device_structures/hemt_structure.py : Device definition")

if __name__ == "__main__":
    main()