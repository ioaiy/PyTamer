import string
from random import choice
from flask import jsonify, request
from url.models import Url
from app import app, db, csrf
# https://github.com/kiteco/kite-python-blog-post-code/tree/master/flask-tutorial/restful-apis
# -with-flask

def get_urls():
    urls = Url.query.all()
    return jsonify(urls=[u.serialize for u in urls])


def get_url(id):
    url = Url.query.filter_by(id=id).one()
    return jsonify(url=url.serialize)


def makeANewUrl(old):
    def gen():
        chars = string.ascii_letters + string.digits
        length = 5
        code = ''.join(choice(chars) for x in range(length))
        print("Checking", code)
        exists = db.session.query(
            db.exists().where(Url.new == code)).scalar()
        if not exists:
            print("Your new code is:", code)
            return code
    code = gen()
    while code is None:
        code = gen()

    if code is not None:
        addedurl = Url(new=code, old=old)
        db.session.add(addedurl)
        db.session.commit()
        return jsonify(Url=addedurl.serialize)


# def updateBook(id, title, author, genre):
#     updatedBook = Url.query.filter_by(id=book_id).one()
#     if not title:
#         updatedBook.title = title
#     if not author:
#         updatedBook.author = author
#     if not genre:
#         updatedBook.genre = genre
#     session.add(updatedBook)
#     session.commit()
#     return 'Updated a Book with id %s' % id
#
#
# def deleteABook(id):
#     bookToDelete = session.query(Url).filter_by(id=id).one()
#     session.delete(bookToDelete)
#     session.commit()
#     return 'Removed Book with id %s' % id
#

@app.route('/')
@app.route('/urlApi', methods=['GET', 'POST'])
@csrf.exempt
def urlsFunction():
    if request.method == 'GET':
        return get_urls()
    elif request.method == 'POST':
        old = request.args.get('old', '')
        return makeANewUrl(old)


@app.route('/urlApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def urlFunctionId(id):
    if request.method == 'GET':
        return get_url(id)

    # elif request.method == 'PUT':
    #     title = request.args.get('title', '')
    #     author = request.args.get('author', '')
    #     genre = request.args.get('genre', '')
    #     return updateBook(id, title, author, genre)
    #
    # elif request.method == 'DELETE':
    #     return deleteABook(id)