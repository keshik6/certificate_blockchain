"""Created by Keshik"""
"""https://docs.python.org/3/library/ssl.html#module-ssl
https://docs.python.org/3/library/socket.html"""

import socket,ssl,hashlib
def getcert(addr, port, timeout=2):
    try:
        """Connect to a TCP service listening on the Internet address (a 2-tuple (host, port)), and return the socket object"""
        with socket.create_connection((addr,port), timeout=timeout) as sock:
            """Return a new SSLContext object with default settings for the given purpose."""
            context = ssl.create_default_context()
            
            """Wrap the existing Python socket sock and return an SSLSocket object.
            The returned SSL socket is tied to the context, its settings and certificates"""
            with context.wrap_socket(sock, server_hostname=addr) as sslsock:
                """If there is no certificate for the peer on the other end of the connection, return None. 
                If the SSL handshake hasn’t been done yet, raise ValueError."""
                return sslsock.getpeercert(),sslsock.getpeercert(True)
    except Exception as e:
        pass
    
"""Print the entire ssl object"""
URL = 'sutd.edu.sg'
result = getcert(URL, 443)


"""Print the organization name"""
if (result != None):
    print(result[0])
    print()
    print(result[0]['subject'][3][0][0] + " : " + result[0]['subject'][3][0][1])

    """Print the thumbprint (Hexadecimal representation of the public address)"""
    thumb_sha1 = hashlib.sha1(result[1]).hexdigest()
    print("THUMBPRINT SHA1: " + thumb_sha1)
else:
    print("Website corresponding to " + URL + " is not secure or doesn't exist")

    


