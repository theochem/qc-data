"""Base data provider interface."""

from abc import ABC, abstractmethod
from pathlib import Path


class BaseProvider(ABC):
    """Base class for data providers."""

    @abstractmethod
    def list(self, dataset: dict, path: str = "", recursive: bool = False) -> list[str]:
        """List files and directories in a dataset."""

    @abstractmethod
    def fetch(self, dataset: dict, cache_dir: Path, path: str = "", recursive: bool = True) -> Path:
        """Fetch a file or directory from a dataset."""
