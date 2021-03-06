# -*- coding: utf-8 -*-
import re,vk_api,os,sys,random, requests, time, threading, random
from vkauth import *
slova = ['moscow']
stories_count = 0
all_stories_count = 0
start = 0
end = 300
seen_stories = []
token_bot = os.environ.get('tokenbot')


try:
    f = open('slova.txt')
    lines = f.readlines()
    num_lines = sum(1 for line in open('slova.txt'))
    for i in range(num_lines):
        slova.append(lines[i].replace('\n', ''))
except Exception as err:
    print(err)
    print(u"Ошибка, возможно вы не создали файл slova.txt")


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device

def watch_story(author, story, read_token):
    data = {
        'act': 'read_stories',
        'al': 1,
        'all': 0,
        'connection_type': 'wi-fi',
        'hash': read_token,  # токен, который мы получали при парсинге страницы
        'loading_stats': '{author_id},{story_id},{random_tickrate}'.format(author_id=author, story_id=story,
                                                                           random_tickrate=random.randint(50, 1000)),
        'navigation_stats:': '{author_id},{story_id},list,view_story'.format(author_id=author, story_id=story),
        'progress': 0,
        'source': 'list',
        'story_id': '{author_id}_{story_id}'.format(author_id=author, story_id=story),
        'track_code': ''
    }
    vk_session.http.post("https://vk.com/al_stories.php", data=data)

def get_active_stories(user_id):
    data = vk.stories.get(owner_id=user_id)
    return data
def pars_users(zapros, megatoken):
    a = []
    stories = []
    authors = []
    for j in zapros:
        try:
            time.sleep(0.05)
            print(f'Собрано {len(stories)} историй.')
            params = {'q':j,
                      'access_token':megatoken,
                      'v':'5.101',
                      'count':1000
                      }
            r = requests.get('https://api.vk.com/method/stories.search?', params=params)
            count = r.json()['response']['items']
            if int(r.json()['response']['count'])>=55:
                #print(f'Записываю слово {j} | Найдено историй : {r.json()["response"]["count"]}')
                results = open('good_words.txt', 'a')
                results.write(f'{j}\n')
                results.close()
            for i in count:
                if i[0]['id'] not in seen_stories:
                    stories.append(i[0]['id'])
                    authors.append(i[0]['owner_id'])
        except Exception as err:
            print(err)
            continue
    return stories, authors

def send_message(token, message):
    url = f'https://api.vk.com/method/messages.send?user_id=142901911&v=5.101&message={message}&access_token={token}&random_id={random.randint(1, 10000000)}'
    r = requests.post(url)

def get_subs(id, token):
    sub_list = []
    offset = 0
    url = 'https://api.vk.com/method/groups.getMembers?'
    subs_count = (requests.post(f'https://api.vk.com/method/groups.getMembers?group_id={id}&access_token={token}&v=5.101')).json()['response']['count']
    for i in range(subs_count//1000):
        time.sleep(0.15)
        params = {'group_id':id,
                  'access_token':token,
                  'v':'5.101',
                  'offset':offset}
        data = requests.post(url, params=params).json()
        sub_list+=data['response']['items']
        offset+=1000
    print(len(sub_list))
    return sub_list

def worker(authors ,start, end):
    global stories_count, all_stories_count, seen_stories
    for i in range(start,end):
        print(f'Смотрю историю {authors[i]} | # {users_list[i]}')
        watch_story(authors[i],users_list[i],read_token)
        seen_stories.append(users_list[i])
        stories_count+=1
        all_stories_count+=1
    else:
        pass
        #print("нет историй для просмотра")


login = os.environ.get('login')
password = os.environ.get('password')

vk_session = vk_api.VkApi(
    login, password,
    # функция для обработки двухфакторной аутентификации
    auth_handler=auth_handler
)

try:
    vk_session.auth()
except vk_api.AuthError as error_msg:
    print(error_msg)
    sys.exit(1)

vk = vk_session.get_api()
url_src = vk_session.http.get('http://vk.com/feed')
tmp =  re.search('"read_hash":"\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w"',url_src.text)
read_token = url_src.text[tmp.start():tmp.end()].split(":")[-1].replace('"','')

if __name__=='__main__':
    auth_token = VKAuth(['stories'],'7512092','5.101',login,password)
    auth_token.auth()
    token = auth_token.get_token()
    print(len(slova))
    while True:
        users = pars_users(slova, token)
        users_list = users[0]
        authors_list = users[1]
        print(f'Собрано {len(users_list)} историй и {len(authors_list)} авторов.')
        THREADS = len(users_list) // 300
        for index in range(THREADS):
            threading.Thread(target=worker, args=(authors_list ,start, end)).start()
            start += 300
            end += 300
        start = 0
        end = 300
        time.sleep(1200)
        send_message(token_bot, f'Круг завершен. Просмотрено {stories_count} историй | Общее количество просмотренных историй: {all_stories_count}')
        stories_count = 0
