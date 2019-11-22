def generate_affiliation_link(url):
    urlsplit = url.split("/")
    id = urlsplit[urlsplit.index("dp") + 1]
    return f"http://www.amazon.com/dp/{id}/?tag=pyb0f-20"
