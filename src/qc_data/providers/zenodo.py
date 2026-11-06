"""Implementation of Zenodo data provider"""

from pathlib import Path

import pooch

from .base import BaseProvider
from .kernels import list_pooch_registry


class ZenodoProvider(BaseProvider):
    """Zenodo data provider class."""

    def list(self, dataset: dict, path: str = "", recursive: bool = False) -> list[str]:
        """List files and directories in a Zenodo dataset.

        Parameters
        ----------
        dataset : dict
            The Zenodo dataset to list.
        path : str, optional
            The path within the dataset to list.
        recursive : bool, optional
            Whether to list recursively.

        Returns
        -------
        list[str]
            A list of files and directories in the specified path.
        """

        downloader = self._create_pooch(dataset, Path(".cache"))
        return list_pooch_registry(downloader, path, recursive=recursive)

    def fetch(
        self, dataset: dict, cache_dir: Path, path: str = "", recursive: bool = True
    ) -> list[Path]:
        """Fetch a file or directory from a Zenodo dataset

        Parameters
        ----------
        dataset : dict
            The Zenodo dataset to fetch from.
        cache_dir : Path
            The directory to cache the fetched file or directory.
        path : str, optional
            The path within the dataset to fetch.
        recursive : bool, optional
            Whether to fetch recursively.

        Returns
        -------
        list[Path]
            Local paths to the fetched files.
        """
        downloader = self._create_pooch(dataset, cache_dir)
        files = list_pooch_registry(downloader, path, recursive=recursive)
        return [Path(downloader.fetch(name)) for name in files]

    def _create_pooch(self, dataset: dict, cache_dir: Path) -> pooch.Pooch:
        """Initialize Pooch for a Zenodo dataset.

        Parameters
        ----------
        dataset : dict
            The Zenodo dataset information.
        cache_dir : Path
            The directory to cache the dataset files.

        Returns
        -------
        pooch.Pooch
            The initialized Pooch instance.
        """
        downloader = pooch.create(path=cache_dir, base_url=f"doi:{dataset['doi']}/")
        downloader.load_registry_from_doi()
        return downloader
