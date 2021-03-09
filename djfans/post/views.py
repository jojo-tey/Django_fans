from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect


from post.forms import NewPostForm
from post.models import Post, PostFileContent
from tier.models import Tier

# Create your views here.


def NewPost(request):
    user = request.user
    files_objs = []

    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('content')
            title = form.cleaned_data.get('title')
            caption = form.cleaned_data.get('caption')
            tier = form.cleaned_data.get('tier')
            tiers = get_object_or_404(Tier, id=tier.id)

            for file in files:
                file_instance = PostFileContent(
                    file=file, user=user, tier=tiers)
                file_instance.save()
                files_objs.append(file_instance)

            p, created = Post.objects.get_or_create(
                title=title, caption=caption, user=user, tier=tiers)
            p.content.set(files_objs)
            p.save()
            return redirect('index')
    else:
        form = NewPostForm()
        form.fields['tier'].queryset = Tier.objects.filter(user=user)

    context = {
        'form': form,
    }

    return render(request, 'newpost.html', context)
