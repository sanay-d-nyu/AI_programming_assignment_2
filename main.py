import json
import dpll
import numpy as np

"""
NOTES:
    - jumpAtoms is all possible jumps given the board
    - return bindings is which of those are true => which jumps for success
"""


def Puzzle2SAT(
    board: list[list[int]], start: list[int], numberOfJumps: int
) -> tuple[list[list[int]], list[list[int]]]:

    # Get all possible jumps, plus Jump(0, 0, 0, 0)
    jump_atoms: list[list[int]] = [[0, 0, 0, 0]]
    possible_jumps: list[list[int]] = []
    for i in range(numberOfJumps):
        possible_jumps.extend(
            jump for triple in board for jump in [[*triple, i], [*triple[::-1], i]]
        )  # map each triple to its reverse and append time i to them
    jump_atoms.extend(possible_jumps)

    # Generate clauses
    clauses: list[list[int]] = []
    num_jumps_arr = np.arange(numberOfJumps + 1)
    vertices = np.unique(np.array(board))
    pegs: list[list[int]] = np.transpose(
        [np.tile(vertices, numberOfJumps + 1), np.repeat(num_jumps_arr, len(vertices))]
    ).tolist()
    # Cartesian product of [0..=numberOfJumps] x [0..=number of unique vertices (holes)]
    # i.e, each possible Peg() token, Peg(0, 0)..Peg(num_holes, numberOfJumps)

    num_holes = int(len(pegs) / (numberOfJumps + 1))
    num_possible_jumps = len(possible_jumps)
    atom_indices = [i + 1 for i in range(num_holes + num_possible_jumps)]

    # offset of where pegs start in the key of atoms (Jumps and Pegs, jumps first, 1 based index)
    peg_offset = num_possible_jumps + 1

    # Precondition
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

    # Precondition
    # for i, jump in enumerate(possible_jumps):
    #     # where the pegs for time i start in the pegs list
    #     peg_i_idx = jump[3] * num_holes
    #
    #     # indices pegs relevant to precondition axiom for this jump
    #     # Basically, the indices of pegs Peg(A, I), Peg(B, I), and Peg(C, I) in the pegs list
    #     rel_indices = []
    #     for j in range(len(jump) - 1):
    #         rel_indices.append(peg_offset + peg_i_idx + jump[j])
    #
    #     # Jump(A, B, C, I) => Peg(A, I) ^ Peg(B, I) ^ ~Peg(C, I) in CNF
    #     clauses.extend(
    #         [
    #             [-(i + 1), rel_indices[0]],
    #             [-(i + 1), rel_indices[1]],
    #             [-(i + 1), -rel_indices[2]],
    #         ]
    #     )

    print(f"atom_indices: {atom_indices}")

    print("pegs:")
    print_helper(pegs)
    return (clauses, jump_atoms)


def Bindings2Jumps(
    found: bool, bindings: list[int], jumpAtoms: list[list[int]]
) -> list[list[int]] | None:
    pass


def PegPuzzle(
    board: list[list[int]], start: list[int], numberOfJumps: int
) -> list[list[int]] | None:
    pass


"""
def PegPuzzle(board,start,numberOfJumps):
    clauses, jumpAtoms = Puzzle2Sat(board,start,numberOfJumps)
    found, bindings = DPLLTop(clauses)
    return Bindings2Jumps(found,jumpAtoms,bindings)
"""


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


def main():
    with open("input.json", "r") as file:
        input_data = json.load(file)

    with open("input1.json", "r") as file1:
        input_data1 = json.load(file1)

    board: list[list[int]]
    start: list[int]
    num_jumps: int
    board, start, num_jumps = input_data.values()

    clauses: list[list[int]]
    jump_atoms_from_input: list[int]
    clauses_from_input, jump_atoms_from_input = input_data1.values()
    # found, bindings = dpll.DPLLTop(clauses)

    # print(f"board: {board}, start: {start}, num_jumps: {num_jumps}")
    print("Clauses from input:")
    print_helper(clauses_from_input)
    print("Jump atoms from input:")
    print_helper(jump_atoms_from_input)
    # print()
    print()
    clauses, jump_atoms = Puzzle2SAT(board, start, 2)
    print("Clauses:")
    print_helper(clauses)
    print("Jump atoms:")
    print_helper(jump_atoms)
    # print(f"found: {found}, bindings {bindings}, len(bindings): {len(bindings)}\n")


if __name__ == "__main__":
    main()
