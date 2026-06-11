"""Audio processing utilities."""

import numpy as np
from scipy import signal


class AudioProcessor:
    """Process and manipulate audio signals."""

    @staticmethod
    def normalize(audio, target_level=-3.0):
        """
        Normalize audio to target dB level.
        
        Args:
            audio: Audio samples
            target_level: Target dB level
        
        Returns:
            Normalized audio
        """
        # Calculate current RMS level
        rms = np.sqrt(np.mean(audio ** 2))
        if rms == 0:
            return audio
        
        # Convert target dB to linear
        target_linear = 10 ** (target_level / 20)
        
        # Scale to target
        return audio * (target_linear / rms)

    @staticmethod
    def compress(audio, threshold=0.5, ratio=4.0, attack=0.005, release=0.1, sr=44100):
        """
        Apply dynamic range compression.
        
        Args:
            audio: Audio samples
            threshold: Compression threshold (0-1)
            ratio: Compression ratio
            attack: Attack time in seconds
            release: Release time in seconds
            sr: Sample rate
        
        Returns:
            Compressed audio
        """
        # Simple compressor implementation
        output = np.zeros_like(audio)
        attack_samples = int(attack * sr)
        release_samples = int(release * sr)
        
        for i in range(len(audio)):
            if np.abs(audio[i]) > threshold:
                # Calculate gain reduction
                excess = np.abs(audio[i]) - threshold
                gain_reduction = 1 - (excess * (ratio - 1) / (ratio * np.abs(audio[i])))
                output[i] = audio[i] * gain_reduction
            else:
                output[i] = audio[i]
        
        return output

    @staticmethod
    def add_reverb(audio, room_size=0.7, damping=0.5, wet=0.3, sr=44100):
        """
        Add reverb effect.
        
        Args:
            audio: Audio samples
            room_size: Room size parameter
            damping: Damping parameter
            wet: Wet signal amount
            sr: Sample rate
        
        Returns:
            Audio with reverb
        """
        # Simple reverb using delay lines
        delay_times = np.array([0.037, 0.041, 0.043, 0.047]) * sr
        delay_times = delay_times.astype(int)
        
        output = audio.copy()
        
        for delay in delay_times:
            delayed = np.zeros_like(audio)
            delayed[delay:] = audio[:-delay] * damping
            output += delayed * wet
        
        return output / (1 + wet)

    @staticmethod
    def mix_tracks(*tracks, levels=None):
        """
        Mix multiple audio tracks.
        
        Args:
            *tracks: Audio tracks to mix
            levels: Level for each track (if None, equal mixing)
        
        Returns:
            Mixed audio
        """
        if levels is None:
            levels = [1.0 / len(tracks)] * len(tracks)
        
        # Find maximum length
        max_length = max(len(t) for t in tracks)
        
        # Mix with padding
        output = np.zeros(max_length)
        for track, level in zip(tracks, levels):
            padded = np.pad(track, (0, max_length - len(track)))
            output += padded * level
        
        return output
