# Extraindo informações de terreno no Blender para o Archicad

## Código para extração de coordenadas

```py
import bpy
from pathlib import Path

# Get the directory of the current .blend file
blend_dir = Path(bpy.data.filepath).parent
save_to_file = blend_dir / "vertices.txt"  # Output file in the same folder
separator = ","  # Custom separator

# Extract vertex coordinates
vertices = [f"{v.co.x}{separator}{v.co.y}{separator}{v.co.z}" for v in bpy.context.object.data.vertices]
    
# Save to file
with open(save_to_file, 'w') as file:

    file.write('\n'.join(vertices))

print(f"Vertices exported to: {save_to_file}")   
 
```
