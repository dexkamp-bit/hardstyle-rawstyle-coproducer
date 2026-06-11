"""Main Co-Producer plugin interface."""

from core.synthesizer import HardstyleSynthesizer, RawstyleSynthesizer
from generators.drum_generator import DrumGenerator
from generators.bass_generator import BassGenerator
from samples.sample_manager import SampleManager
from samples.sample_library import SampleLibrary
import numpy as np
from typing import Dict, List, Optional


class HardstyleCoProducer:
    """Main Hardstyle Co-Producer plugin class."""

    def __init__(self, sample_rate=44100, bpm=150):
        self.sample_rate = sample_rate
        self.bpm = bpm
        
        # Initialize synthesis engines
        self.hardstyle_synth = HardstyleSynthesizer(sample_rate)
        self.rawstyle_synth = RawstyleSynthesizer(sample_rate)
        
        # Initialize generators
        self.drum_generator = DrumGenerator(bpm)
        self.bass_generator = BassGenerator(bpm)
        
        # Initialize sample manager
        self.sample_manager = SampleManager()

    def generate_hardstyle_kick(self, bpm: Optional[int] = None, intensity=0.8, duration=0.5):
        """
        Generate hardstyle kick sound.
        
        Args:
            bpm: Beats per minute (uses self.bpm if None)
            intensity: Kick intensity (0-1)
            duration: Duration in seconds
        
        Returns:
            Audio samples
        """
        bpm = bpm or self.bpm
        return self.hardstyle_synth.generate_kick(bpm, intensity=intensity, duration=duration)

    def generate_hardstyle_snare(self, intensity=0.8, duration=0.15):
        """
        Generate hardstyle snare sound.
        
        Args:
            intensity: Snare intensity (0-1)
            duration: Duration in seconds
        
        Returns:
            Audio samples
        """
        return self.hardstyle_synth.generate_snare(duration=duration, intensity=intensity)

    def generate_hardstyle_hihat(self, open_time=0.08, closed=False, intensity=0.8):
        """
        Generate hardstyle hi-hat.
        
        Args:
            open_time: Open hi-hat duration
            closed: True for closed hat
            intensity: Hi-hat intensity (0-1)
        
        Returns:
            Audio samples
        """
        return self.hardstyle_synth.generate_hihat(open_time, closed, intensity)

    def generate_rawstyle_bass(self, bpm: Optional[int] = None, pitch=40, intensity=0.9, duration=0.5):
        """
        Generate rawstyle bass sound.
        
        Args:
            bpm: Beats per minute
            pitch: Fundamental frequency
            intensity: Bass intensity (0-1)
            duration: Duration in seconds
        
        Returns:
            Audio samples
        """
        bpm = bpm or self.bpm
        return self.rawstyle_synth.generate_rawstyle_bass(bpm, pitch, intensity, duration)

    def generate_rawstyle_kick(self, bpm: Optional[int] = None, pitch=50, intensity=0.95, duration=0.6):
        """
        Generate rawstyle kick sound.
        
        Args:
            bpm: Beats per minute
            pitch: Fundamental frequency
            intensity: Kick intensity (0-1)
            duration: Duration in seconds
        
        Returns:
            Audio samples
        """
        bpm = bpm or self.bpm
        return self.rawstyle_synth.generate_raw_kick(bpm, pitch, intensity, duration)

    def generate_drum_pattern(self, style='hardstyle', bars=4, intensity=0.8) -> Dict:
        """
        Generate complete drum pattern.
        
        Args:
            style: 'hardstyle' or 'rawstyle'
            bars: Number of bars
            intensity: Pattern intensity (0-1)
        
        Returns:
            Dict with drum pattern
        """
        if style == 'hardstyle':
            return self.drum_generator.generate_hardstyle_pattern(bars, intensity)
        elif style == 'rawstyle':
            return self.drum_generator.generate_rawstyle_pattern(bars, intensity)
        else:
            raise ValueError(f"Unknown style: {style}")

    def generate_bass_progression(self, bars=4, root_note=40, aggressive=False, intensity=0.9) -> Dict:
        """
        Generate bass progression.
        
        Args:
            bars: Number of bars
            root_note: MIDI root note
            aggressive: True for aggressive pattern
            intensity: Bass intensity (0-1)
        
        Returns:
            Dict with bass progression
        """
        if aggressive:
            return self.bass_generator.generate_aggressive_bass_line(bars, root_note, intensity)
        else:
            return self.bass_generator.generate_bass_progression(bars, root_note, intensity)

    def get_available_samples(self, style='hardstyle') -> Dict[str, List[str]]:
        """
        Get available samples for style.
        
        Args:
            style: 'hardstyle' or 'rawstyle'
        
        Returns:
            Dict of available samples
        """
        if style == 'hardstyle':
            return SampleLibrary.get_all_hardstyle_sounds()
        elif style == 'rawstyle':
            return SampleLibrary.get_all_rawstyle_sounds()
        else:
            raise ValueError(f"Unknown style: {style}")

    def search_samples(self, query: str) -> List[Dict]:
        """
        Search sample library.
        
        Args:
            query: Search query
        
        Returns:
            List of matching samples
        """
        return self.sample_manager.search_samples(query)

    def export_midi(self, pattern: Dict, output_file: str):
        """
        Export pattern as MIDI file.
        
        Args:
            pattern: Drum pattern dictionary
            output_file: Output MIDI file path
        """
        # MIDI export would be implemented with python-midi library
        midi_sequence = self.drum_generator.create_midi_sequence(pattern)
        print(f"MIDI export to {output_file}: {len(midi_sequence)} events")

    def set_bpm(self, bpm: int):
        """
        Set global BPM.
        
        Args:
            bpm: Beats per minute
        """
        self.bpm = bpm
        self.drum_generator.bpm = bpm
        self.bass_generator.bpm = bpm

    def set_sample_rate(self, sample_rate: int):
        """
        Set audio sample rate.
        
        Args:
            sample_rate: Sample rate in Hz
        """
        self.sample_rate = sample_rate
        self.hardstyle_synth.sample_rate = sample_rate
        self.rawstyle_synth.sample_rate = sample_rate
