from flask import Flask, request, jsonify, render_template
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import logging

app = Flask(__name__)

# Set your OpenAI API key directly in the script
openai_api_key = 'your-api-key'

llm = OpenAI(api_key=openai_api_key, model_name="text-embedding-ada-002")

# Define a prompt template
template = PromptTemplate(template="{prompt}")

# Mocking flag
USE_MOCK = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        prompt = request.form['prompt']
        if USE_MOCK:
            # Mock response
            response = f"Mocked response for prompt: {prompt}— The weather is really good today! "
        else:
            chain = LLMChain(llm=llm, prompt=template)
            response = chain.run(prompt=prompt)
        return jsonify({'response': response})
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

