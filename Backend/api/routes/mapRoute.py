from fastapi import FastAPI

router = FastAPI()

# Dummy data for Bangladesh heatmap
dummy_data = [
    {"lat": 23.8103, "lon": 90.4125, "value": 10},
    {"lat": 24.3636, "lon": 88.6241, "value": 5},
    {"lat": 23.6850, "lon": 90.3563, "value": 8},
    # Add more dummy data points as needed
]

@router.get("/getmapdata")
def get_custom_data():
    return {dummy_data}
