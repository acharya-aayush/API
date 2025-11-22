from fastapi import APIRouter, HTTPException
from .schemas import CommentCreate, Post, PostCreate
from .services import add_comment, add_post, get_all_posts, get_post

router = APIRouter()

@router.get("/", response_model=list[Post])
def list_posts():
    return get_all_posts()

@router.post("/", response_model=Post, status_code=201)
def create_post(payload: PostCreate):
    return add_post(payload)

@router.get("/{post_id}", response_model=Post)
def read_post(post_id: int):
    post = get_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.get("/{post_id}/comments")
def list_comments(post_id: int):
    post = get_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post.comments

@router.post("/{post_id}/comments", response_model=dict, status_code=201)
def create_comment(post_id: int, payload: CommentCreate):
    comment = add_comment(post_id, payload)
    if comment is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return comment
