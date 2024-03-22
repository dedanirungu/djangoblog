# Blog Test Project

This is a test project for a blog application.

## Installation

1. Clone the repository: `git clone https://github.com/dedanirungu/djangoblog.git`
2. Navigate to the project directory: `cd djangoblog`

## Usage by Docker

Build the Docker image:

```
docker build -t my_django_app .
```

Run the Docker container:

```
docker run -d -p 8000:8000 my_django_app
```


## Usage by installation

1. Install the dependencies: `pip install -r requirements.txt`
2. Start the development server: `python manage.py runserver`
3. Open your web browser and visit `http://localhost:8000` to view the blog.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).