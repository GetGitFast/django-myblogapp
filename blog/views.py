from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
import requests
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post  # .models indicates same directory and from the models file in the current package
from .models import Announcement
from django.conf import settings
from .models import City


# from django.http import HttpResponse
# Create your views here.


"""posts = [
    {'author': 'Anil Dhar',
     'title': 'Introduction to Django',
     'content': 'Django is a Python-based free and open-source web framework, which follows the model-template-view '
                'architectural pattern.',
     'date_posted': 'July 27, 2019'
     },
    {'author': 'Rita Dhar',
     'title': 'What is  Physics?',
     'content': 'Physics is the natural science that studies matter, its motion and behavior through space and time, '
                'and that studies the related entities of energy and force.',
     'date_posted': 'July 28, 2019'
     },
    {'author': 'Shailja Dhar',
     'title': 'All about Chemical Engineering',
     'content': 'Environmental engineering is a sub-discipline of civil engineering and chemical engineering',
     'date_posted': 'July 29, 2019'
     }
]"""


# Below are examples of function based views
def home(request):
    #  return HttpResponse('<h1>Blog Home</h1>')
    context = {
        # 'posts': posts
        # posts below is like a key of the context dictionary which we can use in the template
        # like posts,author, post.title etc.
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context, {'title': 'Home'})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def technology(request):
    return render(request, 'blog/technology.html', {'title': 'Technology'})


def knowledge(request):
    return render(request, 'blog/knowledge.html',  {'title': 'Knowledge Centre'})


def oksana(request):
    return render(request, 'blog/oksana.html',  {'title': 'Oksana'})


def weather(request):
    """ Gets weather report for a selected city that is found in the City table. Otherwise, it will take the city
    from DEFAULT_CITY environment variable-currently set to 'Sydney'. The City table needs have atleast 'Sydney',
    or else the website would go in a spin."""
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+settings.OWM_API.strip()

    if request.method == 'GET':
        search_key = request.GET.get('q1')

    if not search_key:
        search_key = settings.DEFAULT_CITY

    try:
        cities = City.objects.filter(Q(name__icontains=search_key)).order_by('name')
    except KeyError:
        messages.warning(request, f'Your city not found. Showing default city')
        return redirect('blog-weather')

    print(f"cities : {cities}")
    weather_data = []
    for city in cities:
        try:
            r = requests.get(url.format(city)).json()
            city_weather = {'city': city.name, 'temperature': r['main']['temp'],
                            'description': r['weather'][0]['description'],
                            'icon': r['weather'][0]['icon'],
                            'humidity': r['main']['humidity'],
                            'maximum': r['main']['temp_max'],
                            'minimum': r['main']['temp_min']}

            weather_data.append(city_weather)
        except KeyError:
            pass

    if weather_data:
        context = {'weather_data': weather_data}
        return render(request, 'blog/weather.html', context)
    else:
        messages.warning(request, f'Your city not found. Showing default city')
        return redirect('blog-weather')


# Below are the examples of class based views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # 'date_posted' would list from oldest to newest. - would change the order
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        """List blogs for a specific user. The username in the get_queryset would be passed from blog|urls.py. The
           method would also make sure to return 404 in case a user doesn't exist"""
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class SearchPostsView(ListView):
    model = Post
    template_name = 'blog/search_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        search_key = self.request.GET.get('q')
        if search_key:
            object_list = Post.objects.filter(
                Q(title__icontains=search_key) |
                Q(content__icontains=search_key) |
                Q(author__username__icontains=search_key) |
                Q(author__first_name__icontains=search_key) |
                Q(author__last_name__icontains=search_key)
            ).order_by('-date_posted')
        else:
            object_list = Post.objects.all().order_by('-date_posted')
        return object_list


class RecentPostsView(ListView):
    model = Post
    template_name = 'blog/recent_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        object_list = Post.objects.all().order_by('-date_posted')[:5]
        return object_list


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):  # Class based views don't accept decorators so LoginRequiredMixin
    model = Post                                       # would make sure that a user is logged in to create new post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ This will prevent any user to update other people's post. Works in conjunction with
        UserPassesTestMixin"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # Will redirect to home page after successful deletion

    def test_func(self):
        """ This will prevent any user to delete other people's post. Works in conjunction with
            UserPassesTestMixin"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AnnouncementView(ListView):
    model = Announcement
    template_name = 'blog/announcements.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'announcements'
    paginate_by = 3

    def get_queryset(self):
        object_list = Announcement.objects.filter(display=True).order_by('-date_posted')
        return object_list










