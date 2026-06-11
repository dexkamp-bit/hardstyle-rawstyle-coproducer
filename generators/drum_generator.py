"""Hardstyle drum pattern generator."""

import numpy as np
from typing import List, Dict, Tuple


class DrumGenerator:
    """Generate hardstyle drum patterns and sequences."""

    def __init__(self, bpm=150, signature=(4, 4)):
        self.bpm = bpm
        self.signature = signature
        self.beat_duration = 60 / bpm  # Duration of one beat in seconds

    def generate_hardstyle_pattern(self, bars=4, intensity=0.8):
        """
        Generate classic hardstyle drum pattern.
        
        Args:
            bars: Number of bars
            intensity: Pattern intensity (0-1)
        
        Returns:
            Dict with kick, snare, hihat patterns
        """
        beats_per_bar = self.signature[0]
        total_beats = bars * beats_per_bar
        sixteenths = total_beats * 4  # 16th note grid
        
        pattern = {
            'kick': [],
            'snare': [],
            'hihat': [],
            'metadata': {
                'bpm': self.bpm,
                'bars': bars,
                'intensity': intensity
            }
        }
        
        # Kick pattern - typical hardstyle (every 16th with variations)
        for i in range(sixteenths):
            beat_position = i % 16
            
            # Main kick hits at 0, 4, 8, 12 (on 16ths)
            if beat_position in [0, 4, 8, 12]:
                pattern['kick'].append({
                    'time': i / 4,
                    'pitch': 55,
                    'intensity': intensity,
                    'duration': 0.5
                })
            # Fill kicks at higher intensity
            elif intensity > 0.7 and beat_position in [2, 6, 10, 14]:
                pattern['kick'].append({
                    'time': i / 4,
                    'pitch': 55,
                    'intensity': intensity * 0.6,
                    'duration': 0.4
                })
        
        # Snare pattern - on 2 and 4
        for bar in range(bars):
            for beat in [2, 4]:  # 2nd and 4th beat of the bar
                snare_time = bar * beats_per_bar + beat - 1
                pattern['snare'].append({
                    'time': snare_time,
                    'intensity': intensity,
                    'duration': 0.15
                })
        
        # Hi-hat pattern
        for i in range(sixteenths):
            beat_position = i % 16
            
            if beat_position % 4 == 0:  # On beat
                pattern['hihat'].append({
                    'time': i / 4,
                    'closed': True,
                    'intensity': intensity * 0.7,
                    'duration': 0.05
                })
            elif beat_position % 2 == 0:  # On 8th notes
                pattern['hihat'].append({
                    'time': i / 4,
                    'closed': False,
                    'intensity': intensity * 0.5,
                    'duration': 0.08
                })
        
        return pattern

    def generate_rawstyle_pattern(self, bars=4, intensity=0.95):
        """
        Generate aggressive rawstyle drum pattern.
        
        Args:
            bars: Number of bars
            intensity: Pattern intensity (0-1)
        
        Returns:
            Dict with kick, snare, hihat patterns
        """
        # Get hardstyle pattern and enhance it
        pattern = self.generate_hardstyle_pattern(bars, intensity)
        
        # Add more kick hits for rawstyle aggression
        kicks = pattern['kick']
        extra_kicks = []
        
        for kick in kicks:
            # Add off-beat kicks
            if np.random.random() < 0.4:  # 40% chance
                offset_time = kick['time'] + 0.25
                if offset_time < bars * self.signature[0]:
                    extra_kicks.append({
                        'time': offset_time,
                        'pitch': kick['pitch'],
                        'intensity': kick['intensity'] * 0.7,
                        'duration': kick['duration']
                    })
        
        pattern['kick'].extend(extra_kicks)
        pattern['kick'].sort(key=lambda x: x['time'])
        
        # Enhance snare
        for snare in pattern['snare']:
            snare['intensity'] = min(1.0, snare['intensity'] * 1.1)
        
        return pattern

    def create_midi_sequence(self, pattern: Dict) -> List[Tuple[float, str, int]]:
        """
        Convert pattern to MIDI sequence.
        
        Args:
            pattern: Drum pattern dictionary
        
        Returns:
            List of (time, note_type, velocity) tuples
        """
        sequence = []
        
        # Add kicks (MIDI note 36)
        for kick in pattern['kick']:
            velocity = int(kick['intensity'] * 127)
            sequence.append((kick['time'], 'kick', velocity))
        
        # Add snares (MIDI note 38)
        for snare in pattern['snare']:
            velocity = int(snare['intensity'] * 127)
            sequence.append((snare['time'], 'snare', velocity))
        
        # Add hi-hats (MIDI note 42 for closed, 46 for open)
        for hihat in pattern['hihat']:
            velocity = int(hihat['intensity'] * 127)
            note_type = 'closed_hat' if hihat['closed'] else 'open_hat'
            sequence.append((hihat['time'], note_type, velocity))
        
        # Sort by time
        sequence.sort(key=lambda x: x[0])
        
        return sequence
