from django.shortcuts import render


# https://docs.djangoproject.com/en/dev/topics/http/views/#writing-views
def post_list(request):
    return render(request, 'blog/post_list.html', {})
