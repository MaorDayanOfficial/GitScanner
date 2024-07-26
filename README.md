After more then a year today i updated the tool :)
# GitScanner

This Tool scans a list of URLs for potential Git source code disclosure vulnerabilities. It's designed to be fast, efficient, and user friendly, providing clear and colorful output in the terminal.

## Features

- Scans multiple URLs concurrently for improved speed
- Detects common Git repository paths that might be exposed
- Provides real-time progress updates with color-coded output
- Saves only vulnerable URLs to a CSV file
- Supports command-line arguments for flexible usage

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system
- pip

## Installation

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/MaorDayanOfficial/GitScanner
   cd GitScanner
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare a text file containing the URLs you want to scan, with one URL per line. For example, `urls_to_scan.txt`:
   ```
   https://example.com
   https://anotherexample.com
   http://testsite.net
   testsite2.net
   ```

2. Run the script from the command line:
   ```
   python git_scanner.py urls_to_scan.txt
   ```

3. (Optional) You can specify an output file name and the number of worker threads:
   ```
   python git_scanner.py urls_to_scan.txt --output vulnerable_sites.csv --workers 20
   ```

## Command-line Arguments

- `input_file`: (Required) Path to the text file containing URLs to scan
- `--output`: (Optional) Name of the CSV file to save vulnerable URLs (default: vulnerable_urls.csv)
- `--workers`: (Optional) Number of parallel worker threads (default: 10)

## Output

The script provides real-time feedback in the terminal:

- Green text for general information and successful completion
- Yellow text for progress updates
- Red text for discovered vulnerabilities

If vulnerabilities are found, they are saved in the specified CSV file (default: vulnerable_urls.csv).

## Contributing

Contributions to improve the script are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and commit them (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

This tool is for educational and ethical testing purposes only. Always ensure you have permission before scanning websites you do not own or operate. The authors are not responsible for any misuse or damage caused by this program.
## WARNING: This project is for educational purposes only and intended for good use. Do not use it for unethical purposes!
