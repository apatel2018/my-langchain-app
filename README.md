# LangChain Demo App

This is a simple demo application that uses LangChain and the OpenAI API to generate responses based on user prompts. The application is built using Flask for the backend and HTML for the frontend.

## Features

- Accepts user input through a web form.
- Uses LangChain and OpenAI to generate responses.
- Displays the generated responses on the web page.

## Technologies Used

- Python
- Flask
- LangChain
- OpenAI API
- HTML
- JavaScript (jQuery)

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Git (optional, for cloning the repository)

### Steps

1. **Clone the repository** (or download the source code):

   ```sh
   git clone https://github.com/apatel2018/my-langchain-app.git
   cd my-langchain-app


2. **Install the required dependencies**:

   ```sh
   pip install langchain openai flask
   ```

3. **Set your OpenAI API key**:

   Replace `'your-api-key'` in `app.py` with your actual OpenAI API key.

4. **Run the application**:

   ```sh
   python app.py
   ```

5. **Open your web browser** and navigate to:

   ```
   http://127.0.0.1:5000
   ```

## Project Structure

```
my-langchain-app/
├── app.py
├── templates/
│   └── index.html
└── README.md
```
```
