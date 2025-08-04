"""
InGaN/GaN HEMT Device Structure Definition
Includes layer stack, dimensions, and doping profiles
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict
from enum import Enum


class LayerType(Enum):
    """Enumeration of layer types in HEMT structure"""
    SUBSTRATE = "substrate"
    NUCLEATION = "nucleation"
    BUFFER = "buffer"
    CHANNEL = "channel"
    SPACER = "spacer"
    BARRIER = "barrier"
    CAP = "cap"
    PASSIVATION = "passivation"
    CONTACT = "contact"


@dataclass
class Layer:
    """Definition of a single layer in the HEMT structure"""
    name: str
    material: str
    thickness: float  # nm
    layer_type: LayerType
    doping_type: Optional[str] = None  # 'n', 'p', or None
    doping_concentration: float = 0.0  # cm^-3
    composition: Optional[Dict[str, float]] = None  # For alloys like InGaN
    
    def __post_init__(self):
        """Validate layer parameters"""
        if self.thickness <= 0:
            raise ValueError(f"Layer thickness must be positive: {self.name}")
        if self.doping_concentration < 0:
            raise ValueError(f"Doping concentration cannot be negative: {self.name}")


@dataclass
class Contact:
    """Contact definition for HEMT device"""
    name: str
    contact_type: str  # 'ohmic' or 'schottky'
    material: str
    position: Tuple[float, float]  # (x_start, x_end) in μm
    work_function: Optional[float] = None  # eV
    contact_resistance: Optional[float] = None  # Ω·mm


class HEMTStructure:
    """Complete HEMT device structure definition"""
    
    def __init__(self, substrate_type: str = "SiC"):
        """
        Initialize HEMT structure with specified substrate
        
        Args:
            substrate_type: 'SiC', 'Si', 'Sapphire', or 'GaN'
        """
        self.substrate_type = substrate_type
        self.layers: List[Layer] = []
        self.contacts: List[Contact] = []
        self.device_dimensions = {
            'gate_length': 0.25,  # μm
            'gate_width': 100,    # μm
            'source_drain_spacing': 4.0,  # μm
            'field_plate_length': 0.5,  # μm
            'device_length': 10.0,  # μm
        }
        
        # Build default layer stack
        self._build_default_structure()
    
    def _build_default_structure(self):
        """Build default InGaN/GaN HEMT layer stack"""
        
        # Substrate
        if self.substrate_type == "SiC":
            substrate_thickness = 350000  # 350 μm
        elif self.substrate_type == "Si":
            substrate_thickness = 525000  # 525 μm
        elif self.substrate_type == "Sapphire":
            substrate_thickness = 430000  # 430 μm
        else:  # GaN substrate
            substrate_thickness = 300000  # 300 μm
        
        self.add_layer(Layer(
            name="Substrate",
            material=self.substrate_type,
            thickness=substrate_thickness,
            layer_type=LayerType.SUBSTRATE
        ))
        
        # Nucleation layer (for non-GaN substrates)
        if self.substrate_type != "GaN":
            self.add_layer(Layer(
                name="Nucleation",
                material="AlN",
                thickness=100,  # nm
                layer_type=LayerType.NUCLEATION
            ))
        
        # Buffer layers for strain relief
        self.add_layer(Layer(
            name="Buffer1",
            material="AlGaN",
            thickness=500,
            layer_type=LayerType.BUFFER,
            composition={'Al': 0.1, 'Ga': 0.9}
        ))
        
        self.add_layer(Layer(
            name="Buffer2",
            material="GaN",
            thickness=1500,
            layer_type=LayerType.BUFFER,
            doping_type='n',
            doping_concentration=1e16
        ))
        
        # Channel layer
        self.add_layer(Layer(
            name="Channel",
            material="GaN",
            thickness=300,
            layer_type=LayerType.CHANNEL,
            doping_type=None,  # Unintentionally doped
            doping_concentration=1e16  # Background doping
        ))
        
        # Spacer layer (optional)
        self.add_layer(Layer(
            name="Spacer",
            material="AlN",
            thickness=1,
            layer_type=LayerType.SPACER
        ))
        
        # Barrier layer (forms 2DEG)
        self.add_layer(Layer(
            name="Barrier",
            material="InAlN",
            thickness=15,
            layer_type=LayerType.BARRIER,
            composition={'In': 0.17, 'Al': 0.83},  # Lattice matched
            doping_type='n',
            doping_concentration=5e18
        ))
        
        # Cap layer
        self.add_layer(Layer(
            name="Cap",
            material="GaN",
            thickness=2,
            layer_type=LayerType.CAP,
            doping_type='n',
            doping_concentration=2e19
        ))
        
        # Define contacts
        self._define_contacts()
    
    def _define_contacts(self):
        """Define source, drain, and gate contacts"""
        
        # Source contact
        self.add_contact(Contact(
            name="Source",
            contact_type="ohmic",
            material="Ti/Al/Ni/Au",
            position=(0.0, 1.0),  # μm
            contact_resistance=0.2  # Ω·mm
        ))
        
        # Drain contact
        drain_start = self.device_dimensions['source_drain_spacing']
        self.add_contact(Contact(
            name="Drain",
            contact_type="ohmic",
            material="Ti/Al/Ni/Au",
            position=(drain_start, drain_start + 1.0),  # μm
            contact_resistance=0.2  # Ω·mm
        ))
        
        # Gate contact
        gate_start = 1.5  # μm from source
        gate_end = gate_start + self.device_dimensions['gate_length']
        self.add_contact(Contact(
            name="Gate",
            contact_type="schottky",
            material="Ni/Au",
            position=(gate_start, gate_end),
            work_function=5.1  # eV
        ))
    
    def add_layer(self, layer: Layer):
        """Add a layer to the structure"""
        self.layers.append(layer)
    
    def add_contact(self, contact: Contact):
        """Add a contact to the structure"""
        self.contacts.append(contact)
    
    def get_total_thickness(self) -> float:
        """Calculate total structure thickness in nm"""
        return sum(layer.thickness for layer in self.layers)
    
    def get_epi_thickness(self) -> float:
        """Calculate epitaxial layer thickness (excluding substrate) in nm"""
        return sum(layer.thickness for layer in self.layers 
                  if layer.layer_type != LayerType.SUBSTRATE)
    
    def get_layer_boundaries(self) -> List[float]:
        """Get z-coordinates of layer boundaries (nm from top)"""
        boundaries = [0.0]
        z = 0.0
        # Start from cap layer (top) and go down
        for layer in reversed(self.layers):
            if layer.layer_type != LayerType.SUBSTRATE:
                z += layer.thickness
                boundaries.append(z)
        return boundaries
    
    def get_2deg_position(self) -> float:
        """Calculate approximate 2DEG position from top surface (nm)"""
        z = 0.0
        for layer in reversed(self.layers):
            if layer.layer_type == LayerType.CAP:
                z += layer.thickness
            elif layer.layer_type == LayerType.BARRIER:
                z += layer.thickness
                # 2DEG forms ~1-2 nm below barrier/channel interface
                z += 1.5
                break
        return z
    
    def export_sentaurus_structure(self, filename: str):
        """Export structure definition for Sentaurus TCAD"""
        with open(filename, 'w') as f:
            f.write("# Sentaurus Structure Editor Script\n")
            f.write("# InGaN/GaN HEMT Structure\n\n")
            
            # Define materials
            f.write("# Material definitions\n")
            materials = set(layer.material for layer in self.layers)
            for mat in materials:
                f.write(f'(define {mat} (material "{mat}"))\n')
            f.write("\n")
            
            # Create regions
            f.write("# Create regions\n")
            z_top = 0.0
            for i, layer in enumerate(reversed(self.layers)):
                if layer.layer_type != LayerType.SUBSTRATE:
                    z_bottom = z_top + layer.thickness / 1000  # Convert to μm
                    f.write(f'(define region_{i} (cuboid ')
                    f.write(f'(position 0 0 {z_top}) ')
                    f.write(f'(position {self.device_dimensions["device_length"]} ')
                    f.write(f'{self.device_dimensions["gate_width"]} {z_bottom})))\n')
                    f.write(f'(define {layer.name} (region {layer.material} ')
                    f.write(f'"region_{i}"))\n\n')
                    z_top = z_bottom
            
            # Define doping
            f.write("# Doping profiles\n")
            for i, layer in enumerate(self.layers):
                if layer.doping_concentration > 0:
                    doping_type = "donor" if layer.doping_type == 'n' else "acceptor"
                    f.write(f'(define doping_{i} (constant ')
                    f.write(f'"{layer.name}" "{doping_type}" ')
                    f.write(f'{layer.doping_concentration:.2e}))\n')
            
            # Define contacts
            f.write("\n# Contact definitions\n")
            for contact in self.contacts:
                f.write(f'(define {contact.name} (contact "{contact.material}" ')
                f.write(f'"{ contact.contact_type}"))\n')
    
    def export_python_mesh(self, filename: str):
        """Export structure as Python mesh for FEM simulations"""
        import json
        
        structure_dict = {
            'substrate_type': self.substrate_type,
            'dimensions': self.device_dimensions,
            'layers': [],
            'contacts': []
        }
        
        for layer in self.layers:
            layer_dict = {
                'name': layer.name,
                'material': layer.material,
                'thickness': layer.thickness,
                'type': layer.layer_type.value,
                'doping_type': layer.doping_type,
                'doping_concentration': layer.doping_concentration,
                'composition': layer.composition
            }
            structure_dict['layers'].append(layer_dict)
        
        for contact in self.contacts:
            contact_dict = {
                'name': contact.name,
                'type': contact.contact_type,
                'material': contact.material,
                'position': contact.position,
                'work_function': contact.work_function,
                'contact_resistance': contact.contact_resistance
            }
            structure_dict['contacts'].append(contact_dict)
        
        with open(filename, 'w') as f:
            json.dump(structure_dict, f, indent=2)
    
    def print_structure(self):
        """Print structure summary"""
        print("InGaN/GaN HEMT Structure Summary")
        print("=" * 50)
        print(f"Substrate: {self.substrate_type}")
        print(f"Total thickness: {self.get_total_thickness()/1000:.1f} μm")
        print(f"Epi thickness: {self.get_epi_thickness()/1000:.3f} μm")
        print(f"2DEG position: {self.get_2deg_position():.1f} nm from surface")
        print("\nLayer Stack (top to bottom):")
        print("-" * 50)
        
        for layer in reversed(self.layers):
            if layer.layer_type != LayerType.SUBSTRATE:
                comp_str = ""
                if layer.composition:
                    comp_str = f" ({layer.composition})"
                doping_str = ""
                if layer.doping_concentration > 0:
                    doping_str = f", {layer.doping_type}-type: {layer.doping_concentration:.1e} cm⁻³"
                print(f"{layer.name:12} | {layer.material:8}{comp_str} | "
                      f"{layer.thickness:6.1f} nm{doping_str}")
        
        print("\nContacts:")
        print("-" * 50)
        for contact in self.contacts:
            print(f"{contact.name:8} | {contact.material:12} | "
                  f"{contact.contact_type:8} | "
                  f"x: {contact.position[0]:.1f}-{contact.position[1]:.1f} μm")


class AdvancedHEMTStructure(HEMTStructure):
    """Advanced HEMT structure with additional features"""
    
    def __init__(self, substrate_type: str = "SiC"):
        super().__init__(substrate_type)
        self.field_plates = []
        self.passivation_layers = []
    
    def add_field_plate(self, name: str, material: str, 
                       position: Tuple[float, float], height: float):
        """Add field plate for electric field management"""
        self.field_plates.append({
            'name': name,
            'material': material,
            'position': position,
            'height': height
        })
    
    def add_passivation(self, material: str, thickness: float):
        """Add passivation layer"""
        self.passivation_layers.append({
            'material': material,
            'thickness': thickness
        })
    
    def add_back_barrier(self, thickness: float = 50, 
                        doping_concentration: float = 5e18):
        """Add back barrier for better confinement"""
        # Insert after channel layer
        channel_idx = next(i for i, layer in enumerate(self.layers) 
                          if layer.layer_type == LayerType.CHANNEL)
        
        back_barrier = Layer(
            name="BackBarrier",
            material="AlGaN",
            thickness=thickness,
            layer_type=LayerType.BUFFER,
            composition={'Al': 0.05, 'Ga': 0.95},
            doping_type='p',
            doping_concentration=doping_concentration
        )
        
        self.layers.insert(channel_idx + 1, back_barrier)


if __name__ == "__main__":
    # Example usage
    # Standard HEMT on SiC
    hemt = HEMTStructure(substrate_type="SiC")
    hemt.print_structure()
    
    # Export for Sentaurus
    hemt.export_sentaurus_structure("sentaurus_hemt.cmd")
    
    # Export for Python FEM
    hemt.export_python_mesh("hemt_structure.json")
    
    print("\n" + "="*50 + "\n")
    
    # Advanced HEMT with back barrier
    adv_hemt = AdvancedHEMTStructure(substrate_type="SiC")
    adv_hemt.add_back_barrier()
    adv_hemt.add_field_plate("GateFP", "Ni/Au", (1.5, 2.0), 0.2)
    adv_hemt.add_passivation("SiN", 100)
    
    print("Advanced HEMT with Back Barrier")
    adv_hemt.print_structure()