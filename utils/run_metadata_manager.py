import os
import json
import uuid
import datetime


class RunMetadataManager:

    def __init__(self):

        self.base_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(self.base_dir, exist_ok=True)

        self.execution_id = str(uuid.uuid4())
        self.timestamp = datetime.datetime.utcnow().isoformat()

        self.metadata_file = os.path.join(
            self.base_dir, f"run_metadata_{self.execution_id}.json"
        )

    def generate_metadata(self, environment, browser_mode):

        metadata = {
            "execution_id": self.execution_id,
            "timestamp_utc": self.timestamp,
            "environment": environment,
            "browser_mode": browser_mode,
        }

        return metadata

    def export_metadata(self, metadata):

        with open(self.metadata_file, "w") as f:
            json.dump(metadata, f, indent=4)

        return self.metadata_file
