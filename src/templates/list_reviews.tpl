% rebase('base_logged_in.tpl', title='List Reviews')

<h2>Your Reviews</h2>

<!-- Filter Buttons -->
<form action="/reviews" method="post">
    <input type="submit" name="filter" value="all" {{ 'checked' if filter_criteria == 'all' else '' }}> All 
    <input type="submit" name="filter" value="published" {{ 'checked' if filter_criteria == 'published' else '' }}> Published 
    <input type="submit" name="filter" value="draft" {{ 'checked' if filter_criteria == 'draft' else '' }}> Draft
</form>

<!-- List Reviews -->
<ul>
% for review in reviews:
    <li>
        {{review.review_text}}
        % if review.status == 'draft':
            <a href="/reviews/{{review.id}}/edit">Edit</a>
        % end
    </li>
% end
</ul>
