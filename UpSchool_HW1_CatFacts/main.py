import requests
from datetime import datetime
from models import Session, CatFact


def fetch_cat_facts():
    url = "https://cat-fact.herokuapp.com/facts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"API request failed. Error code: {response.status_code}")
        return None


def save_facts_to_db(facts):
    session = Session()
    for fact in facts:
        cat_fact = CatFact(
            id=fact['_id'],
            text=fact['text'],
            createdAt=datetime.fromisoformat(fact['createdAt'].replace('Z', '+00:00')),
            updatedAt=datetime.fromisoformat(fact['updatedAt'].replace('Z', '+00:00')),
            type=fact['type']
        )
        session.merge(cat_fact)
    session.commit()
    session.close()


def display_facts():
    session = Session()
    facts = session.query(CatFact).all()
    for fact in facts:
        print(f"ID: {fact.id}")
        print(f"Fact: {fact.text}")
        print(f"Created At: {fact.createdAt}")
        print(f"Updated At: {fact.updatedAt}")
        print(f"Type: {fact.type}")
        print("-" * 50)
    session.close()


def main():
    facts = fetch_cat_facts()
    if facts:
        save_facts_to_db(facts)
        print("Data successfully saved.")
        print("\nSaved data:")
        display_facts()
    else:
        print("Failed to retrieve data.")


if __name__ == "__main__":
    main()
