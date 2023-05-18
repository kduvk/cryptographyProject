from django.urls import path
from . import views
urlpatterns = [
        path('', views.home, name='page_home'),
        path('caesar/', views.caesar_cipher, name='caesar_cipher_url'),
        path('atbash/', views.atBash_cipher, name='atBash_cipher_url'),
        path('vigenere/', views.vigenere_cipher, name='vigenere_cipher_url'),
        path('beaufort/', views.beaufort_cipher, name='beaufort_cipher_url'),
        path('railFence/', views.railFence_cipher, name='railFence_cipher_url'),
        path('gronsfeld/', views.gronsfeld_cipher, name='gronsfeld_cipher_url')
]
