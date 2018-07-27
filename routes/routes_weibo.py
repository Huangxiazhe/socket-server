from models.weibo import Weibo
from routes import (
    SeizerTemplate,
    html_response,
)


def index(request):
    """
    weibo 页的路由函数， 返回 weibo 页面
    """
    weibos = Weibo.all()
    # 替换模板文件中的标记字符串
    body = SeizerTemplate.render('weibo_index0.html')
    return html_response(body)


def route_dict():
    """
    路由字典
    key 是路由(路由就是 path)
    value 是路由处理函数(就是响应)
    """
    d = {
        '/weibo/index': index,
    }
    return d
