from langchain_ollama import OllamaLLM  # Import Ollama model from LangChain
from langchain_core.prompts import ChatPromptTemplate  # Import prompt handling module

# Initialize the Ollama LLM with the specified model version
model = OllamaLLM(model="llama3.1:latest")

# Define a prompt template for AI-based content extraction
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Function to process content using Ollama AI
def parse_withollama(dom_chunks, parse_description):
    """
    Uses the Ollama model to extract specific information from the given text chunks.

    Parameters:
        dom_chunks (list of str): List of text chunks to process.
        parse_description (str): The user-defined query specifying what to extract.

    Returns:
        str: The extracted information from all chunks, combined as a single string.
    """
    
    # Create a LangChain chat prompt from the template
    prompt = ChatPromptTemplate.from_template(template)
    
    # Create a processing chain that links the prompt with the AI model
    chain = prompt | model

    parsed_results = []  # List to store processed results

    # Iterate over each chunk of content and process it using the AI model
    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})

        print(f"Parsed batch {i} of {len(dom_chunks)}")  # Display progress
        parsed_results.append(response)  # Store the AI's response

    # Combine all extracted data into a single output string
    return "\n".join(parsed_results)
