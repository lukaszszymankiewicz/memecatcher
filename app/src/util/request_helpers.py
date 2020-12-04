import urllib.request


def get_url_content(url: str) -> str:
    """Get url content.

    Attrs:
        url - string representation of site to get content on.

    Returns:
        bytes object representing site content.

    """
    return urllib.request.urlopen(url).read()
