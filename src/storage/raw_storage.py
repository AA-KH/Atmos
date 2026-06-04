import json
from pathlib import Path

class RawStorage:
    RAW_DIR = Path("data/raw")

    @classmethod
    def save(cls,filename,data):
        cls.RAW_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        filepath = (cls.RAW_DIR / filename)
        with open(filepath,"w") as f:
            json.dump(data,f,indent=4)