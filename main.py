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

    clauses: list[list[int]] = []
    jump_atoms: list[list[int]] = [[0, 0, 0, 0]]
    possible_jumps: list[list[int]] = []
    for i in range(numberOfJumps):
        possible_jumps.extend(map(lambda triple: [*triple, i], board))
        possible_jumps.extend(map(lambda triple: [*triple[::-1], i], board))
    jump_atoms.extend(possible_jumps)

    return ([[0]], jump_atoms)


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
    # found, bindings = dpll.DPLLTop(clauses)

    # print(f"board: {board}, start: {start}, num_jumps: {num_jumps}")
    print(
        f"clauses_from_input: {clauses_from_input}, jump_atoms_from_input: {jump_atoms_from_input}\n"
    )
    # print()
    print()
    clauses, jump_atoms = Puzzle2SAT(board, start, 2)
    print(f"clauses: {clauses}, jump_atoms: {jump_atoms}\n")
    # print(f"found: {found}, bindings {bindings}, len(bindings): {len(bindings)}\n")


if __name__ == "__main__":
    main()
