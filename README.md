
## Requirements

To run the chatbot system, ensure you have the following installed:

- Python 3.x
- All dependencies listed in `requirements.txt`

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/amanpoddar375/chatbot1.git
    ```
2. Create .env file and put the value of openai api key:
   ```bash
   OPENAI_API_KEY = 'your-openai-api-key'
   ```
3. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

4. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Run the program
```bash
python3 main1.py
```
```bash
#Enter your query when prompted, and the chatbot will respond accordingly.
```

#### PS : The main1.py is the RAG based CLI Chatbot System Using Llamaindex Framework
#### And the main4.py is the implementation of the weaviate vectordb which is incomplete working on it. 
