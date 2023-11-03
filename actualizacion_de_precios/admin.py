from django.contrib import admin
from .script import procesar_excel

from .models import Producto, ExcelFile
import openpyxl as o




@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('archivo', 'fecha_subida')
    actions = ['procesar_y_actualizar']


    def procesar_y_actualizar(self, request, queryset):
            for excel_file in queryset:
                procesar_excel(excel_file.archivo)

            self.message_user(request, "Archivos Excel procesados y base de datos actualizada con éxito.")

    
    procesar_y_actualizar.short_description = "Procesar Excel y Actualizar Base de Datos"





@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'codigo','nombre', 'precio')






