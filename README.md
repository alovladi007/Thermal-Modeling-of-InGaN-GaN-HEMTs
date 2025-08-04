# InGaN/GaN HEMT Thermal Modeling and Simulation

This project provides a comprehensive framework for thermal modeling and simulation of InGaN/GaN High Electron Mobility Transistors (HEMTs) using both Sentaurus TCAD and Python-based numerical methods.

## Features

- Complete device structure definition for InGaN/GaN HEMTs
- Material properties database for III-N semiconductors
- Thermal simulation models including:
  - Self-heating effects
  - Temperature-dependent material properties
  - Joule heating
  - Thermal boundary resistance
- Support for both Sentaurus TCAD and open-source solvers
- Visualization and post-processing tools

## Directory Structure

```
.
├── device_structures/      # HEMT device geometry definitions
├── materials/             # Material properties database
├── simulations/           # Simulation scripts and configurations
│   ├── sentaurus/        # Sentaurus TCAD scripts
│   └── python/           # Python-based simulations
├── results/              # Simulation results and outputs
├── visualization/        # Post-processing and plotting tools
└── docs/                 # Documentation and references
```

## Requirements

### For Sentaurus TCAD simulations:
- Synopsys Sentaurus TCAD (version 2020.09 or later)
- Linux environment with appropriate licenses

### For Python simulations:
- Python 3.8+
- NumPy, SciPy, Matplotlib
- FEniCS or COMSOL (optional, for FEM simulations)

## Quick Start

1. Set up the environment:
   ```bash
   pip install -r requirements.txt
   ```

2. Run a basic thermal simulation:
   ```bash
   python simulations/python/thermal_simulation.py
   ```

3. For Sentaurus TCAD users:
   ```bash
   cd simulations/sentaurus
   sdevice hemt_thermal.cmd
   ```

## Physics Models

The simulation framework includes:

1. **Drift-Diffusion Model**: Carrier transport with temperature effects
2. **Heat Transfer Equation**: Thermal conduction with Joule heating
3. **Piezoelectric Polarization**: Strain-induced effects in III-N heterostructures
4. **Temperature-Dependent Properties**: Mobility, thermal conductivity, etc.

## Contact

For questions or contributions, please open an issue or submit a pull request.