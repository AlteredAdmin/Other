import feedparser
import sqlite3

def parse_rss(rss_url):
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Connect to the database
    conn = sqlite3.connect("parsed_entries.db")
    c = conn.cursor()

    # Create the table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS parsed_entries (id INTEGER PRIMARY KEY, link TEXT)''')

    # Iterate through the entries in the feed
    for entry in feed.entries:
        # Check if the entry has been parsed before
        c.execute("SELECT * FROM parsed_entries WHERE link=?", (entry.link,))
        if c.fetchone() is None:
            # If the entry has not been parsed, insert it into the database
            c.execute("INSERT INTO parsed_entries (link) VALUES (?)", (entry.link,))
            # Process the entry
            print(f"Processing entry: {entry.title}")
        else:
            # If the entry has already been parsed, skip it
            print(f"Skipping entry: {entry.title}")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage
parse_rss("http://www.example.com/rss")
