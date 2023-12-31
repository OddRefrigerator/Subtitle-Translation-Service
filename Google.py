import os
import pysubs2
from google.cloud import translate_v2 as translate

# Set your API key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"

# Instantiate the translation client
client = translate.Client()

# Function to translate a subtitle line, handling potential errors
def translate_line(line, target_language):
    try:
        translation = client.translate(line.text, target_language=target_language)
        return pysubs2.SSALine(start=line.start, end=line.end, text=translation['translatedText'])
    except Exception as e:
        print(f"Error translating line: {e}")
        return line  # Return original line if translation fails

# Function to translate an SRT file, incorporating error handling and progress feedback
def translate_srt(srt_file, target_language):
    try:
        subs = pysubs2.load(srt_file, encoding="utf-8")
        translated_subs = subs.copy()

        for i, line in enumerate(translated_subs):
            translated_line = translate_line(line, target_language)
            translated_subs.lines[i] = translated_line
            print(f"Translated line {i+1}/{len(translated_subs)}")  # Show progress

        # Save the translated SRT file
        translated_srt_file = os.path.splitext(srt_file)[0] + "_translated.srt"
        translated_subs.save(translated_srt_file)

        print(f"Subtitle file translated and saved as: {translated_srt_file}")
    except Exception as e:
        print(f"Error processing SRT file: {e}")

# Example usage
srt_file = "path/to/your/subtitle.srt"
target_language = "en"  # Replace with the desired target language code
translate_srt(srt_file, target_language)
