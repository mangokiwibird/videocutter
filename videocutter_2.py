from moviepy.editor import VideoFileClip
import time

class cutter:
    def __init__(self):
        pass
    
    def cutting(self, input_path, output_path): #TODO: input_path and output_path are string(?) which point to videopath
        first = time.time()  #처음 발견지점 == 시작 == 이 모듈이 불려온 시점
        if first <= 30:
            start = 0
        else:
            start = first - 30 #앞뒤로 30초씩 중에 앞
        end = first + 30 #앞뒤로 30초씩 중에 뒤

        video = VideoFileClip(input_path)
        clip = video.subclip(start, end)
        clip.write_videofile(output_path)
        print("videoclip made successfully")
    
    def mediumcutter(self, activity):
        if activity != None:
            self.cutting("?", f"\{activity}") #inputpath를 어케 써야 할지 몰라서 다른 방법도 고안해 봤지만 쉽지 않음. +outputpath는 저렇게 써도 될지 미지수
    
    #결론: 나는 조졌다 우린 조졌다 ㅅ1ㅂ!!!