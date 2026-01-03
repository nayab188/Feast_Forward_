import joblib
import json
from datetime import datetime, timezone


def train_and_save(menu_item, csv_path, output_dir):
    """
    ML LOGIC IS A BLACK BOX FOR NOW
    """

    # fake model (placeholder)
    model = {
        "menu_item": menu_item,
        "trained_on": csv_path
    }

    joblib.dump(model, f"{output_dir}/model.pkl")

    meta = {
        "menu_item": menu_item,
        "trained_at": datetime.now(timezone.utc).isoformat()
    }

    with open(f"{output_dir}/meta.json", "w") as f:
        json.dump(meta, f)
