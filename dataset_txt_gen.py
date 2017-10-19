'''
generate dataset.txt from train/valid json file
'''
import json

dataset_txt = 'train_labels.txt'
label_file_path = '../dataset/ai-challenger/train/keypoint_train_annotations_20170909.json'

letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

with open(label_file_path) as json_file:
    labels = json.load(json_file)

with open(dataset_txt, 'w') as f:
    for it in range(len(labels)):
        if it%1000 == 0:
            print('%d of the %d labels are processeing'%(it, len(labels)))
        item = labels[it]
        img_name = item['image_id'] + '.jpg'
        if len(item['keypoint_annotations'])!=1:
            continue
        for id in range(len(item['keypoint_annotations'])):
            human_id = 'human' + str(id+1)
            # human_letter = letter[id]
            human_box = item['human_annotations'][human_id]
            out_flow = []
            out_flow.append(img_name)
            out_flow.extend(human_box)
            key_points = item['keypoint_annotations'][human_id]
            del_list = [i*3+2 for i in range(int(len(key_points)/3-1), -1, -1)]
            for i in del_list:
                del key_points[i]
            key_points = [-1 if kp==0 else kp for kp in key_points]
            out_flow.extend(key_points)
            out_flow.extend(['\n'])
            for out in enumerate(out_flow):
                f.write(str(out[1]))
                if out[1] != '\n':
                    f.write(' ')
