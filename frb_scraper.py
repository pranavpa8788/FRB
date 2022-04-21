from datetime import datetime
from praw import Reddit

def reddit_scraper_main(
    client_id,
    client_secret,
    user_agent,
    subreddit_name,
    sort_mode,
    post_limit,
    keyword_list
    ): 

    posts = {}
    
    reddit = Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
        )

    subreddit = reddit.subreddit(subreddit_name)
    sort_mode = getattr(subreddit, sort_mode)
    subreddit = sort_mode(limit=post_limit)
    
    for post in subreddit: 
        post_title = post.title

        if any(word in post_title.lower() for word in keyword_list):
            post_url = post.url

            post_created = post.created_utc
            post_date = datetime.today() - datetime.fromtimestamp(post_created)
            post_date_total_seconds = post_date.total_seconds()
            post_date_hours = post_date_total_seconds//3600
            post_date_minute = (post_date_total_seconds%3600)//60
            post_date_seconds = int(post_date_total_seconds%60)

            post_date = f'{post_date_hours}h {post_date_minute}m {post_date_seconds}s ago'

            posts[post_title] = [post_url, post_date]
            
    return posts
        
if __name__ == '__main__': 

    client_id = '7GW4nj-Su8m_1A'
    client_secret = 'OtEv-BTFlJAgOpsiwBkkVsuldKc'
    user_agent = 'memebot33127'

    posts = reddit_scraper_main(client_id, client_secret, user_agent, 'slavelabour', 'new', 20, ['task'])

    for key, value in posts.items():
        print(key, value)
        print('\n')

    subreddits = {
            'slavelabour' : 'task',
            'remotework' : 'hiring',
            'forhire' : 'hiring',
            'freelance_forhire' : 'hiring'}
 
