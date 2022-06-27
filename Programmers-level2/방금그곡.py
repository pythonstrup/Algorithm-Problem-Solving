# 내 풀이
def solution(m, musicinfos):
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")

    find_music = [] # 제목과 재생시간을 담을 것임
    for music in musicinfos:
        value = music.split(",")
        start = value[0].split(":")
        end = value[1].split(":")
        value[3] = value[3].replace("C#", "c")
        value[3] = value[3].replace("D#", "d")
        value[3] = value[3].replace("F#", "f")
        value[3] = value[3].replace("G#", "g")
        value[3] = value[3].replace("A#", "a")

        hour = int(end[0]) - int(start[0])
        minute = int(end[1]) - int(start[1])
        total_time = hour * 60 + minute

        music_length = len(value[3])
        temp = ""
        for i in range(total_time):
            temp += value[3][i%music_length]

        if m in temp:
            if find_music and total_time > find_music[1]:
                find_music[0] = value[2]
                find_music[1] = total_time
            else:
                find_music.append(value[2])
                find_music.append(total_time)

    return find_music[0] if find_music else '(None)'

# 내풀이 개선
def substitution(str):
    return str.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

def solution(m, musicinfos):
    m = substitution(m)

    find_music = [] # 제목과 재생시간을 담을 것임
    for music in musicinfos:
        value = music.split(",")
        start = value[0].split(":")
        end = value[1].split(":")
        value[3] = substitution(value[3])

        hour = int(end[0]) - int(start[0])
        minute = int(end[1]) - int(start[1])
        total_time = hour * 60 + minute

        music_length = len(value[3])
        temp = ""
        for i in range(total_time):
            temp += value[3][i%music_length]

        if m in temp:
            if find_music and total_time > find_music[1]:
                find_music[0] = value[2]
                find_music[1] = total_time
            else:
                find_music.append(value[2])
                find_music.append(total_time)

    return find_music[0] if find_music else '(None)'

# 다른 사람 풀이 1
# 내 것보다 2배 가량 성능이 좋다
def shap_to_lower(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m,musicinfos):
    answer=[0,'(None)']   # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
        if m in full_notes and time_length>answer[0]:
            answer=[time_length,title]
    return answer[-1]

# 다른 사람 풀이 2
# 내 것보다 2배 가량 성능이 좋다
class Music:
    def __init__(self, start_time, end_time, name, sound):
        self.start_time = start_time
        self.end_time = end_time
        self.name = name
        self.sound = sound

        self.set_music_time()
        self.set_full_sound()

    def set_music_time(self):
        start = self.start_time.split(":")
        end = self.end_time.split(":")

        hours = int(start[0]) - int(end[0])
        minutes = int(start[1]) - int(end[1])

        time = (hours * 60) + minutes

        if time < 0:
            self.run_time = -time
        else:
            self.run_time = time

    def set_full_sound(self):
        self.full_sound = str()

        if len(self.sound) >= self.run_time:
            self.full_sound = self.sound[:self.run_time]
        else:
            tmp = self.run_time / len(self.sound)
            self.full_sound += self.sound * int(tmp)

            tmp = self.run_time % len(self.sound)
            self.full_sound += self.sound[:int(tmp)]

    def contain_sound(self, m):
        if m in self.full_sound:
            return True

        return False

    def __str__(self):
        return """
        name: %s
        start_time: %s
        end_time: %s
        run_time: %s
        sound: %s
        full_sound: %s
        """ % (self.name, self.start_time, self.end_time, self.run_time, self.sound, self.full_sound)

    def __lt__(self, other):
        return self.run_time > other.run_time

def set_music(music_info):

    return Music(music_info.split(",")[0],
                 music_info.split(",")[1],
                 music_info.split(",")[2],
                 encode_sound(music_info.split(",")[3]))

def encode_sound(before_sound):
    encode = before_sound
    sound_encodes = ['C#', 'D#', 'F#', 'G#', 'A#']
    sound_decodes = ['c', 'd', 'f', 'g', 'a']

    for sound_encode, sound_decode in zip(sound_encodes, sound_decodes):
        if sound_encode in encode:
            encode = encode.replace(sound_encode, sound_decode)

    return encode

def solution(m, musicinfos):
    answer = "(None)"

    tmp_answer = []
    for musicinfo in musicinfos:
        tmp = set_music(musicinfo)
        if tmp.contain_sound(encode_sound(m)):
            tmp_answer.append(tmp)

    if len(tmp_answer) != 0:
        answer = sorted(tmp_answer)[0].name

    return answer