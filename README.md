<br />
<p align="center">
  <a href="#">
    <img src=".github/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">NeoNews</h3>

  <p align="center">
    News article websites with multi-language support. Also supports adding articles using an API.
    <br />
  </p>
</p>


[![Product Name Screen Shot][product-screenshot]](#)


### Built With

This project is built using the [Django](https://www.djangoproject.com/) web framework.

## Getting Started

### Prerequisites

You must have python 3.6 or higher installed on your machine.

### Installation

1. Clone the repo

```sh
git clone https://github.com/yxor/neonews.git
```

2. Install the dependencies (this project is only dependant on django)

```sh
pip install -r requirements.txt
```

3. Migrate the database and create the tables

```sh
python manage.py migrate --run-syncdb
```

4. Collect the static files

```sh
python manage.py collectstatic
```

5. Create an admin account

```sh
python manage.py createsuperuser
```

## Usage

Just run the local development server and the website should be available at `localhost:8000`.

```sh
python manage.py runserver
```

**Note**: To add content to the site you can use the admin site app at `/admin`.

## License

Distributed under the MIT License. See `LICENSE` for more information.

[product-screenshot]: .github/social.png
