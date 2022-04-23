import pygame
import librosa
import time
import os 
from os import environ
import ui_1 as ui
unreal_flag=[0]
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
"""
函数:
    play_music(music)  音乐播放函数，参数：音乐名称（不含扩展名，默认flac格式，可手动修改为mp3格式）

"""
def get_mp3_duration(audio_path):
    """
    得到 mp3 的时长
    :param audio_path: mp3 路径
    :return:mp3 时长
    """
    duration = librosa.get_duration(filename=audio_path)
    return duration

def play_music(music):
        # filepath =music+".flac";
        filepath =music;
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(start=0.0)
        music_time=get_music_time(filepath)
        music_time=int(music_time)
        time.sleep(music_time)
        pygame.mixer.music.stop()
def get_music_time(music_str_name):
    audio_path = music_str_name
    start = time.time()
    duration = get_mp3_duration(audio_path)
    end = time.time()
#     print('时长:',duration)
#     print('运行时间: {} 秒'.format(end - start))
    return duration

def file_name():   
    for root, dirs, files in os.walk('./voice'):  
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        for i in range(len(files)):
            print('第%d次循环开始标记\n'%(i))
            music_root=str(root)
            music_name=str(files[i])
            music_os=music_root+'/'+music_name
            playMusic(music_os)
            print('本次循环结束标记')
def playMusic(filename, loops=0, start=0.0, value=0.5):
    """
    :param filename: 文件名
    :param loops: 循环次数
    :param start: 从多少秒开始播放
    :param value: 设置播放的音量，音量value的范围为0.0到1.0
    :return:
    """
    flag = False  # 是否播放过
    pygame.mixer.init()  # 音乐模块初始化
    while 1:
        if flag == 0:
            pygame.mixer.music.load(filename)
            # pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
            pygame.mixer.music.play(loops=loops, start=start)
            pygame.mixer.music.set_volume(value)  # 来设置播放的音量，音量value的范围为0.0到1.0。
        if pygame.mixer.music.get_busy() == True:
            flag = True
        if ui.flag1[0]!=1:
            unreal_flag[0]=1
        else:
            if flag:
                pygame.mixer.music.stop()  # 停止播放
                break
def run():
    file_name()
# file_name()