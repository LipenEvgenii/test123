from django import forms

from . import models
from .models import Category,Product,ExtendUser

class CategoryForm(forms.Form):
    name=forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)

    def save(self):
        new_category=Category.objects.create(
            name=self.cleaned_data['name'],
            slug=self.cleaned_data['slug']

        )
        return new_category


class ProductForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),label="Категория",empty_label="Категории")
    name = forms.CharField(max_length=200,label="Продукт")
    slug = forms.SlugField(max_length=200)
    image = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":30}),label="Описание")
    price = forms.DecimalField(max_digits=10, decimal_places=2,label="Цена")
    stock = forms.IntegerField(min_value=0)
    available = forms.BooleanField(label="Разместить",required=False)

    def save(self):
        new_product=Product.objects.create(
            category =self.cleaned_data['category'],
            name=self.cleaned_data['name'],
            slug=self.cleaned_data['slug'],
            image=self.cleaned_data['image'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            stock=self.cleaned_data['stock'],
            available=self.cleaned_data['available']

        )
        return new_product


class UserFormRegister(forms.ModelForm):
    class Meta:
        models=ExtendUser
        fields='__all__'



# class ProductForm(forms.ModelForm):
#     class Meta:
#         model=Product
#         # fields='__all__' #  возмет из модели все аргементы и создаст в форме!

        # fields=['category','name','slug','description','price','stock','available','image']

