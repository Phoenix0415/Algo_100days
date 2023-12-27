# File: vertex.py
# Created Time: 2023-02-23
# Author: Krahets (krahets@163.com)


class Vertex:
    """the class of vertex"""

    def __init__(self, val: int):
        self.val = val


def vals_to_vets(vals: list[int]) -> list["Vertex"]:
    """take value list vals, return vertex list vets"""
    return [Vertex(val) for val in vals]


def vets_to_vals(vets: list["Vertex"]) -> list[int]:
    """take vertex list vets, return value list vals"""
    return [vet.val for vet in vets]
