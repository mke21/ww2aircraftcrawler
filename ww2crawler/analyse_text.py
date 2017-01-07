from .aircraft import aircraft as ac

def make_aircraftlist(text):
    """
    Will make a list of matching aircraft
    """
    result = [
        key
        for key, regex in ac
        if regex.search(text)
        ]
    return result
        

def getdate(d):
    s = d.split('-')
    return {
        'year': int(s[0]),
        'month': int(s[1])
        }


def analyse_post(post):
    """
    post = dictionary from files
    return: dictionary like:
    {
      'author': author,
      'year': 2016,
      'month': 12,
      'postno': 1
      'aircraft': []
    }
    """
    result = getdate(post['date'])
    result['aircraft'] = make_aircraftlist(post['text'])
    try:
        result['author'] = post['author']
    except:
        result['author'] = 'None'
    result['postno'] = int(post['postno'][1:])
    return result
