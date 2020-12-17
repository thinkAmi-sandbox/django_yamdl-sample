import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.views import View

from myapp.models import Apple


class AppleView(View):
    def get(self, request, *args, **kwargs):
        apples = Apple.objects.all().values()

        data_json = json.dumps(list(apples), ensure_ascii=False, cls=DjangoJSONEncoder)
        return HttpResponse(data_json, content_type='application/json')
