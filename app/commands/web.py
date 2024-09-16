import webbrowser

def open_website(url):
    if not url.startswith('http'):
        url = 'http://' + url
    webbrowser.open(url)
    return f"Opening {url}"

def search_web(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    return f"Searching for {query} on the web"
