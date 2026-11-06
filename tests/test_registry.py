from pathlib import Path

from qc_data.registry import DatasetRegistry


def test_from_toml():
    """Test parsing a TOML dataset registry from a file."""
    toml_path = Path(__file__).parent / "testdata" / "registry.toml"
    registry = DatasetRegistry.from_toml(toml_path.read_text(encoding="utf-8"))

    expected = {
        "spherical": {"provider": "zenodo", "record_id": "example_record_id"},
        "atomic": {"provider": "federated", "record_id": "1234567"},
    }

    assert registry.datasets == expected
    assert registry.cache == {"namespace": "grid"}
