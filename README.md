# Purpose
Sometimes the Way Back Machine (archive.org) indexes domain URLs that are in an error state.  In these states, code, debug, and potentially sensitive data can be exposed. In order to protect a domain, it's important to know what is publically indexed on historic entries.  



This small OSINT script will run a query against web.archive.org for a domain and filter the results for URLs that have a 500+ status code.  



## Usage
>python main.py 

When prompted enter your domain.

## Preventative Measures
If sensitive data is found, you can write info@archive.org to open a ticket for removing sensitive URLs, subdomains or domains.

There is a procedure that will be required. They will respond with a methodology to verify ownership of the domain (often asking for a txt file to be put into the root of the domain). 

Following their ownership verification, they will remove entries for your domain/subdomain.