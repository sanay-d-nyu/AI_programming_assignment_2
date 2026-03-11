import json
import dpll
import numpy as np
from puzzle2sat import Puzzle2SAT, print_helper

"""
NOTES:
    - jumpAtoms is all possible jumps given the board
    - return bindings is which of those are true => which jumps for success
"""


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
    clauses, jump_atoms = Puzzle2SAT(board, start, 2)

    # print(f"board: {board}, start: {start}, num_jumps: {num_jumps}")
    # print("Clauses from input:")
    # print_helper(clauses_from_input)
    # print("Jump atoms from input:")
    # print_helper(jump_atoms_from_input)
    # # print()
    # print()
    # print("Clauses:")
    # print_helper(clauses)
    # print("Jump atoms:")
    # print_helper(jump_atoms)
    # print(f"found: {found}, bindings {bindings}, len(bindings): {len(bindings)}\n")
    found0, res0 = dpll.DPLLTop(clauses_from_input)
    found1, res1 = dpll.DPLLTop(clauses)

    print(f"results equal: {res0 == res1}")


if __name__ == "__main__":
    main()
