"""Basic usage examples of the Co-Producer plugin."""

from coproducer import HardstyleCoProducer

# Initialize the Co-Producer
producer = HardstyleCoProducer(bpm=150)

# Example 1: Generate a hardstyle kick
print("Generating hardstyle kick...")
kick = producer.generate_hardstyle_kick(intensity=0.8)
print(f"Kick generated: {len(kick)} samples")

# Example 2: Generate a rawstyle kick
print("\nGenerating rawstyle kick...")
raw_kick = producer.generate_rawstyle_kick(intensity=0.95)
print(f"Rawstyle kick generated: {len(raw_kick)} samples")

# Example 3: Generate hardstyle drum pattern
print("\nGenerating hardstyle drum pattern...")
hard_pattern = producer.generate_drum_pattern(style='hardstyle', bars=4, intensity=0.8)
print(f"Drum pattern: {len(hard_pattern['kick'])} kicks, {len(hard_pattern['snare'])} snares")

# Example 4: Generate rawstyle drum pattern
print("\nGenerating rawstyle drum pattern...")
raw_pattern = producer.generate_drum_pattern(style='rawstyle', bars=4, intensity=0.95)
print(f"Rawstyle pattern: {len(raw_pattern['kick'])} kicks, {len(raw_pattern['snare'])} snares")

# Example 5: Generate bass progression
print("\nGenerating aggressive bass progression...")
bass = producer.generate_bass_progression(bars=4, root_note=40, aggressive=True, intensity=0.95)
print(f"Bass progression: {len(bass['notes'])} notes")

# Example 6: Search sample library
print("\nSearching for hardstyle kicks...")
samples = producer.search_samples('hardstyle_kick')
for sample in samples:
    print(f"  - {sample['name']} in {sample['category']}")

# Example 7: Export MIDI
print("\nExporting pattern as MIDI...")
producer.export_midi(hard_pattern, 'hardstyle_pattern.mid')

print("\n✅ All examples completed!")
