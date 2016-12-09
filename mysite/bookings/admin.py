from django.contrib import admin

from .models import Booking, Step


def make_published(modeladmin, request, queryset):
	queryset.update(status='p', is_live=True)

make_published.short_description = "Mark selected bookings as Published"

class StepInline(admin.StackedInline):
	model = Step


class BookingAdmin(admin.ModelAdmin):
	inlines = [StepInline,]

	search_fields = ['title','description']

	list_filter = ['created_at', 'is_live']

	list_display = ['title',
	                'created_at',
	                'is_live',
	                'status']

	list_editable = ['status']

	class Media:
		js =('js/vendor/markdown.js', 'js/preview.js')



admin.site.register(Booking, BookingAdmin)
admin.site.register(Step)

