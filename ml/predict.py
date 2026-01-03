

import os
import joblib
import time

def predict_demand(restaurant_id, menu_item, features):
    """
    restaurant_id : int
    menu_item     : str
    features      : dict from form (date, temperature, etc.)
    """

    model_path = f"ml/storage/user_{restaurant_id}/{menu_item}/model.pkl"

    if not os.path.exists(model_path):
        return {
            "error": "This menu item has not been trained yet."
        }

    model = joblib.load(model_path)


    # Part for My ML code module

    # Dummy prediction for now -(checking kosam)
    predicted_servings = 120

    return {
        "id": f"{menu_item}_{int(time.time())}",
        "menu_item": menu_item,
        "demand": predicted_servings
    }
