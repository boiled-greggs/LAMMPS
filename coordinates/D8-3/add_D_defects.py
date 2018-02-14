import numpy as np
import math

def get_atoms(f):
    atoms = []
    for line in f:
        atom = line.split()
        coords = [float(atom[1]), float(atom[2]), float(atom[3])]
        atoms.append(coords)
    return atoms

def write_out(atoms, out):
    out.write("%d atoms" %(len(atoms)))
    for atom in atoms:
        out.write("\nC %.7f %.7f %.7f" %(atom[0], atom[1], atom[2]))

def rotation_matrix(axis, theta):
    axis = np.squeeze(np.asarray(axis))
    axis = axis/math.sqrt(np.dot(axis, axis))
    a = math.cos(theta/2.0)
    b, c, d = -axis*math.sin(theta/2.0)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    return np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                     [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                     [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])

    
    
if __name__ == "__main__":
    f = open("cpP8-3.xyz", "r")
    out = open("cpP8-3defected.xyz", "w")

    f.readline()
    atoms = get_atoms(f)

    rotate_pairs = [[93,85], [693,749], [752, 696], [748,692], [694,750], [697,753],\
            [751,695], [747,691], [49,57], [499,443], [495,439], [441,497], [440,496],\
            [501,445], [444,500], [498,442]]

    atoms = rotate(atoms, rotate_pairs)

    write_out(atoms, out)
