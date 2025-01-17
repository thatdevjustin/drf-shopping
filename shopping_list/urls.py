from django.urls import path

from shopping_list.views import AddShoppingItem, ListAddShoppingList, ShoppingItemDetail, ShoppingListDetail


urlpatterns = [
    path("api/shopping-lists/", ListAddShoppingList.as_view(), name="all_shopping_lists"),
    path("api/shopping-list/<uuid:pk>/", ShoppingListDetail.as_view(), name="shopping_list_detail"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/", AddShoppingItem.as_view(), name="add_shopping_item"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/<uuid:item_pk>/", ShoppingItemDetail.as_view(), name="shopping_item_detail"),
]