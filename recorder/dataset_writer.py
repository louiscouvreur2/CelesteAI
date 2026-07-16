from pathlib import Path

import numpy as np


SEQUENCE_LENGTH = 8
CHUNK_SIZE = 256


class DatasetWriter:

    def __init__(self, folder="recordings"):
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=True)

    def save(self, session):

        session_dir = self._next_session_dir()
        session_dir.mkdir(parents=True, exist_ok=True)

        frames = np.asarray(session.frames, dtype=np.uint8)
        actions = np.asarray(session.actions, dtype=np.uint8)
        timestamps = np.asarray(session.timestamps, dtype=np.float64)

        sequences, seq_actions, seq_timestamps = self._build_sequences(
            frames, actions, timestamps
        )

        n_chunks = self._write_chunks(
            session_dir, sequences, seq_actions, seq_timestamps
        )

        print(f"[Recorder] Session sauvegardée : {session_dir}")
        print(f"[Recorder] Séquences : {len(sequences)}")
        print(f"[Recorder] Chunks : {n_chunks}")

    def _next_session_dir(self):

        existing = sorted(self.folder.glob("session_*"))
        index = len(existing) + 1

        return self.folder / f"session_{index:04d}"

    def _build_sequences(self, frames, actions, timestamps):

        n_frames = len(frames)
        n_sequences = n_frames // SEQUENCE_LENGTH

        usable = n_sequences * SEQUENCE_LENGTH

        frames = frames[:usable]
        actions = actions[:usable]
        timestamps = timestamps[:usable]

        sequences = frames.reshape(
            n_sequences, SEQUENCE_LENGTH, *frames.shape[1:]
        )

        seq_actions = actions.reshape(
            n_sequences, SEQUENCE_LENGTH, *actions.shape[1:]
        )[:, -1]

        seq_timestamps = timestamps.reshape(
            n_sequences, SEQUENCE_LENGTH
        )[:, -1]

        return sequences, seq_actions, seq_timestamps

    def _write_chunks(self, session_dir, sequences, seq_actions, seq_timestamps):

        n_sequences = len(sequences)
        n_chunks = (n_sequences + CHUNK_SIZE - 1) // CHUNK_SIZE

        for chunk_index in range(n_chunks):

            start = chunk_index * CHUNK_SIZE
            end = start + CHUNK_SIZE

            chunk_path = session_dir / f"chunk_{chunk_index:04d}.npz"

            np.savez_compressed(
                chunk_path,
                frames=sequences[start:end],
                actions=seq_actions[start:end],
                timestamps=seq_timestamps[start:end],
            )

        return n_chunks