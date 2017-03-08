from collections import Counter

num_scientist = int(raw_input())

scientist_to_lang = [int(x) for x in raw_input().split()]

num_movies = int(raw_input())

audio_to_lang = [int(x) for x in raw_input().split()]
sub_to_lang = [int(x) for x in raw_input().split()]

cntr = Counter(scientist_to_lang)

_max = {
	"a_val": cntr[audio_to_lang[0]],
	"s_val": cntr[sub_to_lang[0]],
	"index": 0
}

for i in xrange(1, len(audio_to_lang)):
	if cntr[audio_to_lang[i]] > _max["a_val"]:
		_max = {
			"a_val": cntr[audio_to_lang[i]],
			"s_val": cntr[sub_to_lang[i]],
			"index": i
		}
	elif cntr[audio_to_lang[i]] == _max["a_val"] and cntr[sub_to_lang[i]] > _max["s_val"]:
		_max = {
			"a_val": cntr[audio_to_lang[i]],
			"s_val": cntr[sub_to_lang[i]],
			"index": i
		}

print _max["index"] + 1
