import requests
import os
import json
from urllib.parse import quote
from tqdm import tqdm

def download_qq_music():
    name = input('请输入想要下载的歌曲名字,不要乱输入哦>>>')
    headers = {
            'cookie': 'pgv_pvid=7367424589; fqm_pvqid=69a72280-8144-4a33-8442-65300a849a0c; ts_refer=cn.bing.com/; ts_uid=1247631040; RK=nzrkibGeQf; ptcz=cbff6893a23eef8a389feb492be969f4d04f247654905bf6c2edb27bcd5b075e; psrf_qqrefresh_token=76B43A37A7728504606E8A0AC784212D; wxopenid=; psrf_qqopenid=BF52369DCCF782D5ED97D9E9CBB93690; psrf_qqaccess_token=74905530E83B2C968E1F0C6CEC544916; wxrefresh_token=; euin=oK6iowCFowSz7c**; wxunionid=; tmeLoginType=2; psrf_qqunionid=; pac_uid=0_99828596a6d53; tvfe_boss_uuid=55324e6a5a045486; eas_sid=f1k6t2k76857I2N7O3P9C5c5u0; fqm_sessionid=d885e5ce-ff4a-479f-a63a-55428802b1fe; pgv_info=ssid=s5176876878; _qpsvr_localtk=0.37199241768292324; login_type=1; psrf_access_token_expiresAt=1636013952; qm_keyst=Q_H_L_208yC460eO0phD8dUIfjs2vuEfgAXmPsk8Cthbdi20JRohh6K_DPL-wDlahoKLB; qm_keyst=Q_H_L_208yC460eO0phD8dUIfjs2vuEfgAXmPsk8Cthbdi20JRohh6K_DPL-wDlahoKLB; qqmusic_key=Q_H_L_208yC460eO0phD8dUIfjs2vuEfgAXmPsk8Cthbdi20JRohh6K_DPL-wDlahoKLB; psrf_musickey_createtime=1628237952; uin=1132682706; ts_last=y.qq.com/n/ryqq/player',
            'referer': 'https://y.qq.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
    }
    url_1 = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.top&searchid=57082778303553309&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w={}&_=1628239189792&cv=4747474&ct=24&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&uin=1132682706&g_tk_new_20200303=1139171391&g_tk=1139171391&hostUin=0&loginUin=1132682706'.format(quote(name))
    html_1 = requests.get(url_1,headers = headers).json()
    # print(html_1)
    song_list = html_1['data']['song']['list']
    print('查询出《{}》前{}首歌曲,结果:'.format(name,(song_list)))

    song_name_list = []
    singer_list = []
    a = 0
    for song in song_list:
        song_name = str(a) + ' ' +song['title']
        singer = song['singer'][0]['name']
        song_name_list.append(song_name)
        singer_list.append(singer)
        # print('歌曲名:{} 歌手:{}'.format(song_name,singer))
        a += 1
    # print(song_name_list,singer_list)
    infs = dict(zip(song_name_list, singer_list)) #将两个列表转化为字典
    # print(infs)
    infs = json.dumps(infs, ensure_ascii=False, indent=4, separators=(',', ':'))
    infs = infs.replace('"', ' ')
    infs = infs.replace(':', '——————')
    print(infs)

    index = int(input('根据上面的歌曲列表,选择一首自己喜欢的吧😊>>>'))
    print('友情提示,有些歌曲可能需要Vip-_-')

    your_choose_song_name= song_name_list[index][2:]
    your_choose_song_singer = singer_list[index]
    print('您选择的歌曲名字是《{}》,歌手-{}'.format(your_choose_song_name,your_choose_song_singer))

    song_mid =html_1['data']['song']['list'][index]['mid']
    url_2 = 'https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data=%7B%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22358840384%22%2C%22songmid%22%3A%5B%22{}%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%221443481947%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A%2218585073516%22%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'.format(song_mid)
    html_2 = requests.get(url_2,headers = headers).json()
    # print(html_2)
    purl = html_2['req_0']['data']['midurlinfo'][0]['purl']
    song_url ='https://dl.stream.qqmusic.qq.com/'+purl
    # print(song_url)

    cwd = os.getcwd()
    file_name = os.path.join(cwd,'qq音乐下载文件夹')
    if not os.path.exists('qq音乐下载文件夹'):
        os.mkdir(file_name)
    for i in tqdm(range(int(10e6)),ncols=100,desc='《{}》正在下载...'.format(your_choose_song_name)):
        pass

    with open(file_name+'\\{}-{}.mp3'.format(your_choose_song_name,your_choose_song_singer),'wb')as qqfile:
        qqfile.write(requests.get(song_url).content)
    print('《{}》-{} 下载完成, 去 {} 打开试听吧☺'.format(your_choose_song_name,your_choose_song_singer,file_name))

if __name__ == '__main__':
    download_qq_music()