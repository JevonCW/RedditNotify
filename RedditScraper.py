import praw
from win10toast import ToastNotifier
from _config import myClientId, mClientSecret, myUserAgent, searchSub, searchFlairs

reddit = praw.Reddit(client_id=myClientId, client_secret=mClientSecret, user_agent=myUserAgent)
subreddit = reddit.subreddit(searchSub)
toaster = ToastNotifier()

for submission in subreddit.stream.submissions(skip_existing=True):
    if str(submission.link_flair_text) in searchFlairs:
        toaster.show_toast("Important Post on "+str(submission.subreddit)+": " + str(submission.title))
        continue
