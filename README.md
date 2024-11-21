# Cat Facts App 🐱

This project is a Python application that fetches interesting cat facts from a public API, saves them to a SQLite database using SQLAlchemy, and displays the stored facts. The project is simple and demonstrates basic API integration, database interaction, and Python programming concepts.


## Features
- Fetches random cat facts from the [Cat Facts API](https://cat-fact.herokuapp.com).
- Stores fetched facts in a SQLite database using SQLAlchemy ORM.
- Displays the stored facts in the terminal.

## Requirements
- Python 3.x
- Required libraries: `requests`, `sqlalchemy`
- SQLite

## Installation

1. Clone or download the repository.
2. Install the required libraries by running:
    ```bash
    pip install -r requirements.txt
    ```
    or manually:
    ```bash
    pip install requests sqlalchemy
    ```

## Usage

1. **Run the application** by executing the following command in your terminal:
    ```bash
    python main.py
    ```

2. This will:
    - Fetch cat facts from the API.
    - Save them into an SQLite database (`cat_facts.db`).
    - Display the facts in the terminal.

### Example output in the terminal:
API isteği başarılı!
ID: 58e008780aac31001185ed05, Fact: Owning a cat can reduce the risk of stroke and heart attack by a third.
ID: 58e009390aac31001185ed10, Fact: Most cats are lactose intolerant, and milk can cause painful stomach cramps and diarrhea. It's best to forego the milk and just give your cat the standard: clean, cool drinking water.
ID: 58e00b5f0aac31001185ed24, Fact: When asked if her husband had any hobbies, Mary Todd Lincoln is said to have replied "cats."
ID: 5887e1d85c873e0011036889, Fact: Cats make about 100 different sounds. Dogs make only about 10.
ID: 58e00af60aac31001185ed1d, Fact: It was illegal to slay cats in ancient Egypt, in large part because they provided the great service of controlling the rat population.

## Database

The cat facts are saved in an SQLite database (`cat_facts.db`). You can inspect the database using any SQLite browser tool or use it in your future projects.

## File Structure
├── main.py         # Main application logic.
├── models.py       # Database models and setup.
├── requirements.txt # Required Python libraries.
├── README.md       # Project documentation.

## Future Improvements
Add a front-end interface to display facts dynamically.
Implement pagination for large datasets.
Allow users to fetch facts by category or keyword.

## Acknowledgments

- This project was created with the help of **ChatGPT**.
- **Cat Facts API** (https://cat-fact.herokuapp.com/) for providing the cat facts.

## License

This project is open-source and available under the [MIT License](LICENSE).
