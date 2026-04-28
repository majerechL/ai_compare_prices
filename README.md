# Price Comparison Assistant

Price Comparison Assistant is a Python project for comparing product prices across multiple stores using an OpenAI assistant, a custom tool, and a simple Streamlit user interface.

The project is currently in a working version and serves as a functional foundation for further improvements.

## About the Project

The goal of the project is to allow the user to enter a product name and get a price comparison from multiple stores.

The project uses:
- an OpenAI assistant
- a custom `get_product_prices` tool
- a `PriceScraper` class
- a Streamlit interface

The assistant receives input from the user, calls the price-fetching tool, and then prepares the response in a suitable format.

## Technologies Used

- Python 3.12
- requests
- beautifulsoup4
- python-dotenv
- streamlit
- openai

## Project Structure

```text
project/
├── main.py
├── assistant_manager.py
├── price_scraper.py
├── tools.py
├── assistant_instructions.txt
├── requirements.txt
├── .env
├── .gitignore
└── app.log
```

## Installation

### Creating a Virtual Environment

First, create a virtual environment called `myenv`:

```bash
python3.12 -m venv myenv
```

### Activating the Virtual Environment

On Windows:

```bash
myenv\Scripts\activate
```

After activation, the environment name should appear before the path in the terminal:

```bash
(myenv)
```

### Deactivating the Environment

```bash
deactivate
```

### Installing Dependencies

The project uses the following third-party libraries:
- requests
- beautifulsoup4
- python-dotenv
- streamlit
- openai

If they are listed in `requirements.txt`, install them like this:

```bash
pip install -r requirements.txt
```

To save the currently installed packages into `requirements.txt`, use:

```bash
pip freeze > requirements.txt
```

---

## Environment Configuration

The project uses a `.env` file to store sensitive data, such as API keys.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

These values should never be shared.

### Loading Environment Variables

Environment variables are loaded using `load_dotenv()` from the `python-dotenv` library.

In an earlier version of the project, values were read using `os.getenv()`. Later, the variable name was changed to `OPENAI_API_KEY` so that the `openai.OpenAI()` client could load it automatically from the environment.

### `.gitignore`

A `.gitignore` file is included in the project so that sensitive or unnecessary files are not pushed to GitHub, for example:

- `.env`
- `myenv/`
- `__pycache__/`
- local or temporary files

---

## Project Development Process

An `assistant_instructions.txt` file was created to store instructions for the assistant on how it should respond when comparing product prices.

In `tools.py`, the `get_product_prices` tool is defined.

Tool parameter:
- `product_name`

Tool purpose:
- fetch product prices from multiple stores

A `price_scraper.py` file and a `PriceScraper` class were created.

Inside it, the following method was added:

```python
get_product_prices(product_name)
```

In its first version, this method returned mock data in the form of a list of offers.

Each offer contains:
- `product_name`
- `shop`
- `price`
- `url`

The basic version worked with mock data from these stores:
- Alza
- Nay
- Smarty

Work also began on the `assistant_manager.py` file, where the `AssistantManager` class was created.

The class accepts:
- `client`
- `assistant`
- `thread`

Basic class attributes:
- `self.run`
- `self.summary`

The `add_message_to_thread(role, content)` method inserts a message into the thread so the assistant can process it.
The `run_assistant()` method starts the assistant on the current thread and stores the run in `self.run`.
The `check_run()` method checks the status of the current run and returns it.
The `wait_for_run_to_complete()` method checks the run status in a loop.

If the run is completed:
- it loads the latest response

If the assistant requires a tool call:
- it prepares the tool outputs
- sends them back

The `format_output(prices_output)` method converts the list of offers into text output in the following format:
- Product name
- Shop
- Price
- URL

The `prepare_tool_outputs(tool_calls)` method:
- loads the tool call arguments
- gets `product_name`
- creates a `PriceScraper` object
- calls `get_product_prices(product_name)`
- formats the result using `format_output`
- prepares the response for the tool output

The `get_latest_response()` method loads the latest message from the thread and stores it in `self.summary`.
The `get_summary()` method returns the stored assistant response.

The `assistant_manager.py` file is currently in its first functional version.

It contains the main project flow, but future improvements are planned:
- handling additional run states
- a short pause in the waiting loop
- safer response reading

In `main.py`, the following imports were added:
- `openai`
- `load_dotenv`
- `logging`

The `read_instructions(file_path)` function loads text from the file containing the assistant instructions.

It also includes handling for `FileNotFoundError` and logs errors into `app.log`.

In `main.py`, the `main()` function was prepared. It:
- loads `.env` using `load_dotenv()`
- sets up logging into `app.log`
- creates the OpenAI client using `openai.OpenAI()`
- sets the model to `gpt-4.1-mini`

The variable name in `.env` was changed to `OPENAI_API_KEY`, so the OpenAI client can load it automatically from the environment.

The `streamlit` library was added to `main.py`, and work began on preparing the user interface.

### Streamlit Form

The following elements were added to the interface:
- the app title using `streamlit.title(...)`
- a form using `streamlit.form(...)`
- a text input for entering the product name
- a submit button

An import of tools from `assistant_tools` was added because it is used in the logic after pressing the submit button.

Inside `if submit_button`, logic for creating the assistant through `streamlit.session_state` was added.

This ensures that the assistant is not recreated on every click, but is instead stored in the session state and reused.

## Usage

Activate the virtual environment:

```bash
myenv\Scripts\activate
```

 Install the dependencies:

```bash
pip install -r requirements.txt
```

 Make sure the API key is set in `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

 Run the application with Streamlit:

```bash
streamlit run main.py
```

Enter a product name in the application.

Submit the form.

The assistant will process the input, use the `get_product_prices` tool, and return a response with the price comparison.

## Planned Improvements

Possible future improvements include:
- real price scraping instead of mock data
- better error handling
- additional terminating run statuses
- a pause in the polling loop
- safer response reading
- better output formatting
- extended price comparison logic