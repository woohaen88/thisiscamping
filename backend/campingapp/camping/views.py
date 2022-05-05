from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from campingapp.camping.forms import PostForm
from campingapp.models import CampingInfo, Photo


def index(request):
    # 캠핑 모델을 불러와야함
    context = {"campinginfo": CampingInfo.objects.all().order_by("-created_at")}
    return render(request, "index.html", context)


def detail(request, camping_info_id):
    camping = CampingInfo.objects.filter(id=camping_info_id).first()

    context = {"camping": camping}

    return render(request, "camping/detail.html", context)


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            camping_info = form.save(commit=False)
            camping_info.total_star = (
                camping_info.facility_star * 0.5 + camping_info.atmosphere_star * 0.5
            )

            camping_info.image = request.FILES.get("image")
            camping_info.user = request.user
            camping_info.save()

            # for img in request.FILES.getlist("imgs"):
            #     photo = Photo()
            #     photo.camping_info = camping_info
            #     photo.image = img
            #     photo.save()

            return redirect("index")
    else:
        # GET 요청
        form = PostForm()

    context = {"form": form}
    return render(request, "camping/post.html", context)


def update(request, camping_info_id):
    camping_info = get_object_or_404(CampingInfo, id=camping_info_id)
    if request.user.id != camping_info.user_id:
        messages.error(request, "수정 권한 없음 ㅅㄱ")
        # return redirect("index")

    if request.method == "POST":
        form = PostForm(request.POST, instance=camping_info)
        if form.is_valid():
            camping = form.save(commit=False)
            camping.image = request.FILES.get("image")
            form.save()

            return redirect("camping:detail", camping_info_id=camping_info.id)
    else:
        form = PostForm(instance=camping_info)
    context = {"form": form, "camping": camping_info}
    return render(request, "camping/update.html", context)


def delete(request, camping_info_id):
    camping_info = get_object_or_404(CampingInfo, id=camping_info_id)
    if request.user.id != camping_info.user_id:
        messages.error(request, "삭제권한없음 ㅅㄱ")
        return redirect("index")

    camping_info.delete()
    return redirect("index")
