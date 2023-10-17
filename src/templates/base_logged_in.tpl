<!DOCTYPE html>
<html>
    <head>
        <title>{{title or 'Default Title'}}</title>
        <link rel="stylesheet" href="/static/css/styles.css">
    </head>
    <body>
        <div class="navbar">
            <a href="/dashboard">Dashboard</a>
            <a href="/create_topic">Create Topic</a>
            <a href="/list_topics">All Topics</a>
            <a href="/list_reviews">My Reviews</a>
            <a href="/logout">Logout</a>
        </div>
        {{!base}}
    </body>
</html>