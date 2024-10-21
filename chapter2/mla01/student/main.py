import requests
def validate_url(url):
    """Validates the given URL string.

    Arguments:
    url -- String, A valid URL should be of the form <Protocol>://<hostname>/<fileinfo>

    Protocol = [http, https, ftp]
    Fileinfo = [.html, .csv, .docx]
    """
    # Step 1: Create lists for valid protocols and file extensions
    valid_protocols = ["http", "https", "ftp"]
    valid_fileinfo = [".html", ".csv", ".docx"]

    # Step 2: Split the URL into components
    try:
        # Split the URL at '://'
        protocol, rest = url.split("://")
        
        # Split the remaining part at the last '/'
        hostname, fileinfo = rest.rsplit("/", 1)
    except ValueError:
        return False  # Invalid URL format

    # Step 3: Check if the protocol is valid
    is_valid_protocol = protocol in valid_protocols

    # Step 4: Check if the fileinfo has a valid extension
    is_valid_fileinfo = any(fileinfo.endswith(ext) for ext in valid_fileinfo)

    # Step 5: Return True if both checks are passed; otherwise, return False
    return is_valid_protocol and is_valid_fileinfo

if __name__ == '__main__':
    url = input("Enter a URL: ")
    print(validate_url(url))
