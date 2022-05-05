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
            attrs={"class": "form-control mt-2", "type": "text", "placeholder": "캠핑장리뷰"}
        ),
    )

    facility_star = forms.IntegerField(
        required=True,
        label="시설평점",
        widget=forms.TextInput(
            attrs={"class": "form-control mt-2", "placeholder": "시설평점"}
        ),
    )

    visited_at = forms.DateField(
        required=True,
        label="방문날짜",
        widget=forms.TextInput(
            attrs={"class": "form-control mt-2", "type": "date", "placeholder": "방문날짜"}
        ),
    )

    class Meta:
        model = CampingInfo
        fields = (
            "title",
            "review",
            "facility_star",
            "visited_at",
        )
