"""VueShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
import xadmin
from VueShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewSet, HotSearchViewSet, BannerViewSet, IndexCategoryViewSet
from users.views import SmsCodeViewSet, UserViewSet
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet, AliPayView

from django.views.generic import TemplateView

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods")

# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")

router.register(r'code', SmsCodeViewSet, base_name="code")

router.register(r'users', UserViewSet, base_name="users")

# 收藏
router.register(r'userfavs', UserFavViewSet, base_name="userfavs")

# 留言
router.register(r'messages', LeavingMessageViewSet, base_name="messages")

# 收获地址
router.register(r'address', AddressViewSet, base_name="address")

# 添加商品
router.register(r'shopcarts', ShoppingCartViewSet, base_name="shopcarts")

# 订单相关url
router.register(r'orders', OrderViewSet, base_name="orders")

# 热搜url
router.register(r'hotsearchs', HotSearchViewSet, base_name="hotsearchs")

# 轮播图url
router.register(r'banners', BannerViewSet, base_name="banners")

# 首页分类商品url
router.register(r'indexgoods', IndexCategoryViewSet, base_name="indexgoods")

# good_list = GoodsListViewSet.as_view({
#     'get': 'list',
#     # 'post': 'create'
# })

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    # url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path('^', include(router.urls)),

    re_path('^index/', TemplateView.as_view(template_name="index.html"), name="index"),

    path('docs/', include_docs_urls(title="六月生鲜")),

    # drf自带的token认证模式
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    re_path(r'^login/', obtain_jwt_token),

    # alipay的认证接口
    re_path(r'^alipay/return/', AliPayView.as_view(), name="alipay"),
]
