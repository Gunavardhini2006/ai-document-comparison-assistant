import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def compare_documents(text_a, text_b):
    """
    Sends Document A and Document B texts to the Gemini API with a structured
    comparison prompt and returns the result.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None, "API key not found. Please check your .env file."

    # Initialize the Google GenAI client
    client = genai.Client(api_key=api_key)

    # Craft the prompt enforcing strict document analysis rules
    prompt = f"""
    You are an expert AI Document Comparison Assistant. Your task is to compare two documents provided below strictly based on their text content.

    INSTRUCTIONS:
    1. Base your comparison ONLY on the supplied text. Do not invent, assume, or hallucinate details.
    2. Keep facts from Document A separate from facts from Document B.
    3. Identify clear similarities and meaningful differences.
    4. Compare key details such as dates, names, amounts, conditions, and requirements where present[cite: 2].
    5. If a detail is missing from either document, state "Not found in the provided text"[cite: 4].
    6. Organize your response clearly with these exact headings:
       - Document A Summary
       - Document B Summary
       - Similarities
       - Differences
       - Key Details Comparison
       - Overall Conclusion
       - Limitations

    ---
    DOCUMENT A TEXT:
    {text_a}
    ---

    DOCUMENT B TEXT:
    {text_b}
    """

    try:
        # Call the Gemini model to generate the comparison
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt
        )
        return response.text, None
        
    except Exception as e:
        return None, f"Error communicating with Gemini API: {str(e)}"