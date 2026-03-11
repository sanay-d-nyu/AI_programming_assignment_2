import json
import dpll
import argparse
from puzzle2sat import Puzzle2SAT, arr_to_string, print_helper
from bindings2jumps import Bindings2Jumps

"""
NOTES:
    - jumpAtoms is all possible jumps given the board
    - return bindings is which of those are true => which jumps for success
"""
debug = True

parser = argparse.ArgumentParser(
    prog="PegGameSolver",
    description="Solves the peg game given by a layout in a json file",
)

parser.add_argument("filepath")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()


def PegPuzzle(
    board: list[list[int]], start: list[int], number_of_jumps: int
) -> list[list[int]] | None:
    """Wrapper function for Puzzle2SAT, DPLL, and Bindings2Jumps"""
    clauses: list[set[int]]
    jump_atoms: list[list[int]]
    clauses, jump_atoms = Puzzle2SAT(board, start, number_of_jumps)

    if args.verbose:
        print("Executing DPLL with clauses:")
        print_helper(clauses)

    found, bindings = dpll.DPLLTop(clauses)

    if not found:
        if debug:
            print("No DPLL solution found!")
        return None

    if args.verbose:
        print(f"Success! DPLL Solution found:")
        print("Jump atoms:")
        print_helper(jump_atoms)
        print(f"bindings: {arr_to_string(bindings)}")

    return Bindings2Jumps(found, bindings, jump_atoms)


def print_jumps(jumps: list[list[int]]):
    """Helper function to print 2d arrays"""
    print("Solution: ")
    for i, jump in enumerate(jumps):
        print(f"\tJump {i+1}: ({jump[0]},{jump[1]},{jump[2]},{jump[3]})")
    print()


def main():
    with open(args.filepath, "r") as file:
        input_data = json.load(file)

    # with open("input1.json", "r") as file1:
    #     input_data1 = json.load(file1)
    #
    board: list[list[int]]
    start: list[int]
    num_jumps: int
    board, start, num_jumps = input_data.values()

    jumps = PegPuzzle(board, start, num_jumps)
    if jumps is None:
        print("No solution found for the Peg Puzzle with those parameters!")
        return

    print_jumps(jumps)


if __name__ == "__main__":
    main()
