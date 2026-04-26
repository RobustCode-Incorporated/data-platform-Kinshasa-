import random

# Types de demandes
REQUEST_TYPES = [
    "Acte de naissance",
    "Acte de mariage",
    "Acte de résidence"
]

# Probabilité par commune (simulation réaliste)
COMMUNE_BEHAVIOR = {
    # Gombe (administratif élevé)
    5: {
        "Acte de naissance": 0.2,
        "Acte de mariage": 0.5,
        "Acte de résidence": 0.3
    },

    # Zones densément peuplées
    6: {  # Kimbanseke
        "Acte de naissance": 0.6,
        "Acte de mariage": 0.2,
        "Acte de résidence": 0.2
    },

    14: {  # Masina
        "Acte de naissance": 0.6,
        "Acte de mariage": 0.2,
        "Acte de résidence": 0.2
    },

    23: {  # Ndjili
        "Acte de naissance": 0.5,
        "Acte de mariage": 0.25,
        "Acte de résidence": 0.25
    }
}

STATUS = ["soumise", "en traitement", "validée"]


def weighted_request_type(commune_id):
    if commune_id in COMMUNE_BEHAVIOR:
        probs = COMMUNE_BEHAVIOR[commune_id]
        return random.choices(
            list(probs.keys()),
            weights=list(probs.values())
        )[0]

    return random.choice(REQUEST_TYPES)


def generate_request(citizen):
    return {
        "citizenId": citizen["id"],
        "type": weighted_request_type(citizen["communeId"]),
        "status": random.choice(STATUS)
    }