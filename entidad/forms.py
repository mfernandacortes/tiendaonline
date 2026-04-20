from django import forms

TALLE_CHOICE = (
    (1, "ExtraChico"),
    (2, "Chico"),
    (3, "Mediano"),
    (4, "Grande"),
    (5, "ExtraGrande"),
    (6, "DobleExtraGrande")
)


GENERO_CHOICE = (
    (1, "Hombre"),
    (2, "Mujer"),
    (3, "Unisex")
)

class RopaForm(forms.Form):
    marca = forms.CharField(label="Marca", max_length=50)
    talle = forms.ChoiceField(label="Talle", choices=TALLE_CHOICE)
    color = forms.CharField(label="Color", max_length=50)
    lisa = forms.BooleanField(label="Remera Lisa", required=False)
    genero = forms.ChoiceField(label="Genero", choices=GENERO_CHOICE)

