from django.contrib import admin
from cycleapp import models
import requests
from django import template
import requests
from PIL import Image
from django.utils.html import format_html

# Register your models here.


def htciapi(html):
    HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
    HCTI_API_USER_ID = '2f523b47-5f55-42e5-967b-c8856d73e249'
    HCTI_API_KEY = '2ca6f00f-2de9-491e-815c-3843b000dd83'

    data = html
    try:
        image = requests.post(url = HCTI_API_ENDPOINT, data = html, auth=(HCTI_API_USER_ID, HCTI_API_KEY))
        print('*'*50)
        print(image.json())
        print("Your image URL is: %s"%image.json()['url'])
        return image.json()['url']
    except:
        return ' '



class MyAdminView(admin.ModelAdmin):
    def show_firm_url(self, obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.image_url)

    list_display = ( 'model' ,'show_firm_url' )
    

    def save_model(self, request, obj, form, change):
        context = {
        'cycle' : obj , 
        'company' : obj.company
    }
        t = template.loader.get_template('cycleapp/cycle.html')
        c = template.Context(context)
        html = t.render(context)
        css_obj = models.StyleSettings.objects.first()
        data = { 'html': html,
            'css': css_obj.css }
        obj.image_url = htciapi(data)
        im = Image.open(requests.get(obj.image_url, stream=True).raw)
        im.save("file_name.png")
        print(obj.image_url)
        super(MyAdminView, self).save_model(request, obj, form, change)
    


admin.site.register(models.Company)
admin.site.register(models.Home)
admin.site.register(models.Cycles , MyAdminView)
admin.site.register(models.StyleSettings)

