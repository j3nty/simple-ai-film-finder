from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Film(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=50,
        unique=True,
    )
    description = models.TextField(_("Description"), max_length=200)

    def __str__(self):
        return self.name


class UserFilm(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
    )
    film = models.ForeignKey(
        Film,
        verbose_name=_("Film"),
        on_delete=models.CASCADE,
    )
    is_watched = models.BooleanField(
        _("Watched"),
        default=False,
        help_text=_("Indicates whether the user has watched this film."),
    )

    def __str__(self):
        status = _("Watched") if self.is_watched else _("Not watched")
        return f"{self.user} — {self.film} ({status})"

    class Meta:
        unique_together = (("user", "film"),)
        verbose_name = (_("User Film"),)
        verbose_name_plural = (_("User Films"),)
