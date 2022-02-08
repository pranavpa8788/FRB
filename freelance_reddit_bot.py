import praw
import datetime

def reddit_scraper_main(subreddit_name, mode, post_limit, keyword) : 
    
    # Put your own client_id, client_secret, user_agent inside "" below
    client_id = "client_id"
    client_secret = "client_secret"
    user_agent = "user_agent"
    
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    posts = {}
    
    keyword_posts = {}
    
    subreddit = eval('reddit.subreddit(subreddit_name).%s(limit=post_limit)' % (mode))
    
    for post in subreddit : 
        
        post_title = post.title
        
        post_url = post.url
        
        post_created = post.created_utc
        
        post_date = datetime.datetime.today() - datetime.datetime.fromtimestamp(post_created)
        
        posts[post_title] = [post_url, post_date]
            
    for key in posts.keys() : 
        
        if ( keyword in key ) or ( keyword.lower() in key ) or ( keyword.upper() in key ) or ( keyword.title() in key ) : 
        
            keyword_posts[key] = posts[key]
            
    return keyword_posts
        
        
if __name__ == '__main__' : 

    # For hiring freelancers
    subreddits_buy = {
            'slavelabour' : 'offer',
            'remotework' : 'hire',
            'forhire' : 'for hire',
            'freelance_forhire' : 'for hire',
            'freelance_forhire' : 'hire me'}

    # For getting hired
    subreddits_sell = {
            'slavelabour' : 'task',
            'remotework' : 'hiring',
            'forhire' : 'hiring',
            'freelance_forhire' : 'hiring'}
    
    # Change subreddits_sell to subreddits_buy if you want to hire freelancers
    for subreddit, keyword in subreddits_sell.items() :

        posts = reddit_scraper_main(subreddit, 'new', 20, keyword)

        print(f'Subreddit : {subreddit}')

        for key, value in posts.items() : 
            
            print(str(key))
            
            for j in value :
                
                print(j)
            
            print('\n')
    
 
