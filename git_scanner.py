import requests
import concurrent.futures
import argparse
import logging
from urllib.parse import urlparse
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()

logging.basicConfig(level=logging.INFO, format='%(message)s')

def scan_for_git_source_code_disclosure(url):
    """
    Scan a URL for Git source code disclosure vulnerability.
    Returns a tuple (is_vulnerable, vulnerability_details).
    """
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url
    
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        if response.status_code == 200:
            git_paths = [
                '/.git/config',
                '/.git/HEAD',
                '/.git/index',
                '/.git/objects/info/packs',
                '/.git/refs/heads/master',
                '/.git/refs/remotes/origin/HEAD',
            ]
            for path in git_paths:
                response = requests.get(url + path, allow_redirects=False, timeout=5)
                if response.status_code == 200 and 'repositoryformatversion' in response.text:
                    return True, f"{url},{path}"
            return False, None
        else:
            return False, None
    except requests.exceptions.RequestException:
        return False, None

def scan_urls(urls, max_workers=10):
    vulnerable_urls = []
    total_urls = len(urls)
    scanned_urls = 0

    print(f"{Fore.CYAN}Starting scan of {total_urls} URLs...{Style.RESET_ALL}\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(scan_for_git_source_code_disclosure, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            scanned_urls += 1
            is_vulnerable, details = future.result()
            if is_vulnerable:
                vulnerable_urls.append(details)
                print(f"{Fore.RED}[VULNERABLE] {details.split(',')[0]}{Style.RESET_ALL}")
            
            # Update progress
            if scanned_urls % 10 == 0 or scanned_urls == total_urls:
                progress = (scanned_urls / total_urls) * 100
                print(f"{Fore.YELLOW}Progress: {scanned_urls}/{total_urls} URLs scanned ({progress:.1f}%){Style.RESET_ALL}")

    return vulnerable_urls

def main():
    parser = argparse.ArgumentParser(description="Git Source Code Disclosure Scanner")
    parser.add_argument("input_file", help="Text file containing list of URLs to scan")
    parser.add_argument("--output", default="vulnerable_urls.csv", help="File to save vulnerable URLs (default: vulnerable_urls.csv)")
    parser.add_argument("--workers", type=int, default=10, help="Number of parallel workers (default: 10)")
    args = parser.parse_args()

    with open(args.input_file, 'r') as file:
        urls = [url.strip() for url in file.readlines()]

    unique_domains = set(urlparse(url).netloc for url in urls)
    print(f"{Fore.GREEN}Loaded {len(urls)} URLs from {len(unique_domains)} unique domains.{Style.RESET_ALL}\n")

    vulnerable_urls = scan_urls(urls, args.workers)

    if vulnerable_urls:
        with open(args.output, 'w') as file:
            file.write("URL,Vulnerable_Path\n")
            for url in vulnerable_urls:
                file.write(f"{url}\n")
        print(f"\n{Fore.RED}Found {len(vulnerable_urls)} vulnerable URLs. Results saved to {args.output}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.GREEN}No vulnerabilities found across all scanned URLs.{Style.RESET_ALL}")

    print(f"\n{Fore.CYAN}Scan completed.{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
