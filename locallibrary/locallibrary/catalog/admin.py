from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance #importando os modelos

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

class BookAdminInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] #entre parenteses ficam na mesma linha
    inlines = [BookAdminInline]

class BooksInstanceInline(admin.TabularInline): #TabularInline é um layout horizontal
    model = BookInstance

@admin.register(Book) #@register decorator faz o mesmo que admin.site.register()
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre') #o django não especifica uma variavel many to many
                                                        #por isso vamos definir uma função para obter as informações
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'borrower', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

admin.site.register(Author, AuthorAdmin)





