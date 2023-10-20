% rebase('base_logged_in.tpl', title='Edit Review')

<h2>Edit Your Review</h2>

<form action="/reviews/{{review.id}}/edit" method="post">
    <label for="review_text">Review:</label>
    <textarea id="review_text" name="review_text" rows="4" cols="50">{{review.review_text}}</textarea>
    <input type="submit" name="save" value="Save Draft">
    <input type="submit" name="publish" value="Publish Review">
</form>
