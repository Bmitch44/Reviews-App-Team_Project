% rebase('base_logged_in.tpl', title='Dashboard')

<h2>Following</h2>
<ul>
% for topic in topics:
    <li>
        {{topic.name}}: {{topic.description}} <br>
        <a href='/topics/{{topic.id}}/create_review'>Create Review</a> 
        <br>
        <form action="/topics/{{topic.id}}/follow" method="post">
            <button type="submit">{{ 'Following' if topic.id in user.following else 'Follow' }}</button>
        </form>
        <ul>
            % for review in reviews.get(topic.id, []):
                <li>
                {{review.review_text}}
                <!-- Effort Rating -->
                <p>Effort expended on this topic: {{review.ratings[0]}}/10</p>

                <!-- Communication Rating -->
                <p>Communication with team: {{review.ratings[1]}}/10</p>

                <!-- Participation Rating -->
                <p>Participation in critical reviews: {{review.ratings[2]}}/10</p>

                <!-- Attendance Rating -->
                <p>Attending team meetings: {{review.ratings[3]}}/10</p>

                <!-- Commment Link -->
                <form action="/reviews/{{review.id}}/comment" method="post">
                    <label for="review_comment">Comment:</label>
                    <textarea id="review_comment" name="review_comment" rows="1" cols="25"></textarea>
                    <input type="submit" name="comment" value="Comment">
                </form>
                <br>
                <ul>
                    % for comment in review.comments:
                         <li>
                        {{comment.get("user_id", "")}}
                        {{comment.get("comment", "")}}
                        </li>
                    % end
                </ul>
                </li>
            % end
        </ul>
    </li>
% end
</ul>