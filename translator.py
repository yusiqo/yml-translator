import os
import yaml
import requests

# Function to translate text using Google Translate API
def translate_text(text, target_language="en"):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "auto",
        "tl": target_language,
        "dt": "t",
        "q": text
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            return response.json()[0][0][0]
        except (IndexError, ValueError):
            raise Exception("Unexpected response from the API.")
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

# Function to translate YAML file
def translate_yaml(input_file, output_file, target_language="en"):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    def translate_item(item):
        if isinstance(item, dict):
            return {key: translate_item(value) for key, value in item.items()}
        elif isinstance(item, list):
            return [translate_item(element) for element in item]
        elif isinstance(item, str):
            return translate_text(item, target_language)
        else:
            return item

    translated_data = translate_item(data)

    with open(output_file, 'w', encoding='utf-8') as file:
        yaml.dump(translated_data, file, allow_unicode=True)

    print(f"Translated: {input_file} -> {output_file}")

# Main function
def main():
    # Get user input for target language and directories
    target_language = input("Enter the target language code (e.g., 'en' for English, 'az' for Azerbaijani): ").strip()
    locale_dir = input("Enter the path to the directory containing .yml files: ").strip()
    output_dir = input("Enter the output directory for translated files: ").strip()

    os.makedirs(output_dir, exist_ok=True)

    translated_list_file = os.path.join(output_dir, "translated_files.txt")

    # Load already translated files
    if os.path.exists(translated_list_file):
        with open(translated_list_file, 'r') as f:
            translated_files = set(f.read().splitlines())
    else:
        translated_files = set()

    for root, _, files in os.walk(locale_dir):
        for file in files:
            if file.endswith(".yml"):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_dir, file)

                if file in translated_files:
                    print(f"Skipping (already translated): {file}")
                    continue

                try:
                    translate_yaml(input_file, output_file, target_language)
                    translated_files.add(file)

                    # Save the name of the translated file
                    with open(translated_list_file, 'a') as f:
                        f.write(file + "\n")

                except Exception as e:
                    print(f"Error translating {file}: {e}")

if __name__ == "__main__":
    main()
