from rest_framework import serializers
from html.parser import HTMLParser
from io import StringIO
import re
from main.models import Author, Tag

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


class TagsSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=50, source="caption")

	class Meta:
		model = Tag

class AuthorsSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=60)
	img = serializers.ImageField()
	desc = serializers.CharField()

	class Meta:
		model = Author


class PostsSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=100, source="ext_name")
	category_name = serializers.CharField(source ='category', read_only=True)
	desc = serializers.CharField()
	main_img = serializers.ImageField()
	date = serializers.DateField()
	slug = serializers.SlugField()
	author = AuthorsSerializer(read_only=True, many=True)
	tags = TagsSerializer(read_only=True, many=True)

class PostDetailsSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=100, source="ext_name")
	category_name = serializers.CharField(source ='category', read_only=True)
	desc = serializers.CharField()
	main_img = serializers.ImageField()
	date = serializers.DateField()
	author = AuthorsSerializer(read_only=True, many=True)
	tags = TagsSerializer(read_only=True, many=True)
	
	content = serializers.CharField()

	#* Time Fields
	open_time = serializers.TimeField(allow_null=True)
	closing_time = serializers.TimeField(allow_null=True)

	#* Cost
	Egyptian = serializers.IntegerField(allow_null=True)
	Egyptian_student = serializers.IntegerField(allow_null=True)
	Foreign = serializers.IntegerField(allow_null=True)
	Foreign_student = serializers.IntegerField(allow_null=True)

	#* Address & Geolocation 
#     address = map_fields.AddressField(
#         max_length=200, null=True, blank=True, verbose_name="العنوان"
#     )
#     geolocation = map_fields.GeoLocationField(
#         max_length=100, null=True, blank=True, verbose_name="الموقع الجغرافي"
#     )

	def to_representation(self, data):
		values = super().to_representation(data)
		values["content"] = strip_tags(values["content"]).replace("\\r\\n", " ")
		print(values['content'])
		return values