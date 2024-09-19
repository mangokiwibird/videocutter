import time
from timer import timer
from moviepy.editor import VideoFileClip

class cutter:

    classcnt = {}

    def __init__(self):
        self.previous_activity = None
        self.timegone = timer()
        self.video = None # TODO: None자리에 원본 비디오 명 넣어야 함

    def cut(self, activity):
        clip = VideoFileClip(self.video)
        dic = {} #TODO: dic에는 rulebase와 probability, mlbase에서 사용된 어떤 딕셔너리를 가져와야 함.
        if activity != "None":
            if self.timegone <= 30:
                time_i = 0
                time_f = time.time() + 30
            else:
                time_i = time.time() - 30
                time_f = time.time() + 30
            cut = clip.subclip(time_i, time_f)
            a = dic[activity]
            cutter.classcnt = [i for i in range(1, a+1)]

            cut.write_videofile(f"{activity}{cutter.classcnt.pop(0)}.mp4", codec="libx264")