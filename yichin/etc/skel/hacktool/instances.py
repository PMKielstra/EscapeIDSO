from dataclasses import dataclass

@dataclass
class Instance:
    time: int
    msgs: list
    sols: list
    final_lines: list

instances = {}
