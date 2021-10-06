import open3d as o3d
import numpy as np
import anvil

def bll(name):
    return anvil.Block('minecraft', name)

mesh = o3d.io.read_triangle_mesh("astronaut.obj")

#o3d.visualization.draw_geometries([mesh])

mesh.scale(1 / np.max(mesh.get_max_bound() - mesh.get_min_bound()), center=mesh.get_center())

voxel_grid = o3d.geometry.VoxelGrid.create_from_triangle_mesh(mesh, voxel_size=0.02)

#o3d.visualization.draw_geometries([voxel_grid])

mat = np.asarray(voxel_grid.get_voxels())

my_region = anvil.EmptyRegion(0,0)

for vox in mat:
    x, z, y = vox.grid_index
    my_region.set_block(bll('light_gray_wool'), x, y, z)

my_region.save('r.0.0.mca')
