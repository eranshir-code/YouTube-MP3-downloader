#!/usr/bin/env python3
"""
Enhanced offline demo showing HTML parsing with local sample data
"""

import json
import re
import sys
from datetime import datetime


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


def extract_paragraphs(html):
    """Extract all paragraph text from HTML"""
    matches = re.findall(r'<p[^>]*>(.*?)</p>', html, re.IGNORECASE | re.DOTALL)
    return [re.sub(r'<[^>]+>', '', p).strip() for p in matches if re.sub(r'<[^>]+>', '', p).strip()]


def extract_articles(html):
    """Extract article tags from HTML"""
    matches = re.findall(r'<article>(.*?)</article>', html, re.IGNORECASE | re.DOTALL)
    return matches


def scrape_local_file(filename, full_analysis=False):
    """Read and parse local HTML file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()

        data = {
            'source': filename,
            'title': extract_title(html),
            'h1_tags': extract_h1_tags(html),
            'size': len(html),
            'analyzed_at': datetime.now().isoformat()
        }

        if full_analysis:
            data['h2_tags'] = extract_h2_tags(html)
            data['links'] = extract_links(html)
            data['paragraphs'] = extract_paragraphs(html)
            data['articles'] = len(extract_articles(html))

        return data
    except FileNotFoundError:
        print(f"✗ File not found: {filename}")
        return None


def save_to_file(data, filename):
    """Save analyzed data to JSON file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n✓ Data saved to: {filename}")
        return True
    except Exception as e:
        print(f"✗ Error saving file: {e}")
        return False


def main():
    """Main function demonstrating HTML parsing"""
    print("Web Scraping Demo - Offline Mode")
    print("=" * 60)

    # Check for command-line arguments
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        full_mode = '--full' in sys.argv
        save_mode = '--save' in sys.argv

        print(f"\nAnalyzing: {filename}")
        print(f"Full analysis: {full_mode}")
        print(f"Save to file: {save_mode}")
        print("-" * 60)

        data = scrape_local_file(filename, full_analysis=full_mode)
        if data:
            print(f"\n✓ Successfully analyzed {filename}")
            print(f"File Size: {data['size']} bytes")
            print(f"Title: {data['title']}")
            print(f"H1 tags: {len(data['h1_tags'])}")

            if full_mode:
                print(f"H2 tags: {len(data.get('h2_tags', []))}")
                print(f"Links: {len(data.get('links', []))}")
                print(f"Paragraphs: {len(data.get('paragraphs', []))}")
                print(f"Articles: {data.get('articles', 0)}")

            if save_mode:
                output_file = f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                save_to_file(data, output_file)

        return

    # Default demo mode
    print("\nRunning in demo mode...")
    print("\nUsage: python3 demo_offline.py <file.html> [--full] [--save]")
    print("  --full : Extract all content (links, paragraphs, etc.)")
    print("  --save : Save results to JSON file")
    print("\n" + "-" * 60)

    # Parse local sample HTML with full analysis
    print("\n1. Analyzing sample_ynet.html (full analysis)...")
    data = scrape_local_file("sample_ynet.html", full_analysis=True)

    if data:
        print(f"\n✓ File Size: {data['size']} bytes")
        print(f"✓ Page Title: {data['title']}")

        print(f"\n✓ Found {len(data['h1_tags'])} H1 tags:")
        for i, h1 in enumerate(data['h1_tags'], 1):
            print(f"    {i}. {h1}")

        if data.get('links'):
            print(f"\n✓ Found {len(data['links'])} links")

        if data.get('paragraphs'):
            print(f"✓ Found {len(data['paragraphs'])} paragraphs")

        print(f"✓ Found {data.get('articles', 0)} articles")

        # Save the analysis
        save_to_file(data, "sample_analysis.json")

    # Demo: JSON data handling
    print("\n" + "=" * 60)
    print("\n2. Demonstrating JSON API data handling...")

    sample_json = {
        "id": 1,
        "title": "Sample news item from Ynet",
        "author": "Reporter Name",
        "category": "News",
        "content": "This is sample news content in Hebrew: חדשות",
        "published": "2024-12-29",
        "tags": ["technology", "Israel", "news"]
    }

    print(f"\n✓ JSON Data:")
    print(json.dumps(sample_json, indent=2, ensure_ascii=False))

    # Save JSON example
    save_to_file(sample_json, "sample_json_data.json")

    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("\n✓ Features demonstrated:")
    print("  • HTML title extraction")
    print("  • H1/H2 tag parsing")
    print("  • Link extraction")
    print("  • Paragraph extraction")
    print("  • Article counting")
    print("  • JSON data handling")
    print("  • File saving")
    print("\nNote: When internet access is available, main.py will")
    print("      fetch live data from ynet.com and other websites")


if __name__ == "__main__":
    main()
