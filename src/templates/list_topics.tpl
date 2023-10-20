% rebase('base_logged_in.tpl', title='List Topics')

<h2>All Topics</h2>
<ul>
% for topic in topics:
    <li>
        {{topic.name}}: {{topic.description}}
        <a href='/topics/{{topic.id}}/create_review'>Create Review</a>
        <ul>
            % for review in reviews.get(topic.id, []):
                <li>{{review.review_text}}</li>
            % end
        </ul>
    </li>
% end
</ul>