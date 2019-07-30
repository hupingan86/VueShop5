from rest_framework import serializers
from goods.models import Goods, GoodsCategory, GoodsImage


class CategorySerizlizer3(serializers.ModelSerializer):
    """
        商品类别序列化，第三类
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerizlizer2(serializers.ModelSerializer):
    """
        商品类别序列化，第二类
    """
    sub_cat = CategorySerizlizer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerizlizer(serializers.ModelSerializer):
    """
        商品类别序列化 ,第一类
    """
    sub_cat = CategorySerizlizer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerizlizer()
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"


