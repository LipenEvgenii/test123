from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, ProductForm, UserFormRegister
from .models import Category, Product, ExtendUser


# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})


class CategoryCreate(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'shop/product/create_category.html', context={'form': form})

    def post(self, request):
        bound_form = CategoryForm(request.POST)

        if bound_form.is_valid():
            category = bound_form.save()
            return redirect(category)
        return render(request, 'shop/product/create_category.html', context={'form': bound_form})


class ProductCreate(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'shop/product/create_product.html', context={'form': form})

    def post(self, request):
        bound_form = ProductForm(request.POST, request.FILES)
        if bound_form.is_valid():
            product = bound_form.save()
            return redirect(product)
        return render(request, 'shop/product/create_product.html', context={'form': bound_form})


def index(request):
    data = request.POST
    # print(data)
    print(data["Login"])
    print(data["Password"])
    return render(request, 'shop/base.html')


class ShopLoginView(LoginView):
    template_name = 'shop/user/login.html'


@login_required
def profile(request):
    return render(request, 'shop/user/profile.html')


class ShopLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'shop/product/list.html'


class ShopUserRegisterView(CreateView):
    model = ExtendUser
    template_name = "shop/user/register.html"
    form_class = UserFormRegister
    success_url = 'shop/product/list.html'
