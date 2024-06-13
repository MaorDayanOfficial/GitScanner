import requests

def scan_for_git_source_code_disclosure(url, results_file, skipped_file):
    """
    Scan a URL for Git source code disclosure vulnerability.
    If vulnerability found, save the URL to results_file.
    If skipped, save the URL to skipped_file.
    """
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    try:
        response = requests.get(url, timeout=5)
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
                response = requests.get(url + path, allow_redirects=False)
                if response.status_code == 200 and 'repositoryformatversion' in response.text:
                    print(f"[VULNERABLE] Git source code disclosure vulnerability found at: {url}")
                    with open(results_file, 'a') as file:
                        file.write(url + '\n')
                    break
            else:
                print(f"[SAFE] No Git source code disclosure vulnerability found at: {url}")
        else:
            print(f"[SKIPPED] URL not accessible: {url}")
            with open(skipped_file, 'a') as file:
                file.write(url + '\n')
    except requests.exceptions.RequestException:
        print(f"[SKIPPED] URL not responsive: {url}")
        with open(skipped_file, 'a') as file:
            file.write(url + '\n')
def main():
    file_path = "DomainsToScan.txt"
    results_file = "results.txt"
    skipped_file = "skipped.txt"
    with open(file_path, 'r') as file:
        urls = file.readlines()
    for url in urls:
        url = url.strip()
        scan_for_git_source_code_disclosure(url, results_file, skipped_file)

if __name__ == '__main__':
    main()
