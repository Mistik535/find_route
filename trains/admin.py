from django.contrib import admin

from trains.models import Train



class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train
    list_display = ("name", "from_city", "to_city", "travel_time")
    list_editable = ("travel_time", ) # "from_city" - лучше не использовать для редактирования так как увеличивает нагрузку на сервер


admin.site.register(Train, TrainAdmin)
