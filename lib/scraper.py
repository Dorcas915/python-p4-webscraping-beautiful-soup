from bs4 import BeautifulSoup
import requests

def scrape_page_title():
    """Scrape the page title from Flatiron School homepage"""
    headers = {'user-agent': 'my-app/0.0.1'}
    html = requests.get("https://flatironschool.com/", headers=headers)
    doc = BeautifulSoup(html.text, 'html.parser')
    
    # Get the page title
    title = doc.select('title')
    if title:
        return title[0].get_text().strip()
    return None

def scrape_all_headings():
    """Scrape all h1, h2, h3 headings from the homepage"""
    headers = {'user-agent': 'my-app/0.0.1'}
    html = requests.get("https://flatironschool.com/", headers=headers)
    doc = BeautifulSoup(html.text, 'html.parser')
    
    # Get all headings
    headings = doc.select('h1, h2, h3')
    heading_texts = []
    
    for heading in headings:
        text = heading.get_text().strip()
        if text:  # Only add non-empty headings
            heading_texts.append(f"{heading.name.upper()}: {text}")
    
    return heading_texts[:10]  # Return first 10 headings

def scrape_links():
    """Scrape navigation links from the homepage"""
    headers = {'user-agent': 'my-app/0.0.1'}
    html = requests.get("https://flatironschool.com/", headers=headers)
    doc = BeautifulSoup(html.text, 'html.parser')
    
    # Get navigation links
    nav_links = doc.select('nav a')
    links = []
    
    for link in nav_links[:5]:  # First 5 nav links
        text = link.get_text().strip()
        href = link.get('href', '')
        if text:
            links.append(f"{text} -> {href}")
    
    return links

if __name__ == "__main__":
    print("=== Beautiful Soup Web Scraping Demo ===")
    
    print("\n1. Page Title:")
    title = scrape_page_title()
    if title:
        print(title)
    
    print("\n2. First 10 Headings:")
    headings = scrape_all_headings()
    for heading in headings:
        print(f"  {heading}")
    
    print("\n3. Navigation Links:")
    links = scrape_links()
    for link in links:
        print(f"  {link}")