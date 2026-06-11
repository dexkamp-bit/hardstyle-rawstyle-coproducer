"""General pattern generation utilities."""

import numpy as np
from typing import List, Dict


class PatternGenerator:
    """Generate musical patterns and sequences."""

    @staticmethod
    def generate_melody(root_note=60, bars=4, scale='minor_pentatonic', intensity=0.7):
        """
        Generate hardstyle/rawstyle melody.
        
        Args:
            root_note: MIDI note number
            bars: Number of bars
            scale: Scale type
            intensity: Melody intensity (0-1)
        
        Returns:
            List of MIDI notes
        """
        # Define scales
        scales = {
            'minor_pentatonic': [0, 3, 5, 7, 10],
            'minor': [0, 2, 3, 5, 7, 8, 10],
            'major': [0, 2, 4, 5, 7, 9, 11],
        }
        
        scale_intervals = scales.get(scale, scales['minor_pentatonic'])
        available_notes = [root_note + interval for interval in scale_intervals]
        
        melody = []
        
        for bar in range(bars):
            # 2 notes per beat for 4/4 time
            for beat in range(4):
                for eighth_note in range(2):
                    # Random note selection from scale
                    note = np.random.choice(available_notes)
                    time = bar * 4 + beat + (eighth_note * 0.5)
                    
                    # Vary velocity for expression
                    velocity = int(intensity * 127 * (0.7 + 0.3 * np.random.random()))
                    
                    # Skip some notes (rest) for breathing room
                    if np.random.random() > 0.3:
                        melody.append({
                            'time': time,
                            'note': note,
                            'velocity': velocity,
                            'duration': 0.25
                        })
        
        return melody

    @staticmethod
    def generate_chord_progression(root_note=40, bars=4, progression='i-VII-VI-VII'):
        """
        Generate chord progression for harmonization.
        
        Args:
            root_note: MIDI note number
            bars: Number of bars
            progression: Chord progression pattern
        
        Returns:
            Dict with chord information
        """
        # Define common rawstyle/hardstyle progressions
        chord_offsets = {
            'i': [0, 3, 7],      # Minor
            'VII': [10, 2, 5],   # VII chord
            'VI': [8, 0, 5],     # VI chord
            'v': [7, 10, 2],     # Minor v
        }
        
        chords = []
        chord_sequence = progression.split('-')
        
        for bar in range(bars):
            chord_name = chord_sequence[bar % len(chord_sequence)]
            offsets = chord_offsets.get(chord_name, [0, 3, 7])
            
            chord_notes = [root_note + offset for offset in offsets]
            
            chords.append({
                'time': bar * 4,
                'chord': chord_name,
                'notes': chord_notes,
                'duration': 4
            })
        
        return {
            'chords': chords,
            'progression': progression,
            'root_note': root_note
        }
