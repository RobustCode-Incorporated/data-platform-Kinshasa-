from ingestion.csv.reader import read_csv
from ingestion.commune.loader import get_communes

from generators.citizen.generator import generate_citizen
from generators.request.generator import generate_request

from services.citizen.service import insert_citizen
from services.request.service import insert_request


def run(file_path):
    people = read_csv(file_path)
    print(f"{len(people)} personnes chargées depuis CSV")

    communes = get_communes()
    commune_ids = [c[0] for c in communes]

    for person in people:
        citizen = generate_citizen(person, commune_ids)

        citizen_id = insert_citizen(citizen)

        if not citizen_id:
            continue

        # enrichir pour request
        citizen["id"] = citizen_id

        # comportement réaliste : nombre de demandes
        num_requests = 1

        # communes denses → plus de demandes
        if citizen["communeId"] in [6, 14, 23]:
            num_requests = random.randint(2, 4)
        else:
            num_requests = random.randint(1, 2)

        for _ in range(num_requests):
            request = generate_request(citizen)
            insert_request(request)


if __name__ == "__main__":
    run("data/csv/names.csv")