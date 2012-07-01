from django.shortcuts import render
from courses.models import Course
from praise.models import Praise
from datetime import datetime
from django.conf import settings
from django.core.cache import cache
import twitter


def index(request):
    course_list = Course.future_objects.filter(display_frontpage=True)
    praise_list = Praise.objects.all()


    tweets = cache.get( 'tweets' )
    if not tweets:
        try:
            tweets = twitter.Api().GetUserTimeline( settings.TWITTER_USER )[:4]
            for tweet in tweets:
                tweet.date = datetime.strptime( tweet.created_at, "%a %b %d %H:%M:%S +0000 %Y" )

            cache.set( 'tweets', tweets, settings.TWITTER_TIMEOUT )
        except:
            pass

    return render(request, 'index.html', {'course_list': course_list, 'tweets': tweets, 'praise_list': praise_list })