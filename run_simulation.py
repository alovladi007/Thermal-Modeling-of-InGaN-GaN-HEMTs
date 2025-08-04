#!/usr/bin/env python3
"""
Quick start script to run InGaN/GaN HEMT thermal simulations
"""

import os
import sys

def main():
    print("InGaN/GaN HEMT Thermal Modeling and Simulation")
    print("=" * 50)
    print("\nThis project provides comprehensive thermal modeling for InGaN/GaN HEMTs")
    print("using both Sentaurus TCAD and Python-based numerical methods.\n")
    
    print("Available simulation options:")
    print("1. Run Python thermal simulation")
    print("2. View device structure")
    print("3. Test material properties")
    print("4. Run example visualization")
    print("5. Exit")
    
    while True:
        choice = input("\nSelect option (1-5): ")
        
        if choice == '1':
            print("\nRunning thermal simulation...")
            os.system("cd simulations/python && python thermal_simulation.py --substrate SiC --analysis dc")
            
        elif choice == '2':
            print("\nDisplaying device structure...")
            os.system("cd device_structures && python hemt_structure.py")
            
        elif choice == '3':
            print("\nTesting material properties...")
            os.system("cd materials && python gan_properties.py")
            
        elif choice == '4':
            print("\nRunning visualization example...")
            os.system("cd visualization && python thermal_visualization.py")
            
        elif choice == '5':
            print("\nExiting...")
            break
            
        else:
            print("Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()