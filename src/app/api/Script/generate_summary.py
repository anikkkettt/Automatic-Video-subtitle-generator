import os
import openai
import json
import sys

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(text):
    """Generate a summary using OpenAI's GPT model."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Summarize the following text: {text}"}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating summary: {e}")
        return None

def main():
    # Take the transcription file path and summary file path as command-line arguments
    if len(sys.argv) < 3:
        print("Please provide the transcription file path and the summary file path.")
        sys.exit(1)

    file_path = sys.argv[1]
    summary_file_path = sys.argv[2]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            transcription_data = json.load(file)

        transcription_text = transcription_data.get("results", {}).get("transcripts", [{}])[0].get("transcript", "")
        
        # Generate summary
        summary = generate_summary(transcription_text)

        # Save summary to the specified summary file path
        with open(summary_file_path, 'w', encoding='utf-8') as summary_file:
            summary_file.write(summary or "Summary generation failed.")

        print(f"Summary saved to {summary_file_path}")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()

