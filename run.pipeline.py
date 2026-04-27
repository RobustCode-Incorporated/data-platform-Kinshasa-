import random
from ingestion.csv.reader import read_csv
from generators.citizen.generator import generate_citizen
from generators.request.generator import generate_request
from services.citizen.service import insert_citizen
from services.request.service import insert_request


def run(file_path):

    print("🚀 PIPELINE START")

    people = read_csv(file_path)
    print(f"📊 CSV loaded: {len(people)} persons")

    if len(people) == 0:
        print("❌ No data in CSV")
        return

    # 🎯 OBJECTIF RÉEL (1.8M)
    TARGET_POPULATION = 1_800_000

    created = 0
    skipped = 0

    for i in range(TARGET_POPULATION):

        person = random.choice(people)

        citizen = generate_citizen(person)
        citizen_id = insert_citizen(citizen)

        if not citizen_id:
            skipped += 1
            continue

        created += 1

        citizen["id"] = citizen_id

        # 1–3 requêtes
        for _ in range(random.randint(1, 3)):
            request = generate_request(citizen)
            insert_request(request)

        # 📊 monitoring
        if created % 10000 == 0:
            print(f"📈 {created} citizens inserted...")

    print("\n✅ PIPELINE DONE")
    print(f"✔ created: {created}")
    print(f"⚠️ skipped: {skipped}")


if __name__ == "__main__":
    run("data/csv/names.csv")