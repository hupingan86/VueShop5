from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self,request):
        """
        通过django的View实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     # json_dict["category"] = good.category
        #     json_dict["market_price"] = good.market_price
        #     json_dict["shop_price"] = good.shop_price
        #     json_dict["goods_sn"] = good.goods_sn
            # json_dict["click_num"] = good.click_num
            # json_dict["sold_num"] = good.sold_num
            # json_dict["fav_num"] = good.fav_num
            # json_dict["goods_num"] = good.goods_num
            # json_dict["goods_brief"] = good.goods_brief
            # json_dict["goods_desc"] = good.goods_desc
            # json_dict["ship_free"] = good.ship_free
            # json_dict["goods_front_image"] = good.goods_front_image
            # json_dict["is_new"] = good.is_new
            # json_dict["is_hot"] = good.is_hot
            # json_dict["add_time"] = good.add_time
            # json_list.append(json_dict)
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # from django.http import HttpResponse
        # import json
        # return HttpResponse(json.dumps(json_list), content_type="application/json")
        import json
        from django.core import serializers
        # 进行序列化
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse
        return JsonResponse(json_data, safe=False)