from .models import Post, Comment
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm, DropViewForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from bootstrap_datepicker_plus import TimePickerInput
from django.views import generic


def image(request):
    carx = Post()
    variables = RequestContext(request,{
        'carx':carx
    })
    return render_to_response('post_detail.html',variables)



class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        try:
            keyword = self.request.GET['q']
        except:
            keyword = ''
        if (keyword != ''):
            object_list = self.model.objects.filter(
                Q(content__icontains=keyword) | Q(title__icontains=keyword) | Q(chamber__icontains=keyword) | Q(address__icontains=keyword))
        else:
            object_list = self.model.objects.all()
        return object_list


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(CustomUser, email=self.kwargs.get('email'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def get_form(self, form_class=None):
        form = super(PostCreateView, self).get_form(form_class)
        form.fields['title'].initial = self.request.user.name
        form.fields['email'].initial = self.request.user.email
        return form

    def form_valid(self, form):
        user1 = self.request.user
        # print('user1', user1)
        form.instance.author = user1
        # print('Post ', self.request.POST)
        # print('user ',self.request.user)
        # print('registration ',self.request.user.name)

        return super().form_valid(form)

    # def rate_object(request, object_pk):
    #     object = get_object_or_404(User.objects.all(), id=user_pk)
    #     if not 'rating' in request.DATA:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #     object.rating = request.DATA['rating']
    #     object.save()
    #     return Response(status=status.HTTP_200_OK)

    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['hours'].widget = TimePickerInput()
    #     return form

def dropView(request):
    # print('Upore  ')
    if(request.method=='POST'):
        form = DropViewForm(request.POST)
        if(form.is_valid()):
            group_categ = form.cleaned_data.get('fields')
            # print('Hello  ',group_categ)


    else:

        form = DropViewForm()

    return render(request, 'blog/dropView.html', {'form': form})



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','chamber','address','fees','days','start_time','end_time','image','review','rating','overall_rating']

    def form_valid(self, form):
        form.instance.author = self.request.user
        # print(self.request.user)
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # print('Post 2', post)
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostImage(TemplateView):
    form = PostForm
    template_name = 'post_detail.html'

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('home', kwargs={'pk': pk}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.POST.get('user_id'))
        text = request.POST.get('text')
        Comment(author=user, post=post, text=text).save()
        messages.success(request, "Your comment has been added successfully.")
    else:
        return redirect('post_detail', pk=pk)
    return redirect('post_detail', pk=pk)
