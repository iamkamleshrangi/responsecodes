## HTTP Status Codes

### Table of Contents
1. [Goal](#goal)
2. [Description](#description)
3. [Getting Started](#getting_started)
	1. [Dependencies](#dependencies)
	2. [File Structure](#file_structure)
	3. [Installing](#installation)
	4. [Instructions](#instructions)
4. [License](#license)

<a name="goal"></a>
### Goal
HTTP status codes are three-digit numbers returned by a server in response to a client's request. They provide information about the status of the requested resource or operation, and are typically used by web browsers and other clients to determine how to handle the response.

### Description
HTTP status codes are typically used by clients to determine how to handle the server's response. For example, a web browser might display a 404 Not Found error page if it receives that status code in response to a request for a web page. In addition, HTTP status codes can be used by servers to provide information about the status of an operation. For example, a server might return a 200 OK status code in response to a successful login request, or a 403 Forbidden status code in response to an unauthorized request to access a protected resource.

HTTP status codes are grouped into five categories to provide feedback regarding the requests made by the client.

**Informational responses (100-199):** These are interim responses that indicate that the client's request is being processed. They are not typically seen by users, as they are usually handled automatically by the client.

**Successful responses (200-299):** These indicate that the client's request was successfully processed by the server. The most commonly used status code in this category is 200 OK, which indicates that the request was successful.

**Redirection messages (300-399):** These indicate that the client must take additional action to complete the request. For example, a 301 Moved Permanently response indicates that the requested resource has been permanently moved to a new location.

**Client error responses (400-499):** These indicate that there was an error in the client's request. Common status codes in this category include 404 Not Found, which indicates that the requested resource could not be found, and 403 Forbidden, which indicates that the client does not have permission to access the requested resource.

**Server error responses (500-599):** These indicate that there was an error on the server side. Common status codes in this category include 500 Internal Server Error, which indicates a generic server error, and 503 Service Unavailable, which indicates that the server is temporarily unable to handle the request.

<a name="getting_started"></a>
### Getting Started

<a name="dependencies"></a>
#### Dependencies
* Python 3.8
* Standard set by the source https://httpwg.org.

<a name="file_structure"></a>
#### File Structure
```
responsecodes
|
├── LICENSE
├── README.md
├── responsecodes
│   ├── __init__.py
│   ├── __version__.py
│   └── responsecodes.py
├── setup.py
└── test
    └── test_responsecodes.py
```

<a name="installation"></a>
### Installing

**httpcodes installation**

```console
pip install responsecodes 
```
- OR

```console
$ python -m pip install responsecodes
```

- OR

**Clone the repository **

```console
    > git clone git@github.com:iamkamleshrangi/responsecodes.git
    > cd responsecodes 
    > ..
```
 
<a name="instructions"></a>
#### Instructions
```python

>>> import responsecodes
>>> 
>>> response_code = 200
>>> responsecodes.get_response_by_code(response_code)
{'code': 200,
 'category': 'Successful responses',
 'short_description': '200 OK',
 'description': 'The request succeeded. The result meaning of "success" depends on the HTTP method:'}
>>>
>>> responsecodes.get_all_responses()
'{100: {'code': 100,
  'category': 'Information...'
>>>
>>> responsecodes.get_all_categories()
['1xx informational response – the request was received, continuing process',
 '2xx successful – the request was successfully received, understood, and accepted',
 '3xx redirection – further action needs to be taken in order to complete the request',
 '4xx client error – the request contains bad syntax or cannot be fulfilled',
 '5xx server error – the server failed to fulfil an apparently valid request']
>>>
>>> responsecodes.is_successful_response(response_code)
True
>>> responsecodes.is_client_error_response(response_code)
False
>>> responsecodes.is_server_error_response(response_code)
False
>>> 
>>>
```

### Resources
For more information about HTTP status codes, see the HTTP/1.1 Status Code Definitions specification.
