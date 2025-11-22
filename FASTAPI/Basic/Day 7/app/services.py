from typing import Optional
from .schemas import Comment, CommentCreate, Post, PostCreate

posts: list[Post] = [
    Post(id=1, title="Launch checklist", body="Plan the first release and gather feedback.", comments=[Comment(id=1, author="team", content="Looks good.")])
]

_next_post_id = 2
_next_comment_id = 2


def get_all_posts() -> list[Post]:
    return posts


def get_post(post_id: int) -> Optional[Post]:
    return next((item for item in posts if item.id == post_id), None)


def add_post(payload: PostCreate) -> Post:
    global _next_post_id
    post = Post(id=_next_post_id, **payload.model_dump())
    posts.append(post)
    _next_post_id += 1
    return post


def add_comment(post_id: int, payload: CommentCreate) -> Optional[dict]:
    global _next_comment_id
    post = get_post(post_id)
    if post is None:
        return None
    comment = Comment(id=_next_comment_id, **payload.model_dump())
    post.comments.append(comment)
    _next_comment_id += 1
    return {"post_id": post_id, "comment": comment}
