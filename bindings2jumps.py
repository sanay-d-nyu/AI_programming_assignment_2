def Bindings2Jumps(
    found: bool, bindings: list[int], jump_atoms: list[list[int]]
) -> list[list[int]] | None:
    """
    Converts the bindings (returned by DPLL) and jump_atoms (from Puzzle2SAT)
    into a list of jumps that solve the game
    """
    if not found:
        return None

    ret_jumps: list[list[int]] = []
    len_jump_atoms: int = len(jump_atoms) - 1  # -1 Jump(0, 0, 0, 0)
    num_jumps = max([jump[3] for jump in jump_atoms]) + 1
    for i in range(len_jump_atoms):
        if len(ret_jumps) == num_jumps:
            break
        if bindings[i] == 1:
            ret_jumps.append(jump_atoms[i])

    return ret_jumps
