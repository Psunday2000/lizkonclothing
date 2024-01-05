# Lizkon Clothing Laravel Project

Welcome to Lizkon Clothing, a Laravel-based web application for clothing recommendations.

## Setup

### Prerequisites

-   PHP (>= 7.4)
-   Composer
-   MySQL

### Installation

1. Clone the repository:

    ```bash
    git clone <https://github.com/psunday2000/lizkon-clothing.git>
    cd lizkon-clothing
    ```

2. Install dependencies:

    ```bash
    composer install
    ```

3. Configure the environment:

    ```bash
    cp .env.example .env
    ```

    Update the `.env` file with your database configuration:

    ```env
    APP_NAME=LizkonClothing
    DB_CONNECTION=mysql
    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_DATABASE=lizkonclothing
    DB_USERNAME=your_database_username
    DB_PASSWORD=your_database_password
    ```

4. Generate the application key:

    ```bash
    php artisan key:generate
    ```

5. Run the development server:

    ```bash
    php artisan serve
    ```

    Access your application at [http://localhost:8000](http://localhost:8000).

### Usage

-   Register an account and log in.
-   Explore clothing recommendations personalized for you.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
