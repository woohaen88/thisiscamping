from django import forms
from campingapp.models import CampingInfo


# title = models.CharField(max_length=20, null=False)
# review = models.CharField(max_length=200, null=False)
# facility_star = models.IntegerField()
# visited_at = models.DateField()
# user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
# total_star = models.FloatField()


class PostForm(forms.ModelForm):
    visited_at = forms.DateField(
        required=True, widget=forms.DateInput(attrs={"type": "date"})
    )

    title = forms.CharField(
        max_length=20,
        required=True,
        label="캠핑장이름",
        widget=forms.TextInput(
            attrs={"class": "form-control mt-2", "type": "text", "placeholder": "캠핑장이름"}
        ),
    )

    review = forms.CharField(
        max_length=100,
        required=True,
        label="캠핑장리뷰",
        widget=forms.TextInput(
            attrs={
                "class": "form-control mt-2",
                "type": "text",
                "placeholder": "캠핑장리뷰",
            }
        ),
    )

    facility_star = forms.IntegerField(
        required=True,
        label="시설평점",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "시설평점",}),
    )

    visited_at = forms.DateField(
        required=True,
        label="방문날짜",
        widget=forms.TextInput(
            attrs={"class": "form-control mt-2", "type": "date", "placeholder": "방문날짜",}
        ),
    )

    image = forms.ImageField(
        required=True,
        label="썸네일: ",
        widget=forms.FileInput(
            attrs={"class": "mt-2", "type": "file", "name": "image"},
        ),
    )

    CHOICES = [("T", "접지"), ("F", "접지x"), ("ETC", "모름")]
    ground_on = forms.CharField(
        required=True,
        label="접지가 되어있니?",
        widget=forms.Select(
            choices=CHOICES,
            attrs={"class": "btn btn-info dropdown-toggle btn-block mt-1"},
        ),
    )

    CHOICES = [("T", "가능"), ("F", "불가"), ("ETC", "모름")]
    with_animal = forms.CharField(
        required=True,
        label="반려동물 가능?",
        widget=forms.Select(
            choices=CHOICES,
            attrs={"class": "btn btn-info dropdown-toggle btn-block mt-1"},
        ),
    )

    CHOICES = [
        ("forest", "숲쀼"),
        ("ocean", "오션뷰~~~"),
        ("lake", "호수뷰!"),
        ("simple", "시설맛집!"),
        ("shit", "똥뷰!"),
        ("etc", "그외!"),
    ]
    kind_of_view = forms.CharField(
        required=True,
        label="쀼는 어때?",
        widget=forms.Select(
            choices=CHOICES,
            attrs={"class": "btn btn-info dropdown-toggle btn-block mt-1"},
        ),
    )

    CHOICES = [
        ("roud", "시끄러움"),
        ("quiet", "조용조용"),
        ("normal", "괜찮음"),
    ]
    kind_of_camper = forms.CharField(
        required=True,
        label="캠퍼는 조용해?",
        widget=forms.Select(
            choices=CHOICES,
            attrs={"class": "btn btn-info dropdown-toggle btn-block mt-1"},
        ),
    )

    CHOICES = [
        ("T", "가능"),
        ("F", "불가능"),
        ("etc", "모름"),
    ]
    can_fire = forms.CharField(
        required=True,
        label="불멍하고싶다",
        widget=forms.Select(
            choices=CHOICES,
            attrs={"class": "btn btn-info dropdown-toggle btn-block mt-1"},
        ),
    )

    atmosphere_star = forms.IntegerField(
        required=True,
        label="분위기 평점",
        min_value=1,
        max_value=5,
        widget=forms.TextInput(attrs={"class": "form-control", "type": "number"}),
    )

    class Meta:
        model = CampingInfo
        fields = (
            "title",
            "review",
            "visited_at",
            "ground_on",
            "with_animal",
            "kind_of_view",
            "kind_of_camper",
            "can_fire",
            "atmosphere_star",
            "facility_star",
            "image",
        )
