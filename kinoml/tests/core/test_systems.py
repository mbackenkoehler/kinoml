"""
Test kinoml.core.systems
"""

import pytest


def test_system():
    from kinoml.core.components import MolecularComponent
    from kinoml.core.systems import System
    from kinoml.core.measurements import BaseMeasurement
    from kinoml.core.conditions import AssayConditions

    components = [MolecularComponent()]
    system = System(components=components)
    # This doesn't raise an error
    System(components=[], strict=False)
    # This does
    with pytest.raises(AssertionError):
        System(components=[])


def test_ligand_system():
    from kinoml.core.systems import LigandSystem
    from kinoml.core.ligands import BaseLigand

    pl = LigandSystem(components=[BaseLigand()])
    assert pl.ligand == list(pl.ligands)[0]

    LigandSystem(components=[], strict=False)
    with pytest.raises(AssertionError):
        LigandSystem(components=[])


def test_protein_system():
    from kinoml.core.systems import ProteinSystem
    from kinoml.core.proteins import BaseProtein

    pl = ProteinSystem(components=[BaseProtein()])
    assert pl.protein == list(pl.proteins)[0]

    ProteinSystem(components=[], strict=False)
    with pytest.raises(AssertionError):
        ProteinSystem(components=[])


def test_protein_ligand_complex():
    from kinoml.core.systems import ProteinLigandComplex
    from kinoml.core.proteins import BaseProtein
    from kinoml.core.ligands import BaseLigand

    pl = ProteinLigandComplex(components=[BaseProtein(), BaseLigand()])
    assert pl.ligand == list(pl.ligands)[0]
    assert pl.protein == list(pl.proteins)[0]

    ProteinLigandComplex(components=[], strict=False)
    with pytest.raises(AssertionError):
        ProteinLigandComplex(components=[])
