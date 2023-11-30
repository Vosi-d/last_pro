from fastapi import Body
from datetime import datetime

from comment import comment_router
from database.commentservice import get_exact_mark_comment_db, add_new_comment_db, \
    delete_exact_comment_db, change_exact_comment_db


@comment_router.get('/mark-comments')
async def get_mark_comments(mark_id: int):
    result = get_exact_mark_comment_db(mark_id)

    return {'status': 1, 'message': result}

@comment_router.post('/add-comment')
async def add_new_comment(student_id: int = Body(...),
                          mark_id: int = Body(...),
                          comment_text: str = Body(...)):
    result = add_new_comment_db(student_id=student_id, mark_id=mark_id,
                                comment_text=comment_text, publish_date=datetime.now())

    return {'status': 1, 'message': result}


@comment_router.put('/edit-comment')
async def edit_exact_comment(comment_id: int = Body(...),
                             new_comment_text: str = Body(...)):
    result = change_exact_comment_db(comment_id, new_comment_text)

    return {'status': 1, 'message': result}

@comment_router.delete('/delete-comment')
async def delete_exact_comment(comment_id):
    result = delete_exact_comment_db(comment_id)

    return {'status': 1, 'message': result}


