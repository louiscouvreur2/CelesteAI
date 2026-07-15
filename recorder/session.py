from dataclasses import dataclass, field


@dataclass
class RecordingSession:

    frames: list = field(default_factory=list)

    actions: list = field(default_factory=list)

    timestamps: list = field(default_factory=list)