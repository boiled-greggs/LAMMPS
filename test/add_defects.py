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
    out.write("\nC %.7f %.7f %.7f" %(atoms[0][0], atoms[0][1], atoms[0][2]))
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

def get_pairs(atoms):
    x = y = z = 0
    for atom in atoms:
        x += atom[0]
        y += atom[1]
        z += atom[2]
    middle = [x/float(len(atoms)), y/float(len(atoms)), z/float(len(atoms))]
    print(middle)
    possible_pairatoms = []
    for i in range(len(atoms)):
        if (3.7 < np.sqrt((atoms[i][0]-middle[0])**2+(atoms[i][1]-middle[1])**2\
                +(atoms[i][2]-middle[2])**2) < 4.0):
            possible_pairatoms.append(i)
    possible_pairs = []
    for i in possible_pairatoms:
        for j in possible_pairatoms:
            if ( 1.4 < np.sqrt((atoms[i][0]-atoms[j][0])**2+(atoms[i][1]-atoms[j][1])**2+\
                    (atoms[i][2]-atoms[j][2])**2) < 1.5):
                possible_pairs.append([i,j])
    
    """
    2.92119/2 = 1.460595
    4.36966 7.87940 9.70088

    """

def rotate_pairs(atoms, pairs):
    for i in range(len(pairs)):
        at1 = atoms[pairs[i][0]]
        at2 = atoms[pairs[i][1]]
        # midpoint is the axis about which atoms must be rotated
        midpoint = [ [(at1[0]+at2[0])/2], [(at1[1]+at2[1])/2], [(at1[2]+at2[2])/2] ]
        theta = np.pi/2
        new_at1 = np.dot(rotation_matrix(midpoint, theta), at1)
        new_at2 = np.dot(rotation_matrix(midpoint, theta), at2)
        atoms[pairs[i][0]] = new_at1
        atoms[pairs[i][1]] = new_at2
    return atoms

def rotate_patch(atoms, theta, axis):
    new_atoms = []
    for i in range(len(atoms)):
        new_atom = np.dot(rotation_matrix(axis, theta), atoms[i])
        new_atoms.append(new_atom)
    return new_atoms

if __name__ == "__main__":
    f = open("patch.xyz", "r")
    out = open("cpP8-3defected.xyz", "w")

    f.readline()
    f.readline()
    atoms = get_atoms(f)

    # pairs = 
    get_pairs(atoms)
    pairs = [ [67,75], [93,85], [57,49] ]
    
    atoms = rotate_pairs(atoms, pairs)
    
    axis = [0,0,1]
    pi = np.pi
    new_atoms1 = rotate_patch(atoms, pi/2, axis)
    new_atoms2 = rotate_patch(atoms, pi, axis)
    new_atoms3 = rotate_patch(atoms, 3*pi/2, axis)
    
    atoms = atoms + new_atoms1 + new_atoms2 + new_atoms3

    axis = [1,0,0]
    atoms = atoms + rotate_patch(atoms, pi, axis)

    write_out(atoms, out)
