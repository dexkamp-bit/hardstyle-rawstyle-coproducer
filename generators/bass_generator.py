"""Rawstyle bass pattern generator."""

import numpy as np
from typing import List, Dict, Tuple


class BassGenerator:
    """Generate rawstyle bass patterns and sequences."""

    def __init__(self, bpm=150):
        self.bpm = bpm
        self.beat_duration = 60 / bpm

    def generate_bass_progression(self, bars=4, root_note=40, intensity=0.9):
        """
        Generate rawstyle bass progression.
        
        Args:
            bars: Number of bars
            root_note: MIDI note number
            intensity: Bass intensity (0-1)
        
        Returns:
            Dict with bass notes and properties
        """
        notes = []
        
        # Generate bass notes (typically 1/4 note rhythm for rawstyle)
        for bar in range(bars):
            # Rawstyle often uses sub-bass hits on each beat
            for beat in range(4):
                time = bar * 4 + beat
                
                # Vary between root and other notes
                if beat % 2 == 0:
                    note = root_note
                else:
                    # Add variation
                    note = root_note + np.random.choice([-7, -5, 0, 2, 5])
                
                velocity = int(intensity * 127 * (0.8 + 0.2 * np.random.random()))
                
                notes.append({
                    'time': time,
                    'note': note,
                    'velocity': velocity,
                    'duration': 0.5,
                    'type': 'bass'
                })
        
        return {
            'notes': notes,
            'root_note': root_note,
            'bpm': self.bpm,
            'intensity': intensity
        }

    def generate_aggressive_bass_line(self, bars=4, root_note=40, intensity=0.95):
        """
        Generate very aggressive rawstyle bass line with more activity.
        
        Args:
            bars: Number of bars
            root_note: MIDI note number
            intensity: Bass intensity (0-1)
        
        Returns:
            Dict with bass notes and properties
        """
        progression = self.generate_bass_progression(bars, root_note, intensity)
        notes = progression['notes']
        
        # Add extra notes for fill patterns
        extra_notes = []
        for bar in range(bars):
            # Add fill pattern every other bar
            if bar % 2 == 1:
                start_time = bar * 4
                # Create ascending/descending fill
                fill_interval = -2  # Descending
                current_note = root_note
                
                for step in range(4):
                    extra_time = start_time + 0.5 + (step * 0.5)
                    extra_velocity = int(intensity * 100)
                    
                    extra_notes.append({
                        'time': extra_time,
                        'note': current_note,
                        'velocity': extra_velocity,
                        'duration': 0.3,
                        'type': 'fill'
                    })
                    
                    current_note += fill_interval
        
        notes.extend(extra_notes)
        notes.sort(key=lambda x: x['time'])
        
        progression['notes'] = notes
        return progression

    def create_midi_bass_sequence(self, progression: Dict) -> List[Tuple[float, int, int]]:
        """
        Convert bass progression to MIDI sequence.
        
        Args:
            progression: Bass progression dictionary
        
        Returns:
            List of (time, midi_note, velocity) tuples
        """
        sequence = []
        
        for note in progression['notes']:
            sequence.append((
                note['time'],
                note['note'],
                note['velocity']
            ))
        
        return sequence
