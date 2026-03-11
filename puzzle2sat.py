import numpy as np


def Puzzle2SAT(
    board: list[list[int]], start: list[int], number_of_jumps: int
) -> tuple[list[list[int]], list[list[int]]]:

    # Get all possible jumps, plus Jump(0, 0, 0, 0)
    jump_atoms: list[list[int]] = [[0, 0, 0, 0]]
    possible_jumps: list[list[int]] = []
    for i in range(number_of_jumps):
        possible_jumps.extend(
            jump for triple in board for jump in [[*triple, i], [*triple[::-1], i]]
        )  # map each triple to its reverse and append time i to them
    jump_atoms.extend(possible_jumps)

    # Generate clauses
    clauses: list[list[int]] = []
    num_jumps_arr = np.arange(number_of_jumps + 1)
    vertices = np.unique(np.array(board))
    pegs: list[list[int]] = np.transpose(
        [
            np.tile(vertices, number_of_jumps + 1),
            np.repeat(num_jumps_arr, len(vertices)),
        ]
    ).tolist()
    # Cartesian product of [0..=numberOfJumps] x [0..=number of unique vertices (holes)]
    # i.e, each possible Peg() token, Peg(0, 0)..Peg(num_holes, numberOfJumps)

    num_holes = int(len(pegs) / (number_of_jumps + 1))
    num_possible_jumps = int(len(possible_jumps) / (number_of_jumps))
    atom_indices = [i + 1 for i in range(num_holes + num_possible_jumps)]

    # start of possible jumps in the jump_atoms list
    jump_offset = 1

    # offset of where pegs start in the key of atoms (Jumps and Pegs, jumps first, 1 based index)
    peg_offset = len(possible_jumps) + jump_offset

    # Precondition clauses
    for i, jump in enumerate(possible_jumps):
        # where the pegs for time i start in the pegs list
        peg_i_idx = jump[3] * num_holes

        # indices pegs relevant to precondition axiom for this jump
        # Basically, the indices of pegs Peg(A, I), Peg(B, I), and Peg(C, I) in the pegs list
        rel_indices = []
        for j in range(len(jump) - 1):
            rel_indices.append(peg_offset + peg_i_idx + jump[j])

        # Jump(A, B, C, I) => Peg(A, I) ^ Peg(B, I) ^ ~Peg(C, I) in CNF
        clauses.extend(
            [
                [-(i + 1), rel_indices[0]],
                [-(i + 1), rel_indices[1]],
                [-(i + 1), -rel_indices[2]],
            ]
        )

    # Casual clauses
    for i, jump in enumerate(possible_jumps):
        # where the pegs for time i + 1 start in the pegs list
        peg_i1_idx = (jump[3] + 1) * num_holes

        # indices of pegs relevant to casual clause for this jump
        # Basically, the indices of pegs Peg(A, I+1), Peg(B, I+1), and Peg(C, I+1) in the pegs list
        rel_indices = []
        for j in range(len(jump) - 1):
            rel_indices.append(peg_offset + peg_i1_idx + jump[j])

        # Jump(A, B, C, I) => ~Peg(A, I+1) ^ ~Peg(B, I+1) ^ Peg(C, I) in CNF
        clauses.extend(
            [
                [-(i + 1), -rel_indices[0]],
                [-(i + 1), -rel_indices[1]],
                [-(i + 1), rel_indices[2]],
            ]
        )

    # Frame clauses

    # A. Peg(H, I) ^ ~Peg(H, I+1) => Jump(X, H, Y, I) || Jump(H, X, Y, I)
    # Jumps where either jump[0] == H or jump[1] == H
    for jump_index in range(number_of_jumps):
        for i in range(num_holes):
            rel_jumps_indices = [
                k + jump_offset
                for k, jump in enumerate(possible_jumps)
                if (jump[0] == i or jump[1] == i) and jump[3] == jump_index
            ]
            clauses.append(
                [
                    -(peg_offset + i + (jump_index * num_holes)),  # index of Peg(H, I)
                    peg_offset
                    + i
                    + ((jump_index + 1) * num_holes),  # index of Peg(H, I+1)
                    *rel_jumps_indices,
                ]
            )

    # B. ~Peg(H, I) ^ Peg(H, I+1) => Jump(X, Y, H, I)
    # Jumps where either jump[2] == H
    for jump_index in range(number_of_jumps):
        for i in range(num_holes):
            rel_jumps_indices = [
                k + jump_offset
                for k, jump in enumerate(possible_jumps)
                if jump[2] == i and jump[3] == jump_index
            ]
            clauses.append(
                [
                    peg_offset + i + (jump_index * num_holes),  # index of Peg(H, I)
                    # index of Peg(H, I+1)
                    -(peg_offset + i + ((jump_index + 1) * num_holes)),
                    *rel_jumps_indices,
                ]
            )

    # One action at a time: ~(Jump(A, B, C, I) ^ Jump(X, Y, Z, I))
    for jump_index in range(number_of_jumps):
        start_idx = jump_index * num_possible_jumps
        end_idx = (1 + jump_index) * num_possible_jumps
        for i in range(start_idx, end_idx):
            invalid_jumps = [
                [-(i + jump_offset), -(k + jump_offset)] for k in range(i + 1, end_idx)
            ]
            clauses.extend(invalid_jumps)

    print(f"atom_indices: {atom_indices}")

    print("pegs:")
    print_helper(pegs)
    return (clauses, jump_atoms)


def arr_to_string(arr1d):
    n = len(arr1d) - 1
    ret_str = "["
    for i, v in enumerate(arr1d):
        ret_str += str(v)
        if i != n:
            ret_str += ", "
    return ret_str + "]"


def print_helper(arr2d):
    print("[")
    for arr in arr2d:
        print(
            f"\t{arr_to_string(arr)},",
        )
    print("]")
