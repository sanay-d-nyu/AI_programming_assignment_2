import json
import dpll

"""
NOTES:
    - jumpAtoms is all possible jumps given the board
    - return bindings is which of those are true => which jumps for success
"""


def Puzzle2SAT(
    board: list[list[int]], start: list[int], numberOfJumps: int
) -> tuple[list[list[int]], list[list[int]]]:
    return ([[0]], [[0]])


def Bindings2Jumps(
    found: bool, bindings: list[int], jumpAtoms: list[list[int]]
) -> list[list[int]] | None:
    pass


def PegPuzzle(
    board: list[list[int]], start: list[int], numberOfJumps: int
) -> list[list[int]] | None:
    pass


def main():
    with open("input.json", "r") as file:
        input_data = json.load(file)

    board: list[list[int]]
    start: list[int]
    num_jumps: int
    board, start, num_jumps = input_data.values()

    print(f"board: {board}, start: {start}, num_jumps: {num_jumps}")

    # with open("input1.json", "r") as file:
    #     input_data = json.load(file)
    #
    # clauses: list[list[int]]
    # jump_atoms: list[int]
    # clauses, jump_atoms = input_data.values()
    # found, bindings = dpll.DPLLTop(clauses)
    #
    # print(f"clauses: {clauses}, jump_atoms: {jump_atoms}\n")
    # print()
    # print()
    # print(f"found: {found}, bindings {bindings}, len(bindings): {len(bindings)}\n")


if __name__ == "__main__":
    main()
