from responsecodes.responsecodes import is_successful_response
from responsecodes.responsecodes import is_client_error_response
from responsecodes.responsecodes import is_server_error_response
from responsecodes.responsecodes import get_response_by_code
from responsecodes.responsecodes import get_all_categories

def test_get_response_by_code():
    assert get_response_by_code(200)=={'code': 200,
    'category': 'Successful responses',
    'short_description': '200 OK',
    'description': 'The request succeeded. The result meaning of "success" depends on the HTTP method:'}

    assert get_response_by_code(204)=={'code': 204,
    'category': 'Successful responses',
    'short_description': '204 No Content',
    'description': 'There is no content to send for this request, but the headers may be useful.  The user agent may update its cached headers for this resource with the new ones.'}

def test_get_all_categories():
    assert get_all_categories() == ['1xx informational response – the request was received, continuing process',
    '2xx successful – the request was successfully received, understood, and accepted',
    '3xx redirection – further action needs to be taken in order to complete the request',
    '4xx client error – the request contains bad syntax or cannot be fulfilled',
    '5xx server error – the server failed to fulfil an apparently valid request']

def test_is_successful_response():
    # Test successful response codes
    assert is_successful_response(200) == True
    assert is_successful_response(204) == True
    assert is_successful_response(299) == True

    # Test non-successful response codes
    assert is_successful_response(100) == False
    assert is_successful_response(300) == False
    assert is_successful_response(400) == False

def test_is_client_error_response():
    # Test client error response codes
    assert is_client_error_response(400) == True
    assert is_client_error_response(404) == True
    assert is_client_error_response(499) == True

    # Test non-client error response codes
    assert is_client_error_response(200) == False
    assert is_client_error_response(300) == False
    assert is_client_error_response(500) == False

def test_is_server_error_response():
    # Test server error response codes
    assert is_server_error_response(500) == True
    assert is_server_error_response(503) == True
    assert is_server_error_response(599) == True

    # Test non-server error response codes
    assert is_server_error_response(200) == False
    assert is_server_error_response(300) == False
    assert is_server_error_response(400) == False

if __name__ == "__main__":
    test_get_response_by_code()
    test_get_all_categories()
    test_is_successful_response()
    test_is_server_error_response()
    test_is_client_error_response()

