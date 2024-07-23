from bs4 import BeautifulSoup

html_doc = """ 
<!DOCTYPE html>
<html lang="en">
  <head><meta charset="UTF-8" />
    <link rel="icon" type="image/png" href="/assets/logo-gDOXtA9d.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>whoami - Prasanna Acharya</title>
    <script type="module" crossorigin src="/assets/index-B4ZfT_8j.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-D8RjI4sC.css">
  </head>
  <body><div id="root"></div></body>
</html> 
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())