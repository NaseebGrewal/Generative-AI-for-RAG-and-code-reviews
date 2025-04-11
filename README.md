# Generative-AI-for-RAG-and-code-reviews

This repository contains code and resources for integrating generative AI techniques with Retrieval-Augmented Generation (RAG) implementations and code reviews.

## Repository Structure

- **README.md**  
  This file with instructions and project details.

- **requirements-rag.txt**  
  List of required Python libraries for the project:
  - `sentence_transformers`
  - `faiss-cpu` (for MAC & Linux)
  - `numpy`
  - `python-dotenv`
  - `openai`
  - `langchain`

- **rag/**  
  Contains the core project modules including:
  - `test_index.py`: Script to create FAISS index, perform search, and retrieve documents.
  - Other modules for creating and searching indexes.

- **utils/**  
  Contains additional utility scripts such as:
  - `Flask.py` (or similarly named Flask application file) – used to run the web interface or API.

- **.env**  
  Environment file located in the root directory.  
  **Note:** Ensure the relevant API keys and configuration values are set correctly.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/NaseebGrewal/Generative-AI-for-RAG-and-code-reviews.git
   cd Generative-AI-for-RAG-and-code-reviews
   ```

2. **Install Dependencies**

   Create a virtual environment and install the required packages:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements-rag.txt
   ```

3. **Configure Environment Variables**

   Update the `.env` file at the repository root with your configuration details (API keys, file paths, etc.).

4. **Run the Application**

   Depending on your desired workflow:

   - **For testing the indexing functionality:**
     
     Navigate to the `rag` directory and run:
     
     ```bash
     python test_index.py
     ```

   - **For running the Flask application:**
     
     Navigate to the `utils` directory and run the Flask file (e.g., `Flask.oy`):
     
     ```bash
     cd utils
     python flask.py
     ```

## Additional Notes

- Ensure you are using a supported Python version based on the dependencies (e.g., Python 3.10 or 3.11 may be necessary for some libraries).
- When dealing with secrets or API keys, avoid committing them to your repository.
- For further enhancements, check the documentation for each library used in this project.

Happy coding!