import pathlib


def read_input_lines(solution_path: str) -> list[str]:
    fpath = pathlib.Path(solution_path).parent / "input.txt"
    with fpath.open() as f:
        return f.readlines()
