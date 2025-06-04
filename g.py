import google.generativeai as genai

# Replace with your API key
API_KEY = "YOUR_API_KEY_HERE"  

# Configure Gemini
genai.configure(api_key="GOOGLE_API_KEY")

# Test function
def test_gemini():
    try:
        model = genai.GenerativeModel('gemini-1.0-pro')  # Most reliable free tier
        response = model.generate_content(
            "Say 'Hello World' in a creative way",
            safety_settings={'HARM_CATEGORY_HARASSMENT':'BLOCK_NONE'},  # Reduce false blocks
            generation_config={'max_output_tokens': 50}  # Short response
        )
        return response.text
    except Exception as e:
        return f"❌ FAILED: {str(e)}"

# Run test
print("Testing Gemini API...")
result = test_gemini()
print("Response:", result)
