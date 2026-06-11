"""Sample library with metadata and search capabilities."""

from typing import List, Dict


class SampleLibrary:
    """High-level sample library interface."""

    HARDSTYLE_KICKS = [
        'hardstyle_kick_tight_150',
        'hardstyle_kick_hard_150',
        'hardstyle_kick_deep_150',
        'hardstyle_kick_punchy_140',
    ]

    RAWSTYLE_KICKS = [
        'rawstyle_kick_aggressive_160',
        'rawstyle_kick_dark_160',
        'rawstyle_kick_massive_170',
        'rawstyle_kick_hard_165',
    ]

    SNARES = [
        'snare_tight',
        'snare_crisp',
        'snare_thick',
        'snare_crack',
    ]

    HIHATS = [
        'hihat_closed_tight',
        'hihat_closed_bright',
        'hihat_open_long',
        'hihat_open_short',
    ]

    BASS_SAMPLES = [
        'bass_sub_deep',
        'bass_sine_pure',
        'bass_aggressive',
        'bass_reese_style',
    ]

    @classmethod
    def get_all_hardstyle_sounds(cls) -> Dict[str, List[str]]:
        """Get all hardstyle sound samples."""
        return {
            'kicks': cls.HARDSTYLE_KICKS,
            'snares': cls.SNARES,
            'hihats': cls.HIHATS,
            'bass': cls.BASS_SAMPLES,
        }

    @classmethod
    def get_all_rawstyle_sounds(cls) -> Dict[str, List[str]]:
        """Get all rawstyle sound samples."""
        return {
            'kicks': cls.RAWSTYLE_KICKS,
            'snares': cls.SNARES,
            'hihats': cls.HIHATS,
            'bass': cls.BASS_SAMPLES,
        }

    @classmethod
    def search(cls, query: str) -> List[str]:
        """Search all samples."""
        all_samples = (
            cls.HARDSTYLE_KICKS +
            cls.RAWSTYLE_KICKS +
            cls.SNARES +
            cls.HIHATS +
            cls.BASS_SAMPLES
        )
        
        return [s for s in all_samples if query.lower() in s.lower()]
