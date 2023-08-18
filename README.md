
# URL Shortener using Fast API

Focused on utilizing FastAPI features, this compact project aimed to create a URL shortener.
This application allows users to convert long URLs into concise, shareable short links.




## Features

- Allow users to submit a long URL.
- Generate a unique and short identifier for the given long URL.
- Return the generated short URL to the user.
- error handling for scenarios where the short URL is not found

## Technologies used

- FastAPI: FastAPI is the chosen framework for building the web application. It enables efficient and rapid development of APIs
- HTTPException: HTTPException is employed to handle exceptions and errors.
- Pydantic: Pydantic is being used for data validation and parsing
- String and Random Modules: The string and random modules are utilized to generate unique and short identifiers for the shortened URLs.
- Status Module: The status module is employed to manage and communicate the HTTP status codes in responses.


## Installation

1) Install the project using the git command

```bash
git clone https://github.com/a7k4a6s3h0/URL_Shortener_Fastapi.git
```

2) Then access to the Project Directory using cd command

```bash
cd your_directory_name
```

3) Install dependencies

```bash
pip install -r requirements.txt
```
4) run the project 

```bash
uvicorn main_file:app --reload
```
The server will start, and you'll see output indicating that the FastAPI app is running and listening for incoming requests.

5) Shutdown the Server:
To stop the FastAPI server, press Ctrl+C in the terminal where it's running.
    
## Documentation

API Endpoints
Shorten URL
Request
- Method: POST
- Endpoint: /shorten
- Request Body:

```bash
{
    "long_url": "https://www.example.com/very/long/url/to/be/shortened"
}
```

Response
- Status Code: 200 OK
- Response Body:

```bash
{
    "status": 200,
    "message": "success",
    "short_url": "AbCdEf"
}
```

Error Response:
- Status Code: 404 Not Found
- Response Body:

```bash
{
    "detail": "shorten url not found"
}
```

Redirect to URL
Request
- Method: GET
- Endpoint: /{short_url}
Response
- Status Code: 200 OK (on successful redirect)
- Response Body:

```bash
{
    "status": 200,
    "message": "success",
    "redirect_url": "https://www.example.com/very/long/url/to/be/shortened"
}
```
Error Response:
- Status Code: 404 Not Found
- Response Body:

```bash
{
    "detail": "URL not found."
}
```




## Usage
- Shorten a URL: Send a POST request to /shorten with the long_url you want to shorten. The response will include the generated short URL.

- Redirect to Original URL: Use a web browser or any HTTP client to access the shortened URL by making a GET request to /{short_url}. You will be redirected to the original long URL.

## Important Notes
- The generated short URLs are case-sensitive and consist of a combination of letters (both lowercase and uppercase) and digits.

- The project maintains an in-memory dictionary url_mapping to store the mapping of short URLs to original long URLs. This data is not persistent and will be lost if the application is restarted.

## Error Handling
- The project utilizes FastAPI's built-in error handling mechanisms to provide appropriate error responses when encountering invalid requests or URLs that do not exist.

## Conclusion
- The URL Shortener project is a simple yet effective way to convert and manage long URLs, making them easier to share and access. It leverages FastAPI and Pydantic to provide a robust and efficient API-based solution.






