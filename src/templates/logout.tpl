% rebase('base_logged_in.tpl', title='Logout')
<link rel="stylesheet" href="/static/css/login.css">
<form action="/logout" method="post">
    <label>Confirm logout?</label>
    <button type="submit">Logout</button>
</form>