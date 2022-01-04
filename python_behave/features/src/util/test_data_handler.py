import json
import os
from pathlib import Path


class TestDataHandler:

    def load_test_data_json(self, filename):
        current_path = os.path.abspath(__file__)
        test_data_path = os.path.join(str(Path(current_path).parents[3]), "test_data")
        with open(f"{test_data_path}/{filename}", 'r') as f:
            loaded_data = json.load(f)
            return loaded_data
