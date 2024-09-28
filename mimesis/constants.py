from pathlib import Path
from typing import Final
__all__ = ['DATADIR', 'LOCALE_SEP']
DATADIR: Final[Path] = Path(__file__).parent / 'datasets'
LOCALE_SEP: Final[str] = '-'