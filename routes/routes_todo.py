from routes import (
    SeizerTemplate,
    html_response,
    login_required,
)


def index(request):
    """
    todo 页的路由函数， 返回 todo 页面
    """
    body = SeizerTemplate.render('todo_index0.html')
    return html_response(body)


def route_dict():
    """
    路由字典
    key 是路由(路由就是 path)
    value 是路由处理函数(就是响应)
    """
    d = {
        '/todo/index': login_required(index),
    }
    return d
