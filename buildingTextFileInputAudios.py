import os
from shutil import copy
import string
import random

ASCII = dict()
for index, letter in enumerate(string.digits + string.ascii_lowercase):
   ASCII[letter] = index

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

def alphabet_position(text):
    text = text.lower()
    numbers = [ASCII[character] for character in text if character in ASCII]
    return concatenate_list_data(numbers)


directory_speakers = '/home/lorenzo/Scrivania/wav'
f = open("/home/lorenzo/Scrivania/text_input.txt", "w")

for speaker_identifier in os.listdir(directory_speakers):
    path_speaker_identifier = os.path.join(directory_speakers, speaker_identifier)
    for speech_batches in os.listdir(path_speaker_identifier):
        path_speech_batches = os.path.join(path_speaker_identifier, speech_batches)
        for audio_file in os.listdir(path_speech_batches):
            dir_audio = '/home/lorenzo/Scrivania/dir_audio'
            if not os.path.exists(dir_audio):
                os.makedirs(dir_audio)
            path_audio = os.path.join(path_speech_batches, audio_file)

            if path_audio.endswith('.wav'):
                destination_path = os.path.join(dir_audio, (speaker_identifier + speech_batches + audio_file))
                copy(path_audio, destination_path)
                speaker_number = alphabet_position(speaker_identifier)
                f.write("%s" % speaker_number + ' ' + destination_path + '\n')

f.close()

g = open("/home/lorenzo/Scrivania/text_input.txt", "r")
speakers = list()
for line in g.readlines():
    speakers.append(line.split()[0])


speakers = dict(enumerate(set(speakers)))
reindexed_speakers = {v: k for k, v in speakers.iteritems()}
print(reindexed_speakers)

h = open("/home/lorenzo/Scrivania/text_input.txt", "r")

with open("/home/lorenzo/Scrivania/text_input_1.txt", "w") as text:
    for line in h.readlines():
        id_speaker = line.split()[0]
        wav_path = line.split()[1]
        new_id_speaker = reindexed_speakers[id_speaker]
        text.write('%d' % new_id_speaker + ' ' + wav_path + '\n')

text.close()

k = open("/home/lorenzo/Scrivania/text_input_1.txt", "r")

with open("/home/lorenzo/Scrivania/text_input_2.txt", "w") as text_sorted:
    lines = k.readlines()
    all_lines_sorted_list = sorted(lines, key=lambda x:float(x.split()[0]), reverse=False)
    for item in all_lines_sorted_list:
        text_sorted.write("%s" % item)

import random

with open('/home/lorenzo/PycharmProjects/3D-convolutional-speaker-recognition/code/0-input/file_path_test2.txt', 'r') as source:
    data = [(random.random(), line) for line in source]
    data.sort()
    with open('/home/lorenzo/PycharmProjects/3D-convolutional-speaker-recognition/code/0-input/file_path_test2.txt', 'w') as target:
        for _, line in data:
             target.write(line)

print("mixed lines in file_path_test2.txt")