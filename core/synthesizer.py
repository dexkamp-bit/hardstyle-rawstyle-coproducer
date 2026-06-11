"""Hardstyle and Rawstyle synthesizer engines."""

import numpy as np
from scipy import signal
import math


class HardstyleSynthesizer:
    """Generate authentic hardstyle sounds and effects."""

    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.duration = 1.0

    def generate_kick(self, bpm=150, pitch=55, intensity=0.8, duration=0.5):
        """
        Generate hardstyle kick drum.
        
        Args:
            bpm: Beats per minute
            pitch: Fundamental frequency in Hz
            intensity: Kick intensity (0.0-1.0)
            duration: Duration in seconds
        
        Returns:
            numpy array of audio samples
        """
        samples = int(self.sample_rate * duration)
        t = np.linspace(0, duration, samples)
        
        # Pitch envelope - classic hardstyle kick pitch drop
        pitch_start = pitch * 1.5
        pitch_end = pitch
        pitch_envelope = np.linspace(pitch_start, pitch_end, samples)
        
        # Decay envelope
        decay = np.exp(-5 * t * intensity)
        
        # Generate sine wave with pitch modulation
        phase = 2 * np.pi * np.cumsum(pitch_envelope) / self.sample_rate
        kick = np.sin(phase) * decay
        
        # Add sub-bass layer
        sub_bass = np.sin(2 * np.pi * pitch * t) * decay * 0.3
        
        # Add click/attack
        click_samples = int(self.sample_rate * 0.01)
        click = np.hanning(click_samples) * 2.0
        kick[:click_samples] += click * intensity
        
        return (kick + sub_bass) * intensity * 0.8

    def generate_snare(self, duration=0.15, intensity=0.8):
        """
        Generate hardstyle snare drum.
        
        Args:
            duration: Duration in seconds
            intensity: Snare intensity (0.0-1.0)
        
        Returns:
            numpy array of audio samples
        """
        samples = int(self.sample_rate * duration)
        t = np.linspace(0, duration, samples)
        
        # Noise component
        noise = np.random.normal(0, 1, samples)
        
        # Decay envelope
        decay = np.exp(-8 * t)
        
        # Filtered noise (band-pass around 200Hz)
        filtered = self._bandpass_filter(noise, 150, 400)
        
        # Pitch component (tone)
        tone_freq = 250
        tone = np.sin(2 * np.pi * tone_freq * t) * 0.4
        
        snare = (filtered + tone) * decay * intensity * 0.7
        return snare

    def generate_hihat(self, open_time=0.08, closed=False, intensity=0.8):
        """
        Generate hardstyle hi-hat.
        
        Args:
            open_time: Open hi-hat duration
            closed: True for closed hat, False for open
            intensity: Hi-hat intensity (0.0-1.0)
        
        Returns:
            numpy array of audio samples
        """
        duration = open_time if not closed else 0.05
        samples = int(self.sample_rate * duration)
        t = np.linspace(0, duration, samples)
        
        # Metallic noise
        noise = np.random.normal(0, 1, samples)
        
        # Decay envelope (faster for closed)
        decay_rate = 15 if closed else 8
        decay = np.exp(-decay_rate * t)
        
        # High-pass filter
        filtered = self._highpass_filter(noise, 8000)
        
        hihat = filtered * decay * intensity * 0.6
        return hihat

    def _bandpass_filter(self, signal_data, low_freq, high_freq):
        """Apply band-pass filter."""
        nyquist = self.sample_rate / 2
        low = low_freq / nyquist
        high = high_freq / nyquist
        b, a = signal.butter(4, [low, high], btype='band')
        return signal.filtfilt(b, a, signal_data)

    def _highpass_filter(self, signal_data, cutoff_freq):
        """Apply high-pass filter."""
        nyquist = self.sample_rate / 2
        normalized_cutoff = cutoff_freq / nyquist
        b, a = signal.butter(4, normalized_cutoff, btype='high')
        return signal.filtfilt(b, a, signal_data)


class RawstyleSynthesizer:
    """Generate authentic rawstyle sounds and effects."""

    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.hardstyle_synth = HardstyleSynthesizer(sample_rate)

    def generate_rawstyle_bass(self, bpm=150, pitch=40, intensity=0.9, duration=0.5):
        """
        Generate aggressive rawstyle bass.
        
        Args:
            bpm: Beats per minute
            pitch: Fundamental frequency in Hz
            intensity: Bass intensity (0.0-1.0)
            duration: Duration in seconds
        
        Returns:
            numpy array of audio samples
        """
        samples = int(self.sample_rate * duration)
        t = np.linspace(0, duration, samples)
        
        # Aggressive pitch modulation (more intense than hardstyle)
        pitch_start = pitch * 1.8
        pitch_end = pitch * 0.9
        pitch_envelope = np.linspace(pitch_start, pitch_end, samples)
        
        # Sharp decay
        decay = np.exp(-8 * t * intensity)
        
        # Generate base sine
        phase = 2 * np.pi * np.cumsum(pitch_envelope) / self.sample_rate
        bass = np.sin(phase) * decay
        
        # Add harmonics for aggression
        harmonics = (
            0.3 * np.sin(phase * 2) * decay +  # 2nd harmonic
            0.15 * np.sin(phase * 3) * decay   # 3rd harmonic
        )
        
        # Add distortion for rawstyle character
        bass_with_harmonics = bass + harmonics
        bass_distorted = self._soft_clip(bass_with_harmonics, intensity)
        
        # Sub-bass layer
        sub_bass = np.sin(2 * np.pi * pitch * t) * decay * 0.4
        
        return (bass_distorted + sub_bass) * intensity * 0.85

    def generate_raw_kick(self, bpm=150, pitch=50, intensity=0.95, duration=0.6):
        """
        Generate aggressive rawstyle kick (more intense than hardstyle).
        
        Args:
            bpm: Beats per minute
            pitch: Fundamental frequency in Hz
            intensity: Kick intensity (0.0-1.0)
            duration: Duration in seconds
        
        Returns:
            numpy array of audio samples
        """
        # Start with hardstyle kick and enhance it
        kick = self.hardstyle_synth.generate_kick(bpm, pitch, intensity, duration)
        
        # Add more harmonics and distortion
        samples = len(kick)
        t = np.linspace(0, duration, samples)
        
        # Add harmonic content
        harmonics = (
            0.4 * np.sin(2 * np.pi * pitch * 2 * t) * np.exp(-6 * t) +
            0.2 * np.sin(2 * np.pi * pitch * 3 * t) * np.exp(-6 * t)
        )
        
        # Combine and distort
        combined = kick + harmonics * intensity
        distorted = self._soft_clip(combined, intensity * 1.2)
        
        return distorted * 0.8

    def _soft_clip(self, signal_data, threshold=1.0):
        """Apply soft clipping for distortion."""
        return np.tanh(signal_data * threshold)
