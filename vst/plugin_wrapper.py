"""VST/CLAP plugin wrapper."""

from coproducer import HardstyleCoProducer


class PluginWrapper:
    """
    VST/CLAP plugin wrapper for FL Studio.
    
    This wrapper adapts the HardstyleCoProducer to work as a VST/CLAP plugin
    in FL Studio and other DAWs.
    """

    def __init__(self):
        self.coproducer = HardstyleCoProducer()
        self.parameters = {
            'bpm': 150,
            'style': 'hardstyle',  # or 'rawstyle'
            'intensity': 0.8,
            'bars': 4,
            'root_note': 40,
        }

    def get_parameter(self, param_id: int) -> float:
        """Get plugin parameter."""
        param_map = {
            0: 'bpm',
            1: 'intensity',
            2: 'bars',
            3: 'root_note',
        }
        return self.parameters.get(param_map.get(param_id), 0.0)

    def set_parameter(self, param_id: int, value: float):
        """Set plugin parameter."""
        param_map = {
            0: 'bpm',
            1: 'intensity',
            2: 'bars',
            3: 'root_note',
        }
        param_name = param_map.get(param_id)
        if param_name:
            self.parameters[param_name] = value
            if param_name == 'bpm':
                self.coproducer.set_bpm(int(value))

    def generate_drums(self) -> bytes:
        """
        Generate drum pattern as MIDI.
        
        Returns:
            MIDI data as bytes
        """
        pattern = self.coproducer.generate_drum_pattern(
            self.parameters['style'],
            int(self.parameters['bars']),
            self.parameters['intensity']
        )
        # Convert to MIDI bytes (implementation depends on MIDI library)
        return b''

    def generate_bass(self) -> bytes:
        """
        Generate bass progression as MIDI.
        
        Returns:
            MIDI data as bytes
        """
        progression = self.coproducer.generate_bass_progression(
            int(self.parameters['bars']),
            int(self.parameters['root_note']),
            self.parameters['style'] == 'rawstyle',
            self.parameters['intensity']
        )
        # Convert to MIDI bytes (implementation depends on MIDI library)
        return b''
