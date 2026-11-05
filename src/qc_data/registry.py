"""Parse toml dataset registry provided by clients"""

import tomllib
from dataclasses import dataclass, field


@dataclass
class DatasetRegistry:
    """Dataset registry class to hold dataset information"""

    # each instance will hold a separate dictionary of datasets
    datasets: dict = field(default_factory=dict)

    @classmethod
    def from_toml(cls, toml_string: str) -> "DatasetRegistry":
        """Create a DatasetRegistry instance from a TOML string.

        Parameters
        ----------
        toml_string : str
            A string containing the TOML representation of the dataset registry.

        Returns
        -------
        DatasetRegistry
            An instance of DatasetRegistry populated with the datasets from the TOML string."""
        data = tomllib.loads(toml_string)
        return cls(datasets=data.get("datasets", {}))
