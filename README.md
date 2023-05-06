# DomainSleuth
DomainSleuth is a versatile and user-friendly command-line tool for discovering valuable information about target domains and their subdomains, making it a handy addition to any bug bounty hunter's toolkit. By leveraging the power of Server Name Indication (SNI) and DNS resolution, DomainSleuth can efficiently unveil alternative domain names hosted on the same TLS server and retrieve potential subdomains associated with a given target domain.

Key Features:

- Obtain SNI information from target domains, including issued certificate names and alternative names.
- Discover subdomains of a target domain using DNS resolution.
- Simple command-line interface for ease of use.

Usage:

```bash
python3 domainsleuth.py <domain>
```

Replace `<domain>` with the domain of interest, and DomainSleuth will return the certificate information and a list of discovered subdomains.

Requirements:

- Python 3.6 or later
- dnspython library (`pip install dnspython`)

Please note that the subdomain discovery method may not be exhaustive and might not find all existing subdomains. For a more comprehensive search, consider using additional techniques such as subdomain bruteforcing, reconnaissance service APIs, or passive data sources.
