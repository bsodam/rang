from datetime import datetime, timedelta
from posts.models import Profile, Post


def my_scheduled_job():
    refill_heart_poop()
    delete_old_posts()


def refill_heart_poop():
    user_profiles = Profile.objects.all()

    for user_profile in user_profiles:
        user_profile.refill_heart()
        user_profile.refill_poop()


def delete_old_posts():
    current_time = datetime.today()
    time_week = timedelta(days=7)
    posts = Post.objects.all()

    for post in posts:
        time_gap = current_time - post.time_created
        if time_gap > time_week:
            post.delete()
            print(post, " deleted")
