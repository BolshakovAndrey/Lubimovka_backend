from datetime import timedelta

from django.utils import timezone

from apps.afisha.models import Event
from apps.articles.models import BlogItem, NewsItem
from apps.core.constants import AFISHA_CURRENT_DAY_TITLE
from apps.core.models import Setting
from apps.core.utilities import get_russian_date
from apps.info.models import Festival, Place
from apps.library.models import Play, ProgramType
from apps.main.models import Banner


class MainObject:
    def add_first_screen_data(self):
        main_add_first_screen = Setting.get_setting("main_add_first_screen")
        if main_add_first_screen:
            title = Setting.get_setting("main_first_screen_title")
            url_title = Setting.get_setting("main_first_screen_url_title")
            url = Setting.get_setting("main_first_screen_url")
            self.first_screen = {
                "title": title,
                "url_title": url_title,
                "url": url,
            }

    def add_blog_data(self):
        main_add_blog = Setting.get_setting("main_add_blog")
        if main_add_blog:
            title = Setting.get_setting("main_blog_title")
            items = BlogItem.ext_objects.published()[:6]
            self.blog = {
                "title": title,
                "items": items,
            }

    def add_news_data(self):
        main_add_news = Setting.get_setting("main_add_news")
        if main_add_news:
            title = Setting.get_setting("main_news_title")
            items = NewsItem.ext_objects.published()[:6]
            self.news = {
                "title": title,
                "items": items,
            }

    def add_afisha(self):
        main_add_afisha = Setting.get_setting("main_add_afisha")
        is_festival = Setting.get_setting("festival_status")
        if main_add_afisha:
            main_show_afisha_only_for_today = Setting.get_setting("main_show_afisha_only_for_today")

            if main_show_afisha_only_for_today:
                today = timezone.now()
                tomorrow = today.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
                items = Event.objects.filter(
                    date_time__range=(today, tomorrow),
                    pinned_on_main=True,
                )
                title = AFISHA_CURRENT_DAY_TITLE + get_russian_date(timezone.localdate())
            else:
                items = (
                    Event.objects.filter(date_time__gte=timezone.now())
                    .filter(pinned_on_main=True)
                    .order_by("date_time")[:6]
                )
                if is_festival:
                    title = Setting.get_setting("afisha_title_festival")
                else:
                    title = Setting.get_setting("afisha_title_regular")

            description = Setting.get_setting("afisha_description_regular")

            self.afisha = {
                "title": title,
                "description": description,
                "items": items,
            }

    def add_banners(self):
        main_add_banners = Setting.get_setting("main_add_banners")
        if main_add_banners:
            items = Banner.objects.all()
            self.banners = {"items": items}

    def add_short_list(self):
        main_add_short_list = Setting.get_setting("main_add_short_list")
        if main_add_short_list:
            program = ProgramType.objects.get(slug="short-list")
            festival = Festival.objects.all().order_by("-year").first()
            items = Play.objects.filter(
                program=program,
                festival=festival,
                is_draft=False,
            )[:4]
            title = Setting.get_setting("main_short_list_title")
            self.short_list = {
                "title": title,
                "items": items,
            }

    def add_video_archive(self):
        main_add_video_archive = Setting.get_setting("main_add_video_archive")
        if main_add_video_archive:
            url = Setting.get_setting("main_video_archive_url")
            photo = Setting.get_setting("main_video_archive_photo")
            self.video_archive = {
                "url": url,
                "photo": photo,
            }

    def add_places(self):
        main_add_places = Setting.get_setting("main_add_places")
        if main_add_places:
            items = Place.objects.all()
            self.places = {"items": items}
