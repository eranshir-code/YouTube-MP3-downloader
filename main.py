#!/usr/bin/env python3
"""
Enhanced web scraping tool with multiple parsing capabilities
"""

import urllib.request
import urllib.error
import json
import re
import os
import sys
from datetime import datetime


def fetch_url(url):
    """Fetch content from a URL using urllib"""
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return {
                'status_code': response.status,
                'content': response.read(),
                'headers': dict(response.headers)
            }
    except urllib.error.URLError as e:
        print(f"Error fetching {url}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def get_json_data(url):
    """Fetch and parse JSON data from an API"""
    response = fetch_url(url)
    if response:
        try:
            return json.loads(response['content'].decode('utf-8'))
        except (ValueError, json.JSONDecodeError):
            print("Response is not valid JSON")
            return None
    return None


def extract_title(html):
    """Extract title from HTML using regex"""
    match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else None


def extract_h1_tags(html):
    """Extract all h1 tags from HTML using regex"""
    matches = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
    return [re.sub(r'<[^>]+>', '', match).strip() for match in matches]


def extract_h2_tags(html):
    """Extract all h2 tags from HTML using regex"""
    matches = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.IGNORECASE | re.DOTALL)
    return [re.sub(r'<[^>]+>', '', match).strip() for match in matches]


def extract_links(html):
    """Extract all links from HTML"""
    matches = re.findall(r'<a[^>]+href=["\'](.*?)["\'][^>]*>(.*?)</a>', html, re.IGNORECASE | re.DOTALL)
    return [{'url': url, 'text': re.sub(r'<[^>]+>', '', text).strip()} for url, text in matches]


def extract_images(html):
    """Extract all image sources from HTML"""
    matches = re.findall(r'<img[^>]+src=["\'](.*?)["\']', html, re.IGNORECASE)
    return matches


def extract_paragraphs(html):
    """Extract all paragraph text from HTML"""
    matches = re.findall(r'<p[^>]*>(.*?)</p>', html, re.IGNORECASE | re.DOTALL)
    return [re.sub(r'<[^>]+>', '', p).strip() for p in matches if re.sub(r'<[^>]+>', '', p).strip()]


def extract_meta_tags(html):
    """Extract meta tags from HTML"""
    meta_tags = {}
    matches = re.findall(r'<meta[^>]+name=["\'](.*?)["\'][^>]+content=["\'](.*?)["\']', html, re.IGNORECASE)
    for name, content in matches:
        meta_tags[name] = content
    return meta_tags


def scrape_webpage(url, full_analysis=False):
    """Scrape and parse HTML content with optional full analysis"""
    response = fetch_url(url)
    if response:
        html = response['content'].decode('utf-8', errors='ignore')
        data = {
            'url': url,
            'status_code': response['status_code'],
            'title': extract_title(html),
            'h1_tags': extract_h1_tags(html),
            'fetched_at': datetime.now().isoformat()
        }

        if full_analysis:
            data['h2_tags'] = extract_h2_tags(html)
            data['links'] = extract_links(html)[:50]  # Limit to first 50 links
            data['images'] = extract_images(html)[:20]  # Limit to first 20 images
            data['paragraphs'] = extract_paragraphs(html)[:10]  # Limit to first 10 paragraphs
            data['meta_tags'] = extract_meta_tags(html)
            data['content_length'] = len(html)

        return data
    return None


def save_to_file(data, filename):
    """Save scraped data to JSON file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n✓ Data saved to: {filename}")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False


def main():
    """Main function demonstrating web access"""
    print("Enhanced Web Scraping Tool")
    print("=" * 60)

    # Check for command-line arguments
    if len(sys.argv) > 1:
        url = sys.argv[1]
        full_mode = '--full' in sys.argv
        save_mode = '--save' in sys.argv

        print(f"\nFetching: {url}")
        print(f"Full analysis: {full_mode}")
        print(f"Save to file: {save_mode}")
        print("-" * 60)

        page_data = scrape_webpage(url, full_analysis=full_mode)
        if page_data:
            print(f"\n✓ Successfully fetched {url}")
            print(f"Status Code: {page_data['status_code']}")
            print(f"Title: {page_data['title']}")
            print(f"H1 tags found: {len(page_data['h1_tags'])}")

            if full_mode:
                print(f"H2 tags found: {len(page_data.get('h2_tags', []))}")
                print(f"Links found: {len(page_data.get('links', []))}")
                print(f"Images found: {len(page_data.get('images', []))}")
                print(f"Paragraphs found: {len(page_data.get('paragraphs', []))}")

            if save_mode:
                filename = f"scraped_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                save_to_file(page_data, filename)

            print("\n" + "=" * 60)
        return

    # Default demo mode
    print("\nRunning in demo mode...")
    print("\nUsage: python3 main.py <url> [--full] [--save]")
    print("  --full : Extract all content (links, images, paragraphs, etc.)")
    print("  --save : Save results to JSON file")
    print("\n" + "-" * 60)

    # Example 1: Basic webpage fetch
    print("\n1. Fetching ynet.com (basic mode)...")
    response = fetch_url("http://www.ynet.co.il")
    if response:
        print(f"✓ Status Code: {response['status_code']}")
        print(f"✓ Content Length: {len(response['content'])} bytes")
        print(f"✓ Content-Type: {response['headers'].get('Content-Type', 'N/A')}")

    # Example 2: JSON API
    print("\n2. Fetching JSON data from API...")
    data = get_json_data("https://jsonplaceholder.typicode.com/todos/1")
    if data:
        print(f"✓ JSON Data:")
        print(f"  - ID: {data.get('id')}")
        print(f"  - Title: {data.get('title')}")
        print(f"  - Completed: {data.get('completed')}")

    # Example 3: Full HTML scraping
    print("\n3. Scraping ynet.com (full analysis)...")
    page_data = scrape_webpage("http://www.ynet.co.il", full_analysis=True)
    if page_data:
        print(f"✓ Page Title: {page_data['title']}")
        print(f"✓ H1 tags: {len(page_data['h1_tags'])}")
        if page_data['h1_tags']:
            for i, h1 in enumerate(page_data['h1_tags'][:3], 1):
                print(f"    {i}. {h1[:80]}")

        if page_data.get('links'):
            print(f"✓ Links found: {len(page_data['links'])}")
            print(f"    First 3 links:")
            for i, link in enumerate(page_data['links'][:3], 1):
                print(f"    {i}. {link['text'][:50]} -> {link['url'][:50]}")

        if page_data.get('images'):
            print(f"✓ Images found: {len(page_data['images'])}")

        # Save the full analysis
        save_to_file(page_data, "ynet_analysis.json")

    print("\n" + "=" * 60)
    print("Demo completed!")
    print("\nTip: Run with a URL to scrape any website:")
    print("     python3 main.py https://example.com --full --save")


if __name__ == "__main__":
    main()
