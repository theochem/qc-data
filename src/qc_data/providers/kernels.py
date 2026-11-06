"""Kernel functions for QC-Data providers."""

import pooch


def list_pooch_registry(
    downloader: pooch.Pooch, path: str = "", recursive: bool = False
) -> list[str]:
    """List files and directories from a Pooch registry.

    Parameters
    ----------
    downloader : pooch.Pooch
        An initialized Pooch instance.
    path : str, optional
        The path within the registry to list. Defaults to "" (root).
    recursive : bool, optional
        Whether to list files recursively. Defaults to False.

    Returns
    -------
    list[str]
        A list of file and directory paths within the registry.
    """
    files = downloader.registry_files
    path = path.strip("/")

    # single file case
    if path in files:
        return [path]

    # directory case
    prefix = f"{path}/" if path else ""
    files = [name for name in files if name.startswith(prefix)]

    # if not recursive, only return the immediate children of the directory
    if not recursive:
        files = [prefix + name[len(prefix) :].split("/")[0] for name in files]

    return sorted(set(files))
