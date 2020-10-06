# Flask URL-Shortener
This app shortened long links

[Live Demo](https://pytamer.herokuapp.com/)

## Features

- Shortens URLs to a default 5-digit prefix using a random character and letter combination.
- Checks if the shortened URL already exists and attempt to re-run the code-generator until it finds an available combination.
- All data is stored in a single PostgreSQL table.
- Case-sensitive. The database distinguishes between upper- and lower-case characters.
- A Stats page lists all the shortened URLs, and shows how many times a target link has been redirected.
- There is a button to automatically copy the shortened URL to clipboard.
- Has an option to use Recaptcha to prevent spambots.

![Screenshot](https://github.com/ioaiy/Flask_URL/blob/master/pytmtk.gif)

