import random

from ingestion.csv.reader import read_csv
from ingestion.commune.loader import get_communes

from generators.citizen.generator import generate_citizen
from generators.request.generator import generate_request

from services.citizen.service import insert_citizen
from services.request.service import insert_request


def run(file_path):

    print("🚀 PIPELINE START")

    # 📥 load CSV
    people = read_csv(file_path)
    print(f"📊 CSV loaded: {len(people)} persons")

    # 🏘 communes
    communes = get_communes()
    commune_ids = [c[0] for c in communes]
    print(f"🏘 communes loaded: {len(commune_ids)}")

    # 🎯 simulation size (IMPORTANT)
    TARGET_POPULATION = 5000

    if len(people) == 0:
        print("❌ No data in CSV")
        return

    sampled_people = random.sample(
        people,
        min(len(people), TARGET_POPULATION)
    )

    print(f"🎯 Simulation size: {len(sampled_people)} citizens")

    created = 0
    skipped = 0

    for person in sampled_people:

        # 👤 generate citizen
        citizen = generate_citizen(person, commune_ids)
        citizen_id = insert_citizen(citizen)

        if not citizen_id:
            skipped += 1
            print("⚠️ citizen skipped (no ID returned)")
            continue

        created += 1
        print(f"👤 citizen created: {citizen_id}")

        citizen["id"] = citizen_id

        # 📄 generate requests (1–3 per citizen)
        num_requests = random.randint(1, 3)

        for _ in range(num_requests):
            request = generate_request(citizen)
            insert_request(request)

        if created % 500 == 0:
            print(f"📈 progress: {created} citizens inserted")

    print("\n✅ PIPELINE DONE")
    print(f"✔ created: {created}")
    print(f"⚠️ skipped: {skipped}")


if __name__ == "__main__":
    run("data/csv/names.csv")