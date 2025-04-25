# Django REST Framework (DRF) 

## What is an API?

An API, or Application Programming Interface, allows different software systems to communicate with each other. It acts like a bridge between two programs, often between a client (like a web browser or mobile app) and a server (where the data lives). A good example is when a user views Instagram reels. The reels are fetched using an API that communicates between the app on your phone and Instagram’s server.

An API can connect not only computers, but also different programming languages or environments. It abstracts the complexity of server logic and gives a simple interface to the client.

## Why Should APIs Be Properly Designed?

A well-designed API ensures users do not directly see backend errors or raw code messages. Instead, it returns meaningful and user-friendly error messages. This improves the user experience and avoids potential security issues. It also makes it easier for developers and teams to collaborate, especially when building frontend and backend systems separately.

A properly designed API is also scalable, easier to maintain, and safer against attacks such as SQL injections or unauthorized data access.

## Common Use Cases of APIs

APIs are used in almost every modern application. Examples include loading videos on YouTube, posting a tweet on Twitter, searching for content on a website, or submitting a form on an e-commerce app. Each of these features communicates with the backend using APIs to fetch or send data.

## Understanding Client-Server Architecture

In this architecture, the client, which is usually a browser like Google Chrome or Firefox, sends a request to the server. The server processes this request and sends a response back to the client. This interaction happens through APIs. The client never talks directly to the database or business logic — it always uses APIs.

## REST API Principles

### Statelessness

REST APIs are stateless, meaning each request is treated independently. The server does not remember any data from previous requests. If a user searches for something and repeats the search again, the server treats it as a new search.

### Uniform Interface

A uniform interface means that the API endpoints follow a consistent structure and behavior. For example, all resources should follow similar patterns like `/api/books/`, and support methods such as GET, POST, PUT, and DELETE.

### Resource-Based

In REST APIs, data is treated as resources, and these resources are exchanged between client and server in formats like JSON or XML. Both sides should agree on the format to ensure smooth communication.

### Self-Descriptive Messages

Every response from the server should be self-explanatory so that any developer using the API can understand it. This helps third-party developers or frontend engineers who are not familiar with the backend logic.

## Comparison of API Protocols

- REST is based on resources and uses standard HTTP methods like GET, POST, PUT, DELETE.
- GraphQL allows clients to specify exactly what data they need, avoiding over-fetching or under-fetching.
- SOAP is an older protocol that uses only XML for data exchange.
- gRPC, developed by Google, allows calling functions directly without defining explicit endpoints, often used for microservices.

## What is an Endpoint?

An endpoint is the part of the URL that identifies a resource. For example, in `http://127.0.0.1:8000/api/books/`, "api/books" is the endpoint. It defines what data or service is being requested from the server.

Endpoints should use nouns and verbs logically. When referring to a collection of resources, plural nouns should be used.

## HTTP Methods and Their Purpose

- GET: Used to retrieve data from the server.
- POST: Used to send new data to the server.
- PUT: Used to update existing data completely.
- PATCH: Used to update a part of the existing data.
- DELETE: Used to delete data from the server.
- OPTIONS: Used to list allowed methods for a resource.

## HTTP Status Codes

- 200 (OK): Request was successful.
- 201 (Created): A new resource was successfully created.
- 204 (No Content): Request was successful but returned no content.
- 301 (Moved Permanently): The resource has moved to a new URL permanently.
- 302 (Found): Temporary redirection.
- 400 (Bad Request): The request was not valid.
- 401 (Unauthorized): Authentication credentials are missing or invalid.
- 403 (Forbidden): The user is not allowed to access the resource.
- 404 (Not Found): The requested resource was not found.
- 405 (Method Not Allowed): The method used is not allowed for the endpoint.
- 409 (Conflict): The request could not be completed due to a conflict.
- 410 (Gone): The resource was deleted and is no longer available.
- 422 (Unprocessable Entity): Data format is wrong or required fields are missing.
- 429 (Too Many Requests): Too many requests from a single client.
- 500 (Internal Server Error): The server encountered an error.
- 502 (Bad Gateway): A gateway or proxy server received an invalid response.
- 503 (Service Unavailable): The server is currently unavailable.
- 504 (Gateway Timeout): A timeout occurred while waiting for the server to respond.

## Error Message Structure

Every error response should include:
- A status code (like 403)
- A message (like "Unauthorized")
- A clear description (explaining the error)
- A suggested action (telling the user what to fix)

## API Throttling

Throttling limits how many requests a user or client can make in a specific time. For example, if a limit is set to 10 requests per minute, sending more than 10 will return a 429 error.

## Pagination Overview

When a dataset is large, pagination helps divide it into pages.

### Types of Pagination:

1. **Page Number Pagination**:  
   Client specifies a page number. Example: `/api/books/?page=2`

2. **Limit Offset Pagination**:  
   Client specifies how many records to retrieve and from which point.  
   Example: `/api/books/?limit=10&offset=20`

3. **Custom Pagination**:  
   You can create a pagination class that fits specific needs like dynamic page sizes or custom formats.

## What is Filtering?

Filtering is used to retrieve a subset of data based on specific criteria. For instance, if you want books by a specific author, a filter helps you get just those records.

### Types of Filtering:

1. **Basic Field Filtering**  
   You can filter based on exact fields.  
   Example: `/api/books/?genre=fiction`

2. **Custom Filtering**  
   You can define custom logic inside views or serializers to filter based on more complex rules.

3. **Search Filtering**  
   Search across multiple fields using a keyword.  
   Example: `/api/books/?search=python`

4. **Ordering Filtering**  
   Sort results based on a field.  
   Example: `/api/books/?ordering=price` or `/api/books/?ordering=-price`

5. **Advanced Filtering (Using DjangoFilterBackend)**  
   Add `django-filter` to your project to support advanced expressions like `lt`, `gt`, `contains`, etc.  
   Example: `/api/books/?price__lt=100`

6. **Case-Insensitive Filtering**  
   Use `lookup_expr='iexact'` to perform case-insensitive matching on fields.

## Serialization and Deserialization

Serialization is converting Python data like querysets or models into formats like JSON that can be shared via APIs. Deserialization is the opposite process — taking JSON data and converting it into Django objects that can be saved or validated.

## ModelSerializer

A ModelSerializer is a type of serializer that automatically maps Django model fields to API fields, reducing the amount of code needed to create a serializer.

## DRF Mixins

Mixins are reusable classes that add behavior to your views:

- ListModelMixin: Allows listing all objects.
- CreateModelMixin: Allows creating a new object.
- RetrieveModelMixin: Allows fetching a single object.
- UpdateModelMixin: Allows updating an object.
- DestroyModelMixin: Allows deleting an object.

These mixins can be combined with GenericAPIView to build custom views.

## GenericAPIView

This is a foundational view in DRF. It supports request handling like GET, POST, PUT, and DELETE and is often used with mixins for cleaner code.

## API Deprecation

When an API becomes outdated or replaced by a newer version, it is marked as deprecated. This lets developers know they should migrate to the new version.

## Security Measures

- Avoid using characters like `<` and `>` to prevent Cross-Site Scripting (XSS).
- Sanitize inputs to prevent SQL injection using terms like `and`, `or`, and symbols.
