"""Manage sample library."""

import os
import json
from typing import List, Dict, Optional


class SampleManager:
    """Manage hardstyle/rawstyle sample library."""

    def __init__(self, library_path='./sample_library'):
        self.library_path = library_path
        self.samples = {}
        self._load_library()

    def _load_library(self):
        """Load sample library from disk."""
        if not os.path.exists(self.library_path):
            os.makedirs(self.library_path)
            self._create_default_library()
        
        # Load metadata
        metadata_file = os.path.join(self.library_path, 'metadata.json')
        if os.path.exists(metadata_file):
            with open(metadata_file, 'r') as f:
                self.samples = json.load(f)

    def _create_default_library(self):
        """Create default sample library structure."""
        default_categories = {
            'kicks': {
                'hardstyle_kick_1': {'bpm': 150, 'pitch': 55, 'intensity': 0.8},
                'rawstyle_kick_1': {'bpm': 150, 'pitch': 50, 'intensity': 0.95},
            },
            'snares': {
                'hardstyle_snare_1': {'duration': 0.15, 'intensity': 0.8},
                'rawstyle_snare_1': {'duration': 0.15, 'intensity': 0.9},
            },
            'hihats': {
                'closed_hat': {'duration': 0.05, 'intensity': 0.7},
                'open_hat': {'duration': 0.08, 'intensity': 0.6},
            },
            'bass': {
                'hardstyle_bass_1': {'root_note': 40, 'intensity': 0.8},
                'rawstyle_bass_1': {'root_note': 40, 'intensity': 0.95},
            },
        }
        
        self.samples = default_categories
        self._save_library()

    def _save_library(self):
        """Save sample library metadata."""
        metadata_file = os.path.join(self.library_path, 'metadata.json')
        with open(metadata_file, 'w') as f:
            json.dump(self.samples, f, indent=2)

    def get_samples_by_category(self, category: str) -> Dict:
        """
        Get samples by category.
        
        Args:
            category: Sample category (kicks, snares, hihats, bass)
        
        Returns:
            Dict of samples in category
        """
        return self.samples.get(category, {})

    def search_samples(self, query: str, category: Optional[str] = None) -> List[Dict]:
        """
        Search samples by name or properties.
        
        Args:
            query: Search query
            category: Specific category to search in
        
        Returns:
            List of matching samples
        """
        results = []
        
        search_dict = {category: self.samples[category]} if category else self.samples
        
        for cat, samples in search_dict.items():
            for sample_name, properties in samples.items():
                if query.lower() in sample_name.lower():
                    results.append({
                        'name': sample_name,
                        'category': cat,
                        'properties': properties
                    })
        
        return results

    def add_sample(self, name: str, category: str, properties: Dict):
        """
        Add sample to library.
        
        Args:
            name: Sample name
            category: Sample category
            properties: Sample properties
        """
        if category not in self.samples:
            self.samples[category] = {}
        
        self.samples[category][name] = properties
        self._save_library()

    def get_sample(self, name: str, category: str) -> Optional[Dict]:
        """
        Get specific sample.
        
        Args:
            name: Sample name
            category: Sample category
        
        Returns:
            Sample properties or None
        """
        return self.samples.get(category, {}).get(name)
