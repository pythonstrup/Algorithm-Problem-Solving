# 내 풀이
def make_music_weight(genres, plays):
    music_weight = {}
    for key, value in zip(genres, plays):
        if key in music_weight:
            music_weight[key] += value
        else:
            music_weight[key] = value

    return music_weight


def make_music_dict(genres, plays):
    music_dict = {}
    # 자동으로 고유번호가 낮은 순으로 들어가게 된다.
    for index, [key, value] in enumerate(zip(genres, plays)):
        if key in music_dict:
            music_dict[key].append((index, value))
        else:
            music_dict[key] = [(index, value)]

    return music_dict


def solution(genres, plays):
    answer = []
    music_weight = make_music_weight(genres, plays)
    music_dict = make_music_dict(genres, plays)

    priority_genres = [(key, value) for key, value in music_weight.items()]
    priority_genres.sort(key=lambda x: x[1], reverse=True)

    for priority in priority_genres:
        music_dict[priority[0]].sort(key=lambda x: x[1], reverse=True)
        answer.append(music_dict[priority[0]][0][0])
        # 해당 장르의 곡이 단 한 개만 있을 수도 있다.
        if len(music_dict[priority[0]]) > 1:
            answer.append(music_dict[priority[0]][1][0])

    return answer


# 다른 사람 풀이 1 - 내 풀이의 성능 조금 더 좋다
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer


# 다른 사람 풀이 2 - 내 풀이보다 좋은 성능
def solution(genres, plays):
    genres_dict = {}
    genres_list = []
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []
        genres_dict[genres[i]].append([i, plays[i]])

    for g in genres_dict:
        genres_dict[g].sort(key=lambda x: x[1], reverse=True)
        genres_list.append([g, sum([play for _, play in genres_dict[g]])])

    genres_list.sort(key=lambda x: x[1], reverse=True)
    answer = []
    for g, _ in genres_list:
        answer.extend([x[0] for x in genres_dict[g][:2]])
    return answer