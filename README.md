
# YAML Translator Tool

This Python tool translates all `.yml` files in a specified directory into a target language using the Google Translate API. It skips previously translated files and logs all translation activities.

## Features

- **Dynamic Target Language**: Specify the target language at runtime.
- **Custom Directories**: Set input and output directories for flexibility.
- **Translation Logging**: Tracks translated files to avoid duplication.
- **Error Handling**: Logs errors and continues with other files.

## Requirements

- Python 3.6 or later
- Required Python packages:
  - `requests`
  - `pyyaml`

Install the dependencies with:
```bash
pip install requests pyyaml
```

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/yaml-translator.git
   cd yaml-translator
   ```

2. Run the script:
   ```bash
   python translator.py
   ```

3. Follow the prompts:
   - Enter the target language code (e.g., `en` for English, `az` for Azerbaijani).
   - Specify the path to the directory containing `.yml` files.
   - Enter the output directory where translated files will be saved.

### Example Workflow

```plaintext
Enter the target language code (e.g., 'en' for English, 'az' for Azerbaijani): en
Enter the path to the directory containing .yml files: ./locale
Enter the output directory for translated files: ./locale_translated

Translated: ./locale/file1.yml -> ./locale_translated/file1.yml
Skipping (already translated): file2.yml
Error translating file3.yml: Unexpected response from the API.
```

## File Structure

- **Input Directory**: The folder containing `.yml` files to translate.
- **Output Directory**: Translated files are saved here.
- **Log File**: A `translated_files.txt` file is created in the output directory to track already translated files.

## Notes

- The script uses a free, keys-less Google Translate API endpoint (`https://translate.googleapis.com/translate_a/single`). Be aware of potential rate limits.
- Ensure your `.yml` files are valid YAML to prevent parsing errors.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
