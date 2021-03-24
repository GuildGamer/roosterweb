from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View, CreateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.utils import timezone
from .models import Item, OrderItem, Order, BillingAddress, Vendor
from django.contrib import messages
from .forms import*
from django.db.models import Q


class HomeView(ListView):
   model = Item
   template_name = "index.html"

context = {
    'items': Item.objects.all()
}
def item_list(request):
    return render(request, "index.html", context)


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"
    
    def ReviewView():
        if request.method == 'POST':
            form = ReviewForm

    '''def ReviewView(self, Item, request):
        if request.method == 'POST':
            form = ReviewForm(data=request.POST)
            if form.is_valid():

                user_review = form.save()
                user_review.save()

        else:
            form = ReviewForm()

        context = {
            'form': form
        }

        return render(request, "product.html", context)'''

class ReviewView(View):

    def get(self, *args, **kwargs):
        #form
        form = ReviewForm()
        context = {
            'form': form
        }

        return render(self.request, "product.html", context)
    def post(self, *args, **kwargs):
        form = ReviewForm(self.request.POST or None)

        print(self.request.POST)
        if form.is_valid():

            review = form.cleaned_data.get('review')
            item = get_object_or_404(Item, slug=Item.slug)

            review_details = Review(
                item = item,
                user = self.request.user,
                review = review

            )
            review_details.save()

            return redirect('base_app:product.html')


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, "order_summary.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")
        


#def product(request):
    #order = Order.objects.get(user=self.request.user, ordered=False)
    #return render(request, "product.html", {'cart':order})


class CheckoutView(View):

    def get(self, *args, **kwargs):
        #form
        form = CheckoutForm()
        order = Order.objects.get(user=self.request.user, ordered=False)
        context = {
            'form': form, 'object': order
        }

        return render(self.request, "checkout.html", context)
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)

        print(self.request.POST)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                address=form.cleaned_data.get('address')
                phone=form.cleaned_data.get('phone')
                city=form.cleaned_data.get('city')
                different_shipping_address=form.cleaned_data.get('different_shipping_address')
                order_notes=form.cleaned_data.get('order_notes')
                save_info=form.cleaned_data.get('save_info')
                payment_option=form.cleaned_data.get('payment _option')
                terms=form.cleaned_data.get('terms')
                billing_address = BillingAddress(
                    user = self.request.user,
                    address = address,
                    phone = phone,
                    city = city,
                    order_notes = order_notes
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()

                return redirect('base_app:checkout')
            messages.warning(self.request, "Failed to checkout")
            return redirect('base_app:checkout')

    
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("base_app:order-summary")
        
            
         
#add to cart
@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created= OrderItem.objects.get_or_create(
        item=item,
        user = request.user,
        ordered = False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug = item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")

    return redirect("base_app:product", slug=slug)

# remove from cart
@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user = request.user,
        ordered = False
    )

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug = item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user = request.user,
                ordered = False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart")
            return redirect("base_app:product", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("base_app:product", slug=slug)
        
    else:
        messages.info(request, "You do not have an active order")
        return redirect("base_app:product", slug=slug)



@login_required
def add_to_cart_order_summary(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created= OrderItem.objects.get_or_create(
        item=item,
        user = request.user,
        ordered = False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug = item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
            return redirect("base_app:order-summary")
        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)
            return redirect("base_app:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
        return redirect("base_app:order-summary")
    

#minus single item from quantity
@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user = request.user,
        ordered = False
    )

    if order_qs.exists():
        order = order_qs[0]
        
        if order.items.filter(item__slug = item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)

            messages.info(request, "This item quantity was updated")
            return redirect("base_app:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("base_app:order-summary")
        
    else:
        messages.info(request, "You do not have an active order")
        return redirect("base_app:product", slug=slug)

@login_required
def remove_from_cart_order_summary(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user = request.user,
        ordered = False
    )

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug = item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user = request.user,
                ordered = False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart")
            return redirect("base_app:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("base_app:order-summary")
        
    else:
        messages.info(request, "You do not have an active order")
        return redirect("base_app:order-summary")


   
def searchResult(request):
    product = None
    object_list = None
    if 'search' in request.GET:
        product = request.GET.get('search')
        if product != '':
            try:
                object_list = Item.objects.all().filter(Q(title__icontains=product) | Q(description__icontains=product) | Q(category__icontains=product))
            except ObjectDoesNotExist:
                object_list = None
                messages.error(request, "Sorry there are no search results")
            return render(request, "search.html", {'items':object_list, 'searched_item':product})
        else:
            return redirect("base_app:item-list")
    else:
        messages.error(request, "Sorry there are no search results")
        return render(request, "search.html", {})

#TODO:reviews view
#costumer care
#sell
#topselling

def sell(request):
    registered = False

    if request.method == 'POST':

        vendor_form = VendorForm(data=request.POST)
        vendor_detail_form = VendorDetailForm(data=request.POST)

        if vendor_form.is_valid() and vendor_detail_form.is_valid():

            seller = vendor_form.save()
            seller.set_password(seller.password)
            seller.save()

            detail = vendor_detail_form.save(commit=False)
            detail.seller = seller
            detail.save()

            registered = True
        else:
            messages.error(request, vendor_form.errors, vendor_detail_form.errors)

    else:
        vendor_form = VendorForm()
        vendor_detail_form = VendorDetailForm()

    context = {
            'v_form': vendor_form, 'v_detail_form': vendor_detail_form
    }

    return render(request, "sell.html", context)

@login_required
def store_managment(request):

    if request.method == 'POST':

        item_form = ItemForm(data=request.POST)

        if item_form.is_valid():

            item = item_form.save()
            item.save()

        else:
            messages.error(request, item_form.errors)

    else:
        item_form = ItemForm()

    context = {'new_item': item_form}

    return render(request, "store_managment.html", context)

"""class store_managment(LoginRequiredMixin, CreateView):

    model = Item

    form_class = ItemForm
    template_name = "store_managment.html" """


