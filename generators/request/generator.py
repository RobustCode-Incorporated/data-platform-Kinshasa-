import random
from services.request.service import generate_request_types

def generate_request(citizen_id):
    types = generate_request_types()

    return {
        "citizenId": citizen_id,
        "type": random.choice(types),
        "status": random.choice(["PENDING", "APPROVED", "REJECTED"])
    }