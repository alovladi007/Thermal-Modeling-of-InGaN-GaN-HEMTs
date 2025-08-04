#!/bin/bash
# Setup script for InGaN/GaN HEMT Thermal Modeling Framework

echo "=========================================="
echo "Setting up InGaN/GaN HEMT Thermal Framework"
echo "=========================================="

# Install system packages
echo "Installing system packages..."
sudo apt-get update -qq
sudo apt-get install -y python3-numpy python3-scipy python3-matplotlib python3-pandas python3-h5py python3-sympy python3-pip python3-venv

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv --system-site-packages thermal_env

# Activate virtual environment
source thermal_env/bin/activate

# Install additional Python packages
echo "Installing additional Python packages..."
pip install --upgrade pip
pip install plotly>=5.0.0 pyvista>=0.32.0 meshio>=5.0.0 scikit-learn>=0.24.0 jupyter ipython

echo "=========================================="
echo "Setup complete!"
echo "To activate the environment, run:"
echo "  source thermal_env/bin/activate"
echo "=========================================="