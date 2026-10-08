# Responsive Portfolio Website Alexa

### Responsive Portfolio Website Alexa

- Responsive Personal Portfolio Website Using HTML CSS & JavaScript
- Smooth scrolling in each section.
- Includes a light and dark mode.
- Developed first with the Mobile First methodology, then for desktop.
- Compatible with all mobile devices and with a beautiful and pleasant user interface.


[![image.png](https://i.postimg.cc/5tXvYNps/image.png)](https://postimg.cc/5HMjDJhz)

## Run locally
Requirements: Podman 4 or later with a compose provider (or Docker Desktop).

1. git clone https://github.com/gthanh2404/Portfolio.git
2. cd Portfolio
3. cp .env.example .env        # then set DB_PASSWORD (letters and digits only)
4. podman compose up --build
5. Open http://localhost:3000  — database check: http://localhost:3000/health/db

Stop:                           podman compose down

Reset the database (data lost): podman compose down -v
