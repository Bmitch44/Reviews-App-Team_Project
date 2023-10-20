% rebase('base_logged_in.tpl', title='Create Review')

<h2>Create Review for Topic ID: {{topic_id}}</h2>
<form action="/topics/{{topic_id}}/create_review" method="post">
    <label for="review_text">Review:</label>
    <textarea id="review_text" name="review_text" rows="4" cols="50" required></textarea>
    <input type="submit" name="save" value="Save Draft">
    <input type="submit" name="publish" value="Publish Review">
</form>
