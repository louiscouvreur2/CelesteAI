import json
import time


class MetadataWriter:

    def write(self, session):

        metadata = {

            "session": session.id,

            "frames": session.frame_count,

            "actions": session.action_count,

            "duration": time.perf_counter() - session.start_time,

        }

        with open(

            session.path / "metadata.json",

            "w",

            encoding="utf8",

        ) as f:

            json.dump(metadata, f, indent=4)