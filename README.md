# GitScanner
A tool for bug hunting or penetration testing that targets (in a good way) websites with publicly accessible .git repositories.

This tool does not exploit it, it was created to scan lists of hundreds / thousands of websites.

## Installation

```bash
  git clone https://github.com/MaorDayanOfficial/GitScanner.git
  cd GitScanner
  pip install -r requirements.txt
```
    
## How to run?

1. Add links in the "DomainsToScan" txt file and save it (basiclly can be thousands) and save it
2. Run the script, it will go one by one until the end of the list.

## Skipped file?
Links listed here are for websites that either blocked the scanner or are no longer online, preventing the scanner from connecting and scanning them.

## results file?
Links listed here are for websites where the scanner has found an open .git directory. Only websites with accessible .git directories will be saved here



## WARNING: This project is for educational purposes only and intended for good use. Do not use it for unethical purposes!
