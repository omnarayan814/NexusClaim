import urllib.request

data = b'------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="file"; filename="test.txt"\r\nContent-Type: text/plain\r\n\r\nTest claim data\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--\r\n'

req = urllib.request.Request('http://127.0.0.1:8000/api/process', data=data, method='POST')
req.add_header('Content-Type', 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW')

try:
    res = urllib.request.urlopen(req)
    print(res.status, res.read())
except urllib.error.HTTPError as e:
    print('ERROR:', e.code, e.read().decode())
