from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.comment import CommentSchema, Comment
from auth import *

comments_bp = Blueprint('comments', __name__, url_prefix='/<int:card_id>/comments')

@comments_bp.route('/', methods=['POST'])
@jwt_required()
def create_comment(card_id):
    comment_info = CommentSchema(only=['message']).load(request.json)
    comment = Comment(
        message = comment_info['message'],
        user_id = get_jwt_identity(),
        card_id = card_id
    )
    db.session.add(comment)
    db.session.commit()
    return CommentSchema().dump(comment), 201

# Update a comment
@comments_bp.route('/<int:comment_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_comment(card_id, comment_id):
    # authorize()
    comment_info = CommentSchema(only=['message']).load(request.json)
    stmt = db.select(Comment).filter_by(id=comment_id) # .where(Comment.id == id)
    comment = db.session.scalar(stmt)
    if comment:
        authorize(comment.user_id)
        comment.message = comment_info.get('message', comment.message)
        db.session.commit()
        return CommentSchema().dump(comment)
    else:
        return {'error': 'Comment not found'}, 404

# Delete a comment
@comments_bp.route('/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(card_id, comment_id):
    # authorize()
    stmt = db.select(Comment).filter_by(id=comment_id) # .where(Comment.id == id)
    comment = db.session.scalar(stmt)
    if comment:
        authorize(comment.user_id)
        db.session.delete(comment)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Comment not found'}, 404