#!/usr/bin/env python3
"""
Run All InGaN/GaN HEMT Thermal Demos
Shows complete thermal modeling capabilities
"""

import subprocess
import time

def run_demo(script_name, description):
    """Run a demo script with header"""
    print("\n" + "="*70)
    print(f"RUNNING: {description}")
    print("="*70)
    time.sleep(1)
    
    try:
        # Run the demo
        if script_name == "demo_interactive.py":
            # For interactive demo, provide automated inputs
            process = subprocess.Popen(['python3', script_name], 
                                     stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     text=True)
            output, _ = process.communicate(input="\n1\n20\n100\nn\n")
            print(output)
        elif script_name == "demo_visual.py":
            # For visual demo, provide enters to progress
            process = subprocess.Popen(['python3', script_name], 
                                     stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     text=True)
            output, _ = process.communicate(input="\n\n\n\n\n\n")
            print(output)
        else:
            # For other demos, just run normally
            subprocess.run(['python3', script_name])
    except Exception as e:
        print(f"Error running {script_name}: {e}")
    
    time.sleep(2)

def main():
    print("="*70)
    print("InGaN/GaN HEMT THERMAL MODELING - COMPLETE DEMONSTRATION")
    print("="*70)
    print("\nThis will run all thermal analysis demonstrations.")
    print("Each demo shows different aspects of thermal modeling.\n")
    
    demos = [
        ("demo_no_deps.py", "Framework Overview and Capabilities"),
        ("demo_thermal_fixed.py", "Realistic Thermal Analysis"),
        ("demo_power_sweep.py", "Power vs Temperature Analysis"),
        ("demo_visual.py", "Visual Temperature Distribution")
    ]
    
    for script, description in demos:
        run_demo(script, description)
    
    # Summary
    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. Thermal resistance for GaN HEMT on SiC: ~50 K/W")
    print("2. Maximum safe power: ~2.5W @ 150°C junction temperature")
    print("3. SiC substrate provides best thermal performance")
    print("4. Pulsed operation significantly reduces average temperature")
    print("5. Hot spot located at 2DEG under gate edge")
    print("\nFor full 3D simulations with visualization:")
    print("1. Install dependencies: ./setup_environment.sh")
    print("2. Run: python simulations/python/thermal_simulation.py")
    print("\n" + "="*70)

if __name__ == "__main__":
    main()