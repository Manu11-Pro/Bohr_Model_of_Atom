import time
import viser
import trimesh
from utils import something

def main():
    server = viser.ViserServer(host="0.0.0.0", port=7860)
    server.scene.add_icosphere(
        name="/nucleus",
        radius=1.0,
        color=(255,0,0),
        position=(0.0,0.0,0.0)
    )
    
    server.scene.add_icosphere(
        name="/electron1",
        radius=0.5,
        color=(0,0,255),
        position=(2.0,0.0,0.0)
    )

    server.scene.add_icosphere(
        name="/electron2",
        radius=0.5,
        color=(0,0,255),
        position=(-2.0,0.0,0.0)
    )

    electron_ring_mesh=trimesh.creation.annulus(r_min=2.0, r_max=2.1, height=0.1)
    server.scene.add_mesh_trimesh(
        name="/electron_ring",
        mesh=electron_ring_mesh
    )

    server.gui.add_markdown("***Bohr_Model_of_Atom***")

    print("Server running on http://localhost:7860 (Ctrl+C to stop)")
    
    while True:
        time.sleep(10.0)


if __name__ == "__main__":
    main()
