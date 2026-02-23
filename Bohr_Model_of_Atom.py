import time
import viser
import trimesh

def main():
    server = viser.ViserServer(share=True)
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

    electron_ring_mesh=trimesh.creation.annulus(r_min=2.0, r_max=2.1, height=0.1)
    server.scene.add_mesh_trimesh(
        name="/electron_ring",
        mesh=electron_ring_mesh
    )

    print("Open your browser to http://localhost:8080")
    print("Press Ctrl+C to exit")

    while True:
        time.sleep(10.0)


if __name__ == "__main__":
    main()