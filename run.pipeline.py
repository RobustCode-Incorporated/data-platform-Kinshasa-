from ingestion.pdf.reader import read_pdf
from parsers.exam_parser import parse_people
from ingestion.commune.loader import get_communes

from generators.citizen.generator import generate_citizen
from generators.request.generator import generate_request

from services.citizen.service import insert_citizen
from services.request.service import insert_request


def run(pdf_path):
    communes = get_communes()

    lines = read_pdf(pdf_path)
    people = parse_people(lines)

    print(f"{len(people)} personnes extraites")

    for person in people:
        citizen = generate_citizen(person, communes)
        citizen_id = insert_citizen(citizen)

        request = generate_request(citizen_id)
        insert_request(request)


if __name__ == "__main__":
    run("data/pdfs/exam.pdf")